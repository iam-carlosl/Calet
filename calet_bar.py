"""Calet: a visual components library based on Flet framework
   - Bars module"""

import flet as ft
from calet_errors import *
from calet_theme import *
from calet_button import *
import math

# app title bar (ok)
class ClAppBar(ft.UserControl):
    """Represents an app title bar to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, title:str, win_actions:list[ClWinButton|ClIconButton],
                 left_title:bool=False, title_icon:str=None, high_title_color:bool=False, left_icon:str=None, 
                 content_size:int=16, bar_size:int=40, defined_sections:bool=False, scrollable_sections:str=None, 
                 expand:bool|int=False, transparent:bool=False, with_blur:bool=False, can_maximize:bool=True, 
                 left_actions:list[ClTextButton|ClIconButton|ClModeButton|ClSwitch|ClMenuButton]=[],
                 right_actions:list[ClTextButton|ClIconButton|ClModeButton|ClSwitch]=[]):
        """Use this properties to personalize the app bar:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - title: is the text to display as title in the app bar.
        - win_actions: is a list of ```calet_button.ClWinButton``` or ```calet_button.ClIconButton``` objects that will be placed in the window buttons zone of the app bar.
        - left_title: is a flag saying if the title must be displayed on the left or middle of the app bar. If left_actions were given the title will always be on the middle.
        - high_title_color: is a flag saying if the title font color must be higher or lower tone.
        - title_icon: is an icon to display on the left of the title text if ```left_title``` is False, else on the right. Can be a Flet.icons constant or a path to an image.
        - left_icon: is an icon to display in the left side of the app bar.
        - bar_size: is th custom size of the bar. If ```expand``` is not False this property will be ignored.
        - content_size: is a personalized size for the title, left icon and title icon.
        - defined_sections: is a flag saying if the app bar sections must be displayed as a visual defined block or not.
        - scrollable_sections: is the scroll mode for app bar sections. Can be 'left' for only left section scrollable_sections, 'right' for only right section scrollable or 'both' for both sections scrollable.
        - expand: is the responsive expansion of the app bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the app bar must be displayed transparent or colored.
        - with_blur: is a flag saying if the app bar must be displayed with blur effect or not.
        - can_maximize: is a flag saying if the app bar can maximize the window with double tap.
        - left_actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClIconButton```, ```calet_button.ClModeButton```, ```calet_button.ClSwitch``` or ```calet_button.ClMenuButton``` objects to be displayed in the left side of the app bar.
        - right_actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClIconButton```, ```calet_button.ClModeButton```, ```calet_button.ClSwitch``` objects to be displayed in the right side of the app bar.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(title, str):
            raise ClError(
                error="Argument Error: <<title>> must be string."
            )
        if not isinstance(left_title, bool):
            raise ClError(
                error="Argument Error: <<left_title>> must be boolean."
            )
        if not isinstance(high_title_color, bool):
            raise ClError(
                error="Argument Error: <<high_title_color>> must be boolean."
            )
        if title_icon is not None and not isinstance(title_icon, str):
            raise ClError(
                error="Argument Error: <<title_icon>> must be string."
            )
        if left_icon is not None and not isinstance(left_icon, str):
            raise ClError(
                error="Argument Error: <<left_icon>> must be string."
            )
        elif left_icon is not None and "/" in left_icon:
            file = None
            try:
                file = open(left_icon)
            except Exception:
                raise ClError(
                    error="Argument Error: <<left_icon>> is an invalid path or the file doesn't exist."
                )
            finally:
                file.close()
            if not left_icon.endswith(("png","jpeg")):
                raise ClError(
                    error="Argument Error: <<left_icon>> is an invalid file. Must be in PNG or JPEG format."
                )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(defined_sections, bool):
            raise ClError(
                error="Argument Error: <<defined_sections>> must be boolean."
            )
        if scrollable_sections is not None and not isinstance(scrollable_sections, str):
            raise ClError(
                error="Argument Error: <<scrollable_sections>> must be string."
            )
        elif scrollable_sections is not None and scrollable_sections not in ("left","right","both"):
            raise ClError(
                error="Argument Error: <<scrollable_sections>> must be 'left', 'right' or 'both'."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        if not isinstance(can_maximize, bool):
            raise ClError(
                error="Argument Error: <<can_maximize>> must be boolean."
            )
        if not isinstance(win_actions, list):
            raise ClError(
                error="Argument Error: <<win_actions>> must be a list."
            )
        else:
            for i in range(len(win_actions)):
                if not isinstance(win_actions[i], (ClWinButton, ClIconButton)):
                    raise ClError(
                        error=f"Argument Error: <<win_actions[{i}]>> must be an instance of 'calet_button.ClWinButton' or 'calet_button.ClIconButton' class."
                    )
        for i in range(len(left_actions)):
            if not isinstance(left_actions[i], (ClTextButton, ClIconButton, ClModeButton, ClSwitch, ClMenuButton)):
                raise ClError(
                    error=f"Argument Error: <<left_actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 'calet_button.ClIconButton','calet_button.ClModeButton', 'calet_button.ClSwitch' or 'calet_button.ClMenuButton' class."
                )
        for i in range(len(right_actions)):
            if not isinstance(right_actions[i], (ClTextButton, ClIconButton, ClModeButton, ClSwitch)):
                raise ClError(
                    error=f"Argument Error: <<right_actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 'calet_button.ClIconButton','calet_button.ClModeButton' or 'calet_button.ClSwitch' class."
                )
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.title = title
        self.win_actions = win_actions
        self.left_title = left_title
        self.title_icon = title_icon
        self.high_title_color = high_title_color
        self.left_icon = left_icon
        self.content_size = content_size
        self.bar_size = bar_size
        self.defined_sections = defined_sections
        self.scrollable_sections = scrollable_sections
        self.expand = expand
        self.transparent = transparent
        self.with_blur = with_blur
        self.can_maximize = can_maximize
        self.left_actions = left_actions
        self.right_actions = right_actions
    
    def build(self):

        # APP BAR CONTENT
        # - app icon
        if self.left_icon is not None:
            self.app_icon = ft.Icon(
                name=self.left_icon,
                color=self.theme.font_three if self.high_title_color else self.theme.primary,
                size=self.content_size+4
            ) if "/" not in self.left_icon else ft.Image(
                src=self.left_icon,
                fit=ft.ImageFit.CONTAIN,
                width=self.content_size+4,
                height=self.content_size+4
            )
        # - app title
        self.app_title = ft.Text(
            value=self.title,
            color=self.theme.font_three if self.high_title_color else self.theme.font_one,
            size=self.content_size,
            text_align=ft.TextAlign.LEFT if self.left_title else ft.TextAlign.CENTER
        )
        # - app title icon
        if self.title_icon is not None:
            self.app_title_icon = ft.Icon(
                name=self.title_icon,
                color=self.theme.font_three if self.high_title_color else self.theme.font_one,
                size=self.content_size
            )
        # - left items
        self.left_items = ft.Row(
            expand=None if self.left_title and not self.left_actions else 1,
            spacing=5,
            alignment=ft.MainAxisAlignment.START,
            controls=[]
        )
        # -- adding app icon
        if self.left_icon is not None:
            self.left_items.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    content=self.app_icon
                )
            )
        # -- adding title in the left
        if self.left_title and not self.left_actions:
            # --> app title
            self.left_items.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    content=self.app_title
                )
            )
            # --> app title icon
            if self.title_icon is not None:
                self.left_items.controls.append(
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=self.app_title_icon
                    )
                )
        # -- adding left actions and title in the middle
        else:
            # --> left actions
            self.left_items.controls.append(
                ft.Container(
                    expand=True if self.scrollable_sections in ("left","both") else None,
                    alignment=ft.alignment.center_left,
                    bgcolor=self.theme.transparent_05 if self.defined_sections else None,
                    padding=2 if self.defined_sections else None,
                    border_radius=5 if self.defined_sections else None,
                    content=ft.Row(
                        spacing=5,
                        scroll=ft.ScrollMode.ADAPTIVE,
                        controls=self.left_actions
                    )
                )
            )
            # - middle items
            self.mid_items = ft.Row(
                expand=1,
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[]
            )
            # -- app title icon
            if self.title_icon is not None:
                self.mid_items.controls.append(
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=self.app_title_icon
                    )
                )
            # -- app title
            self.mid_items.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    content=self.app_title
                )
            )
        # - right items
        self.right_items = ft.Row(
            expand=True if self.left_title and not self.left_actions else 1,
            spacing=5,
            alignment=ft.MainAxisAlignment.END,
            controls=[
                # -- right actions
                ft.Container(
                    expand=True if self.scrollable_sections in ("right","both") else None,
                    alignment=ft.alignment.center_right,
                    bgcolor=self.theme.transparent_05 if self.defined_sections else None,
                    padding=2 if self.defined_sections else None,
                    border_radius=5 if self.defined_sections else None,
                    content=ft.Row(
                        spacing=5,
                        scroll=ft.ScrollMode.ADAPTIVE,
                        controls=self.right_actions
                    )
                ),
                # -- win actions
                ft.Row(
                    spacing=5,
                    controls=self.win_actions
                )
            ]
        )

        # APP BAR
        return ft.WindowDragArea(
            maximizable=self.can_maximize,
            content=ft.Container(
                bgcolor=self.theme.transparent if self.transparent else self.theme.background_one,
                blur=5 if self.with_blur else None,
                height=self.bar_size if not self.expand else None,
                padding=ft.padding.only(left=5, top=4, right=5, bottom=4),
                content=ft.Row(
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        self.left_items,
                        self.right_items
                    ] if self.left_title and not self.left_actions else [
                        self.left_items,
                        self.mid_items,
                        self.right_items
                    ]
                )
            )
        )

