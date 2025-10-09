import flet as ft
from calet.calet_buttons import *
from calet.calet_themes import Theme

class TextInput(ft.Container):
    """Represents a field for general kind of inputs"""
    def __init__(self, cltheme:Theme, default_value:str=None, label:str=None, placeholder:str=None, content_size:int=12, 
                 max_length:int=None, max_lines:int=None, min_lines:int=None, multiline:bool=False, allowed_characters:str="all", 
                 expand:bool|int=False, visible:bool=True, one_border:bool=False, margin:int=None):
        """Use this properties to personalize the aspect and behavior of the input:
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the input field.
        - default_value: is a text to display as default input in the field.
        - label: is a text label to display in the input area when the field is empty and blurred, otherwise in the input border.
        - placeholder: is a help text to display in the input area when the field is empty.
        - content_size: is a personalized size for the input, label and placeholder texts. 
        - max_lenght: is the max number of allowed characters for the input.
        - max_lines: is the max number of visible lines for the field.
        - min_lines: is the min number of visible lines for the field.
        - multiline: is a flag saying if the field allow multiple lines for the input.
        - allowed_characters: is the allowed type of text characters for the input. Can be 'all', 'alphanumeric', or 'numeric'.
        - expand: is the responsive expansion of the app bar in his container. See ```expand``` Flet property for more information.
        - visible: is a flag saying if the field is visible or not.
        - one_border: is a flag saying if the field must be displayed with only one bottom border or all borders.
        """
        super().__init__()
        self.cltheme = cltheme
        self.default_value = default_value
        self.label = label
        self.placeholder = placeholder
        self.content_size = content_size
        self.max_length = max_length
        self.max_lines = max_lines
        self.min_lines = min_lines
        self.multiline = multiline
        self.allowed_characters = allowed_characters
        self.allowed_characters_code = {"all": ".", "alphanumeric": "\w", "numeric": "\d"}[allowed_characters]
        self.expand = expand
        self.visible = visible
        self.one_border = one_border
        self.margin = margin

        # FORM
        # - field
        self.field = ft.TextField(
            value=self.default_value,
            text_size=self.content_size,
            label=self.label if not one_border else None,
            label_style=ft.TextStyle(
                color=self.cltheme.font_one,
                size=self.content_size,
            ),
            hint_text=self.placeholder,
            hint_style=ft.TextStyle(
                color=self.cltheme.font_one,
                size=self.content_size,
            ),
            suffix_text=f"0/{self.max_length}" if self.max_length else None,
            suffix_style=ft.TextStyle(
                color=self.cltheme.font_one,
                size=self.content_size
            ),
            error_style=ft.TextStyle(
                color=self.cltheme.error,
                size=self.content_size
            ),
            content_padding=10,
            border=ft.InputBorder.OUTLINE,
            border_radius=5,
            border_width=1,
            focused_border_width=2,
            border_color=self.cltheme.transparent,
            focused_border_color=self.cltheme.primary if not one_border else self.cltheme.transparent,
            color=self.cltheme.font_one,
            focused_color=self.cltheme.font_two,
            bgcolor=self.cltheme.transparent_1,
            focused_bgcolor=self.cltheme.transparent_inverse_4,
            cursor_color=self.cltheme.font_two,
            selection_color=self.cltheme.primary_block,
            text_align=ft.TextAlign.LEFT,
            max_lines=self.max_lines,
            min_lines=self.min_lines,
            multiline=self.multiline,
            input_filter=ft.InputFilter(regex_string=str("^"+f"{self.allowed_characters_code}"+"{0,"+f"{self.max_length}"+"}$")) if max_length else None,
            on_focus=self.tf_focused,
            on_blur=self.tf_blurred,
            on_change=self.tf_changed
        )
        # - field container
        self.field_container = ft.Container(
            border_radius=5 if one_border else None,
            height=40 if not min_lines else None,
            bgcolor=cltheme.transparent,
            border=ft.border.only(bottom=ft.BorderSide(width=2, color=cltheme.font_one)) if one_border else None,
            content=self.field
        )
        # - error container
        self.error_container = ft.Container(
            bgcolor=self.cltheme.error_block, 
            border_radius=5, 
            padding=ft.padding.only(left=5, top=2, right=5, bottom=2), 
            alignment=ft.alignment.center_left, 
            visible=False,
            content=ft.Text(value="", color=self.cltheme.error)
        )

        self.content = ft.Column(spacing=5, controls=[self.field_container, self.error_container])

    # HANDLERS
    def tf_focused(self, e:ft.ControlEvent):
        self.error_container.visible = False
        self.field.label_style.color = self.cltheme.primary
        if self.one_border:
            self.field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.primary))
        self.update()
    
    def tf_blurred(self, e:ft.ControlEvent):
        self.field.label_style.color = self.cltheme.primary if self.field.value else self.cltheme.font_one
        if self.one_border:
            self.field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()
    
    def tf_changed(self, e:ft.ControlEvent):
        if self.max_length:
            self.field.suffix_text = f"{len(self.field.value)}/{self.max_length}"
            self.update()

    def error(self, error_text:str=""):
        if error_text:
            self.error_container.content.value = error_text
            self.error_container.visible = True
        if self.one_border:
            self.field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.error))
        self.update()
    
    def not_error(self):
        self.error_container.visible = False
        if self.one_border:
            self.field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()

