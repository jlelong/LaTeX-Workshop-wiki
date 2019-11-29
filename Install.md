# Installation and basic settings

## Requirements

- LaTeX distribution in system PATH. For example, [TeX Live](https://www.tug.org/texlive/).
- Please note [MikTeX](https://miktex.org/) does not ship with SyncTeX. Please use [built-in synctex functionality](View#latex-workshopsynctexsynctexjsenabled).
- `latexmk` is required for the default recipe for building LaTeX projects to work. Alternatively, you can [set up your own LaTeX recipe](Compile#latex-recipes).
- _Optional_: Install [ChkTeX](http://www.nongnu.org/chktex) to lint LaTeX projects.
- _Optional_: Install [latexindent.pl](https://github.com/cmhughes/latexindent.pl) for formatting support if it is not provided by your LaTeX distribution.

## Installation

Installing LaTeX Workshop is simple. You can find it in [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), or simply run `ext install latex-workshop` in VS Code Quick Open (`ctrl`/`cmd` + `P`).

## Setting PATH environment variable

Usually, you do **NOT** have to set PATH environment variable. TeX distributions appropriately set the variable on your system. And, LaTeX Workshop never touches the variable. If VS Code cannot find executables of TeX, it means that **the setting of your system is broken**. For the ways of setting environment variables on Windows, see [link](https://docs.telerik.com/teststudio/features/test-runners/add-path-environment-variables) or [link](https://www.computerhope.com/issues/ch000549.htm). On macOS and Linux, refer to a [document](https://github.com/rbenv/rbenv/wiki/unix-shell-initialization) by the rbenv dev team.

If you can not fix the setting of your system, you can also override PATH with the `env` property of [LaTeX recipes](Compile#latex-recipes).

## Usage

The typical usage is to open a `.tex` file and have a look at the _TeX_ sidebar to access all the extension features. If you wish to use a keybinding to open the _TeX_ sidebar, you just need to associate one with the command `latex-workshop.actions`.

- [Building](Compile#building-the-document)
- [Viewing and going from source to PDF back and forth](View)
- [Catching errors and warnings](Compile#catching-errors-and-warnings)
- [Navigating in environments](Environments#Navigating)
- Navigating the document structure. The section names of LaTeX outline hierarchy are defined in `latex-workshop.view.outline.sections`. This property is an array of case-sensitive strings in the order of document structure hierarchy. For multiple tags in the same level, separate the tags with `|` as delimiters, e.g., `section|alternative`. It is also used by the folding mechanism.
- Miscellaneous actions
  - Open citation browser, see also [Intellisense for citations](Intellisense#Citations)

If you prefer to access some of the most common actions through a right click menu, set `latex-workshop.showContextMenu` to `true`. Default is `false`.

## Using Docker

Starting with 1.35.0, VS Code supports Docker with [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). LaTeX Workshop works well with the extension. Try the extension at first.

Starting with release 5.3.0, there is an experimental implementation on Docker support following the idea of [@Arxisos](https://github.com/Arxisos). You can set `latex-workshop.docker.enabled` to `true` to use a docker based LaTeX distribution. The docker image to be used is defined by `latex-workshop.docker.image.latex`, the default value is `tianon/latex`. It is advised that the image is 'pre-'pulled.

[@Arxisos](https://github.com/Arxisos) created [snippets](https://github.com/Arxisos/LaTex-Workshop-Docker) for LaTeX binaries in docker, and [@lippertmarkus](https://github.com/lippertmarkus) had another [short description](https://github.com/James-Yu/LaTeX-Workshop/issues/302) on how to use Docker with LaTeX Workshop.

## Using WSL

Starting with 1.35.0, VS Code supports WSL through [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). LaTeX Workshop works well with the extension.
