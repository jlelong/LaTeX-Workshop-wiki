# Multi File projects

While it is fine to write all contents in one `.tex` file, it is common to split things up for simplicity. For such LaTeX projects, the file with `\begin{document}` is considered as the root file, which serves as the entry point to the project. LaTeX Workshop intelligently finds the root file when a new document is opened, the active editor is changed, or any LaTeX Workshop command is executed.

To find the root file, LaTeX Workshop will follow the steps below, stopping whenever one is found:

1. **Magic comment** `% !TEX root = relative/or/absolute/path/to/root/file.tex`. If such comments exist in the currently active editor, the referred file is set as root.
2. **Self check** If current active editor contains `\begin{document}`, it is set as root.
3. **Root directory check** LaTeX Workshop iterates through all `.tex` files in the root folder of the workspace. The first one containing `\begin{document}` and which includes the file in the active editor is set as the root file. To avoid parsing all `.tex` files in the workspace, you can narrow the search by specifying [`latex-workshop.latex.search.rootFiles.include`](#latex-workshoplatexsearchrootFilesinclude) and/or [`latex-workshop.latex.search.rootFiles.exclude`](#latex-workshoplatexsearchrootFilesexclude).

If no root file is found, most of the features in LaTeX Workshop will not work.

Once the root file is determined, it is parse to discover all files it includes using `input`, `include`, `InputIfFileExists`, `subfile`, `import` and `subimport` and the process goes on recursively. All these files are considered to define a LaTeX project.

**Note**: for all this to work, you have to open the directory (or one of its antecedents) containing the whole LaTeX project.

## Relevant settings

### latex-workshop.latex.search.rootFiles.include

Patterns of files to consider for the root detection mechanism.

Relative paths are computed from the workspace folder. To detect the root file and the tex file tree, we parse all the `.tex` listed here.\nIf you want to specify all `.tex` files inside directory, say `foo`, and all its subdirectories recursively, you need to use `**/foo/**/*.tex`. If you only want to match `.tex` files at the top level of the workspace, use `*.tex`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

| type       | default value  |
| ---------- | -------------- |
| _string[]_ | `["**/*.tex"]` |

### latex-workshop.latex.search.rootFiles.exclude

Patterns of files to exclude from the root detection mechanism.

See also `latex-workshop.latex.search.rootFiles.include`. For more details on glob patterns, see [here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).

| type       | default value  |
| ---------- | -------------- |
| _string[]_ | `[]`           |
