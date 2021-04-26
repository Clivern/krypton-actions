FROM python:3.9

LABEL "com.github.actions.name"="krypton-actions"
LABEL "com.github.actions.description"="Open Source Workflow Automation"
LABEL "com.github.actions.icon"="package"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/Clivern/krypton-actions"
LABEL "homepage"="http://github.com/clivern"
LABEL "maintainer"="Clivern <hello@clivern.com>"

ENV PYTHONUNBUFFERED 1

RUN git clone --depth=1 --branch=1.0.0-alpha.1 https://github.com/silverbackhq/krypton.git /krypton

RUN rm -rf /krypton/.git

COPY entrypoint.sh /krypton

RUN chmod +x /krypton/entrypoint.sh

WORKDIR /krypton

RUN pip install -r requirements.txt

ENTRYPOINT ["/krypton/entrypoint.sh"]
