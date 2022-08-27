# Snippets and shortcuts

Many snippets are available to help users enter LaTeX commands or symbols. _Snippet View_ is also available from the TeX badge.

All commands are listed as <kbd>ctrl</kbd>+<kbd>some key</kbd>. If you're on Mac, don't worry we have written equivalents, so every time you see <kbd>ctrl</kbd> just imagine it's <kbd>⌘</kbd>.

To have intellisense automatically triggered inside snippets, set `editor.suggest.snippetsPreventQuickSuggestions` to `false`. This is useful for instance if you want to enter `\frac{x_{1}}{2}` using `@/`+ `x` + `__` + `1`+ `2` using <kbd>TAB</kbd> to move from one tabstop to the next.

## Environments

Some environments have a dedicated snippet in the form `BXY` where `XY` are the two first letters of the environment name. The starred versions use the prefix `BSXY`.

| Prefix | Environment name |
| ------ | ---------------- |
| `BEQ`  | `equation`       |
| `BSEQ` | `equation*`      |
| `BAL`  | `align`          |
| `BSAL` | `align*`         |
| `BGA`  | `gather`         |
| `BSGA` | `gather*`        |
| `BMU`  | `multline`       |
| `BSMU` | `multline*`      |
| `BIT`  | `itemize`        |
| `BEN`  | `enumerate`      |
| `BSPL` | `split`          |
| `BCAS` | `cases`          |
| `BFR`  | `frame`          |
| `BFI`  | `figure`         |

## Sectioning

### Inserting a sectioning command

Sectioning commands can of course be inserted by just typing them as they are automatically completed by the intellisense mechanism. One can also use the following snippets.

| Prefix | Sectioning level |
| ------ | ---------------- |
| SPA    | part             |
| SCH    | chapter          |
| SSE    | section          |
| SSS    | subsection       |
| SS2    | subsubsection    |
| SPG    | paragraph        |
| SSP    | subparagraph     |

For instance, typing `SSE` + `TAB` expands to `\section{}` with the cursor inside the brackets.

### Selecting a whole section

The current section along with all its subsections can be selected by calling the command `latex-workshop.select-section`. Repeated calls ends in expanding the selection in two ways:

- First, outer sections are selected
- If there is not outer section, the selection is expanded upwards be selection the previous section.

### Promoting/demoting sectioning levels

Adjusting sectioning levels can be done by calling one of the two commands `latex-workshop.promote-sectioning` and `latex-workshop.demote-sectioning` from the _Command Palette_.

These methods replace all sectioning commands with the sectioning command one level higher or lower. They apply either to the current line or to a selection.

#### Example

Applying `latex-workshop.promote-sectioning` to the following selection,

```latex
\subsection{Demo}
\paragraph{Content}
```

yields

```latex
\section{Demo}
\subsubsection{Content}
```

To recursively promote/demote a section and and all its subsections, first call `latex-workshop.select-section` to select the section and all its subsections and then call `latex-workshop.promote-sectioning` or `latex-workshop.demote-sectioning`.

#### Keybindings

This functionality has two keybindings

| Method               | Shortcut                                    | Alternate                                 |
| -------------------- | ------------------------------------------- | ----------------------------------------- |
| Promote Sectioning | <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>[</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>[</kbd> |
| Demote Sectioning | <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>]</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>]</kbd> |

To use the alternate shortcuts, set `latex-workshop.bind.altKeymap.enabled` to `true`.

## Handy mathematical snippets

Some common mathematical symbols or commands have a dedicated snippet.
| Prefix               | Command                  |
| -------------------- | ------------------------ |
| `__`                 | `_{$1}`                  |
| `**`                 | `^{$1}`                  |
| `...`                | `\dots`                  |

## Font commands and snippets

The following shortcuts are toggle commands. When some text is selected, it gets surrounded by the font command. When no text is actually selected, either the cursor is already inside the font command in which case the font command is removed or the command is inserted at the cursor position. The shortcuts work with multi-selections and multi-cursors.

| Prefix     | Shortcut                                                       | Command                  |
| ---------- | -------------------------------------------------------------- | ------------------------ |
| `fontsize` |                                                                | Opens font size select   |
| `FNO`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>n</kbd>     | `\textnormal{${1}}`      |
| `FRM`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>r</kbd>     | `\textrm{${1}}`          |
| `FEM`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>e</kbd>     | `\emph{${1}}`            |
| `FSF`      |                                                                | `\textsf{${1}}`          |
| `FTT`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>t</kbd>     | `\texttt{${1}}`          |
| `FIT`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>i</kbd>     | `\textit{${1}}`          |
| `FSL`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>s</kbd>     | `\textsl{${1}}`          |
| `FSC`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>c</kbd>     | `\textsc{${1}}`          |
| `FUL`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>u</kbd>     | `\underline{${1}}`       |
| `FUC`      |                                                                | `\uppercase{${1}}`       |
| `FLC`      |                                                                | `\lowercase{${1}}`       |
| `FBF`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>b</kbd>     | `\textbf{${1}}`          |
| `FSS`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>6</kbd>     | `\textsuperscript{${1}}` |
| `FBS`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>minus</kbd> | `\textsubscript{${1}}`   |

## Mathematical font commands and snippets

The following shortcuts are toggle commands. When some text is selected, it gets surrounded by the font command. When no text is actually selected, either the cursor is already inside the font command in which case the font command is removed or the command is inserted at the cursor position. The shortcuts work with multi-selections and multi-cursors.

| Prefix | Shortcut                                                                    | Command          |
|--------|-----------------------------------------------------------------------------|------------------|
| `MRM`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>r</kbd>                  | `\mathrm{${1}}`  |
| `MSF`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>s</kbd>                  | `\mathsf{${1}}`  |
| `MBF`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>b</kbd>                  | `\mathbf{${1}}`  |
| `MBB`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>b</kbd> | `\mathbb{${1}}`  |
| `MCA`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>c</kbd>                  | `\mathcal{${1}}` |
| `MIT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>i</kbd>                  | `\mathit{${1}}`  |
| `MTT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>t</kbd>                  | `\mathtt{${1}}`  |

## Miscellaneous Actions

| Shortcut                                                       | Action                   |
| -------------------------------------------------------------- | ------------------------ |
| <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>Enter</kbd> | Insert newline + `\item` |

## Surrounding text

### With a command

To surround text with a command, just select some text and use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>w</kbd> (<kbd>⌘</kbd>+<kbd>l</kbd>, <kbd>⌘</kbd>+<kbd>w</kbd> on Mac) or call _Surround selection with LaTeX command_ from the _Command Palette_ (command `latex-workshop.surround`). A new menu pops up to select the command. This works with multi selections.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/wrap.gif" alt="wrap demo" height="140px">

Alternatively, you can just select the text and enter the command using autocompletion

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/wrap2.gif" alt="wrap demo" height="140px">

### With an environment

To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-env.gif" alt="Surround with environment demo">

## User-defined snippets

VScode provides the function for users to **define their own snippets**. Do as follows: click <kbd>Code</kbd>+<kbd>
Preferences</kbd>+<kbd>Configure User Snippets</kbd>, then enter `latex.json` in the inputbox and return to edit the `latex.json` file.

Here we give an example:

For those who major in mathematics, you must use the inline math formulas (i.e., formulas surrounded by two dollars `$<formula>$`) frequently. If you feel troublesome to input the dollars symbols since you have to press the <kbd>shift</kbd> button every time. You can define a code snippet as follows:
```json
"inline-math": {
  "prefix": "dd",
  "body": ["\\$$0\\$"],
  "description": "Insert inline math formula"
}
```
Then you just need to enter <kbd>d</kbd>+<kbd>d</kbd> and return to get the double dollars with cursor between them.

<img src="https://github.com/SwitWu/LaTeX-Workshop-wiki/blob/master/configureSnippets.gif" alt="configure user snippets demo" height="200px">
