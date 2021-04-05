import sqlite3 as sl
from .model import Stat

with Stat() as stat_store:
    stat_store.drop()
    stat_store.create()
