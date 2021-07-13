#!/usr/bin/env bash
BASE=$1
LIDAR=$2
echo "export RIKIBASE=$BASE" >> ~/.bashrc
echo "export RIKILIDAR=$LIDAR" >> ~/.bashrc
source ~/.bashrc
