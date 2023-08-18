# Hovering and previewing features

Hover can also be triggered using `C-k C-i`.

## Documentation of a package

To open a package documentation, hover the package name inside the `\usepackage` call and click on the _View documentation_ link. As it internally calls `texdoc`, if it is not in your path you may need to set [`latex-workshop.texdoc.path`](#latex-workshoptexdocpath) to the full path of `texdoc` and tweak [`latex-workshop.texdoc.args`](#latex-workshoptexdocargs).

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-package.gif" alt="Hover on a package demo">

You may also directly call one the following commands

- _LaTex Workshop: Show package documentation_: you will get an input box to type in the package name. If you want to define a keybinding for this feature, associate it to the internal command `latex-workshop.texdoc`.
- _LaTex Workshop: Show package documentation actually used_ : you can select the package name within a list. If you want to define a keybinding for this feature, associate it to the internal command `latex-workshop.texdocUsepackages`.

## Previewing equations

### On the fly

When you move the mouse cursor over inline math, `\[`, `$$`, `\begin{align}`, and `\begin{...}` of other math environments, math preview on hover is rendered. When you move the mouse cursor over `\ref`, and other reference commands referring math equations, math preview on hover is also rendered.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover.gif" alt="Preview maths demo" height="120px">

Supported math environments are `align`, `align*`, `alignat`, `alignat*`, `aligned`, `alignedat`, `array`, `Bmatrix`, `bmatrix`, `cases`, `CD`, `eqnarray`, `eqnarray*`, `equation`, `equation*`, `gather`, `gather*`, `gathered`, `matrix`, `multline`, `multline*`, `pmatrix`, `smallmatrix`, `split`, `subarray`, `Vmatrix`, `vmatrix`.

The `tabular` environment is not supported.

| Setting key | Description |
|------------|------------|
| [`latex-workshop.hover.preview.enabled`](#latex-workshophoverpreviewenabled) | Enable hover preview |
| [`latex-workshop.hover.preview.scale`](#latex-workshophoverpreviewscale) | Scale of hover preview |
| [`latex-workshop.hover.preview.cursor.enabled`](#latex-workshophoverpreviewcursorenabled) | Render cursor in hover preview |
| [`latex-workshop.hover.preview.cursor.symbol`](#latex-workshophoverpreviewcursorsymbol) | Define the cursor symbol |
| [`latex-workshop.hover.preview.cursor.color`](#latex-workshophoverpreviewcursorcolor) | Define the cursor color |
| [`latex-workshop.hover.preview.newcommand.parseTeXFile.enabled`](#latex-workshophoverpreviewnewcommandparseTeXFileenabled) | Add newcommands to preview |
| [`latex-workshop.hover.preview.newcommand.newcommandFile`](#latex-workshophoverpreviewnewcommandnewcommandFile) | Path of a file containing newcommands |
| [`latex-workshop.hover.preview.mathjax.extensions`](#latex-workshophoverpreviewmathjaxextensions) | MathJax extensions to load |

### Realtime math preview panel

You can preview equation in realtime in a separate editor by using the _math preview panel_. The position of the editor is determined by [`latex-workshop.mathpreviewpanel.editorGroup`](#latex-workshopmathpreviewpaneleditorGroup)

- To open the panel call _Open Math Preview Panel_ (internal command is `latex-workshop.openMathPreviewPanel`)
- To close the panel call _Close Math Preview Panel"_ (internal command is `latex-workshop.closeMathPreviewPanel`)
- To toggle the panel call _Toggle Math Preview Panel_ (internal command is `latex-workshop.toggleMathPreviewPanel`)

Only math environments with less than [`latex-workshop.hover.preview.maxLines`](#latex-workshophoverpreviewmaxLines) lines are properly updated.

## Previewing graphics

When [`latex-workshop.hover.preview.enabled`](#latex-workshophovercitationenabled) is set to `true`, moving the mouse over an argument of `\includegraphics` shows a preview of the graphics file.

## Previewing citation details

When [`latex-workshop.hover.citation.enabled`](#latex-workshophovercitationenabled) is set to `true`, moving the mouse over an argument of a `\cite` related command displays the details of the bibliography as a tooltip. See [`latex-workshop.intellisense.citation.format`](Intelissense##latex-workshopintellisensecitationformat)

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-cite.gif" alt="Hover on \cite demo">

## Previewing references

When [`latex-workshop.hover.ref.enabled`](#latex-workshophoverrefenabled) is set to `true`, moving the mouse over a `\ref` related command displays the piece of `tex` with the corresponding label as a tooltip. Moreover, if the label refers to a math environment as described in [Preview equations](#Preview-equations), math preview is rendered instead of showing the tex content. The tooltip has a `View on pdf` link to jump to the corresponding location in the `PDF` viewer. It only calls `synctex` as if you were directly calling _SyncTeX from cursor_ and therefore it requires a PDF viewer for the current `.tex` file to be opened.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-ref.gif" alt="Hover on \ref demo" height="300px">

| Setting key | Description |
|------------|------------|
| [`latex-workshop.hover.ref.enabled`](#latex-workshophoverrefenabled) | Enable hover on references |
| [`latex-workshop.hover.ref.number.enabled`](#latex-workshophoverrefnumberenabled) | Show number assigned to the reference in the previous compilation |

## Documentation of a command

When [`latex-workshop.hover.command.enabled`](#latex-workshophovercommandenabled) is set to `true`, moving the mouse over a command displays the different forms (signatures) of the command with their arguments as a tooltip. You can directly access the documentation of the package(s) defining the command by clicking on the package name(s).

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-command.gif" alt="Hover on a command demo">

## Configuration variables

### `latex-workshop.hover.ref.enabled`

Enable Hover on References.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.ref.number.enabled`

Show the number assigned to the reference in the previous compilation.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.citation.enabled`

Enable Hover on Citations.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.command.enabled`

Enable Hover on Commands to show the possible signatures.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.preview.enabled`

Enable preview on hover.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.preview.scale`

Scale of preview on hover.

| type     | default value |
| -------- | ------------- |
| _number_ | `1`           |

### `latex-workshop.hover.preview.newcommand.parseTeXFile.enabled`

Enable newcommands defined in the current TeX file to be included in Hover Preview. We currently only support commands defined on **a single line**.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.preview.newcommand.newcommandFile`

Set the path of a file containing newcommands to be used in Hover Preview. If the path is relative, it is joined with the root dir.

| type     | default value |
| -------- | ------------- |
| _string_ | ""            |

### `latex-workshop.hover.preview.mathjax.extensions`

MathJax extensions to load for Hover Preview. See [the list](https://docs.mathjax.org/en/latest/input/tex/extensions/index.html). Notice that extensions, `ams`, `color`, `newcommand`, `noerrors`, and `noundefined` are loaded by default. They cannot be disabled.

| type     | default value | possible values |
| -------- | ------------- | -- |
| _array_  | []            | `"amscd"`, `"bbox"`, `"boldsymbol"`, `"braket"`, `"bussproofs"`, `"cancel"`, `"cases"`, `"centernot"`, `"colortbl"`, `"empheq"`, `"enclose"`, `"extpfeil"`, `"gensymb"`, `"html"`, `"mathtools"`, `"mhchem"`, `"physics"`, `"textcomp"`, `"textmacros"`, `"unicode"`, `"upgreek"`, `"verb"` |

### `latex-workshop.hover.preview.cursor.enabled`

Render cursor in math preview on hover at the current position.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.hover.preview.cursor.symbol`

Define the cursor symbol in math preview on hover.

| type     | default value |
| -------- | ------------- |
| _string_ | `\ddagger`    |

### `latex-workshop.hover.preview.cursor.color`

Define the color of the cursor in math preview on hover.

| type     | default value | possible values                                                                                                                                                                                                                |
| -------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| _string_ | "auto"        | `"auto"`, `"black"`, `"blue"`, `"brown"`, `"cyan"`, `"darkgray"`, `"gray"`, `"green"`, `"lightgray"`, `"lime"`, `"magenta"`, `"olive"`, `"orange"`, `"pink"`, `"purple"`, `"red"`, `"teal"`, `"violet"`, `"white"`, `"yellow"` |

### `latex-workshop.view.pdf.ref.viewer`

PDF viewer used for `[View on PDF]` link on hover over `\ref`, and other reference commands.

| type     | default value | possible values                          |
| -------- | ------------- | ---------------------------------------- |
| _string_ | "auto"        | `"auto"`, `"tabOrBrowser"`, `"external"` |

### `latex-workshop.texdoc.path`

Define the location of texdoc executable.

| type      | default value |
| --------- | ------------- |
| _string_  | "texdoc"      |

### `latex-workshop.texdoc.args`

Texdoc arguments to see a package documentation.

| type      | default value |
| --------- | ------------- |
| _array_   | `["--view"]`  |

The package name is automatically appended to the arguments.

### `latex-workshop.mathpreviewpanel.editorGroup`

The editor group in which to open the math preview panel.

| type       | default value |
| ---------- | ------------- |
| _string_   | `"below"`     |

The accepted values are:

- current: Use the current editor group
- left: Put the math preview panel in a new group on the left of the current one
- right: Put the math preview panel in a new group on the right of the current one
- above: Put the math preview panel in a new group above the current one
- below: Put the math preview panel in a new group below the current one

### `latex-workshop.mathpreviewpanel.cursor.enabled`

**This feature is experimental. If you report an issue to us on this feature, we may not fix it. We will not accept any pull requests.**
Render a cursor on the math preview panel.

| type       | default value |
| ---------- | ------------- |
| _boolean_  | `false`       |


### `latex-workshop.hover.preview.maxLines`

Maximum number of lines between the beginning of the math environment and the cursor position to allow preview.

| type       | default value |
| ---------- | ------------- |
| _number_   | `20`          |
