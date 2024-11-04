# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature ft The Workshop Spaceroom V1",
        description="A spaceroom variant customized as more of a workshop area for a busybody Monika with obviously too much time on her hands.",
        version="1.0.0"
    )

#Day images
image submod_dayworkshop-spaceroom-day = "mod_assets/location/workshopclassroom/workshop-spaceroom.png"
image submod_dayworkshop-spaceroom-rain = "mod_assets/location/workshopclassroom/workshop-spaceroom-rain.png"
image submod_dayworkshop-spaceroom-overcast = "mod_assets/location/workshopclassroom/workshop-spaceroom-rain.png"
image submod_dayworkshop-spaceroom-snow = "mod_assets/location/workshopclassroom/workshop-spaceroom-snow.png"

#Night images
image submod_nightworkshop-spaceroom-night = "mod_assets/location/workshopclassroom/workshop-spaceroom-n.png"
image submod_nightworkshop-spaceroom-rain-night = "mod_assets/location/workshopclassroom/workshop-spaceroom-n.png"
image submod_nightworkshop-spaceroom-overcast-night = "mod_assets/location/workshopclassroom/workshop-spaceroom-n.png"
image submod_nightworkshop-spaceroom-snow-night = "mod_assets/location/workshopclassroom/workshop-spaceroom-snow-n.png"

#Sunset images
image submod_ssworkshop-spaceroom-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/workshopclassroom/workshop-spaceroom.png"
    )
image submod_ssworkshop-spaceroom-rain-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/workshopclassroom/workshop-spaceroom-rain.png"
    )
image submod_ssworkshop-spaceroom-overcast-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/workshopclassroom/workshop-spaceroom-rain.png"
    )
image submod_ssworkshop-spaceroom-snow-ss = "mod_assets/location/workshopclassroom/workshop-spaceroom-ss-snow"

init -1 python: 
    submod_workshop_spaceroom = MASFilterableBackground(
        "submodworkshopclassroom",
        "SCL's Workshop Spaceroom",
        
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_dayworkshop-spaceroom-day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_dayworkshop-spaceroom-rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_dayworkshop-spaceroom-overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_dayworkshop-spaceroom-snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_nightworkshop-spaceroom-night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_nightworkshop-spaceroom-rain-night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_nightworkshop-spaceroom-overcast-night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_nightworkshop-spaceroom-snow-night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_ssworkshop-spaceroom-ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_ssworkshop-spaceroom-rain-ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_ssworkshop-spaceroom-overcast-ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_ssworkshop-spaceroom-snow-ss",
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
        entry_pp=store.mas_background._Workshop_spaceroom_entry,
        exit_pp=store.mas_background._Workshop_spaceroom_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

init -2 python in mas_background:
    def _Workshop_spaceroom_entry(_old, **kwargs):
        """
        Entry programming point for Workshop_spaceroom background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("workshop_spaceroom_switch_dlg"):
                store.pushEvent("workshop_spaceroom_switch_dlg")

        store.monika_chr.tablechair.table = "workshop"
        store.monika_chr.tablechair.chair = "workshop"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _Workshop_spaceroom_exit(_new, **kwargs):
        """
        Exit programming point for Workshop_spaceroom background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

###START: Topics
label workshop_spaceroom_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Mind the mess, [player]!",
            "Lots of projects to work on today!",
            "I think the mismatched furniture gives it some extra charm, yeah?",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Wow, that was a lot of stuff to put away at once..",
            "Miss the classic look?",
            "Brings back memories...",
        ]))

    m 1hua "[switch_quip]"
    return

## remove the readme
init 0 python:
    store.mas_utils.trydel(renpy.config.basedir.replace('\\', '/') + "/readme.md")