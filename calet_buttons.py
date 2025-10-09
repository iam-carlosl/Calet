import flet as ft
from calet.calet_themes import Theme
from calet.calet_utilities import AnimationEmulator
import time

# tooltip for calet buttons
class Tooltip(ft.Tooltip):
    """Represents a tooltip with calet appereance and behavior to be used in calet objects.
    """
    def __init__(self, cltheme:Theme, message:str, content_size:int=14):
        super().__init__()
        self.cltheme = cltheme
        self.message = message
        # self.bgcolor = ft.colors.with_opacity(0.3, cltheme.font_four)
        self.bgcolor = cltheme.transparent_inverse_8
        self.padding = 5
        self.border_radius = 5
        self.wait_duration = 500
        self.text_align = ft.TextAlign.LEFT
        self.text_style = ft.TextStyle(color=cltheme.font_three, size=content_size)
        self.margin = ft.margin.only(left=20)

# calet button
class CaletButton(ft.Container):
    """Represents a template for all calet buttons.
    """
    def __init__(self, cltheme:Theme, visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__()
        self.cltheme = cltheme
        self.action = action
        self.data = data
        self.visible = visible
        self.opacity = 1 if visible else 0
        self.scale = 1 if visible else 0
        self.tooltip = Tooltip(cltheme, tooltip) if tooltip is not None else None
        self.animate = ft.Animation(150, ft.AnimationCurve.LINEAR)
        self.animate_scale = ft.Animation(100, ft.AnimationCurve.LINEAR)
        self.animate_opacity = ft.Animation(200, ft.AnimationCurve.LINEAR)
        self.on_animation_end = self.button_animated

    # LIFE CICLE
    def did_mount(self):
        self.animation_emulator = AnimationEmulator(self.page, self.animation_emulator_animated)
    
    # HANDLERS
    def button_clicked(self, e:ft.ControlEvent):
        self.scale = 0.9
        self.update()
        if self.action is not None:
            self.action(e)

    def button_animated(self, e:ft.ControlEvent):
        if self.scale == 0.9:
            self.scale = 1
        elif self.opacity == 0:
            self.visible = False
        self.update()

    # OTHER METHODS
    def animation_emulator_animated(self):
        self.opacity = 1
        self.scale = 1
        self.update()
    
    def show(self):
        self.visible = True
        self.animation_emulator.animate()
        self.update()
    
    def hide(self):
        self.opacity = 0
        self.scale = 0
        self.update()

# icon button
class IconButton(CaletButton):
    """Represents an icon button with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str, content_size=16, button_size=None, content_padding:ft.Padding=None,
                 expand:bool|int|None=None, circular:bool=False, visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.expand = expand
        self.width = button_size
        self.height = button_size
        self.padding = 2 if content_padding is None else content_padding
        self.border_radius = 5
        self.shape = ft.BoxShape.CIRCLE if circular else None
        self.bgcolor = self.cltheme.transparent
        self.on_click = self.button_clicked
        self.on_hover = self.button_hovered

        # BUTTON CONTENT
        self.button_icon = ft.Icon(name=icon, color=cltheme.font_two, size=content_size)
        self.content = self.button_icon
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        self.button_icon.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
        self.bgcolor = self.cltheme.transparent_1 if e.data == "true" else self.cltheme.transparent
        self.update()

    # OTHER METHODS
    def upd(self, icon:str=None):
        if icon is not None:
            self.button_icon.name = icon
            self.update()

# window actions button
class WinButton(IconButton):
    """Represents a calet icon button with window actions appereance and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, content_size:int=16, button_size:int=None, content_padding:ft.Padding=None, 
                 expand:bool|int|None=None, circular:bool=False, visible:bool=True, action=None, winaction="close", 
                 data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon={
                "close": ft.icons.CLOSE,
                "minimize": ft.icons.MINIMIZE,
                "maximize": ft.icons.MAXIMIZE_ROUNDED,
                "unmaximize": ft.icons.MAXIMIZE_OUTLINED
            }[winaction],
            content_size=content_size,
            button_size=button_size,
            content_padding=content_padding,
            expand=expand,
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.winaction = winaction

    # HANDLERS
    def button_clicked(self, e:ft.ControlEvent):
        super().button_clicked(e)
        if self.action is None:
            match self.winaction:
                case "close": 
                    time.sleep(0.1)
                    self.page.window.destroy()
                case "minimize": 
                    self.page.window.minimized = True
                    self.page.update()
                case "maximize":
                    self.page.window.maximized = True
                    self.icon = ft.icons.MAXIMIZE_OUTLINED
                    self.winaction = "unmaximize"
                    self.update()
                    self.page.update()
                case "unmaximize":
                    self.page.window.maximized = False
                    self.icon = ft.icons.MAXIMIZE_ROUNDED
                    self.winaction = "maximize"
                    self.update()
                    self.page.update()
        else:
            self.action(e)

    def button_hovered(self, e:ft.ControlEvent):
        if self.winaction == "close":
            self.bgcolor = self.cltheme.cancel if e.data == "true" else self.cltheme.transparent
            self.update()
        else:
            super().button_hovered(e)

# mode button
class ModesButton(IconButton):
    """Represents a modes indicator icon button with calet appereance, animations and behavior to be used 
    in Flet apps.
    """
    def __init__(self, cltheme:Theme, icons:list[str|None], mode:int=0, content_size:int=16, button_size:int=None, 
                 content_padding:ft.Padding=None, is_selectable:bool=False, expand:bool|int|None=None, circular:bool=False, 
                 visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icons[mode],
            content_size=content_size,
            button_size=button_size,
            content_padding=content_padding,
            expand=expand,
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.is_selectable = is_selectable
        self.icons = icons
        self.mode = mode
        self.button_icon.animate_opacity = ft.Animation(50, ft.AnimationCurve.LINEAR)
        self.button_icon.on_animation_end = self.button_icon_animated
        if is_selectable and mode != 0:
            self.button_icon.color = cltheme.primary

    # HANDLERS
    def button_clicked(self, e: ft.ControlEvent):
        self.mode = 0 if self.mode == len(self.icons)-1 else self.mode + 1
        self.button_icon.opacity = 0
        self.update()
        super().button_clicked(e)

    def button_hovered(self, e: ft.ControlEvent):
        if not self.is_selectable or not self.mode != 0:
            super().button_hovered(e)

    def button_icon_animated(self, e:ft.ControlEvent):
        if self.button_icon.opacity == 0:
            self.button_icon.color = self.cltheme.primary if self.is_selectable and self.mode != 0 else self.cltheme.font_three
            self.button_icon.name = self.icons[self.mode]
            self.button_icon.opacity = 1
            self.update()

# text button
class TextButton(CaletButton):
    """Represents a text button with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True, 
                 width:int=None, height:int=None, content_padding:ft.Padding=None, expand:bool|int|None=None, circular:bool=False, 
                 is_primary:bool=False, visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.is_primary = is_primary
        self.width = width
        self.height = height
        self.padding = 5 if content_padding is None else content_padding
        self.border_radius = 5 if not circular else 50
        self.bgcolor = cltheme.transparent
        self.expand = expand
        self.on_click = self.button_clicked
        self.on_hover = self.button_hovered

        # BUTTON CONTENT
        self.button_content = ft.Row(
            spacing=5, 
            alignment="center" if centered_content else "start", 
            controls=[]
        )
        # - icon
        self.button_icon = ft.Icon(
            name=icon, 
            color=cltheme.font_two if not is_primary else cltheme.primary, 
            size=content_size,
            animate_rotation=ft.Animation(200, ft.AnimationCurve.LINEAR)
        ) if icon is not None else None
        if self.button_icon is not None:
            self.button_content.controls.append(self.button_icon)
        # - text
        self.button_text = ft.Text(
            value=text, 
            color=cltheme.font_two if not is_primary else cltheme.primary, 
            size=content_size, 
            font_family=text_font,
            weight=ft.FontWeight.BOLD if is_primary else None
        ) if text is not None else None
        if self.button_text is not None:
            self.button_content.controls.append(self.button_text)
        
        self.content = self.button_content
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        if not self.is_primary:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
        self.bgcolor = self.cltheme.transparent_1 if e.data == "true" else self.cltheme.transparent
        self.update()
    
    # SUPPORT METHODS
    def upd_button_style(self, is_primary:bool, on_hover:bool):
        self.is_primary = is_primary
        if is_primary:
            if self.button_text is not None:
                self.button_text.color = self.cltheme.primary
        else:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_three if on_hover else self.cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_three if on_hover else self.cltheme.font_two
        self.cltheme.transparent_1 if on_hover else self.cltheme.transparent
        self.update()

# filled button
class FilledButton(TextButton):
    """Represents a filled text button with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True,
                 width:int=None, height:int=None, content_padding:ft.Padding=None, expand:bool|int|None=None, circular:bool=False, 
                 is_primary:bool=False, visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            text_font=text_font,
            content_size=content_size,
            centered_content=centered_content,
            width=width,
            height=height,
            content_padding=content_padding,
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip,
            expand=expand,
            is_primary=is_primary
        )
        self.bgcolor = cltheme.transparent_1 if not is_primary else cltheme.primary

        # BUTTON CONTENT
        if is_primary:
            if self.button_icon is not None:
                self.button_icon.color = cltheme.font_four
            if self.button_text is not None:
                self.button_text.color = cltheme.font_four
        if self.button_icon is not None:
            self.button_icon.size += 2
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        if not self.is_primary:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
            self.bgcolor = self.cltheme.transparent_2 if e.data == "true" else self.cltheme.transparent_1
        else:
            self.bgcolor = self.cltheme.primary_hovered if e.data == "true" else self.cltheme.primary
        self.update()
    
    # SUPPORT METHODS
    def upd_button_style(self, is_primary:bool, on_hover:bool):
        self.is_primary = is_primary
        if is_primary:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_four
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_four
            self.bgcolor = self.cltheme.primary_hovered if on_hover else self.cltheme.primary
        else:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_three if on_hover else self.cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_three if on_hover else self.cltheme.font_two
            self.bgcolor = self.cltheme.transparent_2 if on_hover else self.cltheme.transparent_1
        self.update()

# selectable button
class SelectableButton(TextButton):
    """Represents a selectable button with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True,
                 width:int=None, height:int=None, circular:bool=False, visible:bool=True, selected:bool=False, 
                 action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            text_font=text_font,
            content_size=content_size,
            centered_content=centered_content,
            width=width,
            height=height,
            content_padding=ft.padding.only(left=10, top=2, right=10, bottom=2),
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.selected = selected

        if selected:
            self.bgcolor = cltheme.primary
            if self.button_icon is not None:
                self.button_icon.color = cltheme.font_four
            if self.button_text is not None:
                self.button_text.color = cltheme.font_four
        else:
            self.bgcolor = cltheme.transparent
            if self.button_icon is not None:
                self.button_icon.color = cltheme.font_one
            if self.button_text is not None:
                self.button_text.color = cltheme.font_one
        if self.button_icon is not None:
            self.button_icon.size += 2
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        if not self.selected:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_two if e.data == "true" else self.cltheme.font_one
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_two if e.data == "true" else self.cltheme.font_one
        self.update()

    # OTHER METHODS
    def upd_selection_state(self, selected:bool):
        self.selected = selected
        if selected:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_four
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_four
            self.bgcolor = self.cltheme.primary
        else:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_one
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_one
            self.bgcolor = self.cltheme.transparent
        self.update()

# tag button
class TagButton(TextButton):
    """Represents a calet text button to be used in Flet apps as an interactive tag.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True,
                 width:int=None, height:int=None, circular:bool=False, visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            text_font=text_font,
            content_size=content_size,
            centered_content=centered_content,
            width=width,
            height=height,
            content_padding=ft.padding.only(left=5, right=5, top=2, bottom=2),
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        ) 
        self.bgcolor = cltheme.transparent_2
        if self.button_icon is not None:
            self.button_icon.color = cltheme.font_three
        if self.button_text is not None:
            self.button_text.color = cltheme.font_three

    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        self.bgcolor = self.cltheme.transparent_3 if e.data == "true" else self.cltheme.transparent_2
        self.update()

# tab button
class TabButton(TextButton):
    """Represents a calet text button with filter tab appereance and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True,
                 width:int=None, height:int=None, circular:bool=False, visible:bool=True, state:str="normal", 
                 action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            text_font=text_font,
            content_size=content_size,
            centered_content=centered_content,
            width=width,
            height=height,
            content_padding=ft.padding.only(left=5, top=5, right=10, bottom=5),
            circular=circular,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.margin = 1
        self.state = state # can be 'normal', 'selected' or 'highlight'
        match state:
            case "selected":
                self.bgcolor = cltheme.primary
                if self.button_icon is not None:
                    self.button_icon.color = cltheme.font_three
                if self.button_text is not None:
                    self.button_text.color = self.cltheme.font_three
            case "hightlight":
                self.bgcolor = ft.colors.with_opacity(0.4, cltheme.primary)
                if self.button_icon is not None:
                    self.button_icon.color = cltheme.font_three
                if self.button_text is not None:
                    self.button_text.color = self.cltheme.font_three
            case "normal":
                self.bgcolor = cltheme.transparent_2
        if self.button_icon is not None:
            self.button_icon.size += 2
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=1,
            color={"selected":self.cltheme.primary, "highlight":self.cltheme.primary, "normal":self.cltheme.font_three}[self.state],
            blur_style=ft.ShadowBlurStyle.OUTER
        ) if e.data == "true" else None
        if self.state == "highlight":
            self.bgcolor = ft.colors.with_opacity(0.5, self.cltheme.primary) if e.data == "true" else ft.colors.with_opacity(0.4, self.cltheme.primary)
        if self.state == "normal":
            self.bgcolor = self.cltheme.transparent_3 if e.data == "true" else self.cltheme.transparent_2
        self.update()

    # OTHER METHODS
    def upd_state(self, new_state:str, changed_by_click:bool=False):
        self.state = new_state
        match new_state:
            case "selected":
                if self.button_icon is not None:
                    self.button_icon.color = self.cltheme.font_three
                if self.button_text is not None:
                    self.button_text.color = self.cltheme.font_three
                self.bgcolor = self.cltheme.primary
                if changed_by_click:
                    self.shadow.color = self.cltheme.primary
            case "highlight":
                if self.button_icon is not None:
                    self.button_icon.color = self.cltheme.font_three
                if self.button_text is not None:
                    self.button_text.color = self.cltheme.font_three
                self.bgcolor = ft.colors.with_opacity(0.4, self.cltheme.primary)
                if changed_by_click:
                    self.shadow.color = self.cltheme.primary
            case "normal":
                if self.button_icon is not None:
                    self.button_icon.color = self.cltheme.font_two
                if self.button_text is not None:
                    self.button_text.color = self.cltheme.font_two
                self.bgcolor = self.cltheme.transparent_2
                if changed_by_click:
                    self.shadow.color = self.cltheme.font_three
        self.update()

# nav button
class NavButton(TextButton):
    """Represents a navigation button with calet appereance, animations and behavior to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, text_font:str=None, content_size:int=14, centered_content:bool=True,
                 width:int=None, height:int=None, circular:bool=False, visible:bool=True, expand:bool=False, selected:str=False, 
                 action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            text_font=text_font,
            content_size=content_size,
            centered_content=centered_content,
            width=width,
            height=height,
            content_padding=ft.padding.only(left=0, top=5, right=10, bottom=5),
            circular=circular,
            expand=expand,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.margin = 1
        self.selected = selected
        if selected:
            self.bgcolor = cltheme.transparent_1
            if self.button_icon is not None:
                self.button_icon.color = cltheme.font_three
            if self.button_text is not None:
                self.button_text.color = cltheme.font_three
        else:
            self.bgcolor = cltheme.transparent
            if self.button_icon is not None:
                self.button_icon.color = cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = cltheme.font_two
        if self.button_icon is not None:
            self.button_icon.size += 2
        
        # BUTTON CONTENT
        # - selection mark
        self.button_selection_mark = ft.Container(
            width=5,
            height=content_size,
            bgcolor=self.cltheme.primary,
            border_radius=50,
            margin=ft.margin.only(right=5),
            opacity=1 if selected else 0,
            scale=1 if selected else 0,
            animate_opacity=200,
            animate_scale=200
        )
        self.button_content.controls.insert(0, self.button_selection_mark)
        self.button_content.alignment = "start"

    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        if not self.selected:
            super().button_hovered(e)

    # OTHER METHODS
    def upd_selection_state(self, selected:bool):
        self.selected = selected
        if selected:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_three
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_three
            self.bgcolor = self.cltheme.transparent_1
            self.button_selection_mark.opacity = 1
            self.button_selection_mark.scale = 1
        else:
            if self.button_icon is not None:
                self.button_icon.color = self.cltheme.font_two
            if self.button_text is not None:
                self.button_text.color = self.cltheme.font_two
            self.bgcolor = self.cltheme.transparent
            self.button_selection_mark.opacity = 0
            self.button_selection_mark.scale = 0
        self.update()

# swap nav button
class SwapNavButton(CaletButton):
    """Represents a navigation button with calet appereance, animations and behavior to be used in ```calet_bars.SwapNavBar```.
    """
    def __init__(self, cltheme:Theme, text:str, content_size:int=12, width:int=None, height:int=None, 
                 content_padding:ft.Padding=None, expand:bool|int|None=None, visible:bool=True, selected:bool=False, 
                 action=None, data=None, tooltip:str=None):
        super().__init__(
            cltheme=cltheme,
            visible=visible,
            action=action,
            data=data,
            tooltip=tooltip
        )
        self.width = width
        self.height = height
        self.padding = ft.padding.only(left=10, right=10) if content_padding is None else content_padding
        self.border_radius = 5
        self.bgcolor = cltheme.transparent
        self.expand = expand
        self.selected = selected
        self.opacity = 0 if selected else 1
        self.on_click = self.button_clicked
        self.on_hover = self.button_hovered

        # BUTTON CONTENT
        # - text
        self.button_text = ft.Text(value=text, color=cltheme.font_one, size=content_size)
        
        self.content = ft.Row(spacing=5, alignment="center", controls=[self.button_text])
    
    # HANDLERS
    def button_hovered(self, e:ft.ControlEvent):
        self.button_text.color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_one
        self.update()

    # ASSIST METHODS
    def upd_selection_state(self, selected:bool):
        self.opacity = 0 if selected else 1
        self.update()

