# Hovering features

Hover can also be triggered using `C-k C-i`.

## Documentation of a package

To open a package documentation, hover the package name inside the `\usepackage` call and click on the _View documentation_ link. As it internally calls `texdoc`, if it is not in your path you may need to set [`latex-workshop.texdoc.path`](latex-workshoptexdocpath) to the full path of `texdoc`.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-package.gif" alt="Hover on a package demo">

You may also directly run the _LaTex Workshop: Show package documentation_ command from the Command Palette and type in the package name.

## Previewing equations

When you move the mouse cursor over inline math, `\[`, `$$`, `\begin{align}`, and `\begin{...}` of other math environments, math preview on hover is rendered. When you move the mouse cursor over `\ref`, and other reference commands referring math equations, math preview on hover is also rendered.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover.gif" alt="Preview maths demo" height="120px">

Supported math environments are `align`, `align*`, `alignat`, `alignat*`, `aligned`, `alignedat`, `array`, `Bmatrix`, `bmatrix`, `cases`, `CD`, `eqnarray`, `eqnarray*`, `equation`, `equation*`, `gather`, `gather*`, `gathered`, `matrix`, `multline`, `multline*`, `pmatrix`, `smallmatrix`, `split`, `subarray`, `Vmatrix`, `vmatrix`.

The `tabular` environment is not supported.

| Setting key | Description |
|------------|------------|
| [`latex-workshop.hover.preview.enabled`](#latex-workshophoverpreviewenabled) | Enable math preview |
| [`latex-workshop.hover.preview.scale`](#latex-workshophoverpreviewscale) | Scale of math preview |
| [`latex-workshop.hover.preview.cursor.enabled`](#latex-workshophoverpreviewcursorenabled) | Render cursor in math preview |
[`latex-workshop.hover.preview.cursor.symbol`](#latex-workshophoverpreviewcursorsymbol) | Define the cursor symbol |
[`latex-workshop.hover.preview.cursor.color`](#latex-workshophoverpreviewcursorcolor) | Define the cursor color |

## Previewing citation details

When [`latex-workshop.hover.citation.enabled`](#latex-workshophovercitationenabled) is set to `true`, moving the mouse over an argument of a `\cite` related command displays the details of the bibliography as a tooltip.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-cite.gif" alt="Hover on \cite demo">

## Previewing references

When [`latex-workshop.hover.reference.enabled`](#latex-workshophoverreferenceenabled) is set to `true`, moving the mouse over a `\ref` related command displays the piece of `tex` with the corresponding label as a tooltip. Moreover, if the label refers to a math environment as described in [Preview equations](#Preview-equations) and [`latex-workshop.hover.preview.ref.enabled`](#latex-workshophoverpreviewrefenabled) is set to `true`, math preview is rendered instead of showing the tex content. The tooltip has a `View on pdf` link to jump to the corresponding location in the `PDF` viewer. It only calls `synctex` 
as if you were directly calling _SyncTeX from cursor_ and therefore it requires a PDF viewer for the current `.tex` file to be opened.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-ref.gif" alt="Hover on \ref demo" height="300px">

| Setting key | Description |
|------------|------------|
| [`latex-workshop.hover.ref.enabled`](#latex-workshophoverrefenabled) | Enable hover on references |
| [`latex-workshop.hover.ref.numberAtLastCompilation.enabled`](#latex-workshophoverrefnumberAtLastCompilationenabled) | Show number the given to ref at the last compilation. |

## Documentation of a command

When [`latex-workshop.hover.command.enabled`](#latex-workshophovercommandenabled) is set to `true`, moving the mouse over a command displays the different forms (signatures) of the command with their arguments as a tooltip. You can directly access the documentation of the package(s) defining the command by clicking on the package name(s).

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover-command.gif" alt="Hover on a command demo">

## Configuration variables

### latex-workshop.hover.ref.enabled

Enable Hover on References.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.ref.numberAtLastCompilation.enabled

Show number the given to ref at the last compilation.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`        |

### latex-workshop.hover.citation.enabled

Enable Hover on Citations.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.command.enabled

Enable Hover on Commands to show the possible signatures.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.preview.enabled

Enable math preview on hover.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.preview.scale

Scale of math preview on hover.

| type     | default value |
| -------- | ------------- |
| _number_ | 1             |

### latex-workshop.hover.preview.newcommand.parseTeXFile.enabled

Enable newcommands defined in the current TeX file to be included in Hover Preview.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.preview.newcommand.newcommandFile

Set the path of a file containing newcommands to be used in Hover Preview. If the path is relative, it is joined with the root dir.

| type     | default value |
| -------- | ------------- |
| _string_ | ""    |

### latex-workshop.hover.preview.cursor.enabled

Render cursor in math preview on hover at the current position.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hover.preview.cursor.symbol

Define the cursor symbol in math preview on hover.

| type     | default value |
| -------- | ------------- |
| _string_ | `\ddagger`    |

### latex-workshop.hover.preview.cursor.color

Define the color of the cursor in math preview on hover.

| type     | default value | possible values                                                                                                                                                                                                                |
| -------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| _string_ | "auto"        | `"auto"`, `"black"`, `"blue"`, `"brown"`, `"cyan"`, `"darkgray"`, `"gray"`, `"green"`, `"lightgray"`, `"lime"`, `"magenta"`, `"olive"`, `"orange"`, `"pink"`, `"purple"`, `"red"`, `"teal"`, `"violet"`, `"white"`, `"yellow"` |

### latex-workshop.hover.preview.ref.enabled

Render math preview on hover over `\ref`, and other reference commands.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.view.pdf.ref.viewer

PDF viewer used for `[View on PDF]` link on hover over `\ref`, and other reference commands.

| type     | default value | possible values                          |
| -------- | ------------- | ---------------------------------------- |
| _string_ | "auto"        | `"auto"`, `"tabOrBrowser"`, `"external"` |
