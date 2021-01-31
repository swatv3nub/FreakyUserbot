from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, load_module, remove_plugin


@Freaky.on(Freaky_on_cmd(pattern="load ?(.*)", outgoing=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Could not load {shortname} because of the following error.\n{str(e)}"
        )


@Freaky.on(Freaky_on_cmd(pattern="unload ?(.*)", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit(
            "Successfully unload {shortname}\n{}".format(shortname, str(e))
        )


CMD_HELP.update(
    {
        "load_unload": "**Load_Unload**\
\n\n**Syntax : **`.load <module name> .unload <module name>`\
\n**Usage :** If You Don't Want To Use A Specific Plugin Use This Plugin."
    }
)
