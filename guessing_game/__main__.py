from .commands import run
import sys

web = True

if not web:
    print(run(sys.argv[1:]))
