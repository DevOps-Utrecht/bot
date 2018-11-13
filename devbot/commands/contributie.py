"""
An easy command that generates a bunq.me link
"""
from urllib.parse import quote
from devbot.registry import Command


@Command(["contributie", "contri", "money"])
async def generate_link(message_contents, *_args, **_kwargs) -> str:
    """
    Generates a contributie link.
    USAGE: !contributie <contributie message>
    """

    if message_contents:
        message = " ".join(message_contents)
        message = quote(message, safe="")
        url = f"https://bunq.me/devops/5,12/{message}"
        return url
    else:
        return "https://bunq.me/devops/5,12/Contributie"
