#!/bin/bash

npx babel --watch $1/jsx --out-dir $1 --presets react-app/prod
