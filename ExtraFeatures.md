# Extra Features

## Structure of the document

The structure of the LaTeX project (`\chapter`, `\section`, `\subsection`, ...) is accessible via the TeX panel on the left of the editor. The entry corresponding to the cursor position in the editor is automatically selected and follows the cursor. The outline hierarchy is defined by [`latex-workshop.view.outline.sections`](#latex-workshopviewoutlinesections).

Note that the Explorer panel also contains an outline view but it only shows the structure of the current file and does not take into account any included file.

### `latex-workshop.view.outline.sections`

The section names of LaTeX outline hierarchy. It is also used by the folding mechanism. See [Code folding](ExtraFeatures#code-folding) for more details.

This property is an array of case-sensitive strings in the order of the document structure hierarchy. For multiple tags of the same level, separate the tags with `|` as delimiters, e.g., `section|alternative`.

|         type         |                           default value                           |
| -------------------- | ----------------------------------------------------------------- |
| _array_ of _strings_ | `[ "part", "chapter", "section", "subsection", "subsubsection" ]` |

The structure of the document can be obtained

### `latex-workshop.view.outline.commands`

The names of the commands to be shown in the outline/structure views. Reload vscode to make any change in this configuration effective.

| type                  | default value      |
|-----------------------|--------------------|
| _array_ of _strings_  | `["label"]`        |

The commands must be called in the form `\commandname{arg}`.

### `latex-workshop.view.outline.floats.enabled`

Show the floating objects (figures and tables) in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

### `latex-workshop.view.outline.floats.number.enabled`

Show the float number in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

### `latex-workshop.view.outline.floats.caption.enabled`

Show the float caption in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

### `latex-workshop.view.outline.numbers.enabled`

Show the sectioning numbers in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

### `latex-workshop.view.outline.follow.editor`

Scrolling the editor will also reveal the corresponding structure items.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

### `latex-workshop.view.outline.sync.viewer`

Clicking on a structure item will also call `synctex` to scroll the PDF viewer to the corresponding location.

| type      | default value |
|-----------|---------------|
| _boolean_ | `false`       |

## Code folding

The following regions (along with their `*`-starred versions) can be folded.

|                          Region                         |
| ------------------------------------------------------- |
|         `\documentclass{} ... \begin{document}`         |
|                        `\part{}`                        |
|                       `\chapter{}`                      |
| `\section{}`, `\subsection{}`, `\subsubsection{}`, etc. |
|           `\begin{<envname>} ... \end{<envname>}`       |
|                 `\begingroup ... \endgroup`             |

The folding mechanism ignores comments, so comments can be used to fold code using the same keywords as above. This means commented out sections and the like can be easily folded for easier editing. To fold arbitrary regions, we recommend using the following comments.

```latex
%\begingroup
...
%\endgroup
```

or

```latex
% region
...
% endregion
```

The keywords `region` and `endregion` may start with a capital letter and be preceded by the `#` sign.

## Counting words

To count the number of words in the current document, call _Count words in LaTeX document_ from the Command Palette (the associated command is `latex-workshop.wordcount`). Setting [`latex-workshop.texcount.autorun`](#latex-workshoptexcountautorun) to `onSave` counts the number of words on every file save and displays it in the status bar.

### `latex-workshop.texcount.autorun`

When to call `texcount`. Default is never.

| type     | default value         |
|----------|-----------------------|
| _string_ | `"onSave" \| "never"`  |

### `latex-workshop.texcount.interval`

The minimal time interval between two consecutive runs of `texcount` in milliseconds when [`latex-workshop.texcount.autorun`](#latex-workshoptexcountautorun) is set to `onSave`.

| type     | default value |
|----------|---------------|
| _number_ | 1000          |

### `latex-workshop.texcount.path`

Define the location of TeXCount executive file/script

| type     | default value |
|----------|---------------|
| _string_ | `"texcount"`  |

This command will be joint with `latex-workshop.texcount.args` and required arguments to form a complete command of TeXCount

### `latex-workshop.texcount.args`

TeXCount arguments to count words in LaTeX document of the entire project from the root file, or the current document.

| type                 | default value |
|----------------------|---------------|
| _array_ of _strings_ | `[]`          |

Arguments must be in separate strings in the array.
Additional arguments, i.e., `-merge %DOC%` for the project and the current document path for counting current file, will be appended when constructing the command.
Note that if `latex-workshop.texcount.args` already contains `-merge`, it will not be added again.
To use the `-inc` mode of `texcount` instead, set this to `["-merge", "-inc", "-total"]`;
  the `-merge` is to prevent LaTeX Workshop appending `-merge` at the end,
  the `-inc` then immediately overrides this setting,
  and the `-total` ensures that LaTex Workshop is able to parse the output.

## Literate programming support using LaTeX

We support the following the programming languages inside a LaTeX document

- `Julia` code using [Weave.jl](https://github.com/JunoLab/Weave.jl). See [Building a `.jnw` file](Compile#Building-a-jnw-file). We use the `jlweave` language mode for this and recognize the following file extensions   `.jnw`, and `.jtexw`.
- `R` code using [knitr](https://yihui.org/knitr/) or [Sweave](https://stat.ethz.ch/R-manual/R-devel/library/utils/doc/Sweave.pdf). See [Building a `.rnw` file](Compile#Building-a-rnw-file) for how to compile LaTeX files using Sweave. We use the `rsweave` language mode for this and recognize the following file extensions   `.rnw`, `.Rnw`, `.Rtex`, `.rtex`, `.snw` and `.Snw`.

For syntax highlighting to be properly working, you need to install the VSCode extension that gives support for the corresponding programming language.

## Collaborative editing using LiveShare (experimental)

The LiveShare extension has some limitations when it comes to interacting with the filesystem and does not support sharing binary files. However, a workaround has been developed with the following features:

- View pdf by clicking on the pdf file
- View pdf by the view command
- Auto refresh pdf view when the pdf file changes
- Inverse and forward synctex

To get started as a host, you need to:
1. Start a LiveShare session
2. Allow for port sharing when prompted. If you miss the prompt, execute the `Share` command.
3. The PDF viewer and LaTeX compiler must be running on the host.
4. Share your invitation link and start collaborating!
5. The guests will acquire the port on connect, but can reacquire it using the same `Share` command.