class SelectionInput(ft.Container):
    
    def __init__(self, cltheme:Theme, options:list[tuple]=[], label:str=None, content_size:int=12,
                 placeholder:str=None, expand:bool|int=False, change_action=None, default_value:str=None,
                 one_border:bool=False, margin:int=None):
        
        super().__init__()
        self.cltheme = cltheme
        self.expand = expand
        self.options = options
        self.default_value = default_value
        self.label = label
        self.placeholder = placeholder
        self.content_size = content_size
        self.one_border = one_border
        self.change_action = change_action
        self.border_radius = 5 if one_border else None
        self.margin = margin
        self.bgcolor = cltheme.transparent
        self.border = ft.border.only(bottom=ft.BorderSide(width=2, color=cltheme.font_one)) if one_border else None

        # SELECTION FIELD
        # - dropdown
        self.selectionfield = ft.Dropdown(
            data=self,
            value=default_value if default_value is not None else 'none',
            text_size=content_size,
            label=self.label,
            label_style=ft.TextStyle(
                color=cltheme.font_three,
                size=content_size,
            ),
            hint_text=placeholder,
            hint_style=ft.TextStyle(
                color=cltheme.font_three,
                size=content_size,
            ),
            counter_style=ft.TextStyle(color=cltheme.font_one),
            content_padding=10,
            border=ft.InputBorder.OUTLINE,
            border_radius=5,
            border_width=1,
            focused_border_width=2,
            border_color=self.cltheme.transparent,
            focused_border_color=self.cltheme.primary if not one_border else self.cltheme.transparent,
            color=self.cltheme.font_one,
            focused_color=self.cltheme.font_two,
            bgcolor=self.cltheme.background_two,
            focused_bgcolor=self.cltheme.transparent_inverse_4,
            on_focus=self.tf_focused,
            on_blur=self.tf_blurred,
            on_change=self.change_action,
            options=[
                ft.dropdown.Option(
                    key=option[0], text=option[1]
                ) for option in self.options
            ] + [
                ft.dropdown.Option(
                    key="none", text="Ninguno"
                )
            ]
        )
        # - field container
        self.field_container = ft.Container(
            border_radius=5,
            height=40,
            bgcolor=cltheme.transparent,
            border=ft.border.only(bottom=ft.BorderSide(width=2, color=cltheme.font_one)) if one_border else None,
            content=self.selectionfield
        )
        # - error container
        self.error_container = ft.Container(
            bgcolor=self.cltheme.error_block, 
            border_radius=5, 
            padding=ft.padding.only(left=5, top=2, right=5, bottom=2), 
            alignment=ft.alignment.center_left, 
            visible=False,
            content=ft.Text(value="", color=self.cltheme.error)
        )

        self.content = ft.Column(spacing=5, controls=[self.field_container, self.error_container])

    # EVENT HANDLER METHODS
    def tf_focused(self, e:ft.ControlEvent):
        self.selectionfield.label_style.color = self.cltheme.primary
        if self.one_border:
            self.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.primary))
        self.update()
    
    def tf_blurred(self, e:ft.ControlEvent):
        self.selectionfield.label_style.color = self.cltheme.primary if self.selectionfield.value else self.cltheme.font_one
        if self.one_border:
            self.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()

    # SUPPORT METHODS
    def error(self, error_text:str=""):
        if error_text:
            self.error_container.content.value = error_text
            self.error_container.visible = True
        if self.one_border:
            self.selectionfield.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.error))
        self.update()
    
    def not_error(self):
        self.error_container.visible = False
        if self.one_border:
            self.selectionfield.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()

    def upd_options(self, new_options):
        self.options = new_options
        self.selectionfield.options = [
            ft.dropdown.Option(
                key=option, text=option
            ) for option in self.options
        ] + [
            ft.dropdown.Option(
                key="none", text="Ninguno"
            )
        ]
        self.selectionfield.value = 'none'
        self.update()

class TimeInput(ft.Container):
    """Represents a field for time inputs"""
    def __init__(self, cltheme:Theme, default_hour:str=None, default_min:str=None, with_label:bool=False, content_size:int=12, 
                 expand:bool|int=False, visible:bool=True, one_border:bool=False, margin:int=None):
        """Use this properties to personalize the aspect and behavior of the input:
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the input field.
        - default_hour: is a number to display as default input in the hour's field.
        - default_min: is a number to display as default input in the minute's field.
        - content_size: is a personalized size for the input, label and placeholder texts. 
        - expand: is the responsive expansion of the app bar in his container. See ```expand``` Flet property for more information.
        - visible: is a flag saying if the field is visible or not.
        - one_border: is a flag saying if the field must be displayed with only one bottom border or all borders.
        """
        super().__init__()
        self.cltheme = cltheme
        self.default_hour = default_hour
        self.default_min = default_min
        self.label_hour = "Hora"
        self.label_min = "Min"
        self.content_size = content_size
        self.expand = expand
        self.visible = visible
        self.one_border = one_border
        self.margin = margin

        # FORM
        # - hour's field
        self.hour_field = ft.TextField(
            value=self.default_hour,
            text_size=self.content_size,
            label=self.label_hour if not one_border else None,
            label_style=ft.TextStyle(
                color=self.cltheme.font_one,
                size=self.content_size,
            ),
            error_style=ft.TextStyle(
                color=self.cltheme.error,
                size=self.content_size
            ),
            content_padding=10,
            border=ft.InputBorder.OUTLINE,
            border_radius=5,
            border_width=1,
            focused_border_width=2,
            border_color=self.cltheme.transparent,
            focused_border_color=self.cltheme.primary if not one_border else self.cltheme.transparent,
            color=self.cltheme.font_one,
            focused_color=self.cltheme.font_two,
            bgcolor=self.cltheme.transparent_1,
            focused_bgcolor=self.cltheme.transparent_inverse_4,
            cursor_color=self.cltheme.font_two,
            selection_color=self.cltheme.primary_block,
            text_align=ft.TextAlign.LEFT,
            input_filter=ft.InputFilter(regex_string=r"^\d{0,2}$")
        )
        # - hour's field container
        self.hour_field_container = ft.Container(
            expand=True,
            border_radius=5 if one_border else None,
            height=40,
            bgcolor=cltheme.transparent,
            border=ft.border.only(bottom=ft.BorderSide(width=2, color=cltheme.font_one)) if one_border else None,
            content=self.hour_field
        )
        # - min's field
        self.min_field = ft.TextField(
            value=self.default_min,
            text_size=self.content_size,
            label=self.label_min if not one_border else None,
            label_style=ft.TextStyle(
                color=self.cltheme.font_one,
                size=self.content_size,
            ),
            error_style=ft.TextStyle(
                color=self.cltheme.error,
                size=self.content_size
            ),
            content_padding=10,
            border=ft.InputBorder.OUTLINE,
            border_radius=5,
            border_width=1,
            focused_border_width=2,
            border_color=self.cltheme.transparent,
            focused_border_color=self.cltheme.primary if not one_border else self.cltheme.transparent,
            color=self.cltheme.font_one,
            focused_color=self.cltheme.font_two,
            bgcolor=self.cltheme.transparent_1,
            focused_bgcolor=self.cltheme.transparent_inverse_4,
            cursor_color=self.cltheme.font_two,
            selection_color=self.cltheme.primary_block,
            text_align=ft.TextAlign.LEFT,
            input_filter=ft.InputFilter(regex_string=r"^\d{0,2}$"),
        )
        # - min's field container
        self.min_field_container = ft.Container(
            expand=True,
            border_radius=5 if one_border else None,
            height=40,
            bgcolor=cltheme.transparent,
            border=ft.border.only(bottom=ft.BorderSide(width=2, color=cltheme.font_one)) if one_border else None,
            content=self.min_field
        )
        # - error container
        self.error_container = ft.Container(
            bgcolor=self.cltheme.error_block, 
            border_radius=5, 
            padding=ft.padding.only(left=5, top=2, right=5, bottom=2), 
            alignment=ft.alignment.center_left, 
            visible=False,
            content=ft.Text(value="", color=self.cltheme.error)
        )

        self.content = ft.Column(spacing=5, controls=[
                ft.Row(expand=True, spacing=10, controls=[
                        self.hour_field_container,
                        ft.Text(value=" : ", color=cltheme.font_one, font_family="calibri", text_align=ft.TextAlign.CENTER),
                        self.min_field_container
                    ]
                ),
                self.error_container
            ]
        )
    
    # HANDLERS
    def tf_focused(self, e:ft.ControlEvent):
        self.error_container.visible = False
        self.hour_field.label_style.color = self.cltheme.primary
        self.min_field.label_style.color = self.cltheme.primary
        if self.one_border:
            self.hour_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.primary))
            self.min_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.primary))
        self.update()
    
    def tf_blurred(self, e:ft.ControlEvent):
        self.hour_field.label_style.color = self.cltheme.primary if self.hour_field.value else self.cltheme.font_one
        self.min_field.label_style.color = self.cltheme.primary if self.min_field.value else self.cltheme.font_one
        if self.one_border:
            self.hour_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
            self.min_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()

    def error(self, error_text:str=""):
        if error_text:
            self.error_container.content.value = error_text
            self.error_container.visible = True
        if self.one_border:
            self.hour_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.error))
            self.min_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.error))
        self.update()
    
    def not_error(self):
        self.error_container.visible = False
        if self.one_border:
            self.hour_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
            self.min_field_container.border = ft.border.only(bottom=ft.BorderSide(width=1, color=self.cltheme.font_one))
        self.update()