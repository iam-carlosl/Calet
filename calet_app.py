from time import sleep
import flet as ft
from calet.calet_themes import Theme
from calet.calet_buttons import CustomFloatingButton
from calet.calet_bars import MenuBar
from calet.calet_utilities import AnimationEmulator

class FloatingActionsField(ft.Column):

    def __init__(self, main_action:CustomFloatingButton, secondary_actions:list[CustomFloatingButton]=None):
        super().__init__()
        self.main_action = main_action
        self.secondary_actions = secondary_actions
        self.expand = True

        self.col_actions = ft.Column(
            width=54,
            alignment="end", 
            controls=[ft.Row(alignment="center", controls=[action_button]) for action_button in secondary_actions] + [
                ft.Row(alignment="center", controls=[main_action])
            ]
        )
        self.controls = [
            ft.Row(expand=True, alignment="end", controls=[
                self.col_actions,
                ft.Column(width=5)
            ]), 
            ft.Row(height=5)
        ]

    def set_main_action(self, action_button:CustomFloatingButton):
        self.main_action = action_button
        self.col_actions.controls[-1].controls[0] = action_button
        self.update()

    def add_secondary_action(self, action_button:CustomFloatingButton):
        self.col_actions.controls.insert(0, ft.Row(alignment="center", controls=[action_button]))
        self.update()

class DialogsField(ft.Container):
    
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.bgcolor = ft.colors.with_opacity(0.05, 'black')
        self.blur = 5
        self.alignment = ft.alignment.center
        self.padding = 20
        self.animate = ft.Animation(150, ft.AnimationCurve.LINEAR)
        self.animate_opacity = ft.Animation(200, ft.AnimationCurve.LINEAR)
        self.on_animation_end = self.field_animated
        self.dlg_row = ft.Row(controls=[])

        self.content = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Column(expand=4),
                ft.Column(
                    expand=4,
                    spacing=0,
                    controls=[
                        ft.Row(expand=True),
                        self.dlg_row,
                        ft.Row(expand=True),
                    ]
                ),
                ft.Column(expand=4)
            ]
        )
    
    # LIFE CICLE
    def did_mount(self):
        self.animation_emulator = AnimationEmulator(self.page, self.animation_emulator_animated)
    
    # HANDLERS
    def field_animated(self, e:ft.ControlEvent):
        if self.opacity == 0:
            self.visible = False
        self.update()

    # OTHER METHODS
    def animation_emulator_animated(self):
        self.opacity = 1
        self.update()

    def show(self):
        self.visible = True
        self.animation_emulator.animate()
        self.update()
    
    def hide(self):
        self.opacity = 0
        self.update()

    def upd_dlg(self, dlg):
        self.dlg_row.controls = [dlg]
        self.update()

class CaletApp(ft.Container):
    """Represents an app template with generic calet layout and behaviors to be used as a base 
    for Flet apps.
    """
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.appbar = None
        self.app_content = None
        self.navigation_bar = None
        self.floating_actions_field = None
        self.dialogs_field = DialogsField()

        self.content = ft.Stack(
            controls=[
                # app content
                # floating actions field
                # dialogs field
                self.dialogs_field
                # notifications field
            ]
        )

    def did_mount(self):
        if self.floating_actions_field is not None:
            self.content.controls.insert(0, self.floating_actions_field)
            self.update()
        if self.app_content is not None:
            self.content.controls.insert(0, self.app_content)
            self.update()
        if self.dialogs_field is not None:
            self.content.controls.append(self.dialogs_field)
            self.update()
        if self.appbar is not None:
            self.page.appbar = self.appbar
            self.page.update()
        if self.navigation_bar is not None:
            self.page.navigation_bar = self.navigation_bar
            self.page.update()
    
    def notify(self):
        pass

    def open_dlg(self, dlg):
        self.dialogs_field.upd_dlg(dlg)
        self.dialogs_field.show()
        self.update()

    def close_dlg(self):
        self.dialogs_field.hide()
        self.update()

class AppLoadScreen(ft.Container):
    """Represents a load screen with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, page:ft.Page, cltheme:Theme, loading_app, load_icon:str=None, load_text:str=None, load_image:str=None):
        """Use this properties to customize the load screen:
        - ```page```: the page where the app will be loaded.
        - ```cltheme```: an instance of ```calet.calte_themes.Theme``` with the colors set to be used for painting the load screen controls.
        - ```loading_app```: the Flet control that represents the app to be loaded.
        - ```load_icon```: an icon to display in the middle of the loading screen.
        - ```load_text```: a text to display in the middle of the loading screen. If ```load_icon``` is also given, the text
                            will be displayed below him.
        - ```load_image```: an image to display in the middle of the load screen. If it is given, both ```load_icon``` and
                            ```load_text``` will be ignored.
        """
        super().__init__()
        self.cltheme = cltheme
        self.loading_app = loading_app
        self.expand = True
        self.page = page
        
        # LOAD SCREEN CONTENT
        # - image
        image = ft.Image(src=load_image, fit=ft.ImageFit.CONTAIN) if load_image is not None else None
        # - icon
        icon = load_icon if load_image is None else None
        if icon is not None:
            icon = ft.Icon(name=load_icon, color=cltheme.font_three, size=40)
        # - text
        text = load_text if load_image is None else None
        if text is not None:
            text = ft.Text(value=load_text, color=cltheme.font_three, size=24, text_align=ft.TextAlign.CENTER)

        # LOAD SCREEN LAYOUT
        # - start screen
        self.start_screen = ft.Container(
            expand=True, 
            bgcolor=cltheme.background_one,
            content=ft.canvas.Canvas(on_resize=self.cv_load_screen_resized)
        )
        # - presentation screen
        self.load_screen = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            opacity=0,
            animate_opacity=ft.Animation(500, ft.AnimationCurve.LINEAR),
            on_animation_end=self.load_screen_animated,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Row(expand=4),
                    ft.Row(expand=6, spacing=0, controls=[
                        ft.Container(expand=2), 
                        ft.Container(expand=8, content=image if image is not None else ft.Column(
                            spacing=10, alignment="center", controls=[icon, text]
                        )),
                        ft.Container(expand=2)
                    ]),
                    ft.Row(expand=4)
                ]
            )
        )

        self.content = ft.Stack(controls=[self.start_screen, self.load_screen])
    
    def cv_load_screen_resized(self, e:ft.canvas.CanvasResizeEvent):
        sleep(1)
        self.load_screen.opacity = 1
        self.update()
    
    def load_screen_animated(self, e:ft.ControlEvent):
        sleep(2)
        self.page.controls.remove(self)
        self.page.add(self.loading_app)
