# Compiling features

## Building the document

A LaTeX file is typically built by calling the command _Build LaTeX project_ from the _Command Palette_ or from the _TeX_ badge. This command is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>b</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut). The recipe called by this command is defined by [`latex-workshop.latex.recipe.default`](#latex-workshop.latex.recipe.default).

If you have a multi-file project, see [multi-files-projects](Multi-File-Projects.md) for more details on how the root file is discovered.

You can define several compiling toolchains to build LaTeX projects using [LaTeX recipes](#latex-recipes) and then call the command _Build with recipe_ to choose the appropriate toolchain for actually building the project. Alternatively, you can directly select the appropriate recipe from the _TeX_ badge.

The following settings are helpful to customize how to build a project and how to deal with failures.

| Setting key                                               | Description                                                                                           | Default  | Type                 |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- | -------------------- |
| [`latex-workshop.latex.autoBuild.run`](#auto-build-latex) | When the extension shall auto build LaTeX project using [the default (first) recipe](#latex-recipes). | `onFileChange` | _string_             |
| [`latex-workshop.latex.recipes`](#latex-recipes)          | Sequence of tools to run for building                                                                 |          | _JSON object_        |
| [`latex-workshop.latex.tools`](#latex-recipes)            | Tools available for building                                                                          |          | _JSON object_        |
| [`latex-workshop.latex.magic.args`](#magic-comments)      | Arguments for the `TeX program`                                                                       |          | _array_ of _strings_ |
| [`latex-workshop.latex.magic.bib.args`](#magic-comments)  | Arguments for the `BIB program`                                                                       |          | _array_ of _strings_ |

## Terminating the current compilation

It is possible to terminate the current compilation by calling `Kill LaTeX compiler process` from the _Command Palette_ or calling `Terminate current compilation` from the TeX badge in the Build LaTeX project item.

## Auto build LaTeX

Besides manually calling the `Build LaTeX Project` command to compile a document, you may also let the extension automatically start compiling it upon file change. This can be defined in `latex-workshop.latex.autoBuild.run`. The recipe called by auto build is defined by [`latex-workshop.latex.recipe.default`](#latex-workshop.latex.recipe.default).

### latex-workshop.latex.autoBuild.run

When to trigger automatic building.

|   type   |  default value   |      possible values       |
| -------- | ---------------- | -------------------------- |
| _string_ | `"onFileChange"` | `"never"`,`"onFileChange"` |

- `"never"`: Disable the auto build feature
- `"onFileChange"`: Build the project upon detecting a file change in any of the dependencies. The file can even be modified outside vscode. See [here](Multi-File-Projects) for explanations on what dependencies are and how some of them can be ignored.

### latex-workshop.latex.autoBuild.interval

The minimal time interval between two consecutive auto builds in milliseconds.

|   type    |  default value   |
| --------- | ---------------- |
| _integer_ | `1000`           |

## Cleaning generated files

LaTeX compilation typically generates several auxiliary files. They can be removed by calling _Clean up auxiliary files_ from the _Command Palette_ or from the _TeX_ badge. This command is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut).

| Setting key                                            | Description                                                                                                               | Default   | Type               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------ |
| `latex-workshop.latex.autoBuild.cleanAndRetry.enabled` | Enable cleaning and building once more after errors in the build toolchain                                                | `true`    | _boolean_          |
| `latex-workshop.latex.autoClean.run`                   | Define when LaTeX auxillary files should be deleted.                                                                      | `"never"` | _string_           |
| `latex-workshop.latex.clean.fileTypes`                 | Extensions of files to clean                                                                                              |           | _array of strings_ |
| `latex-workshop.latex.clean.subfolder.enabled`         | Clean LaTeX auxillary files recursively in sub-folders of [`latex-workshop.latex.outDir`](View#latex-workshoplatexoutDir) | false     | _boolean_          |

### latex-workshop.latex.autoClean.run

| type     | default value | possible values                     |
| -------- | ------------- | ----------------------------------- |
| _string_ | `"never"`     | `"never"`,`"onFailed"`, `"onBuilt"` |

- `"never"`: Disable the auto cleaning feature
- `"onFailed"`: Clean the project upon failed compilation.
- `"onBuilt"`: Clean the project upon completing a compilation, whether it is successful or not.

## LaTeX recipes

A LaTeX recipe refers to a sequence/array of commands which LaTeX Workshop executes sequentially when building LaTeX projects. It is defined by `latex-workshop.latex.recipes`. By default, LaTeX Workshop includes two basic recipes defined by the variables `latex-workshop.latex.recipes` and `latex-workshop.latex.tools`:

- The first one simply relies on the `latexmk` command
- The second one run the following sequence of commands `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

```
[
  {
    "name": "latexmk 🔃",
    "tools": [
      "latexmk"
    ]
  },
  {
    "name": "pdflatex ➞ bibtex ➞ pdflatex`×2",
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
    ],
    "env": {}
  },
  {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOC%"
    ],
    "env": {}
  },
  {
    "name": "bibtex",
    "command": "bibtex",
    "args": [
      "%DOCFILE%"
    ],
    "env": {}
  }
]
```

You can create multiple recipes with different tools. Each recipe is an object in the configuration list, consisting of a `name` field and a list of `tools` to be invoked in the recipe.

The `tools` in recipes can be defined in `latex-workshop.latex.tools`, in which each command is a `tool`. Each tool is an object consisting of a `name`, a `command` to be spawned, its arguments (`args`) and some specific environment variables (`env`). The `env` entry is a dictionary. Imagine you want to use a `texmf` subdirectory local to your home project, just write

```
  "env": {
      "TEXMFHOME": "%DIR%/texmf"
  }
```

To include a tool in a recipe, the tool's `name` should be included in the recipe's `tools` list.

When building the project, the [magic comments](#magic-comments) in the root file is used if given, otherwise the first recipe is used. You can compile with another recipe by command `latex-workshop.recipes`. By default [`latexmk`](http://personal.psu.edu/jcc8/software/latexmk/) is used. This tool is bundled in most LaTeX distributions, and requires perl to execute. For non-perl users, the following `texify` toolchain from MikTeX may worth a try:

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
  ],
    "env": {}
}]
```

The `args` and `env` parameters can contain symbols surrounded by `%`. These placeholders are replaced on-the-fly. LaTeX Workshop registers the following placeholders:

| Placeholder | Replaced by                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------- |
| `%DOC%`     | The LaTeX root file path and name without the `.tex` extension                                     |
| `%DOCFILE%` | The LaTeX root file name without the `.tex` extension                                              |
| `%DIR%`     | The LaTeX root file path                                                                           |
| `%TMPDIR%`  | A temporary folder for storing ancillary files                                                     |
| `%OUTDIR%`  | The output directory configured in [`latex-workshop.latex.outDir`](View#latex-workshoplatexoutDir) |

Alternatively, you can also set your commands without the placeholder, just like what you may input in a terminal.
As most LaTeX compiler accepts root file name without extension, `%DOC%` and `%DOCFILE%` do not include `.tex` extension. Meanwhile, `texify` requires the extension. So in the above tool `%DOC%` and `.tex` are concatenated for completeness.

### latex-workshop.latex.recipe.default

Define which recipe is used by the _Build LaTeX project_ command.

|   type   | default value |    possible values     |
| -------- | ------------- | ---------------------- |
| _string_ | `"first"`     | `"first"`,`"lastUsed"` |

- `"first"`: Use the first recipe defined in [`latex-workshop.latex.recipes`](#LaTeX-recipes).
- `"lastUsed"`: Use the last used recipe by the command _LaTeX Workshop: Build with recipe_.


## External build command

Versatile though the recipe mechanism described above may be, it may fail to match your needs when building the whole LaTeX project is done by a personal script or a Makefile. For this particular case, we provide an external build command mechanism, which completely bypasses the recipe machinery. Just define your command along with its arguments using

```
"latex-workshop.latex.external.build.command": {
  "command": "",
  "args": [
    ""
  ]
}
```

## Magic comments

### TeX programm and options

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

Alternatively, you can directly define the args in the `.tex` file by using the magic comment `! %TEX options`, which overrides `latex-workshop.latex.magic.args`. Note that it must contain the file to proceed. For instance, to reproduce the default behavior, you should use

```
% !TEX options = -synctex=1 -interaction=nonstopmode -file-line-error "%DOC%"
```

Suppose there is a line `% !TEX program = xelatex` in the root file. Upon building the project, LaTeX Workshop will parse the root file and figure out that `xelatex` should be used.

### BIB program and options

When using `% !TEX program` with bibliographies, a `bib` compiler must be defined with `% !BIB program` comment, e.g., `% !BIB program = bibtex`. Otherwise the extension will only run one-pass compilation with the specified LaTeX compiler. If needed, you can pass extra arguments to the `!BIB program` using the `latex-workshop.latex.magic.bib.args` variable:

```
"latex-workshop.latex.magic.bib.args": [
  "%DOCFILE%"
]
```

Alternatively, you can directly define the args in the `.tex` file by using the magic comment `! %BIB options`, which overrides `latex-workshop.latex.magic.bib.args`. Note that it must contain the file to proceed. For instance, to reproduce the default behavior, you should use `! %BIB options = "%DOCFILE%"`.



## Catching errors and warnings

The warnings and errors issued by the compiling toolchain are rendered in the _Problems_ Pane. The following settings enable you to customize what you want to get in that panel. If the messages displayed in the panel seem to be wrong, see the [FAQ](#The-Problem-Pane-displays-wrong-messages).

The raw compiler logs can be accessed in the _Output Pane_, choose _LaTeX Compiler_. The default is to clear the logs before calling every tool of a recipe. If you prefer to keep the logs from all the tools of a recipe, set [`latex-workshop.latex.build.clearLog.everyRecipeStep.enabled`](latex-workshoplatexbuildclearLogeveryRecipeStepenabled) to `false`.

### Settings Details

#### latex-workshop.message.log.show

Display LaTeX Workshop debug log in output panel.

This property defines whether LaTeX Workshop will output its debug log to the log panel.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### latex-workshop.message.badbox.show

Show badbox information in the problems panel.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### latex-workshop.message.latexlog.exclude

Exclude log messages that matches the given regexp from the problems panel.

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

#### latex-workshop.message.information.show

Display information messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.message.warning.show

Display warning messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### latex-workshop.message.error.show

Display error messages in popup notifications.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### latex-workshop.message.update.show

Display LaTeX Workshop update message on new versions.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### latex-workshop.latex.build.clearLog.everyRecipeStep.enabled

Clear the LaTeX Compiler logs before every step of a recipe.

Set this property to false to keep the logs of all tools in a recipe.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |
