#!/bin/zsh

cd ~/Pictures/Wallpapers
python ./download_wallpaper.py
export WALLPAPER_NAME=`ls -lt ./Display| head -n 2 | tail -n 1 | awk '{print $9}'`
osascript ./change_wallpaper.scpt $WALLPAPER_NAME