# app menu bar section (ok)
class ClMenuSection(ft.UserControl):
    """Represents a section of an app submenu bar to be used in ```calet_bar.ClSubmenuBar``` objects."""
    def __init__(self, theme:ClTheme, actions:list[list], lateral:bool=False, defined:bool=False, expand:bool|int=False):
        """Use this properties to personalize the menu section:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - actions: is a list of lists of ```calet_button.ClTextButton```, ```calet_button.ClButton```, ```calet_button.ClAcceptButton```, ```calet_button.ClCancelButton```, ```calet_button.ClSelectableTextButton```, ```calet_button.ClModeButton```, ```calet_button.ClIconButton```, ```calet_button.ClMenuButton```, ```calet_button.ClCheck```, ```calet_button.ClRadio```, ```calet_button.ClSwitch``` where each sublist will represent a different column of actions in the section.
        - defined: is a flag saying if the section must be displayed as a visual defined block or not.
        - lateral: is a flag saying if the section will be displayed in a normal or lateral menu.
        - expand: is the responsive expansion of the menu section in his container. See ```expand``` Flet property for more information.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(defined, bool):
            raise ClError(
                error="Argument Error: <<defined>> must be boolean."
            )
        if not isinstance(lateral, bool):
            raise ClError(
                error="Argument Error: <<lateral>> must be boolean."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(actions, list):
            raise ClError(
                error="Argument Error: <<actions>> must be a list."
            )
        else:
            for i in range(len(actions)):
                if not isinstance(actions[i], list):
                    raise ClError(
                        error=f"Argument Error: <<actions[{i}]>> is not a list. <<actions>> must be a list of lists."
                    )
                else:
                    for j in range(len(actions[i])):
                        if not isinstance(actions[i][j], (ClTextButton, ClButton, ClAcceptButton, ClCancelButton, ClSelectableTextButton, ClModeButton, ClIconButton, ClMenuButton, ClCheck, ClRadio, ClSwitch)):
                            raise ClError(
                                error=f"""Argument Error: <<actions[{i}][{j}]>> must be an instance of 
                                    'calet_button.ClTextButton', 'calet_button.ClButton', 'calet_button.ClAcceptButton', 
                                    'calet_button.ClCancelButton', 'calet_button.ClSelectableTextButton', 
                                    'calet_button.ClModeButton', 'calet_button.ClIconButton', 'calet_button.ClMenuButton', 
                                    'calet_button.ClCheck', 'calet_button.ClRadio', 'calet_button.ClSwitch' class."""
                            )
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.actions = actions
        self.lateral = lateral
        self.defined = defined
        self.expand = expand

    def build(self):

        # SECTION
        # - creating the section
        self.section = ft.Row(
            spacing=0,
            controls=[]
        ) if not self.lateral else ft.Column(
            spacing=0,
            controls=[]
        )
        # - adding the section content
        for actions_group in self.actions:
            for action in actions_group:
                action.expand = 1
            self.section.controls.append(
                ft.Column(
                    spacing=5,
                    controls=actions_group
                ) if not self.lateral else ft.Row(
                    spacing=5,
                    controls=actions_group
                )
            )

        return ft.Container(
            bgcolor=self.theme.transparent_05 if self.defined else None,
            alignment=ft.alignment.center,
            border_radius=5,
            content=self.section
        )

# app Menu bar (ok)
class ClMenuBar(ft.UserControl):
    """Represents an app menu bar to be used in Flet apps directly or combined with a ```calet_bar.ClNavBar``` or
    ```calet_bar.ClLateralNavBar```.
    """
    def __init__(self, theme:ClTheme, sections:list[ClMenuSection], lateral:bool=False, bar_size:int=100, 
                 defined:bool=False, expand:bool|int=False, transparent:bool=False, with_blur:bool=False,
                 right_actions:list[ClTextButton|ClIconButton]=[]):
        """Use this properties to personalize the menu:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - sections: is a list of ```calet_bar.ClMenuSection``` objects where each object will be displayed as a different section of the menu.
        - lateral: is a flag saying if the menu must be displayed verticaly or horizontaly.
        - bar_size: is the custom size of the bar. If ```expand``` is not False this property will be ignored.
        - defined: is a flag saying if the entire bar must be displayed as a defined visual block with margin from the sides of his container.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the menu must be displayed transparent or colored.
        - with_blur: is a flag saying if the menu must be displayed with blur effect or not.
        - right_actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClIconButton```, ```calet_button.ClModeButton```, ```calet_button.ClSwitch``` objects to be displayed in the right side of the menu bar.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(lateral, bool):
            raise ClError(
                error="Argument Error: <<lateral>> must be boolean."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(defined, bool):
            raise ClError(
                error="Argument Error: <<defined>> must be boolean."
            )
        if not isinstance(expand, (bool, int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        if not isinstance(sections, list):
            raise ClError(
                error="Argument Error: <<sections>> must be a list."
            )
        else:
            for i in range(len(sections)):
                if not isinstance(sections[i], ClMenuSection):
                    raise ClError(
                        error=f"Argument Error: <<sections[{i}]>> must be an instance of 'calet_bar.ClMenuSection' class."
                    )
                sections[i].lateral = lateral
        if not isinstance(right_actions, list):
            raise ClError(
                error="Argument Error: <<right_actions>> must be a list."
            )
        else:
            for i in range(len(right_actions)):
                if not isinstance(right_actions[i], ClTextButton, ClIconButton, ClModeButton, ClSwitch):
                    raise ClError(
                        error=f"Argument Error: <<right_actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 'calet_button.ClIconButton', 'calet_button.ClModeButton', 'calet_button.ClSwitch' class."
                    )
        # INITIAlIZATION
        super().__init__()
        self.theme = theme
        self.sections = sections
        self.lateral = lateral
        self.bar_size = bar_size
        self.defined = defined
        self.expand = expand
        self.transparent = transparent
        self.with_blur = with_blur
        self.right_actions = right_actions

    def build(self):

        # MENU
        # - creating the menu
        self.menu = ft.Row(
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[]
        ) if not self.lateral else ft.Column(
            spacing=5,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[]
        )
        # - adding the menu content
        for section in self.sections:
            if section != self.sections[-1]:
                self.menu.controls.extend(
                    [section, ft.VerticalDivider(thickness=1, color=self.theme.divider) if not self.lateral else ft.Divider(thickness=1, color=self.theme.divider)]
                )
            else:
                self.menu.controls.append(section)
        
        # RIGHT ITEMS
        # - right items
        if self.right_actions:
            self.right_items = ft.Row(
                spacing=5,
                alignment=ft.MainAxisAlignment.END,
                controls=self.right_actions
            )

        # BAR
        self.bar = ft.Container(
            height=self.bar_size if not self.expand and not self.lateral else None,
            width=self.bar_size if not self.expand and self.lateral else None,
            bgcolor=self.theme.background_two if not self.transparent else self.theme.transparent,
            blur=5 if self.with_blur else None,
            border=ft.border.only(bottom=ft.BorderSide(1, self.theme.divider)) if not self.lateral else ft.border.only(right=ft.BorderSide(1, self.theme.divider)),
            alignment=ft.alignment.center_left if not self.lateral else ft.alignment.top_center,
            padding=5,
            animate=ft.Animation(100, ft.AnimationCurve.EASE_OUT),
            content=ft.Row(
                spacing=0,
                controls=[
                    self.menu,
                    self.right_items
                ]
            ) if self.right_actions else self.menu
        )
        if self.defined:
            self.bar.border = None
            self.bar.border_radius = 10
            self.bar.margin = ft.margin.only(
                left=5, right=5
            ) if not self.lateral else ft.margin.only(
                top=5, bottom=5
            )

        return self.bar

    def upd(self, bar_size:int=None):

        if bar_size is not None and not self.expand:
            self.bar_size = bar_size
            if self.lateral:
                self.bar.width = bar_size
            else:
                self.bar.height = bar_size
        self.update()

# app nav bar (ok)
class ClNavBar(ft.UserControl):
    """Represents a tabs navigation bar to be used in Flet Apps."""
    def __init__(self, theme:ClTheme, options:list[ClNavTab|ClSelectableTextButton], selected_option:int=0, 
                 bar_size:int=40, expand:bool|int=False, transparent:bool=False, with_blur:bool=False,
                 actions:list[ClTextButton|ClButton|ClIconButton|ClModeButton|ClSwitch]=[], 
                 submenus:list[ClMenuBar]=[]):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - options: is a list of ```calet_button.ClNavTab``` or ```calet_button.ClSelectableTextButton``` objects where each object will represent a different option in the nav bar. All objects in the list must be of the same class.
        - selected_option: is the index of the default selected option in the nav bar.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the submenu must be displayed transparent or colored.
        - with_blur: is a flag saying if the submenu must be displayed with blur effect or not.
        - actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClButton```, ```calet_button.ClIconButton```, ```calet_button.ClModeButton``` or ```calet_button.ClSwitch``` objects to be displayed as actions in the right side of the nav bar.
        - submenus: is a list of ```calet_bar.ClMenuBar``` objects where each object will be displayed as the submenu of a different option in the menu bar. If it's given, must have the same length of ```options``` list. 
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(selected_option, int):
            raise ClError(
                error="Argument Error: <<selected_option>> must be boolean."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        options_map = {}
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list."
            )
        else:
            if not options:
                raise ClError(
                    error="Argument Error: <<options>> must be a list with at least one option."
                )
            if not 0 <= selected_option < len(options):
                raise ClError(
                    error="Argument Error: <<selected_option>> is out of the range of options."
                )
            for i in range(len(options)):
                if not isinstance(options[i], (ClNavTab, ClSelectableTextButton)):
                    raise ClError(
                        error=f"""Argument Error: <<options[{i}]>> must be an instance of 'calet_bar.ClNavTab' or 
                            'calet_bar.ClSelectableTextButton' class."""
                    )
                if isinstance(options[0], ClNavTab) and not isinstance(options[i], ClNavTab):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClNavTab' class
                            because the first one is it."""
                    )
                elif isinstance(options[0], ClSelectableTextButton) and not isinstance(options[i], ClSelectableTextButton):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClSelectableTextButton' class
                            because the first one is it."""
                    )
                # - selecting the default option
                options[i].selected = False if i != selected_option else True
                # - using the same 'for' cicle to extend action of each option in the list
                options_map[options[i]] = i, options[i].action
                options[i].action = self.option_clicked
        if not isinstance(actions, list):
            raise ClError(
                error="Argument Error: <<actions>> must be a list."
            )
        else:
            for i in range(len(actions)):
                if not isinstance(actions[i], (ClTextButton, ClButton, ClIconButton, ClModeButton, ClSwitch)):
                    raise ClError(
                        error=f"""Argument Error: <<actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 
                            'calet_button.ClButton', 'calet_button.ClIconButton', 'calet_button.ClModeButton' or 
                            'calet_button.ClSwitch' class."""
                    )
        submenus_maxsize = []
        if not isinstance(submenus, list):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list."
            )
        elif submenus and len(submenus) < len(options):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list with the same lenght of 'options' list."
            )
        else:
            for i in range(len(submenus)):
                if not isinstance(submenus[i], ClMenuBar):
                    raise ClError(
                        error=f"Argument Error: <<submenus[{i}]>> must be an instance of 'calet_bar.ClMenuBar' class."
                    )
                submenus_maxsize.append(submenus[i].bar_size)
                submenus[i].expand = 2 if expand else False
                submenus[i].lateral = False
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.options = options
        self.selected_option = selected_option
        self.bar_size = bar_size
        self.transparent = transparent
        self.with_blur = with_blur
        self.expand = expand
        self.actions = actions
        self.submenus = submenus
        self.submenus_maxsize = submenus_maxsize
        self.options_map = options_map

    def build(self):
        
        # NAV BAR
        # - bar left items
        self.left_items = ft.Container(
            alignment=ft.alignment.center_left,
            expand=True,
            content=ft.Row(
                spacing=0,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=self.options
            )
        )
        # - bar right items
        if self.submenus:
            self.b_toggle = ft.IconButton(
                data=self.expand,
                style=ft.ButtonStyle(
                    bgcolor={
                        ft.MaterialState.DEFAULT: self.theme.transparent,
                        ft.MaterialState.SELECTED: self.theme.transparent_1
                    },
                    overlay_color={
                        ft.MaterialState.HOVERED: self.theme.transparent_05
                    },
                    padding=0,
                    shape=ft.RoundedRectangleBorder(radius=5),
                ),
                selected=True,
                content=ft.Icon(
                    name=ft.icons.EXPAND_MORE,
                    color=self.theme.font_two,
                    size=self.options[0].content_size+4,
                    rotate=math.pi,
                    animate_rotation=200
                ),
                on_click=self.b_toggle_clicked
            )
            self.actions.append(self.b_toggle)
        if self.actions:
            self.right_items = ft.Container(
                alignment=ft.alignment.center,
                padding=5,
                content=ft.Row(
                    spacing=5,
                    controls=self.actions
                )
            )
        # - bar
        self.bar = ft.Container(
            expand=1 if self.expand else False,
            height=self.bar_size if not self.expand else None,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=15),
            bgcolor=self.theme.background_one,
            border=ft.border.only(bottom=ft.BorderSide(1, self.theme.divider)) if not self.submenus else None,
            content=ft.Row(
                spacing=0,
                controls=[self.left_items, self.right_items]
            ) if self.actions else self.left_items
        )

        # SUBMENUS
        if self.submenus:
            self.bar = ft.Container(
                bgcolor=self.theme.background_one,
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=0,
                    controls=[self.bar, self.submenus[self.selected_option]]
                )
            )

        return self.bar

    def b_toggle_clicked(self, e:ft.TapEvent):
        e.control.selected = not e.control.selected
        if not self.expand:
            self.submenus[self.selected_option].upd(bar_size=self.submenus_maxsize[self.selected_option] if e.control.selected else 0)
        else:
            self.expand = e.control.data if e.control.selected else 1
            self.submenus[self.selected_option].visible = True if e.control.selected else False
        e.control.content.rotate = math.pi if e.control.selected else 0
        e.control.content.color = self.theme.font_two if e.control.selected else self.theme.font_one
        self.update()

    def option_clicked(self, e:ft.TapEvent):
        # mapping the index of the clicked option and updating selection
        clicked_index = self.options_map[e.control.data][0]
        if self.selected_option != clicked_index: # else nothing change in the selections
            self.options[self.selected_option].upd(selected=False)
            self.selected_option = clicked_index
            # openning submenu of clicked option
            if self.submenus:
                self.bar.content.controls[1] = self.submenus[self.selected_option]
                if self.expand:
                    self.submenus[self.selected_option].visible = True if self.b_toggle.selected else False
                else:
                    self.submenus[self.selected_option].bar_size = self.submenus_maxsize[self.selected_option] if self.b_toggle.selected else 0
            self.update()
        # mapping the custom action of the clicked option and redirecting it to the user
        clicked_action = self.options_map[e.control.data][1]
        if clicked_action is not None:
            clicked_action(e)

