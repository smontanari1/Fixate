from fixate.config import CONFIG_LOADED, RESOURCES
from fixate.config.local_config import setup_config
import fixate.core as lib
from .__main__ import run_main_program

__version__ = '10'

if not CONFIG_LOADED:
    setup_config()