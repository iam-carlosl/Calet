# Calet

**Calet** is a visual components mini library based on **Flet Framework** and made for personal uses in my Flet apps. It offers custom components combining Flet controls and giving them personalized aspects, behaviors and animations. Calet components are customizable too, but in a less advanced way than base Flet controls, making the specific apps code more clean and faster to write.

> **IMPORTANT**: All components in this library works only in Flet apps.

### Modules

Right now, it has only two types of visual components completely functional: **buttons** and **bars**. But there are more in the way.

The ```calet_button``` module includes:

- **ClTextButton**: Represents a text button.
- **ClOutlinedButton**: Represents an outlined button.
- **ClTonalButton**: Represents a tonal button.
- **ClButton**: Represents a primary button.
- **ClCrystalButton**: Represents a semitransparent button.
- **ClAcceptButton**: Represents an accept action button.
- **ClCancelButton**: Represents a cancel action button.
- **ClModeButton**: Represents a text button that alternate between two modes when is clicked.
- **ClSelectableTextButton**: Represents a text button that alternate between selected and not selected status when is clicked.
- **ClSelectableButton**: Represents a primary button that alternate between selected and not selected status when is clicked.
- **ClSelectableCrystalButton**: Represents a crystal button that alternate between selected and not selected status when is clicked.
- **ClFilterButton**: Represents a filter button to be used in ```calet_bar.FilterBar```.
- **ClCrystalFilterButton**: Represents a crystal filter button to be used in ```calet_bar.FilterBar```.
- **ClRemovableFilter**: Represents a filter button with a close button attached.
- **ClRemovableCrystalFilter**: Represents a crystal filter button with a close button attached.
- **ClSwapDestination**: Represents a special button to be used as a destination in a ```calet_bar.ClSwapNavBar```.
- **ClNavTab**: Represents a nav tab button to be used as an option in ```calet_bar.ClNavBar```.
- **ClMarkTab**: Represents a nav tab button with a selection indicator to be used as an option in ```calet_bar.ClNavBar``` or ```calet_bar.ClLateralNavBar```.
- **ClIconButton**: Represents an icon button.
- **ClNavButton**: Represents a navigation button to be used in ```calet_bar.ClLateralNavBar``` or ```calet_bar.ClBottomNavBar```.
- **ClWinButton**: Represents a window action button.
- **ClColorButton**: Represents a color selection button.
- **ClOptionButton**: Represents a menu option button to be used as an option of a ```calet_button.ClMenuButton``` menu.
- **ClMenuButton**: Represents a button that display a context menu when is clicked.
- **ClSwitch**: Represents a switch button.
- **ClRadio**: Represents a radio button.
- **ClCheck**: Represents a check button.

The ```calet_bar``` module includes:

- **ClAppBar**: Represents an app title bar.
- **ClMenuSection**: Represents a section of a menu bar to be used in ```calet_bar.ClMenuBar```.
- **ClMenuBar**: Represents a menu bar to be used directly or combined with ```calet_bar.ClNavBar``` or ```calet_bar.ClLateralNavBar```.
- **ClNavBar**: Represents a tabs navigation bar.
- **ClFilterBar**: Represents a container bar for filters.
- **ClLateralNavBar**: Represents a lateral navigation bar to be used in Flet Apps directly or combined with another ```calet_bar.ClLateralNavBar```.
- **ClBottomNavBar**: Represents a bottom app navigation bar.
- **ClSwapNavBar**: Represents a navigation bar with a focus swapping animation.

The ```calet_theme``` module includes:

- **ClLightTheme**: Is a light set of colors for a ```calet_theme.ClTheme```.
- **ClDarkTheme**: Is a dark set of colors for a ```calet_theme.ClTheme```.
- **ClTheme**: Is a colors theme to be used in Calet components.

> All Calet components need a ```calet_theme.ClTheme``` to be renderized. As a tip, you can build a parent control with the app theme as a property value and pass it trought all components builded after him to have the same colors pattern everywhere.

The ```calet_errors``` module includes:

- **ClError**: Is a custom exception rised when a Calet object receive incorrect parameters in his constructor.

------------

> See my repository [randomly](https://github.com/iam-carlosl/randomly) to have an example of a Flet app builded with Calet components.