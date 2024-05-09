import flet as ft

from src.components.expense import Expense

def start(page: ft.Page):
    page.title = 'Bank Felipe'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    app = Expense()
    page.add(app)
    page.update()
    
if __name__ == '__main__':
    ft.app(target=start)
    