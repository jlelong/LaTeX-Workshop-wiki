# Compiling features

## Multi File projects

While it is fine to write all contents in one `.tex` file, it is common to split things up for simplicity. For such LaTeX projects, the file with `\begin{document}` is considered as the root file, which serves as the entry point to the project. LaTeX Workshop intelligently finds the root file when a new document is opened, the active editor is changed, or any LaTeX Workshop command is executed.

### The root file

To find the root file, LaTeX Workshop will follow the steps below, stopping whenever one is found:

1. **Magic comment** `% !TEX root = relative/or/absolute/path/to/root/file.tex`. If such comments exist in the currently active editor, the referred file is set as root. You can use the command `latex-workshop.addtexroot` to help you insert the magic comment.
1. **Self check** If current active editor contains `\begin{document}`, it is set as root.
1. **Root directory check** LaTeX Workshop iterates through all `.tex` files in the root folder of the workspace. The first one containing `\begin{document}` and which includes the file in the active editor is set as the root file. To avoid parsing all `.tex` files in the workspace, you can narrow the search by specifying [`latex-workshop.latex.search.rootFiles.include`](#latex-workshoplatexsearchrootFilesinclude) and/or [`latex-workshop.latex.search.rootFiles.exclude`](#latex-workshoplatexsearchrootFilesexclude).
1. **The `subfiles` package case** The main file is used to provide intellisense. The non-interactive functions `autobuild`, `autoclean` and forward `synctex` rely on the value of the configuration variable [`latex-workshop.latex.rootFile.useSubFile`](#latex-workshoplatexrootFileuseSubFile) to choose between the main file and the subfile.
    - if [`latex-workshop.latex.rootFile.doNotPrompt`](#latex-workshoplatexrootFiledoNotPrompt) is `false`,  all the interactive commands `build`, `clean` and `view` use a quick pick box to ask the user which file is to be considered as the root File.
    - if [`latex-workshop.latex.rootFile.doNotPrompt`](#latex-workshoplatexrootFiledoNotPrompt) is `true`,  all the interactive commands `build`, `clean` and `view` use variable [`latex-workshop.latex.rootFile.useSubFile`](#latex-workshoplatexrootFileuseSubFile) to choose between the main file and the subfile automatically.

    Note that each subfile has to be compiled from its respective directory, where LaTeX is able to locate all included text files or images. However, following the discussion in [1895](https://github.com/James-Yu/LaTeX-Workshop/issues/1895) we decided that all paths should be relative to the root file directory. Hence, the recipe is launched from the root file directory and the `-cd` option must be added to `latexmk`. As discussed in [1932](https://github.com/James-Yu/LaTeX-Workshop/issues/1932), this option breaks `makeindex` (this should be solved in the next release of `latexmk`). So the solution is to add a `.latexmkrc` file in the root file directory containing `$do_cd = 1;`

1. **The `.fls` files** LaTeX compilers when called with the `-recorder` option produce a file with `.fls` extension containing all the files _input_ and _output_ during compilation. The list of _input_ files contains all classes, packages, fonts, input `.tex` files, listings, graphs, ... Using `latexmk` always produces a `.fls` file.

If no root file is found, most of the features in LaTeX Workshop will not work.

**Note**: for all this to work, you have to open the directory (or one of its antecedents) containing the whole LaTeX project.

### The dependencies

Once the root file is determined, it is parsed to discover all the files it includes using `input`, `include`, `InputIfFileExists`, `subfile`, `import` and `subimport` and the process goes on recursively. All these files are called dependencies and are considered to define a LaTeX project. If you include some files located in some external directories, you can list these extra directories in [`latex-workshop.latex.texDirs`](#latex-workshoplatextexDirs).

Moreover, when a `.fls` file with the same basename as the root file exists, it is used to compute the full list of dependencies, ie all classes, packages, fonts, input `.tex` files, listings, graphs, ... All these files are parsed to provide intellisense completion. When  [`latex-workshop.latex.autoBuild.run`](Compile#auto-build-latex) is set to `onFileChange`, building is automatically triggered whenever any of the dependencies is modified. You can use [`latex-workshop.latex.watch.files.ignore`](#latex-workshoplatexwatchfilesignore) to prevent some files from being watched. The default is to ignore files inside your TeX distribution and files with `.code.tex` or `.sty` suffix.

### Relevant settings

#### latex-workshop.latex.search.rootFiles.include

Patterns of files to consider for the root detection mechanism.

Relative paths are computed from the workspace folder. To detect the root file and the tex file tree, we parse all the `.tex` listed here.\nIf you want to specify all `.tex` files inside directory, say `foo`, and all its subdirectories recursively, you need to use `**/foo/**/*.tex`. If you only want to match `.tex` files at the top level of the workspace, use `*.tex`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

|         type         | default value  |
| -------------------- | -------------- |
| _array_ of _strings_ | `["**/*.tex"]` |

#### latex-workshop.latex.search.rootFiles.exclude

Patterns of files to exclude from the root detection mechanism.

See also `latex-workshop.latex.search.rootFiles.include`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

#### latex-workshop.latex.texDirs

List of directories where to look for extra input `.tex` files.

Absolute paths are required. You may also need to set the environment variable `TEXINPUTS` properly for the LaTeX compiler to find the `.tex` files, see the `env` parameter of [recipes](#latex-recipes).

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

#### latex-workshop.latex.rootFile.useSubFile

When the `subfiles` package is used, either the main file or any subfile containing `\\documentclass[main.tex]{subfiles}` can be LaTeXing. When set to `true`, the extension uses the subfile as the rootFile for the `autobuild`, `clean` and `synctex` commands.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `true`        |

#### latex-workshop.latex.rootFile.doNotPrompt

When the `subfiles` package is used, either the main file or any subfile containing `\\documentclass[main.tex]{subfiles}` can be LaTeXing. When set to `false`, the `build` and `view` commands  ask the user's choice first. When set to `true`, the subfile is used when `latex-workshop.latex.rootFile.useSubFile` is also `true`, otherwise the rootFile is used.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `false`       |

## Building the document

A LaTeX file is typically built by calling the command _Build LaTeX project_ from the _Command Palette_ or from the _TeX_ badge. This command is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>b</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut). The recipe called by this command is defined by [`latex-workshop.latex.recipe.default`](#latex-workshoplatexrecipedefault).

If you have a multi-file project, see [multi-files-projects](#multi-file-projects) for more details on how the root file is discovered.

You can define several compiling toolchains to build LaTeX projects using [LaTeX recipes](#latex-recipes) and then call the command _Build with recipe_ to choose the appropriate toolchain for actually building the project. Alternatively, you can directly select the appropriate recipe from the _TeX_ badge.

The following settings are helpful to customize how to build a project and how to deal with failures.

| Setting key                                               | Description                                                                                           | Default  | Type                 |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- | -------------------- |
| [`latex-workshop.latex.autoBuild.run`](#auto-build-latex) | When the extension shall auto build LaTeX project using [the default (first) recipe](#latex-recipes). | `onFileChange` | _string_             |
| [`latex-workshop.latex.recipes`](#latex-recipes)          | Sequence of tools to run for building                                                                 |          | _JSON object_        |
| [`latex-workshop.latex.tools`](#latex-recipes)            | Tools available for building                                                                          |          | _JSON object_        |
| [`latex-workshop.latex.magic.args`](#magic-comments)      | Arguments for the `TeX program`                                                                       |          | _array_ of _strings_ |
| [`latex-workshop.latex.magic.bib.args`](#magic-comments)  | Arguments for the `BIB program`                                                                       |          | _array_ of _strings_ |
| [`latex-workshop.latex.build.forceRecipeUsage`](#latex-workshoplatexbuildforceRecipeUsage) | Force the use of recipes | false | _boolean_ |

when [`latex-workshop.progress.enabled`](latex-workshopprogressenabled) is set, a progress bar indicates the building progress. It can be customized using the following configuration variables

- [`latex-workshop.progress.location`](#latex-workshopprogresslocation)
- [`latex-workshop.progress.runIconType`](#latex-workshopprogressrunIconType)
- [`latex-workshop.progress.barLength`](#latex-workshopprogressbarLength)
- [`latex-workshop.progress.barStyle`](#latex-workshopprogressbarStyle)

## Building a `.jnw` file

Files associated to the `jlweave` language mode can be compiled using two different approaches, depending on how you would like code to be rendered

1. **Using the `Verbatim` environment.** Once executed the Julia code and its output are rendered using the `Verbatim` environment. This approach requires to add the following instructions to the `.jnw` file

    ```latex
    \usepackage{fancyvrb}

    \DefineVerbatimEnvironment{juliaout}{Verbatim}{}
    \DefineVerbatimEnvironment{juliacode}{Verbatim}{fontshape=sl}
    \DefineVerbatimEnvironment{juliaterm}{Verbatim}{}
    ```

    Then, the file can be compiled using the following recipe

    ```json
      {
        "name": "Compile jnw files",
        "tools": [
          "jnw2tex",
          "latexmk"
        ]
      }
    ```

    with the `jnw2tex` tool defined by

    ```json
      {
        "name": "jnw2tex",
        "command": "julia",
        "args": [
          "-e",
          "using Weave; weave(\"%DOC_EXT%\", doctype=\"tex\")"
        ],
        "env": {}
      }
    ```

1. **Using the `minted` environment.** Once executed the Julia code and its output are rendered using the `minted` environment. This approach requires to add the following instructions to the `.jnw` file

    ```latex
    \usepackage{minted}
    ```

    and to pass the `-shell-escape` to the LaTeX compiler. See the [FAQ](FAQ#how-to-pass--shell-escape-to-latexmk) for explanations on how to add this flag.

    Then, the file can be compiled using the following recipe

    ```json
      {
        "name": "Compile jnw files",
        "tools": [
          "jnw2texminted",
          "latexmk"
        ]
      }
    ```

    with the `jnw2tex` tool defined by

    ```json
      {
        "name": "jnw2texminted",
        "command": "julia",
        "args": [
          "-e",
          "using Weave; weave(\"%DOC_EXT%\", doctype=\"texminted\")"
        ],
        "env": {}
      }
    ```

    and create a `.latexmkrc` file in the workspace directory containing

    ```perl
    $pdflatex='pdflatex -shell-escape';
    ```

When using auto-build and the file has not been compiled inside the extension yet, we use the first recipe with name (converted to lowercase) containing either `jnw` or `jlweave`.

## Building a `.rnw` file

Files associated to the `rsweave` language mode can be automatically compiled using the following recipe definition

```json
  {
    "name": "Compile Rnw files",
    "tools": [
      "rnw2tex",
      "latexmk"
    ]
  }
```

with the `rnw2tex` tool defined by

```json
  {
    "name": "rnw2tex",
    "command": "Rscript",
    "args": [
      "-e",
      "knitr::opts_knit$set(concordance = TRUE); knitr::knit('%DOCFILE_EXT%')"
    ],
    "env": {}
  }
```

When using auto-build and the file has not been compiled inside the extension yet, we use the first recipe with name (converted to lowercase) containing either `rnw` or `rsweave`.

## Terminating the current compilation

It is possible to terminate the current compilation by calling `Kill LaTeX compiler process` from the _Command Palette_ (command `latex-workshop.kill`) or calling `Terminate current compilation` from the TeX badge in the Build LaTeX project item.

## Auto build LaTeX

Besides manually calling the `Build LaTeX Project` command to compile a document, you may also let the extension automatically start compiling it upon file change. This can be defined in `latex-workshop.latex.autoBuild.run`. The recipe called by auto build is defined by [`latex-workshop.latex.recipe.default`](#latex-workshoplatexrecipedefault).

### latex-workshop.latex.autoBuild.run

When to trigger automatic building.

|   type   |  default value   |      possible values                    |
| -------- | ---------------- | --------------------------------------- |
| _string_ | `"onFileChange"` | `"never"`, `"onSave"`, `"onFileChange"` |

- `"never"`: Disable the auto build feature
- `"onSave"`: Build the project upon saving a `.tex` file.
- `"onFileChange"`: Build the project upon detecting a file change in any of the dependencies. The file can even be modified outside vscode. See [here](#multi-file-projects) for explanations on what dependencies are and how some of them can be ignored. See the [FAQ](FAQ#I-use-build-on-save-but-I-occasionally-want-to-save-without-building) for how to save without triggering the build when this feature is on. When a file changes, we wait for a delay before triggering the build. This delay is configured by [`latex-workshop.latex.watch.delay`](#latex-workshoplatexwatchdelay)

### latex-workshop.latex.autoBuild.interval

The minimal time interval between two consecutive auto builds in milliseconds.

|   type    |  default value   |
| --------- | ---------------- |
| _integer_ | `1000`           |

### latex-workshop.latex.watch.files.ignore

Files to be ignored from the watching mechanism used for triggering autobuild.

This property must be an array of globs pattern. The patterns are matched against the absolute file path. To ignore everything inside the `texmf` tree, `**/texmf/**` can be used.

With the default value, we do not watch files inside the `texmf` tree of the LaTeX distribution.

|         type         | default value  |
| -------------------- | -------------- |
| _array_ of _strings_ | `["**/*.bbx", "**/*.cbx", "**/*.cfg", "**/*.clo", "**/*.cnf", "**/*.def", "**/*.fmt", "**/*.lbx", "**/*.map", "**/*.pfb", "**/*.tfm", "**/texmf-{dist,var}/**", "C:/**texmf/**", "/usr/local/share/miktex-texmf/**", "/Library/Application Support/MiKTeX/texmfs/**"]` |

### latex-workshop.latex.watch.usePolling

Use polling to watch changes on files.

When TeX files are placed on network drives or OneDrive, this option should be turned on. Setting this option to true might lead to high CPU utilization.

You must reload VSCode to take into account a change in this configuration.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `false`       |

### latex-workshop.latex.watch.interval

Interval of polling, in milliseconds.

You must reload VSCode to take into account a change in this configuration.

| type               | default value |
| ------------------ | ------------- |
| _number_           | `300`         |

### latex-workshop.latex.watch.delay

Delay before starting builds, in milliseconds.

You must reload VSCode to take into account a change in this configuration.

| type               | default value |
| ------------------ | ------------- |
| _number_           | `250`         |

## Cleaning generated files

LaTeX compilation typically generates several auxiliary files. They can be removed by calling _Clean up auxiliary files_ from the _Command Palette_ or from the _TeX_ badge. The associated internal command `latex-workshop.clean` is bind to <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>c</kbd>. If you cannot use <kbd>ctrl</kbd>+<kbd>alt</kbd> in a keybinding, see [the FAQ](FAQ#i-cannot-use-ctrlalt-in-a-shortcut).

| Setting key                                            | Description                                                                                                               | Default   | Type               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------ |
| `latex-workshop.latex.autoBuild.cleanAndRetry.enabled` | Enable cleaning and building once more after errors in the build toolchain                                                | `true`    | _boolean_          |
| `latex-workshop.latex.autoClean.run`                   | Define when LaTeX auxillary files should be deleted.                                                                      | `"never"` | _string_           |
| `latex-workshop.latex.clean.fileTypes`                 | Extensions of files to clean                                                                                              |           | _array of strings_ |
| `latex-workshop.latex.clean.subfolder.enabled`         | Clean LaTeX auxillary files recursively in sub-folders of [`latex-workshop.latex.outDir`](View#latex-workshoplatexoutDir) | `false`   | _boolean_          |

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

```json
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

```json
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

```json
  "env": {
      "TEXMFHOME": "%DIR%/texmf"
  }
```

You can also override PATH environment variable.

To include a tool in a recipe, the tool's `name` should be included in the recipe's `tools` list.

When building the project, the [magic comments](#magic-comments) in the root file are used if present, otherwise the first recipe is used. You can compile with another recipe by command `latex-workshop.recipes`. By default [`latexmk`](http://personal.psu.edu/jcc8/software/latexmk/) is used. This tool is bundled in most LaTeX distributions, and requires perl to execute. For non-perl users, the following `texify` toolchain from MikTeX may worth a try:

```json
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
    "%DOC_EXT%"
  ],
    "env": {}
}]
```

The `args` and `env` parameters can contain symbols surrounded by `%`. These placeholders are replaced on-the-fly.

### Placeholders

LaTeX Workshop registers the following placeholders
| Placeholder     | Replaced by  |
| --------------- | ------------------------------------------------------------ |
| `%DOC%`         | The root file full path without the extension |
| `%DOC_W32%`     | The root file full path without the extension with `\` path separator on Windows|
| `%DOCFILE%`     | The root file name without the extension |
| `%DOC_EXT%`     | The root file full path with the extension |
| `%DOC_EXT_W32%` | The root file full path with the extension with `\` path separator on Windows |
| `%DOCFILE_EXT%` | The root file name with the extension |
| `%DIR%`         | The root file directory |
| `%DIR_W32%`     | The root file directory with `\` path separator on Windows |
| `%TMPDIR%`      | A temporary folder for storing ancillary files |
| `%OUTDIR%`      | The output directory configured in [`latex-workshop.latex.outDir`](View#latex-workshoplatexoutDir) |
| `%OUTDIR_W32%`  | The output directory configured in [`latex-workshop.latex.outDir`](View#latex-workshoplatexoutDir) with `\` path separator on Windows |

As most LaTeX compiler accepts root file name without extension, `%DOC%` and `%DOCFILE%` do not include the filename extension. Meanwhile, the `texify` tool requires the complete filename with its extension, hence the use of `%DOC_EXT%` in the configuration of `texify`.

Most commands accept the use of the `/` path separator even on Windows and most LaTeX tools even require its use. On the contrary, some Windows commands only work with the `\` path separator. So, we propose two versions of the placeholders. All placeholders without the `_W32` suffix always use the `/` path separator even on Windows. All placeholders with the `_W32` suffix use the `\` path separator on Windows. Note on Linux and Unix systems, placeholders with and without the `_W32` suffix are equivalent.

### latex-workshop.latex.recipe.default

Define which recipe is used by the _Build LaTeX project_ command.
It also applies to auto build. Recipes are refered to by their names as defined in `latex-workshop.latex.recipes`. Note there are two special values:

- `"first"`: Use the first recipe defined in [`latex-workshop.latex.recipes`](#LaTeX-recipes).
- `"lastUsed"`: Use the last used recipe by the command _LaTeX Workshop: Build with recipe_.

|   type   | default value |
| -------- | ------------- |
| _string_ | `"first"`     |

### latex-workshop.latex.build.forceRecipeUsage

Force the use of the recipe system even when a magic comment defines a TeX command.

|   type    |  default value   |
| --------- | ---------------- |
| _boolean_ | `false`          |

## External build command

Versatile though the recipe mechanism described above may be, it may fail to match your needs when building the whole LaTeX project is done by a personal script or a Makefile. For this particular case, we provide an external build command mechanism, which completely bypasses the recipe machinery. Just define your command along with its arguments using the following two configuration variables

### latex-workshop.latex.external.build.command

The external command to execute when calling `latex-workshop.build`.

This is useful when compiling relies on a Makefile or a bespoke script. When defined, it completely bypasses the recipes and root file detection mechanism. The command is launched from the workspace directory.

|   type    |  default value   |
| --------- | ---------------- |
| _string_  | `""`             |

### latex-workshop.latex.external.build.args

The arguments of [`latex-workshop.latex.external.build.command`](#latex-workshoplatexexternalbuildcommand) when calling `latex-workshop.build`

If the rootFile is defined, you can use any of the placeholders defined in the [section on LaTeX Recipes](#LaTeX-recipes).

|   type      |  default value   |
| ---------   | ---------------- |
| _string[]_  | `[]`             |

## Magic comments

### TeX program and options

LaTeX Workshop supports `% !TEX program` magic comment to specify the compiler program. However, it is advised to use the recipe system instead of magic program to define the building process, since the latter is only implemented for backward compatibility.

For `% !TEX program` magic comment, its arguments are defined in `latex-workshop.latex.magic.args`:

```json
"latex-workshop.latex.magic.args": [
  "-synctex=1",
  "-interaction=nonstopmode",
  "-file-line-error",
  "%DOC%"
]
```

Alternatively, you can directly define the args in the `.tex` file by using the magic comment `% !TEX options`, which overrides `latex-workshop.latex.magic.args`. Note that it must contain the file to proceed. For instance, to reproduce the default behavior, you should use

```
% !TEX options = -synctex=1 -interaction=nonstopmode -file-line-error "%DOC%"
```

Suppose there is a line `% !TEX program = xelatex` in the root file. Upon building the project, LaTeX Workshop will parse the root file and figure out that `xelatex` should be used.

### BIB program and options

When using `% !TEX program` with bibliographies, a `bib` compiler must be defined with `% !BIB program` comment, e.g., `% !BIB program = bibtex`. Otherwise the extension will only run one-pass compilation with the specified LaTeX compiler. If needed, you can pass extra arguments to the `% !BIB program` using the `latex-workshop.latex.magic.bib.args` variable:

```json
"latex-workshop.latex.magic.bib.args": [
  "%DOCFILE%"
]
```

Alternatively, you can directly define the args in the `.tex` file by using the magic comment `% !BIB options`, which overrides `latex-workshop.latex.magic.bib.args`. Note that it must contain the file to proceed. For instance, to reproduce the default behavior, you should use `% !BIB options = "%DOCFILE%"`.

## Catching errors and warnings

The warnings and errors issued by the compiling toolchain are rendered in the _Problems_ Pane. The following settings enable you to customize what you want to get in that panel. If the messages displayed in the panel seem to be wrong, see the [FAQ](FAQ#The-Problem-Pane-displays-wrong-messages).

The raw compiler logs can be accessed in the _Output Pane_, choose _LaTeX Compiler_. The default is to clear the logs before calling every tool of a recipe. If you prefer to keep the logs from all the tools of a recipe, set [`latex-workshop.latex.build.clearLog.everyRecipeStep.enabled`](#latex-workshoplatexbuildclearLogeveryRecipeStepenabled) to `false`.

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

#### latex-workshop.progress.enabled

Enable the progress bar and the LaTeX compilation info panel.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.progress.location

Optionally display the compilation progress in a pop-up notification dialogue.

| type   | default value   | Possible values                           |
| ------ | --------------- | ----------------------------------------- |
| _enum_ | `"Status Bar"`  | `"Status Bar"`, `"Notification Dialogue"` |

### latex-workshop.progress.runIconType

The style of number to use to indicate the run number"

| type      | default value            |
| --------- | ------------------------ |
| _enum_    | `"Parenthesised"`        |

The possible values are

- `"Parenthesised"`: "⑴ ⑵ ⑶ …",
- `"Circled"`: "① ② ③ …",
- `"Solid Circled"`: "❶ ❷ ❸ …",
- `"Full Stop"`: "⒈ ⒉ ⒊ …"

### latex-workshop.progress.barLength

_Only applies if `latex-workshop.progress.location` is set to `Status Bar`._

The length in characters of the progress bar.

| type      | default value |
| --------- | ------------- |
| _number_  | `15`          |

### latex-workshop.progress.barStyle

_Only applies if `latex-workshop.progress.location` is set to `Status Bar`._

| type   | default value    |
| ------ | ---------------- |
| _enum_ | `"Block Shading` |

The possible values are

- `"Block Width"`: "█████▋░░░ (8 levels per block)",
- `"Block Shading"`: "█████▓░░░ (4 levels per block)",
- `"Block Quadrants"`: "█████▙░░░ (4 levels per block)",
- `"none"`: No bar.
