# VS Code Remote Development

LaTeX Workshop can work with [VS Code Remote Development extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&ssr=false). You can see their [technical details](https://code.visualstudio.com/docs/remote/remote-overview). Not only you can edit a TeX file inside a Docker container or in WSL, but also you can preview the pdf file.

You can also edit a TeX file on a remote server and preview the pdf file. However, when you use this feature on a remote server, please consider the following security risks.

## VS Code Remote Sever can be accessed by other users on the remote server

VS Code Remote Development extensions start a server to host VS Code extensions on the remote server. Other users on the remote server can access the server.

- https://code.visualstudio.com/docs/remote/troubleshooting#_improving-security-on-multiuser-servers
- https://github.com/microsoft/vscode-remote-release/issues/1927#issuecomment-942462191

## Your PDF file can be read by other users on the remote server

LaTeX Workshop starts a http server to preview the pdf file on the remote server. Other users on the remote server can access the server and can read your pdf file.

## Summary

**VS Code Remote Development extensions are NOT supposed to be used on a usual server logged in by multiple users.**