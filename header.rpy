# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="SATURNVENUS",
        name="Memories of Self Care and Literature",
        description="Metaverse Enterprise Solutions Analytics & Engagements Tools, Internal Use Only.) A submod adding content to every bit of MAS that you can add content to!",
        version="1.0.1",
        settings_pane=""
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Memories of Self Care and Literature",
            user_name="Barsonvenus",
            repository_name="Memories-of-Self-Care-and-Literature"
        )