# custom Flet floating action button
class CustomFloatingButton(ft.FloatingActionButton):
    """Represents a Flet floating action button styled with calet appereance, animations and behavior to be used in Flet 
    apps directly or combined with a ```calet_overlays.ClFloatingActionsField```.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, circular:bool=False, is_primary:bool=True, 
                 visible:bool=True, action=None, data=None, tooltip:str=None):
        super().__init__()
        self.cltheme = cltheme
        self.action = action
        self.visible = visible
        self.scale = 1 if visible else 0
        self.opacity = 1 if visible else 0
        self.bgcolor = cltheme.primary if is_primary else cltheme.background_two
        self.foreground_color = cltheme.font_two
        self.shape = ft.BoxShape.CIRCLE if circular else None
        self.mini = not is_primary
        self.icon = icon
        self.text = text
        self.tooltip = Tooltip(cltheme, tooltip) if tooltip is not None else None
        self.animate_scale = ft.Animation(100, ft.AnimationCurve.LINEAR)
        self.animate_opacity = ft.Animation(200, ft.AnimationCurve.LINEAR)
        self.on_click = self.button_clicked
        self.on_animation_end = self.button_animated

        ft.FloatingActionButton()

    # LIFE CICLE
    def did_mount(self):
        self.animation_emulator = AnimationEmulator(self.page, self.animation_emulator_animated)
    
    # HANDLERS
    def button_clicked(self, e:ft.ControlEvent):
        self.scale = 0.9
        self.update()
        if self.action is not None:
            self.action(e)

    def button_animated(self, e:ft.ControlEvent):
        if self.scale == 0.9:
            self.scale = 1
        elif self.opacity == 0:
            self.visible = False
        self.update()

    # OTHER METHODS
    def show(self):
        self.visible = True
        self.animation_emulator.animate()
        self.update()
    
    def hide(self):
        self.opacity = 0
        self.scale = 0
        self.update()

    def animation_emulator_animated(self):
        self.opacity = 1
        self.scale = 1
        self.update()

# custom Flet popup menu item button
class PopupItemButton(ft.PopupMenuItem):
    """Represents a Flet popup menu item styled with calet appereance, animations and behavior to be used in Flet 
    apps combined with a ```calet_buttons.PopupMenuButton```.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, content_size:int=18, height:int=None, 
                 content_padding:ft.Padding=None, action=None, data=None):
        super().__init__()
        self.cltheme = cltheme
        self.content_size = content_size
        self.action = action
        self.data = data
        self.padding = 2 if content_padding is None else content_padding
        self.height = height

        # ITEM CONTENT
        if icon is not None or text is not None:
            self.on_click = self.button_clicked
            self.content = ft.Row(spacing=5, alignment="start", controls=[])
            # - button icon
            self.button_icon = ft.Icon(
                name=icon,
                color=cltheme.font_two,
                size=content_size,
                animate_scale=ft.Animation(100, ft.AnimationCurve.LINEAR),
                on_animation_end=self.button_animated
            ) if icon is not None else None
            if self.button_icon is not None:
                self.content.controls.append(self.button_icon)
            # - button text
            self.button_text = ft.Text(
                value=text,
                color=cltheme.font_two,
                size=content_size-4,
                text_align=ft.TextAlign.LEFT,
                animate_scale=ft.Animation(100, ft.AnimationCurve.LINEAR),
                on_animation_end=self.button_animated
            )
            if self.button_text is not None:
                self.content.controls.append(self.button_text)

    # HANDLERS
    def button_clicked(self, e:ft.ControlEvent):
        if self.button_icon is not None:
            self.button_icon.scale = 0.9
        if self.button_text is not None:
            self.button_text.scale = 0.9
        if self.action is not None:
            self.action(e)
        self.update()

    def button_animated(self, e:ft.ControlEvent):
        if self.button_icon is not None:
            if self.button_icon.scale == 0.9:
                self.button_icon.scale = 1
        if self.button_text is not None:
            if self.button_text.scale == 0.9:
                self.button_text.scale = 1
        self.update()

