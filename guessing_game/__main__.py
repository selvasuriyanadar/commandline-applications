import sys
from .commands import config_data
from paraivari.parser import parse

parse(sys.argv[1:], config_data)

