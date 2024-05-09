import flet as ft

from src.components.icons_expense import icon
from src.components.grid_transfers import grid_transfers
from src.components.grid_payments import grid_payments

class Expense(ft.UserControl):
    # Animation
    def hover_animation(self, e):
        if e.data == 'true':
            e.control.content.controls[2].offset = ft.transform.Offset(0, 0)
            e.control.content.controls[2].opacity = 100
            e.control.update()
        else:
            e.control.content.controls[2].offset = ft.transform.Offset(0, 1)
            e.control.content.controls[2].opacity = 0
            e.control.update()
    
    def main_container(self):
        self.main = ft.Container(width=290, height=600, bgcolor= 'black', border_radius= 35, padding= 8,)
        
        # Main column
        self.main_col = ft.Column()
        
        # Green top container
        self.green_container = ft.Container(
            width= self.main.width,
            height= self.main.height * 0.40,
            border_radius= 27,
            gradient= ft.LinearGradient(
                begin= ft.alignment.top_left,
                end= ft.alignment.bottom_right,
                colors= ['#0f766e', '#064e3b']
            )
        )
        
        # 
        self.invests = icon(ft.icons.AUTO_GRAPH_ROUNDED, 'white54', True)
        self.hide = icon(ft.icons.HIDE_SOURCE, 'white54', False)
        self.payments_screen = icon(ft.icons.ATTACH_MONEY, 'white54', False)
        
        # icons column
        self.icon_column = ft.Column(
            alignment= 'center',
            spacing= 3,
            controls= [
                self.invests, self.hide, self.payments_screen
            ],
        )
        
        # Inner Green Container
        self.inner_green_container = ft.Container(
            width= self.green_container.width,
            height= self.green_container.height,
            content= ft.Row(
                spacing= 0,
                controls=[
                    ft.Column(
                        expand= 4,
                        controls= [
                            ft.Container(
                                padding= 20,
                                expand= True,
                                content= ft.Row(
                                    controls= [
                                        ft.Column(
                                            controls= [
                                                ft.Text('Bem-vindo de volta, ', size= 11, color='white70'),
                                                ft.Text('Felipe.', size= 18, weight= 'bold'),
                                                ft.Container(
                                                    padding= ft.padding.only(top= 3, bottom= 10),
                                                    content= ft.Icon(size= 50, name=ft.icons.SUPERVISED_USER_CIRCLE)
                                                ),
                                                ft.Text('Saldo Total, ', size= 10, color='white70'),
                                                ft.Text('R$ 328,74', size= 22, weight= 'bold')
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                    ft.Column(
                        expand= 1,
                        controls= [
                            ft.Container(
                                padding= ft.padding.only(right= 10), 
                                expand= True,
                                content= ft.Row(
                                    alignment= 'center',
                                    controls= [
                                        ft.Column(
                                            alignment= 'center',
                                            horizontal_alignment= 'center',
                                            controls= [
                                                ft.Column(
                                                    alignment= 'center',
                                                    horizontal_alignment= 'center',
                                                    controls= [
                                                        ft.Container(
                                                            width= 40, height= 150, bgcolor='white10', border_radius= 14,
                                                            content= self.icon_column
                                                        )
                                                    ],
                                                )
                                            ],
                                        )
                                    ]
                                )   
                            )
                        ]
                    )
                ]
            )
        )
        
        self.grid_transfers = grid_transfers()
        self.grid_payments = grid_payments()
        
        self.main_content_area = ft.Container(
            width= self.main.width,
            height= self.main.height * 0.50,
            
            padding= ft.padding.only(top= 10, left= 10, right= 10),
            content= ft.Column(
                spacing= 20,
                controls=[
                    ft.Row(
                        alignment= 'spaceBetween',
                        vertical_alignment= 'center',
                        controls=[
                            ft.Container(
                                content= ft.Text('Pix Realizados', size= 14, weight= 'bold')
                            ),
                            ft.Container(
                                content= ft.TextButton(content= ft.Text('Ver Tudo', size= 9, weight= 'w400', color='white54')),
                            )
                        ]
                    ),
                    ft.Container(
                        height= 50, content= self.grid_transfers
                    ),
                    ft.Row(
                        alignment= 'spaceBetween',
                        vertical_alignment= 'center',
                        controls=[
                            ft.Container(
                                content= ft.Text('Pagamentos Pendentes', size= 14, weight= 'bold')
                            ),
                            ft.Container(
                                content= ft.TextButton(content= ft.Text('Ver Tudo', size= 9, weight= 'w400', color='white54')),
                            )
                        ]
                    ),
                    ft.Container(
                        height= 125, content= self.grid_payments,
                    )
                ]
            )
        )
        
        info_list = ['MV', 'LC', 'GL', 'JL', 'PH', 'MF', 'VJ', 'AS']
        for i in info_list:
            __ = ft.Container(
                width= 100, height= 100, bgcolor= 'white10', border_radius= 15, alignment=  ft.alignment.center,
                content= ft.Text(f'{i}', weight='bold')
            )
            self.grid_transfers.controls.append(__)
            
        payment_list = [
            ['Fornecedores', 'R$ 239,80'],
            ['Energia e Internet', 'R$ 148,20'],
            ['Água', 'R$ 129,90'],
            ['Encargos', 'R$ 7890,27'],
            ['Higiene', 'R$ 990,12']
        ]
        
        for i in payment_list:
            __ = ft.Container(
                width= 100, height= 100, bgcolor= 'white10', border_radius= 15, alignment= ft.alignment.center,
                content= ft.Text(f'{i}', weight='bold'), on_hover= lambda e: self.hover_animation(e)
            )
            self.grid_payments.controls.append(__)
            
            for x in i:
                __.content = ft.Column(
                    alignment= 'center',
                    horizontal_alignment= 'center',
                    controls= [
                        ft.Text(f'{i[0]}', size= 11, color='white54'),
                        ft.Text(f'{i[1]}', size= 16, weight= 'bold'),
                        ft.Text('Clique para pagar', size= 9, color='white10', text_align= 'start', weight='w400',
                                offset=ft.transform.Offset(0, 1), animate_offset=ft.animation.Animation(duration=900,
                                                                                                        curve='decelerate'),
                                animate_opacity=300, opacity=0)
                    ]
                )
        
        self.green_container.content = self.inner_green_container
        
        self.main_col.controls.append(self.green_container)
        self.main_col.controls.append(self.main_content_area)
        
        self.main.content = self.main_col
        
        return self.main
    
    def build(self):
        return ft.Column(
            controls=[
                self.main_container()
            ]
        )