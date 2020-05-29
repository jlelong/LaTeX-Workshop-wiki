# FAQ and common issues

- [Known incompatible extensions](#known-incompatible-extensions)
- [Using LaTeX Workshop with WSL](#using-latex-workshop-with-wsl)
- [Using with Linux under Virtual Box, VM Workstation Player, Crostini, and others.](#using-with-linux-under-virtual-box-vm-workstation-player-crostini-and-others)
- [Cygwin is not supported](#cygwin-is-not-supported)
- [code-server is not supported](#code-server-is-not-supported)
- [Visual Studio Online with self-hosted environments is not supported](#visual-studio-online-with-self-hosted-environments-is-not-supported)
- [Visual Studio Live Share is not supported](#visual-studio-live-share-is-not-supported)
- [File watcher does not work when used with OneDrive or a network drive](#file-watcher-does-not-work-when-used-with-onedrive-or-a-network-drive)
- [The directory ~/node_modules/ may cause errors](#the-directory-node_modules-may-cause-errors)
- [The extension freezes when used with a network drive](#The-extension-freezes-when-used-with-a-network-drive)
- [I cannot build from a subfile](#i-cannot-build-from-a-subfile)
- [The Problem Pane displays wrong messages](#the-Problem-Pane-displays-wrong-messages)
- [Encoding issues with file names in the Problem Pane](#Encoding-issues-with-file-names-in-the-Problem-Pane)
- [I cannot use `ctrl`+`alt` in a shortcut](#i-cannot-use-ctrlalt-in-a-shortcut)
- [Disable automatic build on save](#disable-automatic-build-on-save)
- [I use build on save but I occasionally want to save without building](#I-use-build-on-save-but-I-occasionally-want-to-save-without-building)
- [Large bibtex files are ignored](#large-bibtex-files-are-ignored)
- [Path containing Chinese or `~` characters](#path-containing-chinese-or--characters)
- [The LaTeX sidebar keeps reopening](#the-latex-sidebar-keeps-reopening)
- [Spell check](#spell-check)
- [I cannot nest snippets](#i-cannot-nest-snippets)
- [Some `@` snippets are not `TAB` completed](#some--snippets-are-not-tab-completed)
- [How to pass `-shell-escape` to `latexmk`](#how-to-pass--shell-escape-to-latexmk)
- [LaTeX-Workshop shadows vscode's default keybindings](#latex-workshop-shadows-vscodes-default-keybindings)
- [Syntax Highlighting does not work for most elements](#syntax-highlighting-does-not-work-for-most-elements)
- [Install older version](#install-older-version)
- [Customizing a Color Theme](#customizing-a-color-theme)
- [Overriding snippets](#overriding-snippets)
- [Autocompletion for `\includegraphics` seems incomplete](#autocompletion-for-includegraphics-seems-incomplete)

## Known incompatible Extensions

The following extensions are known to cause issues when active at the same time as LaTeX-Workshop

- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright): high CPU load, Enter key delay
- [Brackets Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2): high CPU load, Enter key delay
- [Prettify Symbols Mode](https://marketplace.visualstudio.com/items?itemName=siegebell.prettify-symbols-mode): high CPU load, Enter key delay
- [Path Autocomplete](https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete): it may break autocompletion for bibliography citations.
- [LaTeX Preview](https://marketplace.visualstudio.com/items?itemName=ajshort.latex-preview): Conflict with LaTeX Workshop.



## Using LaTeX Workshop with WSL

Starting with 1.35.0, VS Code supports WSL through [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). LaTeX Workshop works well with the extension.

Also, in WSL2 file watchers might not work. For now, you have to set [`latex-workshop.latex.watch.usePolling`](Compile#latex-workshoplatexwatchusepolling) to `true`, and restart VS Code. See https://github.com/microsoft/WSL/issues/4739 for more information about the issue.

## Using with Linux under Virtual Box, VM Workstation Player, [Crostini](https://chromium.googlesource.com/chromiumos/docs/+/master/containers_and_vms.md), and others.

Display problems can occur. In that case, start VS Code with `--disable-gpu`. See [official doc](https://code.visualstudio.com/docs/supporting/FAQ#_vs-code-is-blank), [realted issue](https://github.com/microsoft/vscode/issues/92970), and [another issue](https://github.com/James-Yu/LaTeX-Workshop/issues/1935).

## Cygwin is not supported

LaTeX Workshop does not support TeX Live installed through Cygwin. Please install TeX Live and other TeX distributions independently of Cygwin.

## code-server is not supported

LaTeX Workshop does not support [code-server](https://github.com/cdr/code-server).

## Visual Studio Online with self-hosted environments is not supported

Visual Studio Online with [self-hosted environments](https://docs.microsoft.com/en-us/visualstudio/online/how-to/vscode#self-hosted) is not supported.

## Visual Studio Live Share is not supported

[Visual Studio Live Share](https://marketplace.visualstudio.com/items?itemName=ms-vsliveshare.vsliveshare) is not supported.

## File watcher does not work when used with OneDrive or a network drive

When your files are located inside `OneDrive` or a network drive, you have to set [`latex-workshop.latex.watch.usePolling`](Compile#latex-workshoplatexwatchusepolling) to `true`, and restart VS Code.

## The directory ~/node_modules/ may cause errors

The directory `~/node_modules/` in the home directory may cause errors on Mac and Linux. The modules in the directory might be unintentionally loaded by VSCode because of the [default behavior](https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders) of node.js, which would cause errors such as _Extension host terminated unexpectedly_. We recommend moving the directory `~/node_modules/` to `~/npm/node_modules/`.

## I cannot build from a subfile

If you cannot build a multi file LaTeX project from a subfile, it means that the root file is not detected properly. See the [Multi file projects](Compile#multi-file-projects) section for details on how the root file is discovered. Note that you must open the directory (or one of its antecedents) containing all the project files in vscode for this mechanism to work.

## The Problem Pane displays wrong messages

LaTeX compilers usually produce hard wrapped log messages, which makes them really hard to parse. To hopefully deal with complex log messages, we have decided to rely on non hard wrapped log messages. This can be achieved either

- by setting the environment variable `max_print_line`. This is automatically done within the extension and works for the TeXLive distribution.
- by adding the `--max-print-line` option to the compilers. This is automatically done within the extension and works for the MiKTeX distribution. Unfortunately, some compilers such as `lualatex` do not understand this option and may therefore fail. To disable the automatic addition of this option, set `latex-workshop.latex.option.maxPrintLine.enabled` to `false`.

Note that when log messages are hard wrapped, the _Problems Pane_ is likely to be messed up.

## Encoding issues with file names in the Problem Pane

If you experience encoding issues with file names displayed in the Problem Pane, you can try to set `latex-workshop.message.convertFilenameEncoding` to `false`.

## I cannot use `ctrl`+`alt` in a shortcut

The default shortcuts for commands related to build and view use the modifiers <kbd>ctrl</kbd>+<kbd>alt</kbd>. On some keyboard layouts, <kbd>ctrl</kbd>+<kbd>alt</kbd> is used to emulate <kbd>AltrGr</kbd>, which makes these shortcuts unusable. Alternatively, you can use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>letter</kbd> instead of <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>letter</kbd> by setting `latex-workshop.bind.altKeymap.enabled` to `true`.

## Disable automatic build on save

Set the configuration variable `latex-workshop.latex.autoBuild.run` to `"never"`.

## I use build on save but I occasionally want to save without building

When `latex-workshop.latex.autoBuild.run` is set to `onFileChange`, building is triggered every time a file is saved. If you want to save a file without building it, you can use the `Save without Building` command from the _Command Palette_. A keybinding can be associated to the internal command `latex-workshop.saveWithoutBuilding` to access this feature more easily.

## Large bibtex files are ignored

Bibtex files listed in a project are parsed for citation completion. This may induce significant slow down with large bibtex files. You can configure the maximum size of bibtex files parsed by the extension with [`latex-workshop.intellisense.citation.maxfilesizeMB`](Intellisense#latex-workshopintellisensecitationmaxfilesizeMB).

## Path containing Chinese or `~` characters

On some platforms, when the path of a TeX file contains Chinese characters or other non-ASCII characters,
the compilation does not work well. In such cases, please use `%DOCFILE%` instead of `%DOC%` in your recipes. See also [LaTeX recipes](Compile#LaTeX-recipes). Note that using relative paths instead of absolute ones may lead to other issues, see the following issues for a discussion on this: [1070](https://github.com/James-Yu/LaTeX-Workshop/issues/1070) and [1137](https://github.com/James-Yu/LaTeX-Workshop/issues/1137).

On some platforms, `synctex` does not work well with the path containing non-ASCII characters either. In such cases, please use a built-in `synctex` functionality.
See [Viewing & Synctex](View#latex-workshopsynctexsynctexjsenabled).

## The LaTeX sidebar keeps reopening

If you like to work with no sidebar in Visual Studio Code and yet the LaTeX sidebar keeps showing up each time you switch focus from a non TeX file to a TeX file, you need to set `latex-workshop.view.autoFocus.enabled` to `false`.

## Spell check

[Code Spellchecker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) did a great job. Users may also find other extensions better alternatives, e.g., [LanguageTool](https://marketplace.visualstudio.com/items?itemName=adamvoss.vscode-languagetool) credited for its multi-lingual support.

## I cannot nest snippets

Nesting snippets requires to have intellisense automatically triggered inside snippets. This can be achieved by setting `editor.suggest.snippetsPreventQuickSuggestions` to `false`.

## Some `@` snippets are not `TAB` completed

This is mostly related to the `editor.quickSuggestions` setting. The following value works well

```
"editor.quickSuggestions": {
        "other": true,
        "comments": false,
        "strings": false
      }
```

It is known that setting `"other": false` will prevent some `@` snippets from being `TAB` expanded.

## How to pass `-shell-escape` to `latexmk`

Some packages such as `minted` requires `LaTeX` compilers to use the `-shell-escape` flag. Passing this flag can be achieved in several different ways.

1. Modify the section of `latex-workshop.latex.tools` related to `latexmk` in the following way

    ````
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
    ````

1. Directly specify `-shell-escape` in the compiler flag of `latexmk`. Modify the section of `latex-workshop.latex.tools` related to `latexmk` in the following way

    ````
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
    ````

1. Create a `.latexmkrc` config file (in your home directory or in the working directory) containing at least

    ````
    $pdflatex='pdflatex -shell-escape';
    ````

## LaTeX-Workshop shadows vscode's default keybindings

### LaTeX-Workshop uses <kbd>Ctrl</kbd>+<kbd>L</kbd> as the first key of many keybindings

Since vscode 1.32.0, <kbd>Ctrl</kbd>+<kbd>L</kbd> has been set to `expandLineSelection`. We define a new keybinding for `expandLineSelection`: <kbd>Ctrl</kbd>+<kbd>L</kbd>, <kbd>Ctrl</kbd>+<kbd>L</kbd>.

### LaTeX-Workshop uses <kbd>Ctrl</kbd>+<kbd>M</kbd> for fonts keybindings

vscode sets <kbd>Ctrl</kbd>+<kbd>M</kbd> to `editor.action.toggleTabFocusMode`. We define a new keybinding for `editor.action.toggleTabFocusMode`: <kbd>Ctrl</kbd>+<kbd>L</kbd>, <kbd>Ctrl</kbd>+<kbd>M</kbd>.

## Syntax Highlighting does not work for most elements

Please change VS Code theme you are using. For example, **Visual Studio Dark** and **Visual Studio Light** do not work with LaTeX Workshop.

## Install older version

You can install older versions of LaTeX Workshop by right-clicking it in the extension panel of VS Code and selecting `Install Another Version`.

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

## Overriding snippets

You can override some snippets provided by the extension by using the [`latex-workshop.intellisense.commandsJSON.replace`](Intellisense#latex-workshopintellisensecommandsJSONreplace) configuration variable.

## Where can I find the definitions of the placeholders

[Compile#placeholders](Compile#Placeholders)

## Autocompletion for `\includegraphics` seems incomplete

Autocompletion for `includegraphics` takes into account the paths listed by the `\graphicspath` command if any. In such a case, we only list the files located under these directories. See also the configuration variables referenced [here](Intellisense#files)