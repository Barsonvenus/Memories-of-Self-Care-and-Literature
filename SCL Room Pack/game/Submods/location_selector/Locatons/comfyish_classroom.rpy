# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature ft The Comfyish Spaceroom V1",
        description="A spaceroom variant that Monika has dressed up elegantly, and then slightly ruined by dedicating some space to dangerous reality-altering experiments.",
        version="1.1.0"
    )

    #0 gifts is blank
#1-3 gifts gets you part 1
#4 gifts gets you part 2
#5+ gifts get you part 3
image CCmas_d25_gifts = ConditionSwitch(
    "len(persistent._mas_d25_gifts_given) == 0", "mod_assets/location/comfyishclassroom/deco/d25/gifts_0.png",
    "0 < len(persistent._mas_d25_gifts_given) < 3", "CC_gifts_1",
    "3 <= len(persistent._mas_d25_gifts_given) <= 4", "CC_gifts_2",
    "True", "CC_gifts_3"
)

image CC_gifts_1 = MASFilterSwitch(
    "mod_assets/location/comfyishclassroom/deco/d25/gifts_1.png"
)

image CC_gifts_2 = MASFilterSwitch(
    "mod_assets/location/comfyishclassroom/deco/d25/gifts_2.png"
)

image CC_gifts_3 = MASFilterSwitch(
    "mod_assets/location/comfyishclassroom/deco/d25/gifts_3.png"
)

image CImas_d25_lights = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(
        "persistent._mas_disable_animations", "mod_assets/location/comfyish_spaceroom/deco/d25/lights_on_1.png",
        "not persistent._mas_disable_animations", "CImas_d25_night_lights_atl"
    ),
    "True", MASFilterSwitch("mod_assets/location/comfyish_spaceroom/deco/d25/lights_off.png")
)

image CImas_d25_night_lights_atl:
    block:
        "mod_assets/location/comfyish_spaceroom/deco/d25/lights_on_1.png"
        3.0
        "mod_assets/location/comfyish_spaceroom/deco/d25/lights_on_2.png"
        3.0
        "mod_assets/location/comfyish_spaceroom/deco/d25/lights_on_3.png"
        3.0
        repeat


init 501 python:
    MASImageTagDecoDefinition.register_img(
        "mas_o31_vignette",
        submod_comfyish_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=21) #21 to be in front of all cgs
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_gifts",
        submod_comfyish_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=6),
        replace_tag="CCmas_d25_gifts"
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_lights",
        submod_comfyish_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=5),
        replace_tag="CImas_d25_lights"
    )


#Day images
image submod_daycomfyish-spaceroom-day = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-day.png"
image submod_daycomfyish-spaceroom-rain = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-rain.png"
image submod_daycomfyish-spaceroom-overcast = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-rain.png"
image submod_daycomfyish-spaceroom-snow = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-snow.png"

#Night images
image submod_nightcomfyish-spaceroom-night = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-n.png"
image submod_nightcomfyish-spaceroom-rain-night = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-n.png"
image submod_nightcomfyish-spaceroom-overcast-night = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-n.png"
image submod_nightcomfyish-spaceroom-snow-night = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-snow-n.png"

#Sunset images
image submod_sscomfyish-spaceroom-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/comfyishclassroom/comfyish-spaceroom-day.png"
    )
image submod_sscomfyish-spaceroom-rain-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/comfyishclassroom/comfyish-spaceroom-rain.png"
    )
image submod_sscomfyish-spaceroom-overcast-ss = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/comfyishclassroom/comfyish-spaceroom-rain.png"
    )
image submod_sscomfyish-spaceroom-snow-ss = "mod_assets/location/comfyishclassroom/comfyish-spaceroom-ss-snow"

init -1 python: 
    submod_comfyish_spaceroom = MASFilterableBackground(
        "submodcomfyishclassroom",
        "SCL's Comfyish Spaceroom",
        
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_daycomfyish-spaceroom-day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_daycomfyish-spaceroom-rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_daycomfyish-spaceroom-overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_daycomfyish-spaceroom-snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_nightcomfyish-spaceroom-night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_nightcomfyish-spaceroom-rain-night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_nightcomfyish-spaceroom-overcast-night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_nightcomfyish-spaceroom-snow-night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_sscomfyish-spaceroom-ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_sscomfyish-spaceroom-rain-ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_sscomfyish-spaceroom-overcast-ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_sscomfyish-spaceroom-snow-ss",
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
        entry_pp=store.mas_background._comfyish_spaceroom_entry,
        exit_pp=store.mas_background._comfyish_spaceroom_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

init -2 python in mas_background:
    def _comfyish_spaceroom_entry(_old, **kwargs):
        """
        Entry programming point for comfyish_spaceroom background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("comfyish_spaceroom_switch_dlg"):
                store.pushEvent("comfyish_spaceroom_switch_dlg")

        store.monika_chr.tablechair.table = "CC"
        store.monika_chr.tablechair.chair = "CC"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _comfyish_spaceroom_exit(_new, **kwargs):
        """
        Exit programming point for comfyish_spaceroom background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

###START: Topics
label comfyish_spaceroom_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "I see my latest project is stable and non-explody! Non-explody's good.",
            "I'm fond of the blue velvet curtains, are you?",
            "Um, don't worry about what's happening outside the right window! It's just for show. Mostly.",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Hopefully that little experiment is fine being shoved in the closet...",
            "Miss the classic look?",
            "Brings back memories...",
        ]))

    m 1hua "[switch_quip]"
    return

## remove the readme
init 0 python:
    store.mas_utils.trydel(renpy.config.basedir.replace('\\', '/') + "/readme.md")
