"""Miniframework de GUI 'Calet', basado en Flet
   - Módulo de temas"""

import flet as ft
from calet_errors import ClError

class ClLightTheme:
    """Represent a light set of colors to be used in Calet components
        """
    def __init__(self, transparent = None, 
            transparent_05 = None, transparent_1 = None, 
            transparent_3 = None, transparent_5 = None, transparent_8 = None,
            transparent_inverse = None,
            background_one = None, background_two = None, divider = None,
            font_one = None, font_two = None, font_three = None, font_four = None,
            primary = None, primary_block = None, primary_hovered = None,
            secondary = None, secondary_block = None,
            tonal = None, tonal_block = None,
            success = None, success_block = None, 
            accept = None, accept_hovered = None,
            error = None, error_block = None,
            cancel = None, cancel_hovered = None,
            warning = None, warning_block = None
        ):
        # white and black transparent colors
        self.transparent = "#00000000" if transparent is None else transparent
        self.transparent_05 = ft.colors.with_opacity(0.05, "black") if transparent_05 is None else transparent_05
        self.transparent_1 = ft.colors.with_opacity(0.1, "black") if transparent_1 is None else transparent_1
        self.transparent_3 = ft.colors.with_opacity(0.3, "black") if transparent_3 is None else transparent_3
        self.transparent_5 = ft.colors.with_opacity(0.5, "black") if transparent_5 is None else transparent_5
        self.transparent_8 = ft.colors.with_opacity(0.8, "black") if transparent_8 is None else transparent_8
        self.transparent_inverse = ft.colors.with_opacity(0.8, "white") if transparent_inverse is None else transparent_inverse 
        # basic colors
        self.background_one = "#006EBE" if background_one is None else background_one
        self.background_two = "#B4C8E6" if background_two is None else background_two
        self.divider = "grey100" if divider is None else divider
        self.font_one = "#363636" if font_one is None else font_one
        self.font_two = "#161616" if font_two is None else font_two
        self.font_three = "black" if font_three is None else font_three
        self.font_four = "white" if font_four is None else font_four
        # special text colors
        self.primary = "blue" if primary is None else primary
        self.primary_block = ft.colors.with_opacity(0.2, self.primary) if primary_block is None else primary_block
        self.primary_hovered = "blue300" if primary_hovered is None else primary_hovered
        self.secondary = "grey700" if secondary is None else secondary
        self.secondary_block = ft.colors.with_opacity(0.2, self.secondary) if secondary_block is None else secondary_block
        self.tonal = self.primary if tonal is None else tonal
        self.tonal_block = self.primary_block if tonal_block is None else tonal_block
        self.success = "green" if success is None else success
        self.success_block = ft.colors.with_opacity(0.2, self.success) if success_block is None else success_block
        self.accept = "green" if accept is None else accept
        self.accept_hovered = "green400" if accept_hovered is None else accept_hovered
        self.error = "red" if error is None else error
        self.error_block = ft.colors.with_opacity(0.2, self.error) if error_block is None else error_block
        self.warning = "yellow" if warning is None else warning
        self.warning_block = ft.colors.with_opacity(0.2, self.warning) if warning_block is None else warning_block
        self.cancel = "red" if cancel is None else cancel
        self.cancel_hovered = "red400" if cancel_hovered is None else cancel_hovered