# selectable custom Flet popup menu button
class PopupItemSelectableButton(PopupItemButton):
    """Represents a selectable Flet popup menu item styled with calet appereance, animations and behavior to be used in Flet 
    apps combined with a ```calet_buttons.PopupMenuButton```.
    """
    def __init__(self, cltheme:Theme, icon:str=None, text:str=None, content_size:int=18, height:int=None, 
                 content_padding:ft.Padding=None, selected:bool=False, action=None, data=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            text=text,
            content_size=content_size,
            height=height,
            content_padding=content_padding,
            action=action,
            data=data
        )
        self.selected = selected

        # ITEM CONTENT
        if icon is not None or text is not None:
            if selected:
                # button icon
                if self.button_icon is not None:
                    self.button_icon.color = cltheme.font_three
                # button text
                if self.button_text is not None:
                    self.button_text.color = cltheme.font_three
            # button check icon
            self.button_check_icon = ft.Icon(
                name=ft.icons.CHECK_ROUNDED,
                color=self.cltheme.font_three,
                size=self.content_size,
                opacity=1 if selected else 0,
                scale=1 if selected else 0,
                animate_scale=ft.Animation(100, ft.AnimationCurve.LINEAR),
                animate_opacity=ft.Animation(100, ft.AnimationCurve.LINEAR)
            )
            self.content.controls.insert(0, self.button_check_icon)

    # OTHER METHODS
    def upd_state(self, selected:bool):
        self.selected = selected
        if self.button_icon is not None:
            self.button_icon.color = self.cltheme.font_three if selected else self.cltheme.font_two
        if self.button_text is not None:
            self.button_text.color = self.cltheme.font_three if selected else self.cltheme.font_two
        self.button_check_icon.opacity = 1 if selected else 0
        self.button_check_icon.scale = 1 if selected else 0
        self.update()

