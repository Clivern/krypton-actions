FROM python:3.6

LABEL "com.github.actions.name"="krypton-actions"
LABEL "com.github.actions.description"="Open Source Workflow Automation"
LABEL "com.github.actions.icon"="package"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/Clivern/krypton-actions"
LABEL "homepage"="http://github.com/clivern"
LABEL "maintainer"="Clivern <hello@clivern.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /krypton

COPY . /krypton

RUN chmod +x /krypton/entrypoint.sh
RUN chmod +x /krypton/app.py

WORKDIR /krypton

RUN pip install -r requirements.txt

ENTRYPOINT ["/krypton/entrypoint.sh"]