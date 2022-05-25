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

set -a
. .env
set +a

if [ ! "$(docker ps -a | grep cicd_db_test)" ]; then
    echop 'Creating postgresql container...'
    
    docker run \
    -d \
    --name cicd_db_test \
    -e POSTGRES_DB="$CITY_API_DB_NAME" \
    -e POSTGRES_USER="$CITY_API_DB_USER" \
    -e POSTGRES_PASSWORD="$CITY_API_DB_PWD" \
    -p "5432:5432" \
    postgres:14-alpine > /dev/null

    sleep 5
elif [ ! "$(docker ps | grep cicd_db_test)" ]; then
    echop 'Starting postgresql...'
    docker start cicd_db_test > /dev/null
fi

if [ $? -eq 0 ]
then
    echop 'Done'
else
    errorp 'Unable to start postgresql container!'
fi

cd src
pipenv run python3 -m pytest -vvv

echop 'Stopping database...'
docker rm -f cicd_db_test > /dev/null
echop 'Done'