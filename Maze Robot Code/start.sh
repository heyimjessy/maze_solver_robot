#!/usr/bin/env bash

#Check if the robot should run all the time
if [[ -e $HOME/RUNROBOTPERMANENT.cfg ]];then
    #Check if the robot should run this time
    if [[ -e  $HOME/RUNROBOTNOW.cfg ]];then
        $HOME/bin/start.py
    else
        #If not, then don't start the robot, but create file again
        touch $HOME/RUNROBOTNOW.cfg
    fi
fi