#!/usr/bin/env bash

if [ ${PWD##*/} == scripts ] ;
then
    cd ..
fi

COLOR_BLACK='\033[0;30m'     
COLOR_DARKGRAY='\033[1;30m'
COLOR_RED='\033[0;31m'
COLOR_LIGHTRED='\033[1;31m'
COLOR_GREEN='\033[0;32m'
COLOR_LIGHTGREEN='\033[1;32m'
COLOR_GOLD='\033[0;33m'
COLOR_YELLOW='\033[1;33m'
COLOR_BLUE='\033[0;34m'
COLOR_LIGHTBLUE='\033[1;34m'
COLOR_PURPLE='\033[0;35m'
COLOR_LIGHTPURPLE='\033[1;35m'
COLOR_CYAN='\033[0;36m'
COLOR_LIGHTCYAN='\033[1;36m'
COLOR_LIGHTGRAY='\033[0;37m'
COLOR_WHITE='\033[1;37m'
COLOR_NULL='\033[0m'

echop () {
    echo -e "${COLOR_BLUE}[CITY INFO]${COLOR_NULL}" $@
}

errorp () {
    echo -e "${COLOR_RED}[CITY ERROR]${COLOR_NULL}" $@
}

docker-compose up -d > /dev/null

sleep 2

if [ $? -eq 0 ]
then
    echop 'Done'
else
    errorp 'Unable to start postgresql container!'
fi

cd src
pipenv run python3 -m pytest -vvv

echop 'Stopping database...'
docker-compose down > /dev/null
echop 'Done'