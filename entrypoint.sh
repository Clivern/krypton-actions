#!/bin/bash

ll -al $GITHUB_WORKSPACE
ll -al /github/workflow/
cat /github/workflow/event.json

python /krypton/app.py