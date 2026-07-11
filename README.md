# 16 Device Macros for MIDI Fighter Twister

This is a very simple mapping setup:

- The first page of the Twister is mapped to as many as 16 Macro knobs on the focused Ableton device
- No other pages on the Twister are mapped, they just send MIDI ccs and all buttons are toggled.
- The *CENTER* side buttons on the Twister switch banks, left is previous, right is next. The other 4 side buttons just send monentary cc control messages.

## Installation

1/ Unzip this mapping and copy the 'Twister_16_Macros' subfolder to your User library, this is typically located at:

* macOS: HD:/Users/[Username]/Library/Preferences/Ableton/Live x.x.x/User Remote Scripts
* Windows: C:\Users\[Username]\AppData\Roaming\Ableton\Live x.x.x\Preferences\User Remote Scripts

( _Note: These folders are hidden by default._ )

2/ In the MIDI Fighter Utility app, go to the File menu, select 'Import Settings', then browser to where you unzipped this mapping and select the file 'Twister_16_Macros.mfs'

_( Note: this will overwrite whatever configuration you had already on the Twister )_

## Credits

This mapping was created using the excellent web-based tool by Structure Void, aka Julien Bayle:

https://midiremotescripts.structure-void.com/generator/

If you want to make changes or additions to this script using Julien's tool, I have included the project file 'Twister_16_Macros.mmproj.json', which you should be able to load into the generator and add to. Always export a JSON file as you make changes! The generator is a nice, simple app but doesn't have advanced project management features.

Note: your broweser of choice ( Zen, Firefox, Chrome ) may ask for permission to use your midi hardware. At this time the generator will not work with Safari as it lacks Web MIDI support.

## Compatibility

This mapping should be compatible with both Ableton 11 and 12. I have only tested it with Ableton 12.
