'''
    Main entry point for devbot.
'''
import logging
import os
import discord
import dotenv
from easy_logger import Logger

CLIENT = discord.Client()
#: The main discord client.
LOGGER = Logger().get_logger(__name__)
#: An Easy_logger instance.

@CLIENT.event
async def on_ready():
    ''' Log bot info. '''
    LOGGER.info('Bot logged is as: %s, with id: %s.',
            CLIENT.user.name, CLIENT.user.id)

def main():
    ''' Initialize the bot. '''
    # Load environment variables using dotenv.
    dotenv.load_dotenv('.env')

    # Connect to discord.
    CLIENT.run(os.environ['TOKEN'])

if __name__ == '__main__':
    main()
