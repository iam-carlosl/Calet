import flet as ft
from calet.calet_themes import Theme, DarkTheme
from calet.calet_buttons import NavButton, TextButton, IconButton, WinButton, FilledButton, SwapNavButton, SelectableButton
from calet.calet_utilities import AnimationEmulator

# MENU BARS
# - app bar
class AppBar(ft.AppBar):
    """Represents an app title bar.
    """
    def __init__(self, cltheme:Theme, app_title:str, app_icon:str=None, app_img:str=None, bar_height:int=40,
                 title_font:str=None, center_title:bool=True, close_action=None):
        super().__init__()
        self.cltheme = cltheme
        self.bgcolor = self.cltheme.background_one
        self.toolbar_height = bar_height
        self.center_title = center_title
        self.title_spacing = 0
        self.leading_width = 40

        # APP TITLE CONTENT
        # - app icon
        self.app_title_icon = ft.Container(
            padding=6,
            width=40,
            height=40,
            margin=ft.margin.only(left=5, right=5),
            alignment=ft.alignment.center,
            content=ft.Image(
                fit=ft.ImageFit.FILL,
                src=app_img
            ) if app_icon is None else ft.Icon(
                name=app_icon,
                color=cltheme.font_three,
                size=16
            )
        )
        # - app title text
        self.app_title_text = ft.Text(
            value=app_title, 
            color=cltheme.font_three, 
            size=14, 
            font_family=title_font
        )

        # APP BAR CONFIGURATION
        self.title = ft.WindowDragArea(
            maximizable=True, 
            content=ft.Row(spacing=0, alignment="center" if center_title else "start", 
                controls=[self.app_title_icon, self.app_title_text]
            ) if app_icon is not None or app_img is not None else self.app_title_text
        )

        self.actions = [ft.Container(
            padding=ft.padding.only(right=10),
            content=ft.Row(spacing=0, controls=[
                WinButton(cltheme=self.cltheme, winaction="minimize", content_padding=5),
                WinButton(cltheme=self.cltheme, content_padding=5, action=close_action)
            ])
        )]

# - menu bar section
class MenuBarSection(ft.Container):
    """Represents a section of an app menu bar to be used in ```calet_bars.MenuBar``` objects."""
    def __init__(self, cltheme:Theme, items_cols:list[list], expand:bool|int=False):
        super().__init__()
        self.cltheme = cltheme
        self.expand = expand
        self.bgcolor = cltheme.transparent
        self.alignment = ft.alignment.center

        # SECTION
        # - the section
        self.section = ft.Row(spacing=5,controls=[])
        # - the section content
        for items_col in items_cols:
            for item in items_col:
                item.expand = 1
            self.section.controls.append(ft.Column(spacing=5, controls=items_col))

        self.content = self.section

# - menu bar
class MenuBar(ft.Container):
    """Represents an app menu bar to be used in Flet apps.
    """
    def __init__(self, cltheme:Theme, sections:list[MenuBarSection]=[], bar_height:int=40, 
                 defined:bool=False, expand:bool|int=False, transparent:bool=False, with_blur:bool=False,
                 actions:list[TextButton|IconButton|FilledButton]=[]):
        super().__init__()
        self.cltheme = cltheme
        self.expand = expand
        self.height = bar_height if not expand else None
        self.bgcolor = cltheme.background_two if not transparent else self.cltheme.transparent
        self.blur = 5 if with_blur else None
        self.alignment = ft.alignment.center_left
        self.padding = ft.padding.only(left=5, top=5, right=10, bottom=5)
        self.animate = ft.Animation(100, ft.AnimationCurve.EASE_OUT)
        if defined:
            self.border = None
            self.border_radius = 10
            self.margin = ft.margin.only(left=5, right=5)

        # BAR CONTENT
        # - menu sections
        self.menu_sections = ft.Row(spacing=0, scroll=ft.ScrollMode.ADAPTIVE, controls=[])
        for section in sections:
            if section != sections[-1]:
                self.menu_sections.controls.extend([section, ft.VerticalDivider(thickness=1, color=self.cltheme.divider)])
            else:
                self.menu_sections.controls.append(section)
        # - menu actions
        self.menu_actions = ft.Row(spacing=5, alignment=ft.MainAxisAlignment.END, controls=actions)

        self.content = ft.Row(spacing=0, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[self.menu_sections, self.menu_actions])

    def upd(self, new_bar_height:int=None):

        if new_bar_height is not None and not self.expand:
            self.height = new_bar_height
        self.update()

    def upd_actions(self, new_actions:list[TextButton|IconButton|FilledButton]):
        self.menu_actions.controls = new_actions
        self.update()

