# Multi File projects

While it is fine to write all contents in one `.tex` file, it is common to split things up for simplicity. For such LaTeX projects, the file with `\begin{document}` is considered as the root file, which serves as the entry point to the project. LaTeX Workshop intelligently finds the root file when a new document is opened, the active editor is changed, or any LaTeX Workshop command is executed.

## The root file

To find the root file, LaTeX Workshop will follow the steps below, stopping whenever one is found:

1. **Magic comment** `% !TEX root = relative/or/absolute/path/to/root/file.tex`. If such comments exist in the currently active editor, the referred file is set as root. You can use the command `latex-workshop.addtexroot` to help you insert the magic comment.
1. **Self check** If current active editor contains `\begin{document}`, it is set as root.
1. **Root directory check** LaTeX Workshop iterates through all `.tex` files in the root folder of the workspace. The first one containing `\begin{document}` and which includes the file in the active editor is set as the root file. To avoid parsing all `.tex` files in the workspace, you can narrow the search by specifying [`latex-workshop.latex.search.rootFiles.include`](#latex-workshoplatexsearchrootFilesinclude) and/or [`latex-workshop.latex.search.rootFiles.exclude`](#latex-workshoplatexsearchrootFilesexclude).
1. **The `subfiles` package case** The main file is used to provide intellisense. The non-interactive functions `autobuild`, `autoclean` and forward `synctex` rely on the value of the configuration variable [`latex-workshop.latex.rootFile.useSubFile`](#latex-workshoplatexrootFileuseSubFile) to choose between the main file and the subfile.
    - if [`latex-workshop.latex.rootFile.doNotPrompt`](#latex-workshoplatexrootFiledoNotPrompt) is `false`,  all the interactive commands `build`, `clean` and `view` use a quick pick box to ask the user which file is to be considered as the root File.
    - if [`latex-workshop.latex.rootFile.doNotPrompt`](#latex-workshoplatexrootFiledoNotPrompt) is `true`,  all the interactive commands `build`, `clean` and `view` use variable [`latex-workshop.latex.rootFile.useSubFile`](#latex-workshoplatexrootFileuseSubFile) to choose between the main file and the subfile automatically.

    Note that each subfile has to be compiled from its respective directory, where LaTeX is able to locate all included text files or images. However, following the discussion in [1895](https://github.com/James-Yu/LaTeX-Workshop/issues/1895) we decided that all paths should be relative to the root file directory. Hence, the recipe is launched from the root file directory and the `-cd` option must be added to `latexmk`. As discussed in [1932](https://github.com/James-Yu/LaTeX-Workshop/issues/1932), this option breaks `makeindex` (this should be solved in the next release of `latexmk`). So the solution is to add a `.latexmkrc` file in the root file directory containing `$do_cd = 1;`

1. **The `.fls` files** LaTeX compilers when called with the `-recoder` option produce a file with `.fls` extension containing all the files _input_ and _output_ during compilation. The list of _input_ files contains all classes, packages, fonts, input `.tex` files, listings, graphs, ... Using `latexmk` always produces a `.fls` file.

If no root file is found, most of the features in LaTeX Workshop will not work.

**Note**: for all this to work, you have to open the directory (or one of its antecedents) containing the whole LaTeX project.

## The dependencies

Once the root file is determined, it is parsed to discover all the files it includes using `input`, `include`, `InputIfFileExists`, `subfile`, `import` and `subimport` and the process goes on recursively. All these files are called dependencies and are considered to define a LaTeX project. If you include some files located in some external directories, you can list these extra directories in [`latex-workshop.latex.texDirs`](#latex-workshoplatextexDirs).

Moreover, when a `.fls` file with the same basename as the root file exists, it is used to compute the full list of dependencies, ie all classes, packages, fonts, input `.tex` files, listings, graphs, ... All these files are parsed to provide intellisense completion. When  [`latex-workshop.latex.autoBuild.run`](Compile#auto-build-latex) is set to `onFileChange`, building is automatically triggered whenever any of the dependencies is modified.  You can use [`latex-workshop.latex.watch.files.ignore`](#latex-workshoplatexwatchfilesignore) to prevent some files from being watched. The default is to ignore files inside your TeX distribution and files with `.code.tex` or `.sty` suffix.

## Relevant settings

### latex-workshop.latex.search.rootFiles.include

Patterns of files to consider for the root detection mechanism.

Relative paths are computed from the workspace folder. To detect the root file and the tex file tree, we parse all the `.tex` listed here.\nIf you want to specify all `.tex` files inside directory, say `foo`, and all its subdirectories recursively, you need to use `**/foo/**/*.tex`. If you only want to match `.tex` files at the top level of the workspace, use `*.tex`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

|         type         | default value  |
| -------------------- | -------------- |
| _array_ of _strings_ | `["**/*.tex"]` |

### latex-workshop.latex.search.rootFiles.exclude

Patterns of files to exclude from the root detection mechanism.

See also `latex-workshop.latex.search.rootFiles.include`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.latex.watch.files.ignore

Files to ignore from the watching mechanism used for triggering autobuild.

This property must be an array of globs pattern. The patterns are matched against the absolute file path. To ignore everything inside the `texmf` tree, `**/texmf/**` can be used.

With the default value, we do not watch files inside the `texmf` tree of the LaTeX distribution.

|         type         | default value  |
| -------------------- | -------------- |
| _array_ of _strings_ | `["**/*.bbx", "**/*.cbx", "**/*.cfg", "**/*.clo", "**/*.cnf", "**/*.def", "**/*.fmt", "**/*.lbx", "**/*.map", "**/*.pfb", "**/*.tfm", "**/texmf-{dist,var}/**", "C:/**texmf/**", "/usr/local/share/miktex-texmf/**", "/Library/Application Support/MiKTeX/texmfs/**"]` |

### latex-workshop.latex.watch.usePolling

Use polling watch changes on files.

When TeX files are placed on network drives or OneDrive, this option should be turned on. Setting this option to true might lead to high CPU utilization.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `false`       |

### latex-workshop.latex.watch.interval

Interval of polling, in milliseconds.

| type               | default value |
| ------------------ | ------------- |
| _number            | `300`         |

### latex-workshop.latex.texDirs

List of directories where to look for extra input `.tex` files.

Absolute paths are required. You may also need to set the environment variable `TEXINPUTS` properly for the LaTeX compiler to find the `.tex` files, see the `env` parameter of [recipes](#latex-recipes).

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.latex.rootFile.useSubFile

When the `subfile` package is used, either the main file or any subfile containing `\\documentclass[main.tex]{subfile}` can be LaTeXing. When set to `true`, the extension uses the subfile as the rootFile for the `autobuild`, `clean` and `synctex` commands.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `true`        |

### latex-workshop.latex.rootFile.doNotPrompt

When the `subfile` package is used, either the main file or any subfile containing `\\documentclass[main.tex]{subfile}` can be LaTeXing. When set to `false`, the `build` and `view` commands  ask the user's choice first. When set to `true`, the subfile is used when `latex-workshop.latex.rootFile.useSubFile` is also `true`, otherwise the rootFile is used.

| type                 | default value |
| -------------------- | ------------- |
| _boolean_            | `false`       |
