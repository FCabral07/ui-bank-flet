from flet import GridView

def grid_payments():
    return GridView(
        expand= True,
        max_extent= 150,
        runs_count= 0,
        spacing= 10,
        run_spacing= 5,
    )
