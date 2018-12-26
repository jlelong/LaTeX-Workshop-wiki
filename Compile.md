# Compiling features

## Building the document

A LaTeX file is typically built by calling the command _Build LaTeX project_ from the _Command Palette_ or from the _TeX_ badge. This command is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>b</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut).

You can define several compiling toolchains to build LaTeX projects using [LaTeX recipes](#latex-recipes) and then call the command _Build with recipe_ to choose the appropriate toolchain for actually building the project. Alternatively, you can directly select the appropriate recipe from the _TeX_ badge.

The following settings are helpful to customize how to build a project and how to deal with failures.

|                       Setting key                        |                     Description                      | Default |        Type        |
| -------------------------------------------------------- | ---------------------------------------------------- | ------- | ------------------ |
| `latex-workshop.latex.autoBuild.onSave.enabled`          | Enable automatic building when saving any tex file   | `true`  | _boolean_          |
| `latex-workshop.latex.autoBuild.onTexChange.enabled`     | Enable LaTeX building after any tex file has changed | `false` | _boolean_          |
| [`latex-workshop.latex.recipes`](#latex-recipe)          | Sequence of tools to run for building                |         | _JSON object_      |
| [`latex-workshop.latex.tools`](#latex-recipe)            | Tools available for building                         |         | _JSON object_      |
| [`latex-workshop.latex.magic.args`](#magic-comments)     | Arguments for the `TeX program`                      |         | _array of strings_ |
| [`latex-workshop.latex.magic.bib.args`](#magic-comments) | Arguments for the `BIB program`                      |         | _array of strings_ |

## Cleaning generated files

LaTeX compilation typically generates several auxiliary files. They can be removed by calling _Clean up auxiliary files_ from the _Command Palette_ or from the _TeX_ badge. This command is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see[the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut).

|                     Setting key                      |                    Description                    | Default |  Type   |
| ---------------------------------------------------- | ------------------------------------------------- | ------- | ------- |
| `latex-workshop.latex.autoBuild.cleanAndRetry.enabled` | Enable cleaning and building once more after errors in the build toolchain | `true` | _boolean_ |
| `latex-workshop.latex.clean.enabled` | Enable cleaning LaTeX auxiliary files after building project | `false` | _boolean_ |
| `latex-workshop.latex.clean.onFailBuild.enabled` | Enable cleaning LaTeX auxiliary files after a failed build | `false` | _boolean_ |
| `latex-workshop.latex.clean.fileTypes` | Extensions of files to clean |  | _array of strings_ |

## LaTeX recipes

A LaTeX recipe refers to a sequence/array of commands which LaTeX Workshop executes sequentially when building LaTeX projects. It is defined by `latex-workshop.latex.recipes`. By default, LaTeX Workshop includes two basic recipes defined by the variables `latex-workshop.latex.recipes` and `latex-workshop.latex.tools`:

- The first one simply relies on the `latexmk` command
- The second one run the following sequence of commands `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

```
[
  {
    "name": "latexmk",
    "tools": [
      "latexmk"
    ]
  },
  {
    "name": "pdflatex -> bibtex -> pdflatex*2",
    "tools": [
      "pdflatex",
      "bibtex",
      "pdflatex",
      "pdflatex"
    ]
  }
]
```

and each tool appearing in the `tools` field is defined `latex-workshop.latex.tools`. Its default value is given by

```
[
  {
    "name": "latexmk",
    "command": "latexmk",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "-outdir=%OUTDIR%",
      "%DOC%"
    ]
  },
  {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOC%"
    ]
  },
  {
    "name": "bibtex",
    "command": "bibtex",
    "args": [
      "%DOCFILE%"
    ]
  }
]
```

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

| Placeholder |                                               Replaced by                                                |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| `%DOC%`     | The LaTeX root file path and name without the `.tex` extension                                           |
| `%DOCFILE%` | The LaTeX root file name without the `.tex` extension                                                    |
| `%DIR%`     | The LaTeX root file path                                                                                 |
| `%TMPDIR%`  | A temporary folder for storing ancillary files                                                           |
| `%OUTDIR%`  | The output directory configured in [`latex-workshop.latex.outputDir`](View#latex-workshoplatexoutputDir) |

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

When using `% !TEX program` with bibliographies, a `bib` compiler must be defined with `% !BIB program` comment, e.g., `% !BIB program = bibtex`. Otherwise the extension will only run one-pass compilation with the specified LaTeX compiler. If needed, you can pass extra arguments to the `!BIB program` using the `latex-workshop.latex.magic.bib.args` variable:

```
"latex-workshop.latex.magic.bib.args": [
  "%DOCFILE%"
]
```

## Catching errors and warnings

The warnings and errors issued by the compiling toolchain are rendered in the _Problems_ Pane. The following settings enable you to customize what you want to get in that panel. If the messages displayed in the panel seem to be wrong, see the [FAQ](#The-Problem-Pane-displays-wrong-messages).

### latex-workshop.message.log.show

Display LaTeX Workshop debug log in output panel.

This property defines whether LaTeX Workshop will output its debug log to the log panel.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.message.badbox.show

Show badbox information in the problems panel.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.message.latexlog.exclude

Exclude log messages that matches the given regexp from the problems panel.

|       type        | default value |
| ----------------- | ------------- |
| _array of strings | `[]`          |

### latex-workshop.message.information.show

Display information messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.message.warning.show

Display warning messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.message.error.show

Display error messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.message.update.show

Display LaTeX Workshop update message on new versions.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |
