#!/bin/bash

ls -al $GITHUB_WORKSPACE
ls -al /github/workflow/
cat /github/workflow/event.json

python /krypton/app.py
