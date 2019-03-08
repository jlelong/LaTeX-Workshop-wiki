# Multi File projects

While it is fine to write all contents in one `.tex` file, it is common to split things up for simplicity. For such LaTeX projects, the file with `\begin{document}` is considered as the root file, which serves as the entry point to the project. LaTeX Workshop intelligently finds the root file when a new document is opened, the active editor is changed, or any LaTeX Workshop command is executed.

## The root file

To find the root file, LaTeX Workshop will follow the steps below, stopping whenever one is found:

1. **Magic comment** `% !TEX root = relative/or/absolute/path/to/root/file.tex`. If such comments exist in the currently active editor, the referred file is set as root.
1. **Self check** If current active editor contains `\begin{document}`, it is set as root.
1. **Root directory check** LaTeX Workshop iterates through all `.tex` files in the root folder of the workspace. The first one containing `\begin{document}` and which includes the file in the active editor is set as the root file. To avoid parsing all `.tex` files in the workspace, you can narrow the search by specifying [`latex-workshop.latex.search.rootFiles.include`](#latex-workshoplatexsearchrootFilesinclude) and/or [`latex-workshop.latex.search.rootFiles.exclude`](#latex-workshoplatexsearchrootFilesexclude).
1. **The `.fls` files** LaTeX compilers when called with the `-recoder` option produce a file with `.fls` extension containing all the files _input_ and _output_ during compilation. The list of _input_ files contains all classes, packages, fonts, input `.tex` files, listings, graphs, ... Using `latexmk` always produces a `.fls` file.

If no root file is found, most of the features in LaTeX Workshop will not work.

**Note**: for all this to work, you have to open the directory (or one of its antecedents) containing the whole LaTeX project.

## The dependencies

Once the root file is determined, it is parsed to discover all the files it includes using `input`, `include`, `InputIfFileExists`, `subfile`, `import` and `subimport` and the process goes on recursively. All these files are called dependencies and are considered to define a LaTeX project.

Moreover, when a `.fls` file with the same basename as the root file exists, it is used to compute the full list of dependencies, ie all classes, packages, fonts, input `.tex` files, listings, graphs, ... All these files are parsed to provide intellisense completion. When  [`latex-workshop.latex.autoBuild.run`](Compile#auto-build-latex) is set to `onFileChange`, building is automatically triggered whenever any of the dependencies is modified. In some cases, you may need to ignore some dependencies, in particular those inside the `texmf` tree. You can use [`latex-workshop.latex.watch.files.ignore`](#latex-workshoplatexwatchfilesignore)

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

|         type         | default value  |
| -------------------- | -------------- |
| _array_ of _strings_ | `["**/*.bbx", "**/*.cbx", "**/*.cfg", "**/*.clo", "**/*.cnf", "**/*.def", "**/*.fmt", "**/*.lbx", "**/*.map", "**/*.pfb", "**/*.tfm"]` |