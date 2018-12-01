# FAQ and common issues

- [Known incompatible extensions](#Known-incompatible-extensions)
- [The Problem Pane displays wrong messages](#The-Problem-Pane-displays-wrong-messages)
- [I cannot use `ctrl`+`alt` in a shortcut](#I-cannot-use-ctrlalt-in-a-shortcut)
- [Disable automatic build on save](#disable-automatic-build-on-save)
- [My file is built when I paste](#my-file-is-built-when-I-paste)

## Known incompatible Extensions

The following extensions are known to cause issues when active at the same time as LaTeX-Workshop, namely a significant delay when using the Enter key in large files.

- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright)
- [Brackets Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
- [Prettify Symbols Mode](https://marketplace.visualstudio.com/items?itemName=siegebell.prettify-symbols-mode)

## The Problem Pane displays wrong messages

LaTeX compilers usually produce hard wrapped log messages, which makes them really hard to parse. To hopefully deal with complex log messages, we have decided to rely on non hard wrapped log messages. This can be achieved either

- by setting the environment variable `max_print_line`. This is automatically done within the extension and works for the TeXLive distribution.
- by adding the `--max-print-line` option to the compilers. This is automatically done within the extension and works for the MiKTeX distribution. Unfortunately, some compilers such as `lualatex` or `xelatex` do not understand this option and may therefore fail. To disable the automatic addition of this option, set `latex-workshop.latex.option.maxPrintLine.enabled` to `false`.

Note that when log messages are hard wrapped, the _Problems Pane_ may be messed up.

## I cannot use `ctrl`+`alt` in a shortcut

The default shortcuts for commands related to build and view use the modifiers <kbd>ctrl</kbd>+<kbd>alt</kbd>. On some keyboard layouts, <kbd>ctrl</kbd>+<kbd>alt</kbd> is used to emulate <kbd>AltrGr</kbd>, which makes these shortcuts unusable. Alternatively, you can use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>letter</kbd> instead of <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>letter</kbd> by setting `latex-workshop.bind.altKeymap.enabled` to `true` (you need reload/reopen vscode for the change to be taken into account).

## Disable automatic build on save

Set the configuration variable `latex-workshop.latex.autoBuild.onSave.enabled` to `false`.

## My file is built when I paste

Set `editor.formatOnPaste` to `false`.

The formatter programm `latexindent` changes the file on disk when formatting and not only the buffer content. VSCode interprets it as a file save and triggers a build if `latex-workshop.latex.autoBuild.onSave.enabled` to `true`
