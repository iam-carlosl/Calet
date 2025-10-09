import flet as ft
from calet.calet_themes import Theme
from calet.calet_buttons import IconButton, FilledButton
from calet.calet_app import DialogsField
import time

class ActionDialog(ft.Container):

    def __init__(self, cltheme:Theme, icon:str, title:str, msg:str, dlg_field:DialogsField, confirm_text:str="OK", text_font:str=None,
                 confirm_action=None, data=None):
        super().__init__()
        self.cltheme = cltheme
        self.data = data
        self.expand = True
        self.bgcolor = self.cltheme.background_one
        self.border_radius = 15
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=5,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
        self.msg = msg
        self.dlg_field = dlg_field
        self.confirm_action = confirm_action

        # DIALOG HEADER
        # - dialog title
        self.dlg_title = ft.Text(
            expand=True,
            value=title,
            font_family=text_font,
            color=self.cltheme.font_three,
            size=24,
            text_align=ft.TextAlign.LEFT
        )
        # - dialog icon
        self.dlg_icon = ft.Icon(
            name=icon,
            color=self.cltheme.font_three,
            size=24
        )
        # - dialog close button
        self.b_close = IconButton(
            icon=ft.icons.CLOSE,
            cltheme=cltheme,
            action=lambda _: self.dlg_field.hide()
        )
        # - dialog header
        self.dlg_header = ft.Container(
            bgcolor=self.cltheme.transparent_05,
            padding=ft.padding.only(left=10, top=5, right=10),
            alignment=ft.alignment.center_left,
            content=ft.Row(
                spacing=5,
                controls=[self.dlg_icon, self.dlg_title, self.b_close]
            )
        )
        
        # DIALOG BODY
        # - dialog message
        self.dlg_msg = ft.Text(
            expand=True,
            value=msg,
            font_family=text_font,
            color=self.cltheme.font_two,
            text_align=ft.TextAlign.CENTER,
            size=18
        )
        # - dialog body
        self.dlg_body = ft.Container(
            bgcolor=self.cltheme.transparent_05,
            padding=20,
            alignment=ft.alignment.center,
            content=ft.Row(controls=[self.dlg_msg])
        )

        # DIALOG ACTIONS
        # - confirmation action
        self.b_confirm = FilledButton(
            data=self,
            cltheme=cltheme,
            expand=1,
            text=confirm_text,
            text_font=text_font,
            is_primary=True,
            action=self.b_confirm_clicked
        )
        # - actions container
        self.dlg_actions = ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=30, top=20, right=30, bottom=20),
            content=ft.Row(
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Container(expand=2), self.b_confirm, ft.Container(expand=2)]
            )
        )

        # DIALOG CONTENT
        self.content = ft.Column(
            spacing=0,
            controls=[
                self.dlg_header,
                self.dlg_body,
                self.dlg_actions
            ]
        )

    def b_confirm_clicked(self, e:ft.ControlEvent):
        self.dlg_field.hide()
        if self.confirm_action is not None:
            self.confirm_action(e)

class ConfirmationDialog(ActionDialog):
    
    def __init__(self, cltheme:Theme, icon:str, title:str, msg:str, dlg_field:DialogsField, confirm_text:str="Confirmar", 
                 cancel_text:str="Cancelar", text_font:str=None, confirm_action=None, cancel_action=None, data=None):
        super().__init__(
            cltheme=cltheme,
            icon=icon,
            title=title,
            msg=msg,
            dlg_field=dlg_field,
            confirm_text=confirm_text,
            text_font=text_font,
            confirm_action=confirm_action,
            data=data
        )
        self.cancel_text = cancel_text
        self.cancel_action = cancel_action

        # DIALOG TITLE
        # - dialog close button
        self.b_close.action = self.b_cancel_clicked

        # DIALOG EXTRA ACTIONS
        # - cancelation button
        self.b_cancel = FilledButton(
            cltheme=cltheme,
            expand=1,
            text=cancel_text,
            text_font=text_font,
            action=self.b_cancel_clicked
        )
        # - dialog actions
        self.dlg_actions.content.controls = [ft.Container(expand=1), self.b_confirm, self.b_cancel, ft.Container(expand=1)]
    
    def b_cancel_clicked(self, e:ft.ControlEvent):
        self.dlg_field.hide()
        if self.cancel_action is not None:
            self.cancel_action(e)

class ProgressDialog(ft.Container):

    def __init__(self, cltheme:Theme, progress_msg:str, dlg_field:DialogsField, text_font:str=None, end_action=None):
        super().__init__()
        self.cltheme = cltheme
        self.expand = True
        self.bgcolor = self.cltheme.background_one
        self.border_radius = 15
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=5,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
        self.msg = progress_msg
        self.dlg_field = dlg_field
        self.text_font = text_font
        self.end_action = end_action

        # DIALOG HEADER
        # - dialog title
        self.dlg_title = ft.Text(
            expand=True,
            value="Progreso",
            font_family=text_font,
            color=self.cltheme.font_three,
            size=24,
            text_align=ft.TextAlign.LEFT
        )
        # - dialog icon
        self.dlg_icon = ft.Icon(
            name=ft.icons.TIMELAPSE_ROUNDED,
            color=self.cltheme.font_three,
            size=24
        )
        # - dialog header
        self.dlg_header = ft.Container(
            padding=ft.padding.only(left=10, top=5, right=10),
            alignment=ft.alignment.center_left,
            content=ft.Row(
                spacing=5,
                controls=[self.dlg_icon, self.dlg_title]
            )
        )

        # DIALOG BODY
        # - dialog message
        self.dlg_msg = ft.Text(
            expand=True,
            value=progress_msg,
            font_family=text_font,
            color=self.cltheme.font_two,
            text_align=ft.TextAlign.CENTER,
            size=18
        )
        # - progress bar
        self.progress_bar = ft.ProgressBar(
            expand=True,
            value=0.0,
            color=cltheme.primary,
            bgcolor=cltheme.transparent_05,
            border_radius=5
        )
        # - dialog body
        self.dlg_body = ft.Container(
            padding=20,
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(controls=[self.dlg_msg]),
                    ft.Row(controls=[self.progress_bar]),
                ]
            )
        )

        # DIALOG CONTENT
        self.content = ft.Column(
            spacing=0,
            controls=[
                self.dlg_header,
                self.dlg_body
            ]
        )

    def upd_progress(self, new_value:float):
        self.progress_bar.value = new_value
        self.update()
        if new_value == 1.0:
            time.sleep(0.1)
            self.dlg_field.hide()
            if self.end_action is not None:
                self.end_action()

class InformationDialog(ft.Container):

    def __init__(self, cltheme:Theme, info_msg:str, dlg_field:DialogsField, info_type:str="success", text_font:str=None, end_action=None):
        super().__init__()
        self.cltheme = cltheme
        self.expand = True
        self.bgcolor = self.cltheme.background_one
        self.border_radius = 15
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=5,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
        self.msg = info_msg
        self.dlg_field = dlg_field
        self.text_font = text_font
        self.end_action = end_action

        # DIALOG BODY
        # - dialog icon
        self.dlg_icon = ft.Icon(
            name={
                "success": ft.icons.CHECK_CIRCLE_ROUNDED,
                "error": ft.icons.ERROR_ROUNDED
            }[info_type],
            color={
                "success": self.cltheme.success,
                "error": self.cltheme.error
            }[info_type],
            size=50
        )
        self.c_dlg_icon = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Container(
                padding=10,
                shape=ft.BoxShape.CIRCLE,
                bgcolor={
                    "success": self.cltheme.success_block,
                    "error": self.cltheme.error_block
                }[info_type],
                alignment=ft.alignment.center,
                # width=60,
                # height=60,
                scale=0,
                animate_scale=ft.Animation(duration=200, curve=ft.AnimationCurve.LINEAR),
                on_animation_end=self.c_icon_animated,
                content=self.dlg_icon
            )
        )
        # - dialog message
        self.dlg_msg = ft.Text(
            expand=True,
            value=info_msg,
            font_family=text_font,
            color=self.cltheme.font_two,
            text_align=ft.TextAlign.CENTER,
            size=18
        )
        # - dialog body
        self.dlg_body = ft.Container(
            padding=20,
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Row(controls=[self.c_dlg_icon]),
                    ft.Row(controls=[self.dlg_msg]),
                ]
            )
        )

        # DIALOG CONTENT
        self.content = ft.Column(
            spacing=0,
            controls=[
                self.dlg_body
            ]
        )

    def start_animation(self):
        self.c_dlg_icon.content.scale = 1.5
        self.update()

    def c_icon_animated(self, e:ft.ControlEvent):
        if self.c_dlg_icon.content.scale == 1.5:
            self.c_dlg_icon.content.scale = 1
        else:
            time.sleep(0.5)
            self.dlg_field.hide()
        self.update()