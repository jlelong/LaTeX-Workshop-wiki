# Playing with environments and LaTeX syntax tree

## Inserting an environment

- To start a new environment, you can type `\begin` and use intellisense. See [Intellisense for Environments](Intellisense#environments) for a detailed explanation of the different mechanisms.
- Most environments can also be started by simply typing `\` followed by the environment name. For instance, to start en `equation` environment, type `\equation` and choose the `\begin{equation}...\end{equation}` snippet. See [Intellisense for Environments](Intellisense#environments)
- Some common environments have specific snippets of the form `B` + the first two or three letters of the environment name, see [the full list](Snippets#Environments).
- To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

## Itemize like environments

When the current line starts with `\item` or `\item[]`, hitting `Enter` automatically adds a newline starting in the same way. For a better handling of the last item, hitting `Enter` on a line only containing `\item` or `\item[]` actually deletes the content of the line. The `alt+Enter` key is bind to the standard newline command.

This automatic insertion of `\item` can be deactivated by setting `latex-workshop.bind.enter.key` to `false`.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/auto item.gif" alt="auto \item demo" height="80px">

In any case, you can use the shortcut <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>Enter</kbd> to insert a newline and `\item`. On Mac, <kbd>ctrl</kbd> is replaced by <kbd>⌘</kbd>.

## Navigating and selecting

- To navigate from `\begin/\end` to the corresponding `\end/\begin`, while on the `begin` or `end` keywords, call _LaTeX Workshop: Navigate to matching begin/end_ from the _Command Palette_ (command `latex-workshop.navigate-envpair`). This function considers blocks surrounded by `\[...\]`, `$$...$$`, `\(...\)` or `$...$` as environments.
- To select the inner content of an environment, excluding the opening and closing statements, call _LaTeX Workshop: Select the current environment content_ from the _Command Palette_ (command `latex-workshop.select-envcontent`). This function considers blocks surrounded by `\[...\]`, `$$...$$`, `\(...\)` or `$...$` as environments. Repeated calls result in selecting the outer environments.
- To select the whole environment, including the opening and closing statements, call _LaTeX Workshop: Select the current environment_ from the _Command Palette_ (command `latex-workshop.select-env`). This function considers blocks surrounded by `\[...\]`, `$$...$$`, `\(...\)` or `$...$` as environments. Repeated calls result in selecting the outer environments.
- To select the current environment name, call _LaTeX Workshop: Select the current environment name_ from the _Command Palette_ (command `latex-workshop.select-envname`). For this command to work, the cursor must be strictly between `\begin{...}` and `\end{...}`. If the current environment is `\[...\]`, this function will automatically convert it into `\begin{equation*}...\end{equation*}`. Repeated calls result in selecting the outer environments. **Note**: this function _does not_ work with the [Vim](https://github.com/VSCodeVim/Vim) extension.
- To add a multi-cursor to the current environment name, call _LaTeX Workshop: Add a multi-cursor to the current environment name_ from the _Command Palette_ (command `latex-workshop.multicursor-envname`). If the current environment is `\[...\]`, this function will automatically convert it into `\begin{}...\end{}`. For this command to work, the cursor must be strictly between `\begin{...}` and `\end{...}`. Repeated calls result in selecting the outer environments.

These three functions are directly available from the TeX badge.

## Changing between `\[...\]` and `\begin{}...\end{}`

- The commands `latex-workshop.select-envname` and `latex-workshop.multicursor-envname` described above, allow one to change a pair of `\[...\]` into any other math environment (e.g. `equation` or `align`).
- To go backwards, call _LaTeX Workshop: Toggle between \\[...\\] and \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.toggle-equation-envname`). This command changes `\[...\]` to `\begin{equation*}...\end{equation*}` (without moving the cursor) and it changes the following environments to `\[...\]`: `equation, align, flalign, alignat, gather, multline, eqnarray` (and their starred variants).

## Closing the current environment

- To auto close LaTeX environments, call _LaTeX Workshop: Close current environment_ from the **Command Palette** (command function `latex-workshop.close-env`).

## Surrounding selection with an environment

To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-env.gif" alt="Surround with environment demo">

Alternatively, you can select the text and insert the environment using either the `\envname` command or the `\beginend` snippet but not the `\begin` snippet.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-envname.gif" alt="Surround with environment demo">

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-beginend.gif" alt="Surround with environment demo">

###`latex-workshop.bind.enter.key`


Enable the automatic insertion of `\item` on a newline when pressing `Enter` in a line starting in `\item`.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

###`latex-workshop.selection.smart.latex.enabled`

Enable AST based smart selection. Command ids are `editor.action.smartSelect.expand` and `editor.action.smartSelect.shrink`.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |
