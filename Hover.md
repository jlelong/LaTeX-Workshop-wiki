# Hovering features

## Access a package documentation

To open a package documentation, hover the package name inside the `\usepackage` call and click on the _View documentation_ link. As it internally calls `texdoc`, if it is not in your path you may need to set [`latex-workshop.texdoc.path`](latex-workshoptexdocpath) to the full path of `texdoc`.

## Preview equations

When you move the mouse cursor over inline math,  `\[`,  `\begin{align}`, and `\begin{...}` of other math environments, math preview on hover is rendered. When you move the mouse cursor over `\ref`, and other reference commands referring math equations, math preview on hover is also rendered.

 <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/hover.gif" alt="auto \item demo" height="120px">

Supported math environments are `align`, `align*`, `alignat`, `alignat*`, `aligned`, `alignedat`, `array`, `Bmatrix`, `bmatrix`, `cases`, `CD`, `eqnarray`, `eqnarray*`, `equation`, `equation*`, `gather`, `gather*`, `gathered`, `matrix`, `multline`, `multline*`, `pmatrix`, `smallmatrix`, `split`, `subarray`, `Vmatrix`, `vmatrix`.

`$$` is not supported. `tabular` not supported.

## View citation details

## Preview references

## View the signatures for a command

## Configuration variables

### latex-workshop.hoverReference.enabled

Enable Hover on References.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |
P
### latex-workshop.hoverCitation.enabled

Enable Hover on Citations.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverCommandDoc.enabled

Enable Hover on Commands to show the possible signatures.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverPreview.enabled

Enable math preview on hover.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverPreview.scale

Scale of math preview on hover.

| type      | default value |
| --------- | ------------- |
| _number_  | 1             |

### latex-workshop.hoverPreview.cursor.enabled

Render cursor in math preview on hover at the current position.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverPreview.cursor.symbol

Define the cursor symbol in math preview on hover.

| type      | default value |
| --------- | ------------- |
| _string_ | `\ddagger`     |

### latex-workshop.hoverPreview.cursor.color

Define the color of the cursor in math preview on hover.

| type      | default value |
| --------- | ------------- |
| _string_  | "auto"        |

The possible values are : ` "auto" | "black" | "blue" | "brown" | "cyan" | "darkgray" | "gray" | "green" | "lightgray" | "lime" | "magenta" | "olive" | "orange" | "pink" | "purple" | "red" | "teal" | "violet" | "white" | "yellow"`.

### latex-workshop.hoverPreview.ref.enabled

Render math preview on hover over `\ref`, and other reference commands.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.view.pdf.ref.viewer

PDF viewer used for `[View on PDF]` link on hover over `\ref`, and other reference commands.

| type      | default value |
| --------- | ------------- |
| _string_  | "auto"        |

The possible values are : `"auto" | "tabOrBrowser" | "external"`.