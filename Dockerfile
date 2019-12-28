FROM python:3.8

LABEL "com.github.actions.name"="Krypton"
LABEL "com.github.actions.description"="Awesome Actions to use on GitHub"
LABEL "com.github.actions.icon"="zap"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/Clivern/Krypton"
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