# NAVIGATION BARS
# - lateral navigation bar
class LateralNavBar(ft.Container):
    """Represents a lateral navigation bar to be used in Flet Apps."""
    def __init__(self, cltheme:Theme, header_text:str, header_font:str=None, destinations:list[NavButton]=[], 
                 bar_width:int=80, header_size:int=16, actions:list[TextButton|IconButton]=None, 
                 subdestinations:list[NavButton]=None):
        super().__init__()
        self.cltheme = cltheme
        self.width = bar_width
        self.bgcolor = cltheme.transparent
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(left=10, top=0, right=10, bottom=5)
        self.destinations = destinations
        self.actions = actions
        self.subdestinations = subdestinations

        # NAVIGATION CONTENT
        # - header
        self.header = ft.Container(
            bgcolor=self.cltheme.transparent,
            height=40,
            alignment=ft.alignment.center_left,
            padding=5,
            content=ft.Text(
                value=header_text,
                font_family=header_font,
                color=self.cltheme.font_three,
                size=header_size
            )
        )
        # - destinations menu
        self.destinations_menu = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            content=ft.Column(
                spacing=5,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=destinations
            )
        )
        # - actions menu
        if actions is not None:
            self.actions_menu = ft.Container(
                alignment=ft.alignment.center,
                content=ft.Row(
                    spacing=5,
                    controls=actions
                )
            )
        # - subdestinations menu
        if subdestinations is not None:
            self.subdestinations_menu = ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=5,
                    controls=subdestinations
                )
            )
        # - content layout
        self.content = ft.Column(spacing=5, controls=[
            self.header,
            self.destinations_menu
        ])
        if actions is not None:
            self.content.controls.append(self.actions_menu)
        if subdestinations is not None:
            self.content.controls.extend([
                ft.Divider(color=cltheme.divider),
                self.subdestinations_menu
            ])

    def add_destination(self, new_destination:NavButton):
        self.destinations.append(new_destination)
        self.destinations_menu.content.controls.append(new_destination)
        self.update()

    def del_destination(self, old_destination:NavButton):
        self.destinations.remove(old_destination)
        self.destinations_menu.content.controls.remove(old_destination)
        self.update()

    def add_subdestination(self, new_subdestination:NavButton):
        self.subdestinations.append(new_subdestination)
        self.subdestinations_menu.content.controls.append(new_subdestination)
        self.update()
    
    def del_subdestination(self, old_subdestination:NavButton):
        self.subdestinations.remove(old_subdestination)
        self.subdestinations_menu.content.controls.remove(old_subdestination)
        self.update()
    
    def upd_destinations(self, new_destinations:list[NavButton]):
        self.destinations = new_destinations
        self.destinations_menu.content.controls = new_destinations
        self.update()

    def upd_destinations_state(self, new_location:NavButton=None):
        if new_location is not None:
            # unselect old destination or subdestination and select the new one
            for destination in self.destinations:
                if destination == new_location:
                    destination.upd_selection_state(selected=True)
                else:
                    destination.upd_selection_state(selected=False)
            if self.subdestinations is not None:
                for subdestination in self.subdestinations:
                    if subdestination == new_location:
                        subdestination.upd_selection_state(selected=True)
                    else:
                        subdestination.upd_selection_state(selected=False)
        else:
            for destination in self.destinations:
                destination.upd_selection_state(selected=False)
            if self.subdestinations is not None:
                for subdestination in self.subdestinations:
                    subdestination.upd_selection_state(selected=False)
        self.update()

# - group nav bar
class GroupNavBar(ft.Container):
    """Represents a navigation bar with switch style to be used in Flet Apps."""
    def __init__(self, cltheme:Theme, destinations:list[SelectableButton], bar_size:int=30, expand:bool|int=False, visible:bool=True):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_themes.Theme``` with the colors set to paint the bar.
        - destinations: is a list of ```calet_button.SelectableButton``` objects where each object will represent a different option in the nav bar. All objects in the list must be of the same class.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        """
        super().__init__()
        self.cltheme = cltheme
        self.destinations = destinations
        self.bar_size = bar_size
        self.expand = expand
        self.bgcolor = self.cltheme.transparent_1
        self.alignment = ft.alignment.center
        self.padding = 3
        self.border_radius = 5
        self.content = ft.Row(spacing=5, controls=self.destinations)
        self.visible = visible
        self.opacity = 1 if visible else 0
        self.scale = 1 if visible else 0
        self.animate = ft.Animation(150, ft.AnimationCurve.LINEAR)
        self.animate_scale = ft.Animation(100, ft.AnimationCurve.LINEAR)
        self.animate_opacity = ft.Animation(200, ft.AnimationCurve.LINEAR)
        self.on_animation_end = self.bar_animated
    
    # LIFE CICLE
    def did_mount(self):
        self.animation_emulator = AnimationEmulator(self.page, self.animation_emulator_animated)

    # HANDLERS
    def bar_animated(self, e:ft.ControlEvent):
        if self.opacity == 0:
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

    def upd_destinations_state(self, new_location:SelectableButton):
        # unselect old destination and select the new one
        for destination in self.destinations:
            if destination == new_location:
                destination.upd_selection_state(selected=True)
            else:
                destination.upd_selection_state(selected=False)
        self.update()
    
    def selected_destination(self):
        for destination in self.destinations:
            if destination.selected:
                return destination.button_text.value

# - swap navigation bar
class SwapNavBar(ft.Container):
    """Represents a navigation bar with swapping style to be used in Flet Apps."""
    def __init__(self, cltheme:Theme, destinations:list[SwapNavButton], selected_option:int=0, 
                 bar_size:int=30, expand:bool|int=False):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_themes.Theme``` with the colors set to paint the bar.
        - destinations: is a list of ```calet_button.SwapDestination```  objects where each object will represent a different option in the nav bar. All objects in the list must be of the same class.
        - selected_option: is the index of the default selected option in the nav bar.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        """
        super().__init__()
        for destination in destinations:
            destination.expand = 1
        self.cltheme = cltheme
        self.selected_option = selected_option
        self.destinations = destinations
        self.bar_size = bar_size
        self.expand = expand

        # ITEMS LAYOUT
        # - items container
        self.items_layout = ft.Container(
            expand=True,
            bgcolor=self.cltheme.transparent_1,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=10,
            content=ft.Row(spacing=0, controls=self.destinations)
        )

        # SELECTION MARK LAYOUT
        # - selection mark
        self.selection_mark = ft.Container(
            expand=1,
            bgcolor=self.cltheme.primary,
            alignment=ft.alignment.center,
            padding=self.destinations[0].padding,
            margin=5,
            border_radius=5,
            offset=ft.Offset(self.selected_option,0),
            animate_offset=ft.Animation(duration=200, curve=ft.AnimationCurve.LINEAR_TO_EASE_OUT),
            content=ft.Text(
                value=self.destinations[self.selected_option].button_text.value,
                color=self.cltheme.font_four,
                size=self.destinations[0].button_text.size,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            )
        )

        self.content = ft.Stack(
            height=self.bar_size,
            controls=[
                self.items_layout,
                ft.Row(spacing=0, expand=True, controls=[
                    self.selection_mark, 
                    ft.Row(
                        expand=len(self.destinations)-1
                    )
                ])
            ]
        )
    
    def upd_destinations_state(self, new_location:SwapNavButton):
        # unselect old destination and select the new one
        for i in range(len(self.destinations)):
            if self.destinations[i] == new_location:
                self.destinations[i].upd_selection_state(selected=True)
                self.selection_mark.content.value = new_location.button_text.value
                self.selection_mark.offset.x = i
            else:
                self.destinations[i].upd_selection_state(selected=False)
        self.update()
    