"""
Updates the bot through the Github branch master
"""
import subprocess
from devbot.registry import Command


@Command(["update"])
async def update_bot(*_args, **_kwargs) -> str:
    """ Update the bot using GitHub. """
    exit_status = subprocess.call(['./scripts/update_bot.sh'])
    if exit_status == 0:
        return "Updated bot"
    return "Bot not updated"
