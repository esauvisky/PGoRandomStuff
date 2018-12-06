TIPS AND TRICKS
===============

_These are not exclusively related to PokémonGo, but they certainly are useful._

## Avoiding exiting PokémonGo to go to Developer Options or elsewhere

### How to clear all data and cache from `adb`
_This also closes the app immediatly._
        $ adb shell pm clear com.nianticlabs.pokemongo

### How to enable Pointer Location from `adb`
- To enable:
        $ adb shell content insert --uri content://settings/system --bind name:s:pointer_location --bind value:i:1

    - _or (depending on your Android version, I guess):_
            $ adb shell settings put system pointer_location 1

- To disable
        $ adb shell content insert --uri content://settings/system --bind name:s:pointer_location --bind value:i:0

    - _or:_
            $ adb shell settings put system pointer_location 0

### How to set a different resolution or density (for slow phones)
**DEPRECATED**
_This is persistent. Don't forget to change it back!_

1. Get your current screen size:
        $ adb shell wm size
        Physical size: 1080x1920

2. Change it to something else. _Try to keep the same ratio! (9:16 in this example)_
        $ adb shell wm size 720x1280

3. Things are going to get weird. You can either reboot to fix them or just play with that and return back to the original resolution afterwards. The game will not change at all, as it's _no-dpi_.


**You can do the same for density, just replace `size` below with density and give it a try.**

### Getting your current (Last Known) location via adb
        $ adb shell dumpsys location | \grep 'Last Known Locations:' -A3 | tail -n1 | sed 's/..* \(-*[0-9.][0-9.]*,-*[0-9.][0-9.]*\) hAcc..*/\1/'


### Sending a map location intent to your spoofer
        $ adb shell am start -a android.intent.action.VIEW -n com.tnqbegkugmeb.erpcrlqlrub/com.tnqbegkugmeb.erpcrlqlrub.ui.main.MainActivity -d "geo:-32.535135,12.132313"

### How to turn off other's apps from running in the background (Android 7 and below)
_There's a new hidden permission called RUN_IN_BACKGROUND on Android 7 and below._

You can revoke the permission on any app, but only via a shell.

To get the current package's permission, run:
        $ adb shell cmd appops get <package_name> RUN_IN_BACKGROUND

To disallow the app to run on the background:
        $ adb shell cmd appops set <package_name> RUN_IN_BACKGROUND ignore

To allow it again:
        $ adb shell cmd appops set <package_name> RUN_IN_BACKGROUND allow

You can find <package_name> on your apps list, usually something like `com.spotify.music`.

### How to do everything at once:

- adb shell wm size 720x1280
- adb shell wm density 230
- adb shell input keyevent KEYCODE_POWER
- adb shell input keyevent KEYCODE_WAKEUP
- adb shell input keyevent KEYCODE_MENU
- adb shell su -c am restart
    OR
    - pkill -l TERM -f com.android.systemui
- Disables mobile data:
    svc data disable

### WIP
Query Wi-Fi (scanning always available) status

settings get global wifi_scan_always_enabled
Store output %Variable
Query currently enabled Location providers

settings get secure location_providers_allowed
Store output %Variable

set location proveiders https://goo.gl/Megic1
For Android 6.0

To Enable use :
For GPS : adb shell settings put secure location_providers_allowed +gps
For Network : adb shell settings put secure location_providers_allowed +network

To Disable :
GPS : adb shell settings put secure location_providers_allowed -gps
For Network : adb shell settings put secure location_providers_allowed -network


### Character Sorting Table
*This is the order in which PokémonGo displays your pokémon when sorting by name.*

- `꩜ ` (the special @, does not exist on Gboard)
- `%`
- `›` (alongside `'`)
- `“` (alongside `"`)
- `⁺` (superscript plus, does not exist on Gboard)
- `»` (alongside `"`)
- `÷`
- `≈` (alongside `=` )
- `·` (alongside `-`)
- `•`
- `♠` (alongside `•`)
- `♦` (alongside `•`)
- `♣` (alongside `•`)
- `♥` (alongside `•`)
- `✓`
- `∞` (alongside `=`)
- `℅` (alongside `%`)