#!/bin/bash

npx babel --watch $1 --out-dir $2 --presets react-app/prod
