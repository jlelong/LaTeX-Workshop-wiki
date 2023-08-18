# Extra Features

## Structure of the document

The structure of the LaTeX project (`\chapter`, `\section`, `\subsection`, ...) is accessible via the TeX panel on the left of the editor. The entry corresponding to the cursor position in the editor is automatically selected and follows the cursor. The outline hierarchy is defined by [`latex-workshop.view.outline.sections`](#latex-workshopviewoutlinesections).

Note that the Explorer panel also contains an outline view but it only shows the structure of the current file and does not take into account any included file.

###`latex-workshop.view.outline.sections`

The section names of LaTeX outline hierarchy. It is also used by the folding mechanism. See [Code folding](Environments#code-folding) for more details.

This property is an array of case-sensitive strings in the order of the document structure hierarchy. For multiple tags of the same level, separate the tags with `|` as delimiters, e.g., `section|alternative`.

|         type         |                           default value                           |
| -------------------- | ----------------------------------------------------------------- |
| _array_ of _strings_ | `[ "part", "chapter", "section", "subsection", "subsubsection" ]` |

The structure of the document can be obtained

###`latex-workshop.view.outline.commands`

The names of the commands to be shown in the outline/structure views. Reload vscode to make any change in this configuration effective.

| type                  | default value      |
|-----------------------|--------------------|
| _array_ of _strings_  | `["label"]`        |

The commands must be called in the form `\commandname{arg}`.

###`latex-workshop.intellisense.fastparse.enabled`

Use fast LaTeX parsing algorithm to build outline/structure. This is done by inherently removing texts and comments before building AST. Enabling this will not tamper the document, but may result in incomplete outline/structure.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

###`latex-workshop.view.outline.floats.enabled`

Show the floating objects (figures and tables) in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

###`latex-workshop.view.outline.floats.number.enabled`

Show the float number in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

###`latex-workshop.view.outline.floats.caption.enabled`

Show the float caption in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

###`latex-workshop.view.outline.numbers.enabled`

Show the sectioning numbers in the outline/structure views.

| type      | default value |
|-----------|---------------|
| _boolean_ | `true`        |

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

To count the number of words in the current document, call _Count words in LaTeX document_ from the Command Palette (the associated command is `latex-workshop.wordcount`). Setting [`latex-workshop.texcount.autorun`](#latex-workshop.texcount.autorun) to `onSave` counts the number of words on every file save and displays it in the status bar.

###`latex-workshop.texcount.autorun`

When to call `texcount`. Default is never.

| type     | default value         |
|----------|-----------------------|
| _string_ | `"onSave" | "never"`  |

###`latex-workshop.texcount.interval`

The minimal time interval between two consecutive runs of `texcount` in milliseconds when [`latex-workshop.texcount.autorun`](#latex-workshop.texcount.autorun) is set to `onSave`.

| type     | default value |
|----------|---------------|
| _number_ | 1000          |

###`latex-workshop.texcount.path`

Define the location of TeXCount executive file/script

| type     | default value |
|----------|---------------|
| _string_ | `"texcount"`  |

This command will be joint with `latex-workshop.texcount.args` and required arguments to form a complete command of TeXCount

###`latex-workshop.texcount.args`

TeXCount arguments to count words in LaTeX document of the entire project from the root file, or the current document.

| type                 | default value |
|----------------------|---------------|
| _array_ of _strings_ | `[]`          |

Arguments must be in separate strings in the array. Additional arguments, i.e., `-merge %DOC%` for the project and the current document path for counting current file will be appended when constructing the command.

## Literate programming support using LaTeX

We support the following the programming languages inside a LaTeX document

- `Julia` code using [Weave.jl](https://github.com/JunoLab/Weave.jl). See [Building a `.jnw` file](Compile#Building-a-jnw-file). We use the `jlweave` language mode for this and recognize the following file extensions   `.jnw`, and `.jtexw`.
- `R` code using [knitr](https://yihui.org/knitr/) or [Sweave](https://stat.ethz.ch/R-manual/R-devel/library/utils/doc/Sweave.pdf). See [Building a `.rnw` file](Compile#Building-a-rnw-file) for how to compile LaTeX files using Sweave. We use the `rsweave` language mode for this and recognize the following file extensions   `.rnw`, `.Rnw`, `.Rtex`, `.rtex`, `.snw` and `.Snw`.

For syntax highlighting to be properly working, you need to install the VSCode extension that gives support for the corresponding programming language.

## Mixing markdown and LaTeX code

The [`markdown` package](https://texlive.mycozy.space/macros/generic/markdown/markdown.html) allows to mix LaTeX and Markdown code inside the markdown environment. If you want to use this package, keep the `.tex` extension to your file but set its language to `markdown_latex_combined`.

Note that the language `markdown_latex_combined` **is not meant** to be used for `.md` files using LaTeX code.
