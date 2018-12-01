# Compiling

| Shortcut                                    | Alternative                                               | Does                               |
| ------------------------------------------- | --------------------------------------------------------- | ---------------------------------- |
| <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>b</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>b</kbd> | Builds current file                |
| <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>alt</kbd>+<kbd>c</kbd> | clean latex build files            |

By default, the shortcuts are set according to the first column. You may switch to an alternative keymap by setting `latex-workshop.bind.altKeymap.enabled` to `true` and reload/reopen vscode. See also [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut).

## Relevant Settings

|                     Setting key                      |                    Description                    | Default |  Type   |
| ---------------------------------------------------- | ------------------------------------------------- | ------- | ------- |
| `latex-workshop.latex.autoBuild.onSave.enabled`      | Enable automatic build when saving any tex file   | `true`  | boolean |
| `latex-workshop.latex.autoBuild.onTexChange.enabled` | Enable LaTeX build after any tex file has changed | `false` | boolean |


## LaTeX recipe

A LaTeX recipe refers to a sequence/array of commands which LaTeX Workshop executes sequentially when building LaTeX projects. It is defined by `latex-workshop.latex.recipes`. By default, LaTeX Workshop includes two basic recipes: one simply running the `latexmk` command, and an other one running the typical sequence of commands `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

You can create multiple recipes with different tools. Each recipe is an object in the configuration list, consisting of a `name` field and a list of `tools` to be invoked in the recipe.

The `tools` in recipes can be defined in `latex-workshop.latex.tools`, in which each command is a `tool`. Each tool is an object consists of a `name`, a `command` to be spawned, and its arguments (`args`). To include a tool in a recipe, the tool's `name` should be included in the recipe's `tools` list.

When building the project, the first recipe is used. You can compile with another recipe by command `latex-workshop.recipes`. By default [`latexmk`](http://personal.psu.edu/jcc8/software/latexmk/) is used. This tool is bundled in most LaTeX distributions, and requires perl to execute. For non-perl users, the following `texify` toolchain from MikTeX may worth a try:
```
"latex-workshop.latex.recipes": [{
  "name": "texify",
  "tools": [
    "texify"
  ]
}],
"latex-workshop.latex.tools": [{
  "name": "texify",
  "command": "texify",
  "args": [
    "--synctex",
    "--pdf",
    "--tex-option=\"-interaction=nonstopmode\"",
    "--tex-option=\"-file-line-error\"",
    "%DOC%.tex"
  ]
}]
```
As you may notice, there is a mystic `%DOC%` in the arguments. Symbols surrounded by `%` are placeholders, which are replaced with its representing string on-the-fly. LaTeX Workshop registers the following placeholders:

| Placeholder | Replaced by                                                |
| ----------- | ---------------------------------------------------------- |
| `%DOC%`     | The LaTeX root file path and name without `.tex` extension |
| `%DOCFILE%` | The LaTeX root file name without `.tex` extension          |
| `%DIR%`     | The LaTeX root file path                                   |
| `%TMPDIR%`  | A temporary folder for storing ancillary files             |

Alternatively, you can also set your commands without the placeholder, just like what you may input in a terminal.
As most LaTeX compiler accepts root file name without extension, `%DOC%` and `%DOCFILE%` do not include `.tex` extension. Meanwhile, `texify` requires the extension. So in the above tool `%DOC%` and `.tex` are concatenated for completeness.

## Magic comments

LaTeX Workshop supports `% !TEX program` magic comment to specify the compiler program. However, it is advised to use the recipe system instead of magic program to define the building process, since the latter is only implemented for backward compatibility.

For `% !TEX program` magic comment, its arguments are defined in `latex-workshop.latex.magic.args`:
```
"latex-workshop.latex.magic.args": [
  "-synctex=1",
  "-interaction=nonstopmode",
  "-file-line-error",
  "%DOC%"
]
```
Suppose there is a line `% !TEX program = xelatex` in the root file. Upon building the project, LaTeX Workshop will parse the root file and figure out that `xelatex` should be used. Arguments are included to invoke the compiler.

When using `% !TEX program` with bibliographies, a `bib` compiler must be defined with `% !BIB program` comment, e.g., `% !BIB program = bibtex`. Otherwise the extension will only run one-pass compilation with the specified LaTeX compiler.