#!/bin/bash
# Update bot using Github branch master

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "master" ]
then
  git stash &&
  git checkout master
fi


git fetch
HEADHASH=$(git rev-parse HEAD)
UPSTREAMHASH=$(git rev-parse master@{upstream})

if [ "$HEADHASH" = "$UPSTREAMHASH" ]
then
  git checkout $BRANCH &&
  git stash apply
  echo ${ERROR}No update necessary.${NOCOLOR}
  exit 1
else
  echo ${ACTION}Updating...${NOCOLOR}
fi


# Prerequisites:
# - Valid SSH key for repo
# - git remote set-url origin git@github.com:DevOps-Utrecht/bot.git
git pull origin master;


# Prerequisites:
# - The virtualenv should be called .venv
.venv/bin/python3 setup.py install &&


# Prerequisites:`
# - systemctl service for the bot, named devbot.service
# - The following line added to the sudoers file for passwordless reloading
#     %LimitedAdmins ALL=NOPASSWD: /bin/systemctl restart devbot.service
sudo /bin/systemctl restart devbot.service;

if [ "$BRANCH" != "master" ]
then
  git checkout $BRANCH &&
  git stash apply
fi

echo
echo ${FINISHED}Bot has been updated.${NOCOLOR}
