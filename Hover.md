# Hovering features

## Access a package documentation

To open a package documentation, hover the package name inside the `\usepackage` call and click on the _View documentation_ link. As it internally calls `texdoc`, if it is not in your path you may need to set [`latex-workshop.texdoc.path`](latex-workshoptexdocpath) to the full path of `texdoc`.

## Preview equations

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

Enable Hover Preview.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverPreview.scale

Scale of Hover Preview.

| type      | default value |
| --------- | ------------- |
| _number_  | 1             |

### latex-workshop.hoverPreview.cursor.enabled

Render cursor in Hover Preview at the current position.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.hoverPreview.cursor.symbol

Define the cursor symbol in Hover Preview.

| type      | default value |
| --------- | ------------- |
| _string_ | `\ddagger`     |

### latex-workshop.hoverPreview.cursor.color

Define the color of the cursor in Hover Preview.

| type      | default value |
| --------- | ------------- |
| _string_  | "auto"        |

The possible values are : ` "auto" | "black" | "blue" | "brown" | "cyan" | "darkgray" | "gray" | "green" | "lightgray" | "lime" | "magenta" | "olive" | "orange" | "pink" | "purple" | "red" | "teal" | "violet" | "white" | "yellow"`.

### latex-workshop.hoverPreview.ref.enabled

Render Hover Preview on `\\ref` commands.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |