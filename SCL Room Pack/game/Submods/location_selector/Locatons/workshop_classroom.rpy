# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature ft The Workshop Spaceroom V1",
        description="A spaceroom variant customized as more of a workshop area for a busybody Monika with obviously too much time on her hands.",
        version="1.0.0"
    )

    #0 gifts is blank
#1-3 gifts gets you part 1
#4 gifts gets you part 2
#5+ gifts get you part 3
image WCmas_d25_gifts = ConditionSwitch(
    "len(persistent._mas_d25_gifts_given) == 0", "mod_assets/location/workshopclassroom/deco/d25/WC_gifts_0.png",
    "0 < len(persistent._mas_d25_gifts_given) < 3", "WC_gifts_1",
    "3 <= len(persistent._mas_d25_gifts_given) <= 4", "WC_gifts_2",
    "True", "WC_gifts_3"
)

image WC_gifts_1 = MASFilterSwitch(
    "mod_assets/location/workshopclassroom/deco/d25/gifts_1.png"
)

image WC_gifts_2 = MASFilterSwitch(
    "mod_assets/location/workshopclassroom/deco/d25/gifts_2.png"
)

image WC_gifts_3 = MASFilterSwitch(
    "mod_assets/location/workshopclassroom/deco/d25/gifts_3.png"
)

image WCmas_d25_lights = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(
        "persistent._mas_disable_animations", "mod_assets/location/workshopclassroom/deco/d25/WC_lights_on_1.png",
        "not persistent._mas_disable_animations", "WCmas_d25_night_lights_atl"
    ),
    "True", MASFilterSwitch("mod_assets/location/workshopclassroom/deco/d25/WC_lights_off.png")
)

image WCmas_d25_night_lights_atl:
    block:
        "mod_assets/location/workshopclassroom/deco/d25/WC_lights_on_1.png"
        0.5
        "mod_assets/location/workshopclassroom/deco/d25/WC_lights_on_2.png"
        0.5
        "mod_assets/location/workshopclassroom/deco/d25/WC_lights_on_3.png"
        0.5
    repeat
    
init 501 python:
    MASImageTagDecoDefinition.register_img(
        "mas_o31_vignette",
        submod_workshop_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=21) #21 to be in front of all cgs
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_gifts",
        submod_workshop_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=6),
        replace_tag="WCmas_d25_gifts"
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_lights",
        submod_workshop_spaceroom.background_id,
        MASAdvancedDecoFrame(zorder=5),
        replace_tag="WCmas_d25_lights"
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
image submod_ssworkshop-spaceroom-snow-ss = "mod_assets/location/workshopclassroom/workshop-spaceroom-ss-snow.png"

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