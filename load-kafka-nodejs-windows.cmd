@ECHO off

TITLE Load Kafka

CD ./producers/nodejs-producer

ECHO #####################################
ECHO #                                   #
ECHO #   Resolving nodejs dependencies   #
ECHO #                                   #
ECHO #####################################

CALL npm install

ECHO #############################
ECHO #                           #
ECHO #       Starting load       #
ECHO #                           #
ECHO #############################

CALL node index.js

ECHO ############################
ECHO #                          #
ECHO #       Load finished      #
ECHO #                          #
ECHO ############################

PAUSE
