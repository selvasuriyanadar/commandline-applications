import sys
from .view import config_data
from paraivari.parser import parse

parse(sys.argv[1:], config_data)

