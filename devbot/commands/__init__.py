'''
    Plugins folder to house all modular command files.
'''
from devbot.tools.logging import get_logger
import os.path
import importlib

LOGGER = get_logger(__name__)

def load_plugins():
    '''
        Import all python files in directory as plugins.
    '''
    root = os.path.dirname(__file__)
    LOGGER.info('Importing files from %s', root)

    for _root, _dirs, files in os.walk(root):
        pyfiles = [file for file in files if file.endswith('.py')]
        for plugin in pyfiles:
            pluginname = plugin[:-3] # Strip extention
            LOGGER.info('Loading plugin %s', pluginname)

            try:
                importlib.import_module(f'.{pluginname}', package=__name__)
            except (NameError, SyntaxError) as err:
                LOGGER.error('Error loading %s', pluginname)
                LOGGER.exception(err)

