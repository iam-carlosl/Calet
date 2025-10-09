# Calet

**Calet** is a visual components mini library based on **Flet Framework** and made for personal uses in my Flet apps. It offers custom components combining Flet controls and giving them personalized aspects, behaviors and animations. Calet components are customizable too, but in a less advanced way than base Flet controls, making the specific apps code more clean and faster to write.

> **IMPORTANT**: All components in this library works only in Calet apps.

### Modules

Right now, it has only two types of visual components completely functional: **buttons** and **bars**. But there are more in the way.

The ```calet_app``` module includes:

- **FloatingActionsField**: Represents a layout to display ```calet_buttons.CustomFloatingButton``` objects.
- **DialogsField**: Represents a layout to display dialogs.
- **CaletApp**: Represents an app template with generic calet layout and behaviors to be used as a base for Flet apps.
- **AppLoadScreen**: Represents a load screen with calet appereance, animations and behavior to be used in Flet apps.

The ```calet_overlays``` module includes:

- **ActionDialog**: Represents a dialog to notify normal actions information with an "OK" button.
- **ConfirmationDialog**: Represents a dialog to ask for actions confirmations with "Accept" and "Cancel" buttons.
- **ProgressDialog**: Represents a dialog to display a real time progress bar for an action wich will be automatically closed on finalization.
- **InformationDialog**: Represents a dialog to notify status information of actions, like success or error.

The ```calet_inputs``` module includes:

- **TextInput**: Represents a field for general kind of inputs.
- **SelectionInput**: Represents a field for selectable inputs from a list.
- **TimeInput**: Represents a field for time inputs.

The ```calet_buttons``` module includes:

- **Tooltip**: Represents a tooltip with calet appereance and behavior to be used in calet objects.
- **CaletButton**: Represents a template for all types of calet buttons.
- **IconButton**: Represents an icon button with calet appereance, animations and behavior to be used in Flet apps.
- **WinButton**: Represents a calet icon button with window actions appereance and behavior to be used in Flet apps.
- **ModesButton**: Represents a modes indicator icon button with calet appereance, animations and behavior to be used in Flet apps.
- **TextButton**: Represents a text button with calet appereance, animations and behavior to be used in Flet apps.
- **FilledButton**: Represents a filled text button with calet appereance, animations and behavior to be used in Flet apps.
- **SelectableButton**: Represents a selectable button with calet appereance, animations and behavior to be used in Flet apps.
- **TagButton**: Represents a calet text button to be used in Flet apps as an interactive tag.
- **TabButton**: Represents a calet text button with filter tab appereance and behavior to be used in Flet apps.
- **NavButton**: Represents a navigation button with calet appereance, animations and behavior to be used in Flet apps.
- **SwapNavButton**: Represents a navigation button with calet appereance, animations and behavior to be used in ```calet_bars.SwapNavBar```.
- **CustomFloatingButton**: Represents a Flet floating action button styled with calet appereance, animations and behavior to be used in Flet apps directly or combined with a ```calet_overlays.ClFloatingActionsField```.
- **PopupItemButtom**: Represents a Flet popup menu item styled with calet appereance, animations and behavior to be used in Flet apps combined with a ```calet_buttons.PopupMenuButton```.
- **PopupItemSelectableButton**: Represents a selectable Flet popup menu item styled with calet appereance, animations and behavior to be used in Flet apps combined with a ```calet_buttons.PopupMenuButton```.
- **PopupMenuButton**: Represents a Flet popup menu button styled with calet appereance, animations and behavior to be used in Flet apps.
- **SwitchButton**: Represents a switch button to be used in Flet apps.

The ```calet_bars``` module includes:

- **AppBar**: Represents an app title bar.
- **MenuBarSection**: Represents a section of a menu bar to be used in ```calet_bars.MenuBar```.
- **MenuBar**: Represents a menu bar to be used in Flet apps.
- **LateralNavBar**: Represents a lateral navigation bar to be used in Flet Apps.
- **GroupNavBar**: Represents a navigation bar with switch style to be used in Flet Apps.
- **SwapNavBar**: Represents a navigation bar with swapping style to be used in Flet Apps.

The ```calet_themes``` module includes:

- **LightTheme**: Represents a light set of colors fpr a ```calet_themes.Theme``` object.
- **DarkTheme**: Represents a dark set of colors for a ```calet_themes.Theme``` object.
- **Theme**: Represents a colors theme to be used in Calet components.

> All Calet components need a ```calet_theme.ClTheme``` to be renderized. As a tip, you can build a parent control with the app theme as a property value and pass it trought all components builded after him to have the same colors pattern everywhere.

The ```calet_utilities``` module includes:

- **AnimationEmulator**: Represents an invisible object to emulate other objects animations, usefull to build complex animations like combining oppacity and visible animations in a single one.
- **AnimationsEmulations**: Represents a layout to display ```AnimationEmulator``` objects.
- **Quote**: Represents a text quote to be used in Flet apps.

------------

> See my repository [randomly](https://github.com/iam-carlosl/randomly) to have an example of a Flet app builded with Calet components.