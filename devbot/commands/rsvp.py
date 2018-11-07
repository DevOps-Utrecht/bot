"""
Commands that allow users to create an event people can RSVP to
"""
import discord
import logging

from devbot.registry import Command

LOGGER = logging.getLogger(__name__)
CURRENT_EVENT = []


@Command("RSVP", category="Tools")
async def rsvp_event(
    message_contents, message, client, *_args, **_kwargs
) -> str or discord.Embed:
    """ Creates an event people can RSVP to. """
    if message_contents:
        description = " ".join(message_contents)
        everyone = [
            x
            for x in message.channel.server.members
            if not x.bot and not x == message.author
        ]
        event = Event(description, [message.author], everyone)
        CURRENT_EVENT.append(event)
        mesg = await client.send_message(message.channel, embed=event.to_embed())
        CURRENT_EVENT[0].set_message(mesg)
        await client.pin_message(mesg)
        return f"{message.author.name} created an event!\nRSVP with !present or !absent"
    else:
        return "Your event needs a name so that people know what to RSVP to.\nAlso include a date if relevant"


@Command(["present", "bij", "aanwezig"], category="Tools")
async def rsvp_present(_content, message, client, *_args, **_kwargs):
    CURRENT_EVENT[0].set_present(message.author)
    await client.edit_message(
        CURRENT_EVENT[0].message, embed=CURRENT_EVENT[0].to_embed()
    )


@Command(["absent", "nietbij", "afwezig"], category="Tools")
async def rsvp_absent(_content, message, client, *_args, **_kwargs):
    CURRENT_EVENT[0].set_absent(message.author)
    await client.edit_message(
        CURRENT_EVENT[0].message, embed=CURRENT_EVENT[0].to_embed()
    )

class Event(object):
    """ An RSVP Event. """

    def __init__(self, name, present, undecided):
        self.name = name
        self.present = present
        self.absent = []
        self.undecided = undecided

    def set_message(self, message):
        self.message = message

    def set_present(self, user):
        """ Changes a user's status to present. """
        if user in self.present:
            return
        if user in self.absent:
            self.absent.remove(user)
        if user in self.undecided:
            self.undecided.remove(user)
        self.present.append(user)

    def set_absent(self, user):
        """ Changes a user's status to absent. """
        if user in self.absent:
            return
        if user in self.present:
            self.present.remove(user)
        if user in self.undecided:
            self.undecided.remove(user)
        self.absent.append(user)

    def to_embed(self):
        """ Builds an RSVP embed. """
        result = discord.Embed()
        result.title = self.name
        if self.present:
            present = ", ".join([x.display_name for x in self.present])
            result.add_field(name="present", value=present)
        if self.absent:
            absent = ", ".join([x.display_name for x in self.absent])
            result.add_field(name="absent", value=absent)
        if self.undecided:
            undecided = ", ".join([x.display_name for x in self.undecided])
            result.add_field(name="limbo", value=undecided)
        return result
