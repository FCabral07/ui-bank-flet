from flet import GridView

def grid_transfers():
    return GridView(
        expand= True,
        max_extent= 150,
        runs_count= 0,
        spacing= 10,
        run_spacing= 5,
        horizontal= True
    )
