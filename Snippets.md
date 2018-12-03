# Snippets and shortcuts

All commands are listed as <kbd>ctrl</kbd>+<kbd>some key</kbd>. If you're on Mac, don't worry we have written equivalents, so every time you see <kbd>ctrl</kbd>  just imagine it's <kbd>⌘</kbd>.

## Environments

| Prefix |                          Command                           |
| ------ | ---------------------------------------------------------- |
| `BEQ`  | `\begin{equation}\n  \label{${1}}\n  $0\n\end{equation}`   |
| `BSEQ` | `\begin{equation*}\n  $0\n\end{equation*}`                 |
| `BAL`  | `\begin{align}\n  \label{${1}}\n  $0\n\end{align}`         |
| `BSAL` | `\begin{align*}\n  $0\n\end{align*}`                       |
| `BIT`  | `\begin{itemize}\n  \item $0\n\end{itemize}`               |
| `BEN`  | `\begin{enumerate}\n  \item $0\n\end{enumerate}`           |
| `BSPL` | `\begin{split}\n  $0\n\end{split}`                         |
| `BCAS` | `\begin{cases}\n  $0\n\end{cases}`                         |
| `BFR`  | `\begin{frame}\n  \frametitle{${1}\n\n  $0\n\n\end{frame}` |

## Inserting Greek letters

Greek Letters can be inserted using the LaTeX command, which will autocomplete or using `@` + letter

| Prefix |    Letter     |
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


| Prefix |       Command        |
| ------ | -------------------- |
| `@(`   | `\left( $0 \right)`  |
| `@{`   | `\left\{ $0\right\}` |
| `@[`   | `\left[ $0 \right]`  |
| `__`   | `_{$0}`              |
| `**`   | `^{$0}`              |
| `...`  | `\dots`              |
| `@.`   | `\cdot`              |
| `@8`   | `\infty`             |
| `@6`   | `\partial`           |
| `@/`   | `\frac{$1}{$2}$0`    |
| `@%`   | `\frac{$1}{$2}$0`    |
| `@^`   | `\Hat{$1}$0`         |
| `@_`   | `\bar{$1}$0`         |
| `@@`   | `\circ`              |
| `@0`   | `^\circ`             |
| `@;`   | `\dot{$1}$0`         |
| `@:`   | `\ddot{$1}$0`        |
| `@=`   | `\equiv`             |
| `@*`   | `\times`             |
| `@<`   | `\leq`               |
| `@>`   | `\geq`               |
| `@2`   | `\sqrt{$1}$0`        |
| `@I`  | `\int_{$1}^{$2}$0`   |
| <code>@&#124;</code>  | <code>\Big &#124;</code>            |
| `@\`   | `\setminus`          |
| `@+`   | `\bigcup`            |
| `@-`   | `\bigcap`            |
| `@,`   | `\nonumber`          |

## Font commands

|   Prefix   |                            Shortcut                            |         Command          |
| ---------- | -------------------------------------------------------------- | ------------------------ |
| `fontsize` |                                                                | Opens font size select   |
| `FNO`      |                                                                | `\textnormal{${1}}`      |
| `FRM`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>r</kbd>     | `\textrm{${1}}`          |
| `FEM`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>e</kbd>     | `\emph{${1}}`            |
| `FSF`      |                                                                | `\textsf{${1}}`          |
| `FTT`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>t</kbd>     | `\texttt{${1}}`          |
| `FIT`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>i</kbd>     | `\textit{${1}}`          |
| `FSL`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>s</kbd>     | `\textsl{${1}}`          |
| `FSC`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>c</kbd>     | `\textsc{${1}}`          |
| `FUL`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>u</kbd>     | `\underline{${1}}`       |
| `FUC`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>u</kbd>     | `\uppercase{${1}}`       |
| `FLC`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>l</kbd>     | `\lowercase{${1}}`       |
| `FBF`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>b</kbd>     | `\textbf{${1}}`          |
| `FSS`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>6</kbd>     | `\textsuperscript{${1}}` |
| `FBS`      | <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>minus</kbd> | `\textsubscript{${1}}`   |


## Mathematical font commands

| Prefix |                                Shortcut                                 |     Command      |
| ------ | ----------------------------------------------------------------------- | ---------------- |
| `MRM`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>r</kbd>              | `\mathrm{${1}}`  |
| `MBF`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>S</kbd>+<kbd>b</kbd> | `\mathbf{${1}}`  |
| `MBB`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>b</kbd>              | `\mathbb{${1}}`  |
| `MCA`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>c</kbd>              | `\mathcal{${1}}` |
| `MIT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>i</kbd>              | `\mathit{${1}}`  |
| `MTT`  | <kbd>ctrl</kbd>+<kbd>m</kbd>, <kbd>ctrl</kbd>+<kbd>t</kbd>              | `\mathtt{${1}}`  |

## Miscellaneous Actions

| Shortcut                                                       | Action                   |
| -------------------------------------------------------------- | ------------------------ |
| <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>Enter</kbd> | Insert newline + `\item` |

## Surround text

### with a command

To surround text with a command, just select some text and use <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>w</kbd> (<kbd>⌘</kbd>+<kbd>l</kbd>, <kbd>⌘</kbd>+<kbd>w</kbd> on Mac). A new menu pops up to select the command. This works with multi selections.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/wrap.gif" alt="wrap demo" height="140px">

### With an environment

To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.