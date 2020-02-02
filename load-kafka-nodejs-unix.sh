#!/bin/bash

cd ./producers/nodejs-producer

ECHO "#####################################"
ECHO "#                                   #"
ECHO "#   Resolving nodejs dependencies   #"
ECHO "#                                   #"
ECHO "#####################################"

npm install

ECHO "#############################"
ECHO "#                           #"
ECHO "#       Starting load       #"
ECHO "#                           #"
ECHO "#############################"

node index.js

ECHO "############################"
ECHO "#                          #"
ECHO "#       Load finished      #"
ECHO "#                          #"
ECHO "############################"
