from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid - Row Height",
)

text1 = """
# Row Height
By default, the grid will display rows with a height of `25px`.  

You can change the row height be using `rowHeight` or setting `autoHeight=True`


### Text Wrapping

If you want text to wrap inside cells rather than truncating, add  `wrapText=True` to the Column Definition.


The example below has `wrapText=True` set on the Latin Text column. Behind the scenes, this results in the CSS property `white-space: normal` being applied to the cell, which causes the text to wrap.
It also sets the row to a fixed height using `rowHeight=120` on the grid level.
"""

text2 = """
>
> If you are providing a custom Cell Renderer Component, you can implement text wrapping in the custom component in your own way. The property wrapText is intended to be used when you are not using a custom Cell Renderer.
>

### Auto Row Height
It is possible to set the row height based on the contents of the cells. To do this, set `autoHeight=True` on each column where height should be calculated from. For example, if one column is showing description text over multiple lines, then you may choose to select only that column to determine the line height.

`autoHeight` is typically used with `wrapText`. If `wrapText` is not set, and no custom Cell Renderer Component is used, then the cell will display all it's contents on one line. This is probably not the intention if using Auto Row Height.

If multiple columns are marked with `autoHeight=True` then the height of the largest column is used.

The example below shows auto height. The column with the latin text has variable length sentences.  It has Auto Height enabled by setting both `wrapText=True` and `autoHeight=True`. 

"""

text3 = """
### Lazy Height Calculation
Auto height works by the grid listening for height changes for all Cells configured for Auto Height. As such it is only looking at rows that are currently rendered into the DOM. As the grid scrolls vertically and more rows are displayed, the height of those rows will be calculated on the fly.

This means the row heights and row positions are changing as the grid is scrolling vertically. This leads to the following behaviours:

- The vertical scroll range (how much you can scroll over) will change dynamically to fit the rows. If scrolling by dragging the scroll thumb with the mouse, the scroll thumb will not follow the mouse. It will either lag behind or jump ahead, depending on whether the row height calculations are increasing or decreasing the vertical scroll range.
- If scrolling up and showing rows for the first time (e.g. the user jumps to the bottom scroll position and then starts slowly scrolling up), then the row positions will jump as the rows coming into view at the top will get resized and the new height will impact the position of all rows beneath it. For example if the row gets resized to be 10 pixels taller, rows below it will get pushed down by 10 rows. If scrolling down this isn't observed as rows below are not in view.

The above are results of Lazy Height Calculation. It is not possible to avoid these effects.

### Auto Height and Column Virtualisation
Columns with Auto Height will always be rendered. The grid needs to have all Auto Height Columns rendered in order to correctly set the height of the row.

### Auto Height Performance Consideration
Because auto-height adds size listeners to cells and stops Column Virtualisation, consideration should be given for when and how to use it. Only apply auto-height to columns where it makes sense. For example, if you have many columns that do not require a variable height, then do not set them to auto-height.

### Height for Pinned Rows
Row height for pinned rows works exactly as for normal rows with one difference: it is not possible to dynamically change the height once set. However this is easily solved by just setting the pinned row data again which resets the row heights. Setting the data again is not a problem for pinned rows as it doesn't impact scroll position, filtering, sorting or group open / closed positions as it would with normal rows if the data was reset.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_height", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rows.row_height_auto", make_layout=make_tabs),
        make_md(text3),
        # up_next("text"),
    ],
)
