# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature ft The Sorta Witchy Spaceroom V1",
        description="A spaceroom variant taking cues from a earthier and more gothic lifestyle, this spaceroom is perfect for a Monika for a slightly darker outlook to life.",
        version="1.0.0"
    )

#Day images
image submod_daywitchy-spaceroom-day = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-day.png"
image submod_daywitchy-spaceroom-rain = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-rain.png"
image submod_daywitchy-spaceroom-overcast = "mmod_assets/location/sortawitchyclassroom/witchy-spaceroom-rain.png"
image submod_daywitchy-spaceroom-snow = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-day.png"

#Night images
image submod_nightwitchy-spaceroom-night = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-n.png"
image submod_nightwitchy-spaceroom-rain-night = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-n.png"
image submod_nightwitchy-spaceroom-overcast-night = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-n.png"
image submod_nightwitchy-spaceroom-snow-night = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-n.png"

#Sunset images
image submod_sswitchy-spaceroom-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-day.png"
    )
image submod_sswitchy-spaceroom-rain-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-rain.png"
    )
image submod_sswitchy-spaceroom-overcast-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-rain.png"
    )
image submod_sswitchy-spaceroom-snow-ss = "mod_assets/location/sortawitchyclassroom/witchy-spaceroom-ss.png"

image red_tree = "mod_assets/location/sortawitchyclassroom/redtree.png"
image blue_tree = "mod_assets/location/sortawitchyclassroom/bluetree.png"
image green_tree = "mod_assets/location/sortawitchyclassroom/greentree.png"
define redtree = False
define bluetree = False
define greentree = True

init -1 python: 
    submod_witchy_spaceroom = MASFilterableBackground(
        "submodwitchyclassroom",
        "SCL's Sorta Witchy Spaceroom",
        
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_daywitchy-spaceroom-day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_daywitchy-spaceroom-rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_daywitchy-spaceroom-overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_daywitchy-spaceroom-snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_nightwitchy-spaceroom-night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_nightwitchy-spaceroom-rain-night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_nightwitchy-spaceroom-overcast-night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_nightwitchy-spaceroom-snow-night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_sswitchy-spaceroom-ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_sswitchy-spaceroom-rain-ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_sswitchy-spaceroom-overcast-ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_sswitchy-spaceroom-snow-ss",
            }),
        ),
        
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),
        hide_calendar=False,
        unlocked=True,
        entry_pp=store.mas_background._witchy_spaceroom_entry,
        exit_pp=store.mas_background._witchy_spaceroom_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

init -2 python in mas_background:
    def _witchy_spaceroom_entry(_old, **kwargs):
        """
        Entry programming point for witchy_spaceroom background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("witchy_spaceroom_switch_dlg"):
                store.pushEvent("witchy_spaceroom_switch_dlg")

        store.monika_chr.tablechair.table = "SW"
        store.monika_chr.tablechair.chair = "SW"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

        store.mas_unlockEVL("scl_change_tree", "EVE") #tree toggle
        

    def _witchy_spaceroom_exit(_new, **kwargs):
        """
        Exit programming point for witchy_spaceroom background
        """
        #Lock islands greet to be sure -- and fire toggle
        store.mas_lockEVL("mas_monika_islands", "EVE")
        store.mas_lockEVL("scl_change_tree", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

###START: Topics
label witchy_spaceroom_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "My lovely tree is as glowing as ever!",
            "The windows are frosted up.. as they always are!",
            "It doesn't have to be halloween for me to give you a trick.. or a treat~",
        ]))
        
    if bluetree == True:
        show blue_tree zorder 6 
    if greentree == True:
        show green_tree zorder 6
    if redtree == True:
        show red_tree zorder 6
    m 1hua "[switch_quip]"


    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Whoof! That tree is far heavier than it should be.",
            "Miss the classic look?",
            "Brings back memories...",
        ]))

    m 1hua "[switch_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="scl_change_tree",
            category=["location"],
            prompt="About the tree's colour...",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.ENAMORED, None)
        ),
        restartBlacklist=True
    )

label scl_change_tree:
    m 1hua "Oh? Did we want to change it?"
    $ _history_list.pop()
    menu:
        "Blue, perhaps?":
            m 6hua "Ooh, a mystic, calming shade then!"
            hide red_tree
            hide green_tree
            show blue_tree zorder 6
            $ bluetree = True
            $ redtree = False
            $ greentree = False
        "Red, maybe?":
            m 6hua "Nice! The sharp colours of autumn it is."
            hide blue_tree
            hide green_tree
            show red_tree zorder 6
            $ bluetree = True
            $ redtree = False
            $ greentree = False
        "Default Green, please!":
            m "Okay! The crisp, refreshing shade of nature at it's finest."
            hide red_tree
            hide green_tree
            show green_tree zorder 6
            $ bluetree = True
            $ redtree = False
            $ greentree = False

        "Actually, I think it's fine as-is.":
            m 1eua "Sounds good to me!"

    return