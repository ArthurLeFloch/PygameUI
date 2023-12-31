# PygameUI

This code was extracted and improved from [TowerDefenseV2](https://github.com/ArthurLeFloch/TowerDefenseV2), and can be install with the following command :
```bash
$ pip install pygame_ui_controls
```

## Presentation
This code allows to create these UI elements :
- Button
- ImageButton
- Slider
- CheckBox
- Text
- View (element behaving like a screen in a screen)

## Callbacks
These elements come with callbacks :
- Button : `on_click`
- ImageButton : `on_click`
- Slider : `on_value_changed` (takes value as argument)
- CheckBox : `on_check`, `on_uncheck`, `on_action` (check or uncheck)
- View : `on_screen_update`

## Notes
- Types might come in the future
- UI components are referenced by names (check [everything.py](examples/everything.py))
- More abstraction might come later, with less access to base functions and more top-level functions

## License
PygameUI is licensed under the [GPL v3.0 License](LICENSE).
