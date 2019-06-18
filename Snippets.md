# Snippets and shortcuts

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
| `BIT`  | `itemize`        |
| `BEN`  | `enumerate`      |
| `BSPL` | `split`          |
| `BCAS` | `cases`          |
| `BFR`  | `frame`          |
| `BFI`  | `figure`         |

## Sectioning

### An overview of the document

The structure of the LaTeX project (`\chapter`, `\section`, `\subsection`, ...) is accessible via the TeX panel on the left of the editor. The entry corresponding to the cursor position in the editor is automatically selected and follows the cursor. The outline hierarchy is defined by [`latex-workshop.view.outline.sections`](latex-workshopviewoutlinesections).

Note that the Explorer panel also contains an outline view but it only shows the structure of the current file and does not take into account any included file.

#### latex-workshop.view.outline.sections

The section names of LaTeX outline hierarchy. It is also used by the folding mechanism.

This property is an array of case-sensitive strings in the order of the document structure hierarchy. For multiple tags of the same level, separate the tags with `|` as delimiters, e.g., `section|alternative`.

|         type         |                           default value                           |
| -------------------- | ----------------------------------------------------------------- |
| _array_ of _strings_ | `[ "part", "chapter", "section", "subsection", "subsubsection" ]` |


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

### Incrementing/decrementing sectioning levels

Adjusting sectioning levels can be done using `latex-workshop.increment-sectioning` and `latex-workshop.decrement-sectioning`.

These methods replace all sectioning commands with the sectioning command one level higher or lower. They apply either to the current line or to every selected line.

#### Example

Applying `latex-workshop.increment-sectioning` to the following selection,

```
\subsection{Demo}
\paragraph{Content}
```

yields

```
\section{Demo}
\subsubsection{Content}
```

#### Keybindings

This functionality has two keybindings

| Method               | Shortcut                                    | Alternate                                 |
| -------------------- | ------------------------------------------- | ----------------------------------------- |
| Increment Sectioning | <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>]</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>]</kbd> |
| Decrement Sectioning | <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>[</kbd> | <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>]</kbd> |

To use the alternate shortcuts, set `latex-workshop.bind.altKeymap.enabled` to `true`.

## Inserting Greek letters

Greek Letters can be inserted using the LaTeX command, which will autocomplete or using `@` + letter

| Prefix | Letter        |
| ------ | ------------- |
| `@a`   | `\alpha`      |
| `@b`   | `\beta`       |
| `@c`   | `\chi`        |
| `@d`   | `\delta`      |
| `@e`   | `\epsilon`    |
| `@f`   | `\phi`        |
| `@g`   | `\gamma`      |
| `@h`   | `\eta`        |
| `@i`   | `\iota`       |
| `@k`   | `\kappa`      |
| `@l`   | `\lambda`     |
| `@m`   | `\mu`         |
| `@n`   | `\nu`         |
| `@p`   | `\pi`         |
| `@q`   | `\theta`      |
| `@r`   | `\rho`        |
| `@s`   | `\sigma`      |
| `@t`   | `\tau`        |
| `@u`   | `\upsilon`    |
| `@s`   | `\sigma`      |
| `@o`   | `\omega`      |
| `@&`   | `\wedge`      |
| `@x`   | `\xi`         |
| `@y`   | `\psi`        |
| `@z`   | `\zeta`       |
| `@D`   | `\Delta`      |
| `@F`   | `\Phi`        |
| `@G`   | `\Gamma`      |
| `@Q`   | `\Theta`      |
| `@L`   | `\Lambda`     |
| `@X`   | `\Xi`         |
| `@Y`   | `\Psi`        |
| `@S`   | `\Sigma`      |
| `@U`   | `\Upsilon`    |
| `@W`   | `\Omega`      |
| `@ve`  | `\varepsilon` |
| `@vf`  | `\varphi`     |
| `@vs`  | `\varsigma`   |
| `@vq`  | `\vartheta`   |

## Handy mathematical snippets

Some common mathematical symbols or commands have a dedicated snippet.

| Prefix               | Command                  |
| -------------------- | ------------------------ |
| `@(`                 | `\left( $1 \right)`      |
| `@{`                 | `\left\{ $1 \right\}`    |
| `@[`                 | `\left[ $1 \right]`      |
| `__`                 | `_{$1}`                  |
| `**`                 | `^{$1}`                  |
| `...`                | `\dots`                  |
| `@.`                 | `\cdot`                  |
| `@8`                 | `\infty`                 |
| `@6`                 | `\partial`               |
| `@/`                 | `\frac{$1}{$2}`          |
| `@%`                 | `\frac{$1}{$2}`          |
| `@^`                 | `\Hat{$1}`               |
| `@_`                 | `\bar{$1}`               |
| `@@`                 | `\circ`                  |
| `@0`                 | `^\circ`                 |
| `@;`                 | `\dot{$1}`               |
| `@:`                 | `\ddot{$1}`              |
| `@=`                 | `\equiv`                 |
| `@*`                 | `\times`                 |
| `@<`                 | `\leq`                   |
| `@>`                 | `\geq`                   |
| `@2`                 | `\sqrt{$1}`              |
| `@I`                 | `\int_{$1}^{$2}`         |
| <code>@&#124;</code> | <code>\Big &#124;</code> |
| `@\` | `\setminus`   |
| `@+`                 | `\bigcup`                |
| `@-`                 | `\bigcap`                |
| `@,`                 | `\nonumber`              |

## Font commands

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

## Mathematical font commands

| Prefix | Shortcut                                                                | Command          |
| ------ | ----------------------------------------------------------------------- | ---------------- |
| `MRM`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>r</kbd>              | `\mathrm{${1}}`  |
| `MBF`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>s</kbd>              | `\mathbf{${1}}`  |
| `MBB`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>b</kbd>              | `\mathbb{${1}}`  |
| `MCA`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>c</kbd>              | `\mathcal{${1}}` |
| `MIT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>i</kbd>              | `\mathit{${1}}`  |
| `MTT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>t</kbd>              | `\mathtt{${1}}`  |

## Miscellaneous Actions

| Shortcut                                                       | Action                   |
| -------------------------------------------------------------- | ------------------------ |
| <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>Enter</kbd> | Insert newline + `\item` |

## Surrounding text

### with a command

To surround text with a command, just select some text and use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>w</kbd> (<kbd>⌘</kbd>+<kbd>l</kbd>, <kbd>⌘</kbd>+<kbd>w</kbd> on Mac). A new menu pops up to select the command. This works with multi selections.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/wrap.gif" alt="wrap demo" height="140px">

### With an environment

To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-env.gif" alt="Surround with environment demo">