class ClDarkTheme:
    """Represent a dark set of colors to be used in Calet components 
        """
    def __init__(self, transparent = None, 
            transparent_05 = None, transparent_1 = None, 
            transparent_3 = None, transparent_5 = None, transparent_8 = None,
            transparent_inverse = None,
            background_one = None, background_two = None, divider = None,
            font_one = None, font_two = None, font_three = None, font_four = None,
            primary = None, primary_block = None, primary_hovered = None,
            tonal = None, tonal_block = None,
            secondary = None, secondary_block = None,
            success = None, success_block = None, 
            accept = None, accept_hovered = None,
            error = None, error_block = None,
            cancel = None, cancel_hovered = None,
            warning = None, warning_block = None
        ):
        # white and black transparent colors
        self.transparent = "#00000000" if transparent is None else transparent
        self.transparent_05 = ft.colors.with_opacity(0.05, "white") if transparent_05 is None else transparent_05
        self.transparent_1 = ft.colors.with_opacity(0.1, "white") if transparent_1 is None else transparent_1
        self.transparent_3 = ft.colors.with_opacity(0.3, "white") if transparent_3 is None else transparent_3
        self.transparent_5 = ft.colors.with_opacity(0.5, "white") if transparent_5 is None else transparent_5
        self.transparent_8 = ft.colors.with_opacity(0.8, "white") if transparent_8 is None else transparent_8
        self.transparent_inverse = ft.colors.with_opacity(0.8, "black") if transparent_inverse is None else transparent_inverse 
        # general colors
        self.background_one = "#333333" if background_one is None else background_one
        self.background_two = "#404040" if background_two is None else background_two
        self.divider = "grey700" if divider is None else divider
        self.font_one = "#A9A9A9" if font_one is None else font_one
        self.font_two = "#E9E9E9" if font_two is None else font_two
        self.font_three = "white" if font_three is None else font_three
        self.font_four = "black" if font_four is None else font_four
        # special colors
        self.primary = "blue" if primary is None else primary
        self.primary_block = ft.colors.with_opacity(0.2, self.primary) if primary_block is None else primary_block
        self.primary_hovered = "blue300" if primary_hovered is None else primary_hovered
        self.secondary = "grey" if secondary is None else secondary
        self.secondary_block = ft.colors.with_opacity(0.2, self.secondary) if secondary_block is None else secondary_block
        self.tonal = self.primary if tonal is None else tonal
        self.tonal_block = self.primary_block if tonal_block is None else tonal_block
        self.success = "green" if success is None else success
        self.success_block = ft.colors.with_opacity(0.2, self.success) if success_block is None else success_block
        self.accept = "green" if accept is None else accept
        self.accept_hovered = "green300" if accept_hovered is None else accept_hovered
        self.error = "red" if error is None else error
        self.error_block = ft.colors.with_opacity(0.2, self.error) if error_block is None else error_block
        self.cancel = "red" if cancel is None else cancel
        self.cancel_hovered = "red300" if cancel_hovered is None else cancel_hovered
        self.warning = "yellow" if warning is None else warning
        self.warning_block = ft.colors.with_opacity(0.2, self.warning) if warning_block is None else warning_block