# custom Flet popup menu button
class PopupMenuButton(ft.PopupMenuButton):
    """Represents a Flet popup menu button styled with calet appereance, animations and behavior to be used in Flet 
    apps.
    """
    def __init__(self, cltheme:Theme, icon:str, items:list[PopupItemButton], content_size:int=16, button_size=None, 
                 content_padding:ft.Padding=None, menu_under_button:bool=False, expand:bool|int|None=None, visible:bool=True, 
                 data=None, tooltip:str=None):
        super().__init__()
        self.cltheme = cltheme
        self.data = data
        self.expand = expand
        self.width = button_size
        self.height = button_size
        self.visible = visible
        self.opacity = 1 if visible else 0
        self.scale = 1 if visible else 0
        self.padding = 2 if content_padding is None else content_padding
        self.bgcolor = cltheme.background_two
        self.shadow_color = "black"
        self.surface_tint_color = cltheme.transparent
        self.menu_position = ft.PopupMenuPosition.UNDER if menu_under_button else ft.PopupMenuPosition.OVER
        self.tooltip = Tooltip(cltheme, tooltip) if tooltip is not None else None
        self.animate_scale = ft.Animation(100, ft.AnimationCurve.LINEAR)
        self.animate_opacity = ft.Animation(200, ft.AnimationCurve.LINEAR)
        self.on_open = self.button_clicked
        self.on_animation_end = self.button_animated
        self.icon = icon
        self.icon_color = cltheme.font_two
        self.icon_size = content_size
        self.items = items

    # LIFE CICLE
    def did_mount(self):
        self.animation_emulator = AnimationEmulator(self.page, self.animation_emulator_animated)
    
    # HANDLERS
    def button_clicked(self, e:ft.ControlEvent):
        self.scale = 0.9
        self.update()

    def button_animated(self, e:ft.ControlEvent):
        if self.scale == 0.9:
            self.scale = 1
        elif self.opacity == 0:
            self.visible = False
        self.update()
    
    def button_hovered(self, e:ft.ControlEvent):
        self.icon_color = self.cltheme.font_three if e.data == "true" else self.cltheme.font_two
        self.update()

    # OTHER METHODS
    def show(self):
        self.visible = True
        self.animation_emulator.animate()
        self.update()
    
    def hide(self):
        self.opacity = 0
        self.scale = 0
        self.update()

    def animation_emulator_animated(self):
        self.opacity = 1
        self.scale = 1
        self.update()

    def upd(self, icon:str=None, tooltip:str=None):
        if icon is not None:
            self.icon = icon
        if tooltip is not None:
            self.tooltip = Tooltip(self.cltheme, tooltip)
        self.update()

