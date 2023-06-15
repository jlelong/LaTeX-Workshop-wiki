# FAQ and common issues

- [Known incompatible extensions](#known-incompatible-extensions)
- [Using LaTeX Workshop with WSL](#using-latex-workshop-with-wsl)
- [Problems with Snap and Flatpak versions of VS Code](#problems-with-snap-and-flatpak-versions-of-vs-code)
- [The PDF viewer is blank or has graphical glitches](#the-pdf-viewer-is-blank-or-has-graphical-glitches)
- [Cygwin is not supported](#cygwin-is-not-supported)
- [code-server is not supported](#code-server-is-not-supported)
- [Gitpod is not supported](#gitpod-is-not-supported)
- [openvscode-server is not supported](#openvscode-server-is-not-supported)
- [Eclipse Theia is not supported](#eclipse-theia-is-not-supported)
- [Onivim 2 is not supported](#onivim-2-is-not-supported)
- [The github.dev web-based editor is not supported](#the-githubdev-web-based-editor-is-not-supported)
- [VSCodium is not officially supported](#vscodium-is-not-officially-supported)
- [Code OSS on Arch Linux and Manjaro is not officially supported](#code-oss-on-arch-linux-and-manjaro-is-not-officially-supported)
- [Visual Studio Live Share is not supported](#visual-studio-live-share-is-not-supported)
- [LaTeX Utilities is not supported](#latex-utilities-is-not-supported)
- [The directory ~/node_modules/ may cause errors](#the-directory-node_modules-may-cause-errors)
- [LaTeX Workshop doesn't work with a multi-file project](#latex-workshop-doesnt-work-with-a-multi-file-project)
- [The Problem Pane displays wrong messages](#the-Problem-Pane-displays-wrong-messages)
- [Encoding issues with file names in the Problem Pane](#Encoding-issues-with-file-names-in-the-Problem-Pane)
- [I cannot use `ctrl`+`alt` in a shortcut](#i-cannot-use-ctrlalt-in-a-shortcut)
- [Auto build does not work sometimes](#auto-build-does-not-work-sometimes)
- [Saving a `.cls` file does not trigger auto build](#saving-a-cls-file-does-not-trigger-auto-build)
- [Suggestions for BibTeX files are not updated](#suggestions-for-bibtex-files-are-not-updated)
- [The internal PDF viewer is not updated](#the-internal-pdf-viewer-is-not-updated)
- [Disable automatic build on save](#disable-automatic-build-on-save)
- [I use build on save but I occasionally want to save without building](#I-use-build-on-save-but-I-occasionally-want-to-save-without-building)
- [Auto build LaTeX results in always twice or infinite loop](#auto-build-latex-results-in-always-twice-or-infinite-loop)
- [With TikZ, builds result in an infinite loop](#with-tikz-builds-result-in-an-infinite-loop)
- [Large bibtex files are ignored](#large-bibtex-files-are-ignored)
- [Path containing Chinese or `~` characters](#path-containing-chinese-or--characters)
- [IME doesn't work well with LaTeX Workshop](#ime-doesnt-work-well-with-latex-workshop)
- [The LaTeX sidebar keeps reopening](#the-latex-sidebar-keeps-reopening)
- [Spell check](#spell-check)
- [I cannot nest snippets](#i-cannot-nest-snippets)
- [Some `@` snippets are not `TAB` completed](#some--snippets-are-not-tab-completed)
- [How to pass `-shell-escape` to `latexmk`](#how-to-pass--shell-escape-to-latexmk)
- [LaTeX-Workshop shadows vscode's default keybindings](#latex-workshop-shadows-vscodes-default-keybindings)
- [Syntax Highlighting does not work for most elements](#syntax-highlighting-does-not-work-for-most-elements)
- [Install an older version of LaTeX Workshop](#install-an-older-version-of-latex-workshop)
- [Downgrade VS Code to an older version](#downgrade-vs-code-to-an-older-version)
- [Customizing a Color Theme](#customizing-a-color-theme)
- [Move the structure view and others to other places](#move-the-structure-view-and-others-to-other-places)
- [Overriding snippets](#overriding-snippets)
- [Where can I find the definitions of the placeholders](#where-can-i-find-the-definitions-of-the-placeholders)
- [Autocompletion for `\includegraphics` seems incomplete](#autocompletion-for-includegraphics-seems-incomplete)
- [Environment variables in `.bashrc` don't take effect with VS Code Remote](#environment-variables-in-bashrc-dont-take-effect-with-vs-code-remote)
- [Environment variables in `.zshrc` don't take effect with VS Code Remote](#environment-variables-in-zshrc-dont-take-effect-with-vs-code-remote)
- [You cannot use a tilde `~` in `PATH`](#you-cannot-use-a-tilde--in-path)
- [`terminal.integrated.shellArgs.linux` doesn't take effect](#terminalintegratedshellargslinux-doesnt-take-effect)
- [What kinds of LaTeX commands does Hover Preview support?](#what-kinds-of-latex-commands-does-hover-preview-support)
- [Hover Preview fails to render math equation with errors](#hover-preview-fails-to-render-math-equation-with-errors)
- [The file `settings.json` doesn't have default values of settings](#the-file-settingsjson-doesnt-have-default-values-of-settings)
- [Why don't you integrate the recipe system with the VS Code task feature?](#why-dont-you-integrate-the-recipe-system-with-the-vs-code-task-feature)
- [How to prevent the internal PDF viewer from opening when selecting a PDF file in the explorer?](#how-to-prevent-the-internal-pdf-viewer-from-opening-when-selecting-a-pdf-file-in-the-explorer)
- [Can I define my own listing environment?](can-i-define-my-own-listing-environment)

## Known incompatible Extensions

The following extensions are known to cause issues when active at the same time as LaTeX-Workshop

- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright): high CPU load, Enter key delay
- [Brackets Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2): high CPU load, Enter key delay
- [Prettify Symbols Mode](https://marketplace.visualstudio.com/items?itemName=siegebell.prettify-symbols-mode): high CPU load, Enter key delay
- [Path Autocomplete](https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete): it may break autocompletion for bibliography citations.
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense): it may break autocompletion for bibliography citations.
- [LaTeX Preview](https://marketplace.visualstudio.com/items?itemName=ajshort.latex-preview): Conflict with LaTeX Workshop.
- [LaTeX language support](https://marketplace.visualstudio.com/items?itemName=torn4dom4n.latex-support): It does not work with some LaTeX Workshop's snippets.
- [Elastic Tabstops Mono](https://marketplace.visualstudio.com/items?itemName=isral.elastic-tabstops-mono): Delay when pressing `Enter`. You can disable this keybinding by setting [`latex-workshop.bind.enter.key`](Environments#latex-workshopbindenterkey) to `false`.

## Using LaTeX Workshop with WSL

Starting with 1.35.0, VS Code supports WSL through [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). LaTeX Workshop works well with the extension.

See https://github.com/microsoft/WSL/issues/4739 for more information about the issue. Alternatively, you can set `latex-workshop.saveWithoutBuilding: onSave` to only trigger a build upon saving a file as it does not require file watchers to work.

## Problems with Snap and Flatpak versions of VS Code

These versions are sandboxed and are known to cause problems (e.g. [here](https://github.com/James-Yu/LaTeX-Workshop/issues/2437)). We strongly recommend not using the snap and flatpack versions of VS Code. We strongly recommend using other installation options, like the .deb package for Debian/Ubuntu based distributions.

## The PDF viewer is blank or has graphical glitches

If the PDF viewer is blank or has graphical glitches, please try restarting VS Code with the option `--disable-gpu`. See [the official document](https://code.visualstudio.com/docs/supporting/FAQ#_vs-code-is-blank), [realted issue](https://github.com/microsoft/vscode/issues/92970), and [another issue](https://github.com/James-Yu/LaTeX-Workshop/issues/1935).

## Cygwin is not supported

LaTeX Workshop does not support TeX Live installed through Cygwin. Please install TeX Live and other TeX distributions independently of Cygwin.

## code-server is not supported

LaTeX Workshop does not support [code-server](https://github.com/cdr/code-server).

## Gitpod is not supported

LaTeX Workshop does not support [Gitpod](https://github.com/gitpod-io/gitpod).

## openvscode-server is not supported

LaTeX Workshop does not support [openvscode-server](https://github.com/gitpod-io/openvscode-server).

## Eclipse Theia is not supported

LaTeX Workshop does not support [Eclipse Theia](https://github.com/eclipse-theia/theia).

## Onivim 2 is not supported

LaTeX Workshop does not support [Onivim 2](https://github.com/onivim/oni2).

## The github.dev web-based editor is not supported

LaTeX Workshop does not support [the github.dev web-based editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) and [vscode.dev](https://code.visualstudio.com/blogs/2021/10/20/vscode-dev).

## VSCodium is not officially supported

[VSCodium](https://github.com/VSCodium/vscodium) is not officially supported due to the maintenance burden. We do not help to resolve issues related to VSCodium.

## Code OSS on Arch Linux and Manjaro is not officially supported

[Open-source builds](https://archlinux.org/packages/community/x86_64/code/) of Visual Studio Code on Arch Linux and Manjaro are not officially supported due to the maintenance burden. We do not help to resolve issues related to those builds. Please use [the official binary distribution](https://aur.archlinux.org/packages/visual-studio-code-bin/).

## Visual Studio Live Share is not supported

[Visual Studio Live Share](https://marketplace.visualstudio.com/items?itemName=ms-vsliveshare.vsliveshare) is not supported.

## LaTeX Utilities is not supported

[LaTeX Utilities](https://github.com/tecosaur/LaTeX-Utilities) is not supported.

## The directory ~/node_modules/ may cause errors

The directory `~/node_modules/` in the home directory may cause errors on Mac and Linux. The modules in the directory might be unintentionally loaded by VSCode because of the [default behavior](https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders) of node.js, which would cause errors such as _Extension host terminated unexpectedly_. We recommend moving the directory `~/node_modules/` to `~/npm/node_modules/`.

## LaTeX Workshop doesn't work with a multi-file project

If you cannot build a multi file LaTeX project from a subfile, it means that the root file is not detected properly. See the [Multi file projects](Compile#multi-file-projects) section for details on how the root file is discovered. Note that you must open the directory (or one of its antecedents) containing all the project files in vscode for this mechanism to work.

If you are directly calling LaTeX commands, `pdflatex`, and others in your recipe, please try passing `-recorder` to the LaTeX command in your recipe.

## The Problem Pane displays wrong messages

Please make sure at first that you call LaTeX compilers with an option `-file-line-error`.

LaTeX compilers usually produce hard wrapped log messages, which makes them really hard to parse. To hopefully deal with complex log messages, we have decided to rely on non hard wrapped log messages. This can be achieved either

- by setting the environment variable `max_print_line`. This is automatically done within the extension and works for the TeXLive distribution.
- by adding the `--max-print-line` option to the compilers. This is automatically done within the extension and works for the MiKTeX distribution. Unfortunately, some compilers such as `lualatex` do not understand this option and may therefore fail. To disable the automatic addition of this option, set `latex-workshop.latex.option.maxPrintLine.enabled` to `false`.

Note that when log messages are hard wrapped, the _Problems Pane_ is likely to be messed up.

## Encoding issues with file names in the Problem Pane

If you experience encoding issues with file names displayed in the Problem Pane, you can try to set `latex-workshop.message.convertFilenameEncoding` to `false`.

## I cannot use `ctrl`+`alt` in a shortcut

The default shortcuts for commands related to build and view use the modifiers <kbd>ctrl</kbd>+<kbd>alt</kbd>. On some keyboard layouts, <kbd>ctrl</kbd>+<kbd>alt</kbd> is used to emulate <kbd>AltrGr</kbd>, which makes these shortcuts unusable. Alternatively, you can use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>letter</kbd> instead of <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>letter</kbd> by setting `latex-workshop.bind.altKeymap.enabled` to `true`.

## Auto build does not work sometimes

Please try setting [`latex-workshop.latex.autoBuild.run`](Compile#latex-workshoplatexautobuildrun) to `onSave`.

Reload vscode to make any change in this configuration effective.

## Saving a `.cls` file does not trigger auto build

You have to compile your project with `latexmk` or manually pass `-recorder` to your LaTeX compiler to produce a `.fls` file. Then, LaTeX Workshop will use it to compute the exact list of included files. See [Compile](Compile#the-dependencies).

## Disable automatic build on save

Set the configuration variable `latex-workshop.latex.autoBuild.run` to `"never"`.

## I use build on save but I occasionally want to save without building

When `latex-workshop.latex.autoBuild.run` is set to `onSave`, building is triggered every time a file is saved inside VSCode. If you want to save a file without building it, you can use the `Save without Building` command from the _Command Palette_. A keybinding can be associated to the internal command `latex-workshop.saveWithoutBuilding` to access this feature more easily.

## Auto build LaTeX results in always twice or infinite loop

There is a possibility that LaTeX Workshop detects changes on files by build scripts during the build process and starts a new build process. That results in unintended multiple build processes. See [#2237](https://github.com/James-Yu/LaTeX-Workshop/issues/2237) and [#2487](https://github.com/James-Yu/LaTeX-Workshop/issues/2487). In that case, please change the setting [`latex-workshop.latex.autoBuild.run`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-workshoplatexautobuildrun) to `"onSave"`.

## With TikZ, builds result in an infinite loop

When builds result in an infinite loop with TikZ or other advanced packages,
please replace `-interaction=nonstopmode` with `-halt-on-error` in your recipe.

## Large bibtex files are ignored

Bibtex files listed in a project are parsed for citation completion. This may induce significant slow down with large bibtex files. You can configure the maximum size of bibtex files parsed by the extension with [`latex-workshop.bibtex.maxFileSize`](Intellisense#latex-workshopbibtexmaxFileSize).

## Path containing Chinese or `~` characters

On some platforms, when the path of a TeX file contains Chinese characters, other non-ASCII characters, or a tilde `"~"`, the compilation does not work well. In such cases, please use [`%DOCFILE%`](Compile#placeholders) instead of `%DOC%` in your recipes. See also [LaTeX recipes](Compile#latex-recipes). Note that using relative paths instead of absolute ones may lead to other issues, see the following issues for a discussion on this: [1070](https://github.com/James-Yu/LaTeX-Workshop/issues/1070) and [1137](https://github.com/James-Yu/LaTeX-Workshop/issues/1137).

On some platforms, `synctex` does not work well with the path containing non-ASCII characters either. In such cases, please use a built-in `synctex` functionality.
See [Viewing & Synctex](View#latex-workshopsynctexsynctexjsenabled).

## IME doesn't work well with LaTeX Workshop

Please try setting [`latex-workshop.bind.enter.key`](Environments#latex-workshopbindenterkey) to `false`.

## The LaTeX sidebar keeps reopening

If you like to work with no sidebar in Visual Studio Code and yet the LaTeX sidebar keeps showing up each time you switch focus from a non TeX file to a TeX file, you need to set `latex-workshop.view.autoFocus.enabled` to `false`.

## Spell check

[LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) is a great tool for checking spelling, grammar and style in many languages. If you only need spell checking, [Code Spellchecker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) does a great job, too.

## I cannot nest snippets

Nesting snippets requires to have intellisense automatically triggered inside snippets. This can be achieved by setting `editor.suggest.snippetsPreventQuickSuggestions` to `false`.

## How to pass `-shell-escape` to `latexmk`

Some packages such as `minted` requires `LaTeX` compilers to use the `-shell-escape` flag. Passing this flag can be achieved in several different ways.

1. Modify the section of `latex-workshop.latex.tools` related to `latexmk` in the following way

    ```json
    "name": "latexmk",
    "command": "latexmk",
    "args": [
        "-shell-escape",
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "-outdir=%OUTDIR%",
        "%DOC%"
    ]
    ```

1. Directly specify `-shell-escape` in the compiler flag of `latexmk`. Modify the section of `latex-workshop.latex.tools` related to `latexmk` in the following way

    ```json
    "name": "latexmk",
    "command": "latexmk",
    "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "-pdflatex=pdflatex -shell-escape %O %S",
        "-outdir=%OUTDIR%",
        "%DOC%"
    ]
    ```

1. Create a `.latexmkrc` config file (in your home directory or in the working directory) containing at least

    ```perl
    $pdflatex='pdflatex -shell-escape';
    ```

## LaTeX-Workshop shadows vscode's default keybindings

### LaTeX-Workshop uses <kbd>Ctrl</kbd>+<kbd>L</kbd> as the first key of many keybindings

Since vscode 1.32.0, <kbd>Ctrl</kbd>+<kbd>L</kbd> has been set to `expandLineSelection`. We define a new keybinding for `expandLineSelection`: <kbd>Ctrl</kbd>+<kbd>L</kbd>, <kbd>Ctrl</kbd>+<kbd>L</kbd>.

### LaTeX-Workshop uses <kbd>Ctrl</kbd>+<kbd>M</kbd> for fonts keybindings

vscode sets <kbd>Ctrl</kbd>+<kbd>M</kbd> to `editor.action.toggleTabFocusMode`. We define a new keybinding for `editor.action.toggleTabFocusMode`: <kbd>Ctrl</kbd>+<kbd>L</kbd>, <kbd>Ctrl</kbd>+<kbd>M</kbd>.

## Syntax Highlighting does not work for most elements

Please change VS Code theme you are using. For example, **Visual Studio Dark** and **Visual Studio Light** do not work with LaTeX Workshop.

## Install an older version of LaTeX Workshop

You can install older versions of LaTeX Workshop by right-clicking it in the extension panel of VS Code and selecting `Install Another Version`.

## Downgrade VS Code to an older version

You can downgrade VS Code to an older version with binaries in [each release note](https://code.visualstudio.com/updates/v1_46).

## Customizing a Color Theme

To customize a color theme, you can refer to the [official documentation](https://code.visualstudio.com/docs/getstarted/themes). The following is an example to make fonts black in math environment. Writing it in your `settings.json`, you can enable that. To find an appropriate scope for each element in a TeX document, you can use the scope inspector of VS Code. Please refer to [this document](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector).

```json
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": [
                    "support.class.math.block.environment.latex",
                ],
                "settings": {
                    "foreground": "#000000"
                }
            }
        ]
    }
```

## Move the structure view and others to other places

You can move the structure view and others with dragging and dropping. See the [release note](https://code.visualstudio.com/updates/v1_46#_flexible-layout). You can also hide the views in your right-click context menu. See the [document](https://code.visualstudio.com/docs/getstarted/userinterface#_views).

## Overriding snippets

You can override some snippets provided by the extension by using the [`latex-workshop.intellisense.command.user`](Intellisense#latex-workshopintellisensecommanduser) configuration variable. Since VS Code v1.52, you can hide snippets. See the [release note](https://code.visualstudio.com/updates/v1_52#_hide-extension-snippet).

## Where can I find the definitions of the placeholders

[Compile#placeholders](Compile#Placeholders)

## Autocompletion for `\includegraphics` seems incomplete

Autocompletion for `includegraphics` takes into account the paths listed by the `\graphicspath` command if any. In such a case, we only list the files located under these directories. See also the configuration variables referenced [here](Intellisense#files)

## Environment variables in `.bashrc` don't take effect with VS Code Remote

Use `.bash_profile` or `.profile` instead of `.bashrc`. See [superuser](https://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile), [stackoverflow](https://stackoverflow.com/questions/18791486/differences-uses-and-similarities-between-bashrc-bash-profile-and-etc-profil), and the [reference manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bash-Startup-Files).

After editing these files, you have to kill `vscode-server`  on the remote host and restart it. Select `Remote-SSH: Kill VS Code Server on Host...` from the Command Palette (F1).

## Environment variables in `.zshrc` don't take effect with VS Code Remote

Use `.zshenv` or `.zprofile` instead of `.zshrc`. See [stackexchange](https://unix.stackexchange.com/questions/71253/what-should-shouldnt-go-in-zshenv-zshrc-zlogin-zprofile-zlogout).

After editing these files, you have to kill `vscode-server`  on the remote host and restart it. Select `Remote-SSH: Kill VS Code Server on Host...` from the Command Palette (F1).

## You cannot use a tilde `~` in `PATH`

You can not use a tilde `~` in the environment variable `PATH` as an abbreviation of your home directory.

## `terminal.integrated.shellArgs.linux` doesn't take effect

The setting `terminal.integrated.shellArgs.linux` is not related to the environment variable on the extension host. You cannot set `PATH` for LaTeX Workshop through the setting.

## What kinds of LaTeX commands does Hover Preview support?

We implement Hover Preview with MathJax. Please see the following for LaTeX commands supported by MathJax:

- http://docs.mathjax.org/en/latest/input/tex/macros/index.html

You have to load [MathJax extensions](http://docs.mathjax.org/en/latest/input/tex/extensions/index.html) for some LaTeX commands. See [the setting](Hover#latex-workshophoverpreviewmathjaxextensions). Notice that MathJax does not support other advanced LaTeX packages.

## Hover Preview fails to render math equation with errors

Please try setting [`latex-workshop.hover.preview.newcommand.parseTeXFile.enabled`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Hover#latex-workshophoverpreviewnewcommandparsetexfileenabled) to `false`.

## The file `settings.json` doesn't have default values of settings

Enter a configuration id you want to configurate, e.g. `"latex-workshop.latex.recipes"`, then trigger auto-completion of VS Code. Related issues, [#127819](https://github.com/microsoft/vscode/issues/127819), [#134908](https://github.com/microsoft/vscode/issues/134908).

## Why don't you integrate the recipe system with the VS Code task feature?

The VS Code task feature doesn't fit our needs.

## How to prevent the internal PDF viewer from opening when selecting a PDF file in the explorer?

Set `"workbench.list.openMode": "doubleClick"` in `settings.json`. See [the document](https://code.visualstudio.com/docs/getstarted/settings#_default-settings).

## Can I define my own listing environment?

Any environment matching `[a-zA-Z]*code` is considered as a code / listing environment. This is the best we can offer as the textmate engine used for colorization does not allow user configuration.
