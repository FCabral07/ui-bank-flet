from flet import IconButton

def icon(name, color, selected):
    return IconButton(
        icon = name,
        icon_size= 18,
        icon_color= color,
        selected= selected,
        on_click= None
)