# experimental app menu bar with experimental menu tabs behavior
class ClExperimentalMenuBar(ft.UserControl):
    """Represents an app menu bar to be used in Flet Apps."""
    def __init__(self, theme:ClTheme, options:list[ClExperimentalMenuTab|ClSelectableTextButton], selected_option:int=0, 
                 transparent:bool=False, with_blur:bool=False, expand:bool=False,
                 actions:list[ClTextButton|ClButton|ClIconButton|ClModeButton|ClSwitch]=[], 
                 submenus:list[ClMenuBar]=[]):
        """Use this properties to personalize the submenu:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - options: is a list of ```calet_button.ClExperimentalMenuTab``` or ```calet_button.ClSelectableTextButton``` objects where each object 
            will represent a different option in the menu bar. All objects in the list must be of the same class.
        - selected_option: is the index of the default selected option in the menu bar.
        - transparent: is a flag saying if the submenu must be displayed transparent or colored.
        - with_blur: is a flag saying if the submenu must be displayed with blur effect or not.
        - expand: is the responsive expansion of the menu bar in his container. See 'expand' Flet
            property for more information.
        - actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClButton```,
            ```calet_button.ClIconButton```, ```calet_button.ClModeButton``` or ```calet_button.ClSwitch``` objects
            to be displayed as actions in the right side of the menu bar.
        - submenus: is a list of ```calet_bar.ClMenuBar``` objects where each object will be displayed as the submenu
            of a different option in the menu bar. If it's given, must have the same length of ```options``` list. 
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(selected_option, int):
            raise ClError(
                error="Argument Error: <<navtabs_style>> must be boolean."
            )
        options_map = {}
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list."
            )
        else:
            if not options:
                raise ClError(
                    error="Argument Error: <<options>> must be a list with at least one option."
                )
            if not 0 <= selected_option < len(options):
                raise ClError(
                    error="Argument Error: <<selected_option>> is out of the range of options."
                )
            is_tabs = False
            for i in range(len(options)):
                if not isinstance(options[i], (ClExperimentalMenuTab, ClSelectableTextButton)):
                    raise ClError(
                        error=f"""Argument Error: <<options[{i}]>> must be an instance of 'calet_bar.ClExperimentalMenuTab' or 
                            'calet_bar.ClSelectableTextButton' class."""
                    )
                if i == 0 and isinstance(options[i], ClExperimentalMenuTab):
                    is_tabs = True
                else:
                    if is_tabs and not isinstance(options[i], ClExperimentalMenuTab):
                        raise ClError(
                            error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClExperimentalMenuTab' class
                                because the first one is it."""
                        )
                    elif not is_tabs and not isinstance(options[i], ClSelectableTextButton):
                        raise ClError(
                            error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClSelectableTextButton' class
                                because the first one is it."""
                        )
                # - selecting the default option
                options[i].selected = False if i != selected_option else True
                if i > 0:
                    options[i-1].right_selected = False if i != selected_option else True
                if i < len(options)-1:
                    options[i+1].left_selected = False  if i != selected_option else True
                # - using the same 'for' cicle to extend action of each option in the list
                options_map[options[i]] = i, options[i].action
                options[i].action = self.tab_clicked
        if not isinstance(actions, list):
            raise ClError(
                error="Argument Error: <<actions>> must be a list."
            )
        else:
            for i in range(len(actions)):
                if not isinstance(actions[i], (ClTextButton, ClButton, ClIconButton, ClModeButton, ClSwitch)):
                    raise ClError(
                        error=f"""Argument Error: <<actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 
                            'calet_button.ClButton', 'calet_button.ClIconButton', 'calet_button.ClModeButton' or 
                            'calet_button.ClSwitch' class."""
                    )
        if not isinstance(submenus, list):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list."
            )
        elif submenus and len(submenus) < len(options):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list with the same lenght of 'options' list."
            )
        else:
            for i in range(len(submenus)):
                if not isinstance(submenus[i], ClMenuBar):
                    raise ClError(
                        error=f"Argument Error: <<submenus[{i}]>> must be an instance of 'calet_bar.ClMenuBar' class."
                    )
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.options = options
        self.selected_option = selected_option
        self.options_map = options_map
        self.transparent = transparent
        self.with_blur = with_blur
        self.expand = expand
        self.actions = actions
        self.submenus = submenus

    def build(self):
        
        # MENU CONTENT
        # - creating left margin container for options section if they are menu tabs
        if isinstance(self.options[0], ClExperimentalMenuTab):
            self.left_margin = ft.Container(
                alignment=ft.alignment.center,
                bgcolor=self.theme.background_one if not self.options[0].selected else self.theme.background_two,
                padding=0,
                animate=100,
                content=ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor=self.theme.background_one,
                    padding=5,
                    border_radius=ft.border_radius.only(bottom_right=5)
                )
            )
        # - creating right margin container for options section
        if isinstance(self.options[0], ClExperimentalMenuTab):
            self.right_margin = ft.Container(
                alignment=ft.alignment.center,
                bgcolor=self.theme.background_one if not self.options[-1].selected else self.theme.background_two,
                padding=0,
                animate=100,
                border=ft.BorderSide(0),
                content=ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor=self.theme.background_one,
                    padding=5,
                    border_radius=ft.border_radius.only(bottom_left=5),
                )
            )

        # MENU
        # - menu bar left items
        self.left_items = ft.Row(
            expand=True,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[self.left_margin]+self.options+[self.right_margin] if isinstance(self.options[0], ClExperimentalMenuTab) else self.options
        )
        # - menu bar right items
        if self.actions:
            self.right_items = ft.Row(
                spacing=0,
                controls=self.actions
            )
        
        return ft.Container(
            bgcolor=self.theme.background_one,
            alignment=ft.alignment.center_left,
            padding=0,
            content=ft.Row(
                spacing=0,
                controls=[self.left_items, self.right_items]
            ) if self.actions else self.left_items
        )
    
    def tab_clicked(self, e:ft.TapEvent):
        print("tab_clicked")
        # mapping the index of the clicked option and updating selection
        clicked_index = self.options_map[e.control.data][0]
        print(self.selected_option)
        print(clicked_index)
        if self.selected_option != clicked_index: # else nothing change in the selections
            self.options[self.selected_option].upd(selected=False)
            # self.options[clicked_index].upd(selected=True)
            if isinstance(self.options[0], ClExperimentalMenuTab):
                if self.selected_option > 0:
                    self.options[self.selected_option-1].upd(right_selected=False)
                if self.selected_option < len(self.options)-1:
                    self.options[self.selected_option+1].upd(left_selected=False)
                if clicked_index > 0:
                    self.options[clicked_index-1].upd(right_selected=True)
                if clicked_index < len(self.options)-1:
                    self.options[clicked_index+1].upd(left_selected=True)
                self.left_margin.bgcolor = self.theme.background_one if not self.options[0].selected else self.theme.background_two
                self.right_margin.bgcolor = self.theme.background_one if not self.options[-1].selected else self.theme.background_two
            print(f"old selected: {self.selected_option}")
            self.selected_option = clicked_index
            print(f"new selected: {self.selected_option}")
            self.update()
            # openning submenu of clicked option
            # ...
        # mapping the custom action of the clicked option and redirecting it to the user
        clicked_action = self.options_map[e.control.data][1]
        if clicked_action is not None:
            clicked_action(e)
        
# filter bar (ok)
class ClFilterBar(ft.UserControl):
    """Represents a container bar for filters to be used in Flet Apps."""
    def __init__(self, theme:ClTheme, filters:list[ClFilterButton|ClCrystalFilterButton], selected_filters:list[int]=[], 
                 bar_size:int=40, expand:bool|int=False, transparent:bool=False, with_blur:bool=False):
        """Use this properties to personalize the submenu:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - filters: is a list of ```calet_button.ClFilterButton``` or ```calet_button.OutlineFilterButton``` objects where each object will represent a different filter in the filter bar. All objects in the list must be of the same class.
        - selected_filters: is a list with the index of each default selected filter in the filter bar.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the filter bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the bar must be displayed transparent or colored.
        - with_blur: is a flag saying if the bar must be displayed with blur effect or not.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        if not isinstance(filters, list):
            raise ClError(
                error="Argument Error: <<filters>> must be a list."
            )
        else:
            if not filters:
                raise ClError(
                    error="Argument Error: <<filters>> must be a list with at least one filter."
                )
            for i in range(len(filters)):
                if not isinstance(filters[i], (ClFilterButton, ClCrystalFilterButton)):
                    raise ClError(
                        error=f"""Argument Error: <<filters[{i}]>> must be an instance of 'calet_bar.ClFilterButton' or 
                            'calet_bar.ClCrystalFilterButton' class."""
                    )
                if isinstance(filters[0], ClFilterButton) and not isinstance(filters[i], ClFilterButton):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClFilterButton' class
                            because the first one is it."""
                    )
                elif isinstance(filters[0], ClCrystalFilterButton) and not isinstance(filters[i], ClCrystalFilterButton):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.OutlineFilterButton' class
                            because the first one is it."""
                    )
                filters[i].selected = False
        if not isinstance(selected_filters, list):
            raise ClError(
                error="Argument Error: <<selected_filters>> must be a list."
            )
        else:
            for i in range(len(selected_filters)):
                if not isinstance(selected_filters[i], int):
                    raise ClError(
                        error=f"Argument Error: <<selected_filters[{i}]>> must be integer"
                    )
                if not 0 <= selected_filters[i] < len(filters):
                    raise ClError(
                        error=f"Argument Error: <<selected_filters[{i}]>> is out of the range of filters."
                    )
                filters[selected_filters[i]].selected = True
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.filters = filters
        self.selected_filters = selected_filters
        self.bar_size = bar_size
        self.transparent = transparent
        self.with_blur = with_blur
        self.expand = expand
    
    def build(self):

        # FILTERS BAR
        # - items
        self.items = ft.Container(
            alignment=ft.alignment.center_left,
            expand=True,
            content=ft.Row(
                spacing=5,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=self.filters
            )
        )
        # - bar
        self.bar = ft.Container(
            bgcolor=self.theme.background_one,
            border=ft.border.only(bottom=ft.BorderSide(1, self.theme.divider)),
            height=self.bar_size if not self.expand else None,
            alignment=ft.alignment.center,
            padding=5,
            content=self.items
        )
        
        return self.bar
    
    def get_selected_filters(self):
        return [self.filters[selected_filter] for selected_filter in self.selected_filters]

# lateral nav bar (ok)
class ClLateralNavBar(ft.UserControl):
    """Represents a lateral navigation bar to be used in Flet Apps directly or combined with another 
    ```calet_bar.ClLateralNavBar```."""
    def __init__(self, theme:ClTheme, options:list[ClNavButton|ClMarkTab], selected_option:int=-1, 
                 bar_size:int=80, separated:bool=False, expand:bool|int=False, transparent:bool=False, with_blur:bool=False,
                 actions:list[ClTextButton|ClButton|ClIconButton|ClModeButton|ClSwitch]=[], 
                 submenus:list=[]):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - options: is a list of ```calet_button.ClNavButton``` or ```calet_button.ClMarkTab``` objects where each object will represent a different option in the nav bar.
        - selected_option: is the index of the default selected option in the nav bar. Can be -1 to start with no selected option.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - separated: is a flag saying if the lateral bar must be displayed separated from the borders of his top and bottom neighbor components or not.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the submenu must be displayed transparent or colored.
        - with_blur: is a flag saying if the submenu must be displayed with blur effect or not.
        - actions: is a list of ```calet_button.ClTextButton```, ```calet_button.ClButton```, ```calet_button.ClIconButton```, ```calet_button.ClModeButton``` or ```calet_button.ClSwitch``` objects to be displayed as actions in the right side of the nav bar.
        - submenus: is a list of ```calet_bar.ClMenuBar``` or ```calet_bar.ClLateralNavBar``` objects or None where each not None object will be displayed as the submenu of a different option in the menu bar. If it's given, must have the same length of ```options``` list. 
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(selected_option, int):
            raise ClError(
                error="Argument Error: <<selected_option>> must be boolean."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(separated, bool):
            raise ClError(
                error="Argument Error: <<separated>> must be boolean."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        options_map = {}
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list."
            )
        else:
            if not options:
                raise ClError(
                    error="Argument Error: <<options>> must be a list with at least one option."
                )
            if not -1 <= selected_option < len(options):
                raise ClError(
                    error="Argument Error: <<selected_option>> is out of the range of possible options."
                )
            for i in range(len(options)):
                if not isinstance(options[i], (ClNavButton, ClMarkTab)):
                    raise ClError(
                        error=f"""Argument Error: <<options[{i}]>> must be an instance of 'calet_bar.ClNavButton' or 'calet_bar.ClMarkTab' class."""
                    )
                if isinstance(options[0], ClNavButton) and not isinstance(options[i], ClNavButton):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClNavButton' class
                            because the first one is it."""
                    )
                elif isinstance(options[0], ClMarkTab) and not isinstance(options[i], ClMarkTab):
                    raise ClError(
                        error=f"""Argument Error: Every object in the list must be an instance of 'calet_bar.ClMarkTab' class
                            because the first one is it."""
                        )
                if isinstance(options[i], ClMarkTab) and options[i].mark_side not in ("left", "right"):
                    options[i].mark_side = "left"
                options[i].selected = True if i == selected_option else False
                options_map[options[i]] = i, options[i].action
                options[i].action = self.option_clicked
        if not isinstance(actions, list):
            raise ClError(
                error="Argument Error: <<actions>> must be a list."
            )
        else:
            for i in range(len(actions)):
                if not isinstance(actions[i], (ClTextButton, ClButton, ClIconButton, ClModeButton, ClSwitch)):
                    raise ClError(
                        error=f"""Argument Error: <<actions[{i}]>> must be an instance of 'calet_button.ClTextButton', 
                            'calet_button.ClButton', 'calet_button.ClIconButton', 'calet_button.ClModeButton' or 
                            'calet_button.ClSwitch' class."""
                    )
        submenus_maxsize = []
        if not isinstance(submenus, list):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list."
            )
        elif submenus and len(submenus) < len(options):
            raise ClError(
                error="Argument Error: <<submenus>> must be a list with the same lenght of 'options' list."
            )
        else:
            for i in range(len(submenus)):
                if submenus[i] is None:
                    submenus[i] = ft.Container(width=0)
                elif not isinstance(submenus[i], (ClMenuBar, ClLateralNavBar)):
                    raise ClError(
                        error=f"Argument Error: <<submenus[{i}]>> must be an instance of 'calet_bar.ClMenuBar' or 'calet_bar.ClLateralNavBar' class or None."
                    )
                submenus_maxsize.append(submenus[i].bar_size if not isinstance(submenus[i], ft.Container) else 0)
                submenus[i].expand = 2 if expand else False
                submenus[i].visible = False if expand else True
                submenus[i].bar_size = 0 if not expand else None
                submenus[i].lateral = True
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.options = options
        self.selected_option = selected_option
        self.bar_size = bar_size
        self.separated = separated
        self.expand = expand
        self.transparent = transparent
        self.with_blur = with_blur
        self.actions = actions
        self.submenus = submenus
        self.options_map = options_map
        self.submenus_maxsize = submenus_maxsize
  
    def build(self):
        
        # NAV BAR
        # - bar top items
        self.top_items = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            content=ft.Column(
                spacing=10 if isinstance(self.options[0], ClNavButton) else 0,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=self.options
            )
        )
        # - bar bottom items
        if self.actions:
            self.bottom_items = ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=5,
                    controls=self.actions
                )
            )
        # - bar
        self.bar = ft.Container(
            expand=1 if self.expand else False,
            width=self.bar_size if not self.expand else None,
            bgcolor=self.theme.background_one,
            border=ft.border.only(right=ft.BorderSide(1,self.theme.divider)),
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=10, top=10, right=10, bottom=5) if isinstance(self.options[0], ClNavButton) else ft.padding.only(top=10, bottom=5),
            animate=ft.Animation(100, ft.AnimationCurve.EASE_OUT),
            content=ft.Column(
                spacing=0,
                controls=[self.top_items, self.bottom_items]
            ) if self.actions else self.top_items
        )

        # SUBMENUS
        if self.submenus:
            self.bar = ft.Container(
                data=self.expand,
                alignment=ft.alignment.center,
                content=ft.Row(
                    spacing=0,
                    controls=[self.bar]+self.submenus
                )
            )

        return self.bar if not self.separated else ft.Column(
            spacing=0,
            controls=[
                ft.Container(height=5, bgcolor=self.theme.background_one),
                ft.Row(expand=True, controls=[self.bar]),
                ft.Container(height=5, bgcolor=self.theme.background_one)
            ]
        )

    def option_clicked(self, e:ft.TapEvent):
        # mapping the index of the clicked option and updating selection
        clicked_index = self.options_map[e.control.data][0]
        # case 1: open a new menu
        if self.selected_option == -1:
            if self.submenus and isinstance(self.submenus[clicked_index], (ClMenuBar, ClLateralNavBar)):
                if self.expand:
                    self.expand = self.bar.data
                    self.submenus[clicked_index].visible = True
                else:
                    self.submenus[clicked_index].upd(bar_size=self.submenus_maxsize[clicked_index])
            self.selected_option = clicked_index
        # case 2: close the menu of an option
        elif self.selected_option == clicked_index:
            if self.submenus and isinstance (self.submenus[clicked_index], (ClMenuBar, ClLateralNavBar)):
                if self.expand:
                    self.expand = 1
                    self.submenus[clicked_index].visible = False
                else:
                    self.submenus[clicked_index].upd(bar_size=0)
            self.selected_option = -1
        # case 3: change to the menu of another option
        elif self.selected_option != clicked_index:
            if self.submenus:
                # case 3.1: both option have menus -> then change old menu for the new one
                if isinstance(self.submenus[self.selected_option], (ClMenuBar, ClLateralNavBar)) and isinstance(self.submenus[clicked_index], (ClMenuBar, ClLateralNavBar)):
                    if self.expand:
                        self.submenus[self.selected_option].visible = False
                        self.submenus[clicked_index].visible = True
                    else:
                        self.submenus[self.selected_option].upd(bar_size=0)
                        self.submenus[clicked_index].upd(bar_size=self.submenus_maxsize[clicked_index])
                # case 3.2: only the new option has menu -> then open a new men
                elif isinstance(self.submenus[clicked_index], (ClMenuBar, ClLateralNavBar)):
                    if self.expand:
                        self.expand = self.bar.data
                        self.submenus[clicked_index].visible = True
                    else:
                        self.submenus[clicked_index].upd(bar_size=self.submenus_maxsize[clicked_index])
                # case 3.3: only the old option has menu -> then close the old menu
                elif isinstance(self.submenus[self.selected_option], (ClMenuBar, ClLateralNavBar)):
                    if self.expand:
                        self.expand = 1
                        self.submenus[self.selected_option].visible = False
                    else:
                        self.submenus[self.selected_option].upd(bar_size=0)
            self.options[self.selected_option].upd(selected=False)
            self.selected_option = clicked_index
        self.update()
        # mapping the custom action of the clicked option and redirecting it to the user
        clicked_action = self.options_map[e.control.data][1]
        if clicked_action is not None:
            clicked_action(e)

    def upd(self, bar_size:int=None):

        if bar_size is not None and not self.expand:
            self.bar_size = bar_size
            self.bar.width = bar_size
        self.update()

# bottom nav bar
class ClBottomNavBar(ft.UserControl):
    """Represents a bottom app navigation bar to be used in Flet Apps."""
    def __init__(self, theme:ClTheme, options:list[ClNavButton], selected_option:int=0, 
                 bar_size:int=60, expand:bool|int=False, transparent:bool=False, with_blur:bool=False,
                 with_shadow=False):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - options: is a list of ```calet_button.ClNavTab``` or ```calet_button.ClSelectableTextButton``` objects where each object will represent a different option in the nav bar. All objects in the list must be of the same class.
        - selected_option: is the index of the default selected option in the nav bar.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the bar in his container. See ```expand``` Flet property for more information.
        - transparent: is a flag saying if the bar must be displayed transparent or colored.
        - with_blur: is a flag saying if the bar must be displayed with blur effect or not.
        - with_shadow: is a flag saying if the bar must be displayed with shadow or solid border.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(selected_option, int):
            raise ClError(
                error="Argument Error: <<selected_option>> must be boolean."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(transparent, bool):
            raise ClError(
                error="Argument Error: <<transparent>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        if not isinstance(with_shadow, bool):
            raise ClError(
                error="Argument Error: <<with_shadow>> must be boolean."
            )
        options_map = {}
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list."
            )
        else:
            if not options:
                raise ClError(
                    error="Argument Error: <<options>> must be a list with at least one option."
                )
            if not -1 <= selected_option < len(options):
                raise ClError(
                    error="Argument Error: <<selected_option>> is out of the range of possible options."
                )
            for i in range(len(options)):
                if not isinstance(options[i], ClNavButton):
                    raise ClError(
                        error=f"""Argument Error: <<options[{i}]>> must be an instance of 'calet_bar.ClNavButton' class."""
                    )
                options[i].selected = True if i == selected_option else False
                options_map[options[i]] = i, options[i].action
                options[i].action = self.option_clicked
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.options = options
        self.selected_option = selected_option
        self.bar_size = bar_size
        self.expand = expand
        self.transparent = transparent
        self.with_blur = with_blur
        self.with_shadow = with_shadow
        self.options_map = options_map
    
    def build(self):

        # NAV BAR
        # - bar items
        self.items = ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=self.options
        )
        # - bar
        self.bar = ft.Container(
            expand=self.expand,
            bgcolor=self.theme.background_one,
            alignment=ft.alignment.center,
            height=self.bar_size if not self.expand else None,
            border=ft.border.only(top=ft.BorderSide(1,self.theme.divider)) if not self.with_shadow else None,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=3,
                color="black",
                blur_style=ft.ShadowBlurStyle.OUTER,
                offset=ft.Offset(0,-1)
            ) if self.with_shadow else None,
            padding=5,
            content=self.items
        )

        return self.bar

    def option_clicked(self, e:ft.TapEvent):
        # mapping the index of the clicked option and updating selection
        clicked_index = self.options_map[e.control.data][0]
        if self.selected_option != clicked_index:
            self.options[self.selected_option].upd(selected=False)
            self.selected_option = clicked_index
            self.update()
            # mapping the custom action of the clicked option and redirecting it to the user
            clicked_action = self.options_map[e.control.data][1]
            if clicked_action is not None:
                clicked_action(e)
        else:  # nothing change in the selections, but the calet selection buttons are always unselected on click, so need to be selected again
            self.options[self.selected_option].upd(selected=True)

# swap nav bar
class ClSwapNavBar(ft.UserControl):
    """Represents a navigation bar with swapping style to be used in Flet Apps."""
    def __init__(self, theme:ClTheme, options:list[ClSwapDestination], selected_option:int=0, 
                 bar_size:int=40, expand:bool|int=False, primary_color:bool=True, with_blur:bool=False):
        """Use this properties to personalize the bar:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the bar.
        - options: is a list of ```calet_button.ClSwapDestination```  objects where each object will represent a different option in the nav bar. All objects in the list must be of the same class.
        - selected_option: is the index of the default selected option in the nav bar.
        - bar_size: is the custom size of the bar. If ```expand``` is not None this property will be ignored.
        - expand: is the responsive expansion of the menu bar in his container. See ```expand``` Flet property for more information.
        - primary_color: is a flag saying if the option's selection mark must be painted with primary or non primary color.
        - with_blur: is a flag saying if the submenu must be displayed with blur effect or not.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' class."
            )
        if not isinstance(selected_option, int):
            raise ClError(
                error="Argument Error: <<selected_option>> must be boolean."
            )
        if not isinstance(bar_size, int):
            raise ClError(
                error="Argument Error: <<bar_size>> must be integer."
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be boolean or integer."
            )
        if not isinstance(primary_color, bool):
            raise ClError(
                error="Argument Error: <<primary_color>> must be boolean."
            )
        if not isinstance(with_blur, bool):
            raise ClError(
                error="Argument Error: <<with_blur>> must be boolean."
            )
        options_map = {}
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list."
            )
        else:
            if not options:
                raise ClError(
                    error="Argument Error: <<options>> must be a list with at least one option."
                )
            if not 0 <= selected_option < len(options):
                raise ClError(
                    error="Argument Error: <<selected_option>> is out of the range of options."
                )
            for i in range(len(options)):
                if not isinstance(options[i], (ClSwapDestination)):
                    raise ClError(
                        error=f"""Argument Error: <<options[{i}]>> must be an instance of 'calet_bar.ClSwapDestination' class."""
                    )
                # - expanding the options
                options[i].expand = 1
                # - selecting the default option
                options[i].selected = False if i != selected_option else True
                # - using the same 'for' cicle to extend action of each option in the list
                options_map[options[i]] = i, options[i].action
                options[i].action = self.option_clicked
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.options = options
        self.selected_option = selected_option
        self.bar_size = bar_size
        self.expand = expand
        self.primary_color = primary_color
        self.with_blur = with_blur
        self.options_map = options_map
    
    def build(self):

        # ITEMS
        # - items
        self.items = ft.Container(
            expand=True,
            bgcolor=self.theme.transparent_1,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=10,
            blur=5 if self.with_blur else None,
            content=ft.Row(
                spacing=0,
                controls=self.options
            )
        )
        # - items selection mark
        self.selection_mark = ft.Container(
            expand=1,
            bgcolor=self.theme.primary if self.primary_color else self.theme.transparent_5,
            alignment=ft.alignment.center,
            padding=5,
            margin=5,
            border_radius=5,
            offset=ft.Offset(self.selected_option,0),
            animate_offset=ft.Animation(duration=200, curve=ft.AnimationCurve.LINEAR_TO_EASE_OUT),
            content=ft.Text(
                value=self.options[self.selected_option].text,
                color=self.theme.font_four if self.primary_color else self.theme.primary,
                size=self.options[0].content_size,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            )
        )

        # - bar
        self.bar = ft.Stack(
            height=self.bar_size,
            controls=[
                self.items,
                ft.Row(
                    spacing=0,
                    controls=[self.selection_mark, ft.Row(expand=len(self.options)-1)]
                )
            ]
        )

        return self.bar
    
    def option_clicked(self, e:ft.TapEvent):
        # mapping the index of the clicked option and updating selection
        clicked_index = self.options_map[e.control.data][0]
        if self.selected_option != clicked_index: # else nothing change in the selections
            self.options[self.selected_option].upd(selected=False)
            self.selected_option = clicked_index
            self.selection_mark.content.value = self.options[clicked_index].text
            self.selection_mark.offset.x = clicked_index
            self.update()
        # mapping the custom action of the clicked option and redirecting it to the user
        clicked_action = self.options_map[e.control.data][1]
        if clicked_action is not None:
            clicked_action(e)
        
# floating menu bar

if __name__ == "__main__":


    def main(page: ft.Page):
        
        lg = ClLightTheme()
        dk = ClDarkTheme()
        theme = ClTheme(on_light=lg, on_dark=dk, mode="dark")

        app_bar = ClAppBar(
            # expand=1,
            theme=theme,
            title="App Bar",
            left_title=True,
            title_icon=ft.icons.PEOPLE,
            left_icon=ft.icons.SETTINGS,
            content_size=15,
            defined_sections=True,
            # scrollable_sections="both",
            left_actions=[
                ClTextButton(theme=theme, text="Boton 1", content_size=14),
                ClTextButton(theme=theme, text="Boton 2", content_size=14),
                ClTextButton(theme=theme, text="Boton 3", content_size=14),
                ClTextButton(theme=theme, text="Boton 4", content_size=14),
                # ClTextButton(theme=theme, text="Boton 5", content_size=14),
                # ClTextButton(theme=theme, text="Boton 6", content_size=14),
                # ClTextButton(theme=theme, text="Boton 7", content_size=14),
                # ClTextButton(theme=theme, text="Boton 8", content_size=14),
                ClMenuButton(
                    theme=theme,
                    options=[
                        ClOptionButton(
                            theme=theme,
                            text="Option 1"
                        ),
                        ClOptionButton(
                            theme=theme,
                            text="Option 2"
                        )
                    ]
                )
            ],
            right_actions=[
                ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                # ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                # ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                # ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                # ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
                # ClIconButton(theme=theme, icon=ft.icons.PERSON, content_size=14),
            ],
            win_actions=[
                ClWinButton(
                    theme=theme,
                    winaction="minimize"
                ),
                ClWinButton(
                    theme=theme,
                    winaction="maximize"
                ),
                ClWinButton(
                    theme=theme
                )
            ]
        )

        nav_bar = ClNavBar(
            # expand=3,
            theme=theme,
            options=[
                ClNavTab(
                    theme=theme,
                    text="Tab 1",
                ),
                ClNavTab(
                    theme=theme,
                    text="Tab 2",
                )
            ],
            actions=[
                ClIconButton(
                    theme=theme,
                    icon=ft.icons.SEARCH
                ),
                ClIconButton(
                    theme=theme,
                    icon=ft.icons.OPEN_IN_BROWSER
                )
            ],
            submenus=[
                ClMenuBar(
                    theme=theme,
                    defined=True,
                    sections=[
                        ClMenuSection(
                            theme=theme,
                            defined=True,
                            actions=[
                                [
                                    ClTextButton(theme=theme, text="Btn 1.1.1", content_size=14),
                                    ClMenuButton(
                                        theme=theme,
                                        main_button=ClTextButton(theme=theme, text="Btn 1.1.2", content_size=14),
                                        content_size=14,
                                        options=[
                                            ClOptionButton(
                                                theme=theme,
                                                text="Option 1"
                                            ),
                                            ClOptionButton(
                                                theme=theme,
                                                text="Option 2",
                                                sub_options=[
                                                    ClOptionButton(
                                                        theme=theme,
                                                        text="Option 3",
                                                    ),
                                                    ClOptionButton(
                                                        theme=theme,
                                                        text="Option 4",
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ],
                                [
                                    ClTextButton(theme=theme, text="Btn 1.1.3", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 1.1.4", content_size=14)
                                ]
                            ]
                        ),
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [
                                    ClTextButton(theme=theme, text="Btn 1.2.1", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 1.2.2", content_size=14),
                                ],
                                [
                                    ClTextButton(theme=theme, text="Btn 1.2.3", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 1.2.4", content_size=14),
                                ]
                            ]
                        )
                    ]
                ),
                ClMenuBar(
                    theme=theme,
                    defined=True,
                    sections=[
                        ClMenuSection(
                            theme=theme,
                            defined=True,
                            actions=[
                                [
                                    ClTextButton(theme=theme, text="Btn 2.1.1", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 2.1.2", content_size=14)
                                ],
                                [
                                    ClTextButton(theme=theme, text="Btn 2.1.3", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 2.1.4", content_size=14)
                                ]
                            ]
                        ),
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [
                                    ClTextButton(theme=theme, text="Btn 2.2.1", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 2.2.2", content_size=14),
                                ],
                                [
                                    ClTextButton(theme=theme, text="Btn 2.2.3", content_size=14),
                                    ClTextButton(theme=theme, text="Btn 2.2.4", content_size=14),
                                ]
                            ]
                        )
                    ]
                )
            ]
        )

        filter_bar = ClFilterBar(
            # expand=1,
            theme=theme,
            filters=[
                ClCrystalFilterButton(
                    theme=theme,
                    text="Filter 1",
                    content_size=14,
                    content_padding=10,
                    rounded=False
                ),
                ClCrystalFilterButton(
                    theme=theme,
                    text="Filter 2",
                    content_size=14,
                    content_padding=10,
                    rounded=False
                ),
                ClCrystalFilterButton(
                    theme=theme,
                    text="Filter 3",
                    content_size=14,
                    content_padding=10,
                    rounded=False
                )
            ]
        )

        latnav_bar = ClLateralNavBar(
            theme=theme,
            options=[
                ClNavButton(
                    theme=theme,
                    label="NavBtn 1",
                    icon=ft.icons.LOCAL_BAR_OUTLINED,
                    selected_icon=ft.icons.LOCAL_BAR,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="NavBtn 2",
                    icon=ft.icons.LOCAL_CAFE_OUTLINED,
                    selected_icon=ft.icons.LOCAL_CAFE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="NavBtn 3",
                    icon=ft.icons.LOCAL_PIZZA_OUTLINED,
                    selected_icon=ft.icons.LOCAL_PIZZA,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                )
            ],
            actions=[
                ClIconButton(
                    theme=theme,
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS
                )
            ],
            submenus=[
                ClMenuBar(
                    theme=theme,
                    lateral=True,
                    sections=[
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Bar 1.1", content_size=14)],
                                [ClTextButton(theme=theme, text="Bar 1.2", content_size=14)]
                            ]
                        ),
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Jobs", content_size=14)],
                            ]
                        )
                    ]
                ),
                ClMenuBar(
                    theme=theme,
                    lateral=True,
                    sections=[
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Coffee 1.1", content_size=14)],
                                [ClTextButton(theme=theme, text="Coffee 1.2", content_size=14)]
                            ]
                        ),
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Jobs", content_size=14)],
                            ]
                        )
                    ]
                ),
                ClMenuBar(
                    theme=theme,
                    lateral=True,
                    sections=[
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Pizza 1.1", content_size=14)],
                                [ClTextButton(theme=theme, text="Pizza 1.2", content_size=14)]
                            ]
                        ),
                        ClMenuSection(
                            theme=theme,
                            actions=[
                                [ClTextButton(theme=theme, text="Jobs", content_size=14)],
                            ]
                        )
                    ]
                )
            ]
        )

        latnav_bar2 = ClLateralNavBar(
            theme=theme,
            separated=True,
            options=[
                ClNavButton(
                    theme=theme,
                    label="NavBtn 1",
                    icon=ft.icons.LOCAL_BAR_OUTLINED,
                    selected_icon=ft.icons.LOCAL_BAR,
                    # rounded=False,
                    all_as_button=True
                ),
                ClNavButton(
                    theme=theme,
                    label="NavBtn 2",
                    icon=ft.icons.LOCAL_CAFE_OUTLINED,
                    selected_icon=ft.icons.LOCAL_CAFE,
                    # rounded=False,
                    all_as_button=True
                ),
                ClNavButton(
                    theme=theme,
                    label="NavBtn 3",
                    icon=ft.icons.LOCAL_PIZZA_OUTLINED,
                    selected_icon=ft.icons.LOCAL_PIZZA,
                    # rounded=False,
                    all_as_button=True
                )
            ],
            submenus=[
                ClLateralNavBar(
                    theme=theme,
                    bar_size=100,
                    options=[
                        ClMarkTab(
                            theme=theme,
                            text="Bar 1",
                            icon=ft.icons.LOCAL_BAR_OUTLINED,
                            hover_icon=ft.icons.LOCAL_BAR,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Bar 2",
                            icon=ft.icons.LOCAL_BAR_OUTLINED,
                            hover_icon=ft.icons.LOCAL_BAR,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Bar 3",
                            icon=ft.icons.LOCAL_BAR_OUTLINED,
                            hover_icon=ft.icons.LOCAL_BAR,
                            height=40
                        )
                    ]
                ),
                ClLateralNavBar(
                    theme=theme,
                    bar_size=100,
                    options=[
                        ClMarkTab(
                            theme=theme,
                            text="Cafe 1",
                            icon=ft.icons.LOCAL_CAFE_OUTLINED,
                            hover_icon=ft.icons.LOCAL_CAFE,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Cafe 2",
                            icon=ft.icons.LOCAL_CAFE_OUTLINED,
                            hover_icon=ft.icons.LOCAL_CAFE,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Cafe 3",
                            icon=ft.icons.LOCAL_CAFE_OUTLINED,
                            hover_icon=ft.icons.LOCAL_CAFE,
                            height=40
                        )
                    ]
                ),
                ClLateralNavBar(
                    theme=theme,
                    bar_size=100,
                    options=[
                        ClMarkTab(
                            theme=theme,
                            text="Pizza 1",
                            icon=ft.icons.LOCAL_PIZZA_OUTLINED,
                            hover_icon=ft.icons.LOCAL_PIZZA,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Pizza 2",
                            icon=ft.icons.LOCAL_PIZZA_OUTLINED,
                            hover_icon=ft.icons.LOCAL_PIZZA,
                            height=40
                        ),
                        ClMarkTab(
                            theme=theme,
                            text="Pizza 3",
                            icon=ft.icons.LOCAL_PIZZA_OUTLINED,
                            hover_icon=ft.icons.LOCAL_PIZZA,
                            height=40
                        )
                    ]
                )
            ]
        )

        swapnav_bar = ClSwapNavBar(
            expand=4,
            theme=theme,
            selected_option=1,
            options=[
                ClSwapDestination(
                    theme=theme,
                    text="Swap 1",
                    content_size=12,
                ),
                ClSwapDestination(
                    theme=theme,
                    text="Swap 2",
                    content_size=12,
                ),
                ClSwapDestination(
                    theme=theme,
                    text="Swap 3",
                    content_size=12,
                ),
            ]
        )

        botnav_bar = ClBottomNavBar(
            theme=theme,
            with_shadow=True,
            bar_size=70,
            options=[
                ClNavButton(
                    theme=theme,
                    label="BNavBtn 1",
                    icon=ft.icons.MUSIC_NOTE_OUTLINED,
                    selected_icon=ft.icons.MUSIC_NOTE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="BNavBtn 2",
                    icon=ft.icons.MUSIC_NOTE_OUTLINED,
                    selected_icon=ft.icons.MUSIC_NOTE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="BNavBtn 3",
                    icon=ft.icons.MUSIC_NOTE_OUTLINED,
                    selected_icon=ft.icons.MUSIC_NOTE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="BNavBtn 4",
                    icon=ft.icons.MUSIC_NOTE_OUTLINED,
                    selected_icon=ft.icons.MUSIC_NOTE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                ),
                ClNavButton(
                    theme=theme,
                    label="BNavBtn 5",
                    icon=ft.icons.MUSIC_NOTE_OUTLINED,
                    selected_icon=ft.icons.MUSIC_NOTE,
                    rounded=False,
                    # all_as_button=True,
                    width=60,
                    height=60
                )
            ]
        )

        page.padding = 0
        page.window_title_bar_hidden = True
        page.theme_mode = ft.ThemeMode.DARK

        page.add(
            ft.Container(
                expand=True,
                bgcolor=theme.background_one,
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        app_bar,
                        nav_bar,
                        ft.Row(
                            expand=True,
                            # expand=15,
                            spacing=0,
                            controls=[
                                # ft.Column(
                                #     spacing=0,
                                #     controls=[
                                #         ft.Container(height=5, bgcolor=theme.background_one),
                                #         ft.Row(expand=True, controls=[latnav_bar2]),
                                #         ft.Container(height=5, bgcolor=theme.background_one)
                                #     ]
                                # ),
                                latnav_bar2, 
                                ft.Column(
                                    expand=True,
                                    spacing=10,
                                    controls=[
                                        filter_bar,
                                        ft.Row(controls=[ft.Container(expand=3), swapnav_bar, ft.Container(expand=3)])
                                    ]
                                )
                            ]
                        ),
                        botnav_bar
                    ]
                )
            )
        )
    
    ft.app(target=main, assets_dir="src")