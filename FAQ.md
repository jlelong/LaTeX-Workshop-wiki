# FAQ and common issues

- [Known incompatible extensions](#Known-incompatible-extensions)
- [Cygwin is not supported](#Cygwin-is-not-supported)
- [WSL is not officially supported](#WSL-is-not-officially-supported)
- [The directory ~/node_modules/ may cause errors](#The-directory-node_modules-may-cause-errors)
- [I cannot build from a subfile](#I-cannot-build-from-a-subfile)
- [The Problem Pane displays wrong messages](#The-Problem-Pane-displays-wrong-messages)
- [I cannot use `ctrl`+`alt` in a shortcut](#I-cannot-use-ctrlalt-in-a-shortcut)
- [Disable automatic build on save](#disable-automatic-build-on-save)
- [I use build on save but I occasionally want to save without building](#I-use-build-on-save-but-I-occasionally-want-to-save-without-building)
- [My file is built when I paste](#my-file-is-built-when-I-paste)
- [Format on save does not work](#format-on-save-does-not-work)
- [My file gets messed up](#my-file-gets-messed-up)
- [Large bibtex files are ignored](#large-bibtex-files-are-ignored)
- [Path containing Chinese characters](#Path-containing-Chinese-characters)
- [The LaTeX sidebar keeps reopening](#the-latex-sidebar-keeps-reopening)
- [Spell check](#spell-check)
- [I cannot nest snippets](#i-cannot-nest-snippets)
- [Some `@` snippets are not `TAB` completed](#some--snippets-are-not-tab-completed)
- [How to pass `-shell-escape` to `latexmk`](#how-to-pass--shell-escape-to-latexmk)
- [LaTeX-Workshop shadows vscode's default keybindings](#latex-workshop-shadows-vscodes-default-keybindings)

## Known incompatible Extensions

The following extensions are known to cause issues when active at the same time as LaTeX-Workshop, namely high CPU load issues, and a significant delay when using the Enter key in large files.

- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright)
- [Brackets Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
- [Prettify Symbols Mode](https://marketplace.visualstudio.com/items?itemName=siegebell.prettify-symbols-mode)

## Cygwin is not supported

LaTeX Workshop does not support TeX Live installed through Cygwin. Please install TeX Live and other TeX distributions independently of Cygwin.

## WSL is not officially supported

LaTeX Workshop does not officially support TeX Live installed through WSL. You can refer to a [setting](https://github.com/James-Yu/LaTeX-Workshop/issues/904#issuecomment-476741279) for TeX Live on WSL. Even with the setting, synctex does not work well. You have to write a wrapper command to make synctex work. We recommend you to install TeX Live and other TeX distributions independently of WSL.

## The directory ~/node_modules/ may cause errors

The directory `~/node_modules/` in the home directory may cause errors on Mac and Linux. The modules in the directory might be unintentionally loaded by VSCode because of the [default behavior](https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders) of node.js, which would cause errors such as _Extension host terminated unexpectedly_. We recommend moving the directory `~/node_modules/` to `~/npm/node_modules/`.

## I cannot build from a subfile

If you cannot build a multi file LaTeX project from a subfile, it means that the root file is not detected properly. See the [Multi file projects](multi-file-projects) page for details on how the root file is discovered. Note that you must open the directory (or one of its antecedents) containing all the project files in vscode for this mechanism to work.

## The Problem Pane displays wrong messages

LaTeX compilers usually produce hard wrapped log messages, which makes them really hard to parse. To hopefully deal with complex log messages, we have decided to rely on non hard wrapped log messages. This can be achieved either

- by setting the environment variable `max_print_line`. This is automatically done within the extension and works for the TeXLive distribution.
- by adding the `--max-print-line` option to the compilers. This is automatically done within the extension and works for the MiKTeX distribution. Unfortunately, some compilers such as `lualatex` do not understand this option and may therefore fail. To disable the automatic addition of this option, set `latex-workshop.latex.option.maxPrintLine.enabled` to `false`.

Note that when log messages are hard wrapped, the _Problems Pane_ is likely to be messed up.

## I cannot use `ctrl`+`alt` in a shortcut

The default shortcuts for commands related to build and view use the modifiers <kbd>ctrl</kbd>+<kbd>alt</kbd>. On some keyboard layouts, <kbd>ctrl</kbd>+<kbd>alt</kbd> is used to emulate <kbd>AltrGr</kbd>, which makes these shortcuts unusable. Alternatively, you can use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>letter</kbd> instead of <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>letter</kbd> by setting `latex-workshop.bind.altKeymap.enabled` to `true` (you need reload/reopen vscode for the change to be taken into account).

## Disable automatic build on save

Set the configuration variable `latex-workshop.latex.autoBuild.run` to `"never"`.

## I use build on save but I occasionally want to save without building

When `latex-workshop.latex.autoBuild.run` is set to `onFileChange`, building is triggered every time a file is saved. If you want to save a file without building it, you can use the `Save without Building` command from the _Command Palette_.

## My file is built when I paste

Set `editor.formatOnPaste` to `false`.

The formatting program `latexindent` changes the file on disk when formatting and not only the buffer content. VSCode interprets it as a file change and triggers a build if `latex-workshop.latex.autoBuild.run` to `"onFileChange"`

## Format on save does not work

This is a known issue but we cannot do much from the extension side.

The formatting utility `latexindent` reads its input from the file on the disk and not from the content of the editor. So when using _Format on Save_, first you format the file on the disk and then you save the content of the buffer. This is obviously done in the wrong order, but we cannot do much from the extension side to fix this. Note that if you save twice, the editor content is indeed formatted. When using _RightClick->Format Document_, we first save the buffer before calling the formatting program.

## My file gets messed up

This is most likely related to the two following variables being set together `latex-workshop.latex.autoBuild.run: "onFileChange"` and `editor.formatOnSave: true`.

Formatting a .tex file actually changes it on the disk and then if `latex-workshop.latex.autoBuild.run` is `"onFileChange"` it saves the file and triggers a build. You will get two formatting processes running together and using the same temporary file. Hence, the mess you see in your file.

## Large bibtex files are ignored

Bibtex files listed in a project are parsed for citation completion. This may induce significant slow down with large bibtex files. You can configure the maximum size of bibtex files parsed by the extension with [`latex-workshop.intellisense.citation.maxfilesizeMB"`](Intelissense#latex-workshopintellisensecitationmaxfilesizeMB).

## Path containing Chinese characters

On some platforms, when the path of a TeX file contains Chinese characters or other non-ASCII characters,
the compilation does not work well. In such cases, please use `%DOCFILE%` instead of `%DOC%` in your recipes. See also [LaTeX recipes](Compile#LaTeX-recipes).

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