class SwitchButton(ft.Switch):
    """Represents a switch button to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, inactive_label:str=None, active_label:str=None, inactive_tooltip:str=None, active_tooltip:str=None,
                 inactive_icon:str=None, active_icon:str=None, inversed_colors:bool=False,
                 expand:bool=None, active:bool=False, data=None, change_action=None):
        
        # INITIALIZATION BLOCK
        super().__init__()
        self.cltheme = cltheme
        self.inversed_colors = inversed_colors
        self.expand = expand
        self.inactive_label = inactive_label
        self.active_label = active_label
        self.inactive_tooltip = inactive_tooltip
        self.active_tooltip = active_tooltip
        self.value = active
        self.height = 30
        self.data = data
        self.change_action = change_action
        self.on_change = self.b_changed

        # SWITCH CONTENT
        # - label
        self.label = active_label if active else inactive_label
        # - tooltip
        self.active_tooltip = Tooltip(cltheme=self.cltheme, message=self.active_tooltip) if active_tooltip else None
        self.inactive_tooltip = Tooltip(cltheme=self.cltheme, message=self.inactive_tooltip) if inactive_tooltip else None
        self.tooltip = self.active_tooltip if active else self.inactive_tooltip
        # thumb and track
        self.thumb_icon = {
            ft.ControlState.DEFAULT: inactive_icon,
            ft.ControlState.SELECTED: active_icon
        }
        self.thumb_color = {
            ft.ControlState.DEFAULT: self.cltheme.secondary,
            ft.ControlState.SELECTED: self.cltheme.primary_block if not self.inversed_colors else self.cltheme.primary,
        }
        self.track_color = {
            ft.ControlState.DEFAULT: self.cltheme.secondary_block,
            ft.ControlState.SELECTED: self.cltheme.primary if not self.inversed_colors else self.cltheme.font_three
        }
        self.focus_color = self.cltheme.primary_block
        
    def b_changed(self, e:ft.ControlEvent):
        self.label = self.active_label if self.value else self.inactive_label
        self.tooltip = self.active_tooltip if self.value else self.inactive_tooltip
        self.update()
        if self.change_action is not None:
            self.change_action(e)
