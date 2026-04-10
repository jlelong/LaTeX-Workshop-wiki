# VS Code Remote Development

LaTeX Workshop can work with [VS Code Remote Development extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&ssr=false). You can read [their technical details](https://code.visualstudio.com/docs/remote/remote-overview). Not only you can edit a TeX file inside a Docker container or in WSL, but also you can preview the pdf file.

## Security risk of VS Codo Remote - SSH

You can also edit a TeX file on a remote server and preview the pdf file. However, when you use this feature on a remote server, please consider the following security risks.

**VS Code Remote Development extensions are NOT supposed to be used on a usual server logged in by multiple users.**

### VS Code Remote Sever can be accessed by other users on the remote server

VS Code Remote Development extensions start a server to host VS Code extensions on the remote server. Other users on the remote server can access the server.

- https://code.visualstudio.com/docs/remote/troubleshooting#_improving-security-on-multiuser-servers
- https://github.com/microsoft/vscode-remote-release/issues/1927#issuecomment-942462191

### Your PDF file can be read by other users on the remote server

LaTeX Workshop starts a http server to preview the pdf file on the remote server. Other users on the remote server can access the server and can read your PDF file.

## Security model of VS Code Remote Development

You **MUST NOT** build an untrusted LaTeX document with VS Code Remote Development. It is **NOT SAFE**.

See the comment: https://github.com/microsoft/vscode-remote-release/issues/6608#issuecomment-1112960548

You should only connect to VS Code servers that you trust. So you should only connect to SSH machines that you trust and only create dev containers from definitions that you trust (i.e. **you should not use dev containers as a sandbox**).

## Using `code serve-web` behind a reverse proxy

When running VS Code as a web server via `code serve-web`, the editor is typically exposed to the browser through a reverse proxy (Caddy, Nginx, etc.). In this kind of deployment, the PDF viewer cannot be reached by the client's browser by default, because LaTeX Workshop's internal PDF server listens on `127.0.0.1` on the remote machine (unless changed via `latex-workshop.changeHostName`), and there is no port-forwarding mechanism between the remote server and the client.

To make the PDF viewer accessible, the reverse proxy must also forward the PDF server's port, and LaTeX Workshop must be told the externally reachable URL.

### Configuration

1. Set `latex-workshop.view.pdf.internal.port` to a fixed port (e.g., `34567`), so the reverse proxy target stays stable across restarts.

2. Add a rule to the reverse proxy that forwards a public path or host to the fixed port. Example using Caddy:

    ```
    yourdomain.com {
        handle_path /latex-workshop-pdf/* {
            reverse_proxy 127.0.0.1:34567
        }
        # ... your existing code serve-web rule
    }
    ```

3. Set `latex-workshop.view.pdf.internal.urlPrefix` to the externally reachable URL, e.g., `https://yourdomain.com/latex-workshop-pdf`.

**Security warning:** The PDF server exposes PDFs without any authentication. Although the URL contains a base64-encoded path of the PDF file and the server only serves files currently being viewed, anyone who knows or obtains the correct URL can read the file. If the proxied path is publicly reachable, consider restricting access (e.g., same authentication as `code serve-web`, VPN, or IP allowlist).

**Note:** LaTeX Workshop listens on `127.0.0.1` by default. If your reverse proxy runs on a different machine, use a tool like `socat` to forward the port locally first.

**Note:** This setup is only needed for environments like `code serve-web` where the browser cannot reach the extension's local port directly. In setups with automatic port forwarding (such as `code tunnel`, Codespaces, Remote-SSH, or [`code-server`](https://github.com/coder/code-server)), the PDF viewer works out of the box without any of the configuration above.
