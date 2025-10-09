import flet as ft
from calet.calet_themes import Theme

class AnimationEmulator(ft.Row):

    def __init__(self, page:ft.Page, animation_handler):
        super().__init__()
        self.scale = 0
        self.animate_scale = 10
        self.on_animation_end = self.animation_emulated
        self.animation_handler = animation_handler
        try:
            self.left = -page.width
            page.overlay.append(self)
            page.update()
        except Exception as ex:
            pass

    def animate(self):
        self.scale = 0.1
        self.update()

    def animation_emulated(self, e:ft.ControlEvent):
        if self.scale == 0.1:
            self.scale = 0
            self.update()
            self.animation_handler()

class AnimationsEmulations(ft.Stack):

    def __init__(self, emulators:list[AnimationEmulator]=None):
        super().__init__()
        self.expand = True
        self.controls = [] if emulators is None else emulators
    
    def add_emulator(self, emulator:AnimationEmulator):
        self.controls.append(emulator)
        self.update()

class Quote(ft.Container):

    def __init__(self, cltheme:Theme, quote:str, quote_type:str="info", content_size:int=10):
        """quote_type: it's a string representing the type of quote must be displayed. Can be 'info', 'warning', 'error' or 'highlight'
        """
        super().__init__()
        self.cltheme = cltheme
        self.margin = 5
        self.padding = 5
        self.border_radius = 5
        self.bgcolor = {
            "info": cltheme.transparent_05,
            "warning": cltheme.warning_block,
            "error": cltheme.error_block,
            "highlight": cltheme.primary_block
        }[quote_type]
        self.alignment = ft.alignment.center_left
        self.expand=True

        # QUOTE TEXT
        self.quote_text = ft.Text(
            value=quote,
            color={
                "info": cltheme.font_one,
                "warning": cltheme.warning,
                "error": cltheme.error,
                "highlight": cltheme.primary
            }[quote_type],
            size=content_size
        )

        self.content = self.quote_text
