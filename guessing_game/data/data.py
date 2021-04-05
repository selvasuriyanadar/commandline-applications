from random import randint
import json
from json import JSONDecodeError
from importlib import resources
import sqlite3 as sl

# data

class StatMisformed(Exception):
    pass

class StatsNotEquivalent(Exception):
    pass

class Stat:
    """
    value:
       random_integer an int which defaults to any random integer.
       guessed is a bool, default is False.
       guesses is an int, default is 0.

    getStat:
       if a valid stat is not get then returns default stat
    """
    def __init__(self):
        pass

    def getStat(self):
        pass

    def putStat(self, stat):
        pass

    def resetStat(self):
        self.putStat(self.defaultStat())

    def defaultStat(self):
        return {
                "random_integer": randint(0, 100),
                "guessed": False,
                "guesses": 0,
            }

    def validateStat(self, stat):
        if all(k in stat for k in ["random_integer", "guessed", "guesses"]):
            if (isinstance(stat["random_integer"], int) and
                isinstance(stat["guessed"], bool) and
                isinstance(stat["guesses"], int)):
                return True
        raise StatMisformed

    def assertEquivalent(self, stat1, stat2):
        self.validateStat(stat1)
        self.validateStat(stat2)
        if (stat1["guessed"] is stat2["guessed"] and
            stat1["guesses"] is stat2["guesses"]):
            return True
        raise StatsNotEquivalent

class StatDb(Stat):
    """
    storage:
       path holds the path of a db file.
       the table stat in the database.
    """

    def __init__(self):
        super().__init__()
        with resources.path(
                "guessing_game.data",
                "data.db"
            ) as path:
            self._path = path
        self._con = sl.connect(self._path)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._con.close()

    def create(self):
        with self._con:
            self._con.execute("""
                CREATE TABLE IF NOT EXISTS stat (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    random_integer INTEGER,
                    guessed INTEGER,
                    guesses INTEGER
                );
            """)
            self._con.execute("""
                INSERT INTO stat (id, random_integer, guessed, guesses)
                VALUES (0, NULL, NULL, NULL);
            """)
            self.resetStat()

    def drop(self):
        with self._con:
            self._con.execute("""
                DROP TABLE IF EXISTS stat;
            """)

    def getStat(self):
        try:
            stat = {}
            with self._con:
                data = self._con.execute("""
                    SELECT random_integer, guessed, guesses
                    FROM stat
                    WHERE id == 0;
                """)
                for row in data:
                    stat["random_integer"] = row[0]
                    stat["guessed"] = row[1] == 1
                    stat["guesses"] = row[2]
            self.validateStat(stat)

        except (StatMisformed) as e:
            stat = self.defaultStat()

        return stat

    def putStat(self, stat):
        try:
            self.validateStat(stat)
        except (StatMisformed) as e:
            stat = self.defaultStat()

        with self._con:
            self._con.execute(f"""
                UPDATE stat SET
                    random_integer = {stat['random_integer']},
                    guessed = {1 if stat['guessed'] else 0},
                    guesses = {stat['guesses']}
                WHERE id == 0;
            """)

class StatJson(Stat):
    """
    storage:
       path holds the path of a json file.
    """

    def __init__(self):
        super().__init__()
        with resources.path(
                "guessing_game.data",
                "stat.json"
            ) as path:
            self._path = path
        self._file = open(self._path, 'r+')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._file.close()

    def create(self):
        self.resetStat()

    def drop(self):
        self._file.truncate(0)
        self._file.seek(0)
        json.dump({}, self._file)

    def getStat(self):
        try:
            self._file.seek(0)
            stat = json.load(self._file)
            self.validateStat(stat)

        except (StatMisformed) as e:
            stat = self.defaultStat()

        return stat

    def putStat(self, stat):
        try:
            self.validateStat(stat)
        except (StatMisformed) as e:
            stat = self.defaultStat()

        self._file.truncate(0)
        self._file.seek(0)
        json.dump(stat, self._file)

