# Playing with environments

## Inserting an environment

- To start a new environment, you can type `\begin` and select the _begin a new environment_ snippet. A multi-cursor is added to enter the environment name simultaneously in the `begin` and `end` commands.
- Most environments can also be started by simply typing `\` followed by the environment name. For instance, to start en `equation` environment, type `\equation` and choose the `\begin{equation}...\end{equation}` snippet.
- Some common environments have specific snippets of the form `B` + the first two or three letters of the environment name, see [the full list](Snippets#Environments).
- To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

## Itemize like environments

When the current line starts with `\item` or `\item[]`, hitting `Enter` automatically adds a newline starting in the same way. For a better handling of the last item, hitting `Enter` on a line only containing `\item` or `\item[]` actually deletes the content of the line. The `alt+Enter` key is bind to the standard newline command.

This automatic insertion of `\item` can be deactivated by setting `latex-workshop.bind.enter.key` to `false`.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/auto item.gif" alt="auto \item demo" height="80px">

In any case, you can use the shortcut <kbd>ctrl</kbd>+<kbd>l</kbd>, <kbd>ctrl</kbd>+<kbd>Enter</kbd> to insert a newline and `\item`. On Mac, <kbd>ctrl</kbd> is replaced by <kbd>⌘</kbd>.

## Navigating

- To navigate from `\begin/\end` to the corresponding `\end/\begin`, while on the `begin` or `end` keywords, call _LaTeX Workshop: Navigate to matching begin/end_ from the **Command Palette** (command `latex-workshop.navigate-envpair`).
- To select the current environment name, call _LaTeX Workshop: Select the current environment name_ from the **Command Palette** (command `latex-workshop.select-envname`). For this command to work, the cursor must be strictly between `\begin{...}` and `\end{...}`. Repeated calls result in selecting the outer environment. **Note**: this function _does not_ work with the [Vim](https://github.com/VSCodeVim/Vim) extension.
- To add a multi-cursor to the current environment name, call _LaTeX Workshop: Add a multi-cursor to the current environment name_ from the **Command Palette** (command `latex-workshop.multicursor-envname`). For this command to work, the cursor must be strictly between `\begin{...}` and `\end{...}`. Repeated calls result in selecting the outer environments.

These three functions are directly available from the TeX badge.

## Closing the current environment

- To auto close LaTeX environments, call _LaTeX Workshop: Close current environment_ from the **Command Palette** (command function `latex-workshop.close-env`).

## Surrounding selection with an environment

To surround some selected text with an environment, call _LaTeX Workshop: Surround/wrap selection with \\begin{}...\\end{}_ from the **Command Palette** (command `latex-workshop.wrap-env`). A multi-cursor is added inside the braces, to insert the environment name.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-env.gif" alt="Surround with environment demo">