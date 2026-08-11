init -990 python in mas_submod_utils:
    h_submod = Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature",
        description="(Metaverse Enterprise Solutions Analytics & Engagements Tools, Internal Use Only.) A submod that adds an entire wealth of dialogue! Check out the github/wiki {a=https://github.com/Barsonvenus/Memories-of-Self-Care-and-Literature}{i}{u}here!{/u}{/i}{/a}",
        version="9.0.0",
        settings_pane="scl_settings_screen"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Memories of Self Care and Literature",
            user_name="Barsonvenus",
            repository_name="Memories-of-Self-Care-and-Literature",
            extraction_depth=2
        )

init -1 python:
    faketooltip = (
        "blank"
    )

#START: Settings pane
screen scl_settings_screen():
    $ submods_screen_tt = store.renpy.get_screen("submods", "screens").scope["tooltip"]
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000

        hbox:
            style_prefix "check"
            box_wrap False

            textbutton _("Chibika's Word of the Day: Counsel"):
                hovered SetField(submods_screen_tt, "value", faketooltip)
                unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)
            
            textbutton _("Chibika Status: Do Not Disturb"):
                hovered SetField(submods_screen_tt, "value", faketooltip)
                unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)
