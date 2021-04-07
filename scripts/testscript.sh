#!/bin/bash

for i in {1..100}
do
    python3 -m unittest $1
done