class ClTheme:
    
    def __init__(self, on_light:ClLightTheme, on_dark:ClDarkTheme=None, mode='light'):
        """Is a colors theme to be used in all calet components.\n
        ---
        - on_light: is an instance of 'ClLightTheme' containing the colors set that will be used
                        when the ClTheme object is in 'light' mode.
        - on_dark: is an instance of 'ClDarkTheme' containing the colors set that will be used
                        when the ClTheme object is in 'dark' mode.
        - mode: is a string saying in which mode is the ClTheme. Can be 'light' for light mode
                or 'dark' for the dark mode. If no dark colors set is given,
                the light mode will be always shown, even if 'mode' value is 'dark'.
        """

        # validation block
        if not isinstance(on_light, ClLightTheme):
            raise ClError(
                error="Argument Error: <<on_light>> value must be an instance of 'ClLightTheme'"
            )
        if on_dark is not None:
            if not isinstance(on_dark, ClDarkTheme):
                raise ClError(
                    error="Argument Error: <<on_dark>> value must be an instance of 'ClDarkTheme'"
                )
        if mode not in ('light','dark'):
            raise ClError(
                error="Argument Error: <<mode>> value must be 'light' or 'dark'"
            )
        
        # initialization block
        self.on_light = on_light
        self.on_dark = on_dark
        self.mode = mode if self.on_dark is not None else "light"
        if self.mode == "light":
            self.to_light()
        else:
            self.to_dark()
        
    def to_light(self):
        self.mode = "light"
        # white and black transparent colors
        self.transparent = self.on_light.transparent
        self.transparent_05 = self.on_light.transparent_05
        self.transparent_1 = self.on_light.transparent_1
        self.transparent_3 = self.on_light.transparent_3
        self.transparent_5 = self.on_light.transparent_5
        self.transparent_8 = self.on_light.transparent_8
        self.transparent_inverse = self.on_light.transparent_inverse
        # general colors
        self.background_one = self.on_light.background_one
        self.background_two = self.on_light.background_two
        self.divider = self.on_light.divider
        self.font_one = self.on_light.font_one
        self.font_two = self.on_light.font_two
        self.font_three = self.on_light.font_three
        self.font_four = self.on_light.font_four
        # special colors
        self.primary = self.on_light.primary
        self.primary_block = self.on_light.primary_block
        self.primary_hovered = self.on_light.primary_hovered
        self.secondary = self.on_light.secondary
        self.secondary_block = self.on_light.secondary_block
        self.tonal = self.on_light.tonal
        self.tonal_block = self.on_light.tonal_block
        self.success = self.on_light.success
        self.success_block = self.on_light.success_block
        self.accept = self.on_light.accept
        self.accept_hovered = self.on_light.accept_hovered
        self.error = self.on_light.error
        self.error_block = self.on_light.error_block
        self.cancel = self.on_light.cancel
        self.cancel_hovered = self.on_light.cancel_hovered
        self.warning = self.on_light.warning
        self.warning_block = self.on_light.warning_block

    def to_dark(self):
        self.mode = "dark"
        # white and black transparent colors
        self.transparent = self.on_dark.transparent
        self.transparent_05 = self.on_dark.transparent_05
        self.transparent_1 = self.on_dark.transparent_1
        self.transparent_3 = self.on_dark.transparent_3
        self.transparent_5 = self.on_dark.transparent_5
        self.transparent_8 = self.on_dark.transparent_8
        self.transparent_inverse = self.on_dark.transparent_inverse
        # general colors
        self.background_one = self.on_dark.background_one
        self.background_two = self.on_dark.background_two
        self.divider = self.on_dark.divider
        self.font_one = self.on_dark.font_one
        self.font_two = self.on_dark.font_two
        self.font_three = self.on_dark.font_three
        self.font_four = self.on_dark.font_four
        # special colors
        self.primary = self.on_dark.primary
        self.primary_block = self.on_dark.primary_block
        self.primary_hovered = self.on_dark.primary_hovered
        self.secondary = self.on_dark.secondary
        self.secondary_block = self.on_dark.secondary_block
        self.tonal = self.on_dark.tonal
        self.tonal_block = self.on_dark.tonal_block
        self.success = self.on_dark.success
        self.success_block = self.on_dark.success_block
        self.accept = self.on_dark.accept
        self.accept_hovered = self.on_dark.accept_hovered
        self.error = self.on_dark.error
        self.error_block = self.on_dark.error_block
        self.cancel = self.on_dark.cancel
        self.cancel_hovered = self.on_dark.cancel_hovered
        self.warning = self.on_dark.warning
        self.warning_block = self.on_dark.warning_block
    
    def upd(self, on_light:ClLightTheme=None, on_dark:ClDarkTheme=None, mode:str=None):
        """Update the value of all given properties of this object.\n
        """
        if on_light is not None:
            if not isinstance(on_light, ClLightTheme):
                raise ClError(
                    error="Argument Error: <<on_light>> value must be an instance of 'ClLightTheme'"
                )
            self.on_light = on_light
            self.to_light()
        if on_dark is not None:
            if not isinstance(on_dark, ClDarkTheme):
                raise ClError(
                    error="Argument Error: <<on_dark>> value must be an instance of 'ClDarkTheme'"
                )
            self.on_dark = on_dark
            self.to_dark()
        if mode is not None:
            if mode not in ('light','dark'):
                raise ClError(
                    error="Argument Error: <<mode>> value must be 'light' or 'dark'"
                )
            self.mode = mode if self.on_dark is not None else "light"
            if self.mode == "light":
                self.to_light()
            else:
                self.to_dark()
