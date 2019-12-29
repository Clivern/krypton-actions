#!/bin/bash

# Event Info
cat /github/workflow/event.json 2>/dev/null

echo "\n\n"

# Krypton Configs
cat $GITHUB_WORKSPACE/.krypton.yml 2>/dev/null

python /krypton/manage.py github_actions
