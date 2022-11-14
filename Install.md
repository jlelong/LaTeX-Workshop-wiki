# Installation and basic settings

## Requirements

- LaTeX distribution in system PATH. For example, [TeX Live](https://www.tug.org/texlive/). We **strongly recommend** TeX Live.
  - For a lighter-weight distribution based on TeX Live, see <a href="https://yihui.org/tinytex">TinyTeX</a>.<br>
    <details><!-- empty line below, so that markdown works -->

    The [TinyTeX distributions](https://github.com/rstudio/tinytex-releases#releases)
    contain only a small subset of the 4000+ packages downloaded by TeX Live.
    Additional packages can be installed with `tlmgr install <pkgname>`.

    Note that TinyTeX does not include offline documentation.
    LaTeX Workshop's [_"Show package documentation"_ functionality][showdoc] will therefore not work.
    (You can instead use the CTAN link, also provided in the hover popup, to download the docs).
    </details>
    
- We don't recommend [MiKTeX](https://miktex.org/) because MiKTeX does not ship with Perl. If you choose MiKTeX, you have to install Perl by yourself, which `latexmk` requires. Without Perl, `latexmk` fails with errors.
- `latexmk` is required for the default recipe for building LaTeX projects to work. Alternatively, you can [set up your own LaTeX recipe](Compile#latex-recipes).
- _Optional_: Install [ChkTeX](https://www.nongnu.org/chktex) to lint LaTeX projects.
- _Optional_: Install [latexindent.pl](https://github.com/cmhughes/latexindent.pl) for formatting support if it is not provided by your LaTeX distribution. You also have to install a few standard Perl modules. See the [official document](https://latexindentpl.readthedocs.io/en/latest/sec-appendices.html#required-perl-modules).

[showdoc]: https://github.com/James-Yu/LaTeX-Workshop/wiki/Hover#documentation-of-a-package

## Installation

Installing LaTeX Workshop is simple. You can find it in [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), or simply run `ext install latex-workshop` in VS Code Quick Open (`ctrl`/`cmd` + `P`). See an [official document](https://code.visualstudio.com/docs/editor/extension-gallery) for the details.

## Setting PATH environment variable

After installing TeX Live, you must add the directory of TeX Live binaries to your PATH environment variable except on Windows. See the [official document](https://www.tug.org/texlive/quickinstall.html). LaTeX Workshop never touches the variable. If VS Code cannot find executables of TeX, it means that **the setting of your system is broken**. For the ways of setting environment variables on Windows, see [link](https://docs.telerik.com/teststudio/features/test-runners/add-path-environment-variables) or [link](https://www.computerhope.com/issues/ch000549.htm). On macOS and Linux, see the  [documentation](https://github.com/rbenv/rbenv/wiki/unix-shell-initialization) by the rbenv dev team.  Very detailed information is also available on [stackoverflow](https://stackoverflow.com/questions/135688/setting-environment-variables-on-os-x) for macOS.

Notice that you have to **restart VS Code and the operating system** after changing the variable.

If you can not fix the setting of your system, you can also override PATH with the `env` property of [LaTeX tools](Compile#latex-tools) in LaTeX recipes.

Notice that, to set the `PATH` environment variable for VS Code Remote Development, you usually have to edit `.bash_profile` or `.profile` instead of `.bashrc`. See the [document](https://code.visualstudio.com/docs/remote/troubleshooting#_configure-the-environment-for-the-remote-extension-host) for WSL and an [issue](https://github.com/microsoft/vscode-remote-release/issues/1671#issuecomment-542818686) for Remote SSH.

If you want to know about environment variable itself, please read [Wikipedia](https://en.wikipedia.org/wiki/Environment_variable) and [stackexchange](https://unix.stackexchange.com/questions/91282/what-exactly-is-an-environment-variable).

## Settings

You can modify settings through the menu of VS Code, `Preferences > Settings`.
You can also modify settings by directly editing `settings.json`. See an [official document](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations) for the location of `settings.json`.

You can also have different settings for each project with `.vscode/settings.json` at the root of each project workspace. See an [official document](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations).

For language-specific editor settings, see an [official document](https://code.visualstudio.com/docs/getstarted/settings#_languagespecific-editor-settings).

## Usage

The typical usage is to open a `.tex` file and have a look at the _TeX_ sidebar to access all the extension features. If you wish to use a keybinding to open the _TeX_ sidebar, you just need to associate one with the command `latex-workshop.actions`.

- [Building](Compile#building-the-document)
- [Viewing and going from source to PDF back and forth](View)
- [Catching errors and warnings](Compile#catching-errors-and-warnings)
- [Navigating and selecting environments](Environments#Navigating-and-selection)
- Navigating the document structure. The section names of LaTeX outline hierarchy are defined in [`latex-workshop.view.outline.sections`](ExtraFeatures#latex-workshopviewoutlinesections). This property is an array of case-sensitive strings in the order of document structure hierarchy. For multiple tags in the same level, separate the tags with `|` as delimiters, e.g., `section|alternative`. It is also used by the folding mechanism.
- Miscellaneous actions
  - Open citation browser, see also [Intellisense for citations](Intellisense#Citations)

If you prefer to access some of the most common actions through a right click menu, set `latex-workshop.showContextMenu` to `true`. Default is `false`.

### Supported languages

In addtions to `LaTeX`, [`LaTeX-Expl3`](https://www.latex-project.org/latex3/) is supported. `LaTeX-Expl3` is a language identifier we tentatively use for the so-called "LaTeX3". With the `LaTeX-Expl3` mode, syntax highlighting and intellisense for commands of `expl3` are supported in addition to basic features for `LaTeX`. You can change the language mode from `LaTeX` to `LaTeX-Expl3` clicking on the language indicator, `LaTeX`, of the satus bar and selecting `LaTeX-Expl3` from the drop-down. See an [official document](https://code.visualstudio.com/docs/languages/overview#_changing-the-language-for-the-selected-file).

[Sweave](https://stat.ethz.ch/R-manual/R-patched/library/utils/doc/Sweave.pdf), [knitr](https://yihui.org/knitr/), and [Weave.jl](https://github.com/JunoLab/Weave.jl) are also supported. See [Building a .rnw file](Compile#building-a-rnw-file) and [Building a .jnw file](Compile#building-a-jnw-file) for the details.

## Using Docker

VS Code supports Docker with [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). LaTeX Workshop works well with the extension. You can see [an example](https://github.com/James-Yu/LaTeX-Workshop/tree/master/samples/docker). We **strongly recommend** you to use the extension instead of our following experimental feature.

LaTeX Workshop has an **experimental** implementation on Docker support following the idea of [@Arxisos](https://github.com/Arxisos). You can set `latex-workshop.docker.enabled` to `true` to use a docker based LaTeX distribution. The docker image to be used is defined by `latex-workshop.docker.image.latex`, the default value is empty. Please find an appropriate image by yourself and set the name to `latex-workshop.docker.image.latex`.

[@Arxisos](https://github.com/Arxisos) created [snippets](https://github.com/Arxisos/LaTex-Workshop-Docker) for LaTeX binaries in docker, and [@lippertmarkus](https://github.com/lippertmarkus) had another [short description](https://github.com/James-Yu/LaTeX-Workshop/issues/302) on how to use Docker with LaTeX Workshop.
You can set up the advanced configuration of Docker through [environment variables](https://docs.docker.com/engine/reference/commandline/cli/#environment-variables) with the `env` property of each [recipe](Compile#latex-recipes).

With the experimental feature, compiling subfiles with the `subfiles` package does not work.

## Using WSL

VS Code supports WSL through [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). LaTeX Workshop works well with the extension.
