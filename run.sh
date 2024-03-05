#!/bin/zsh

export PATH="/opt/homebrew/anaconda3/bin:${PATH}"
alias python="/opt/homebrew/anaconda3/bin/python"
cd ~/Pictures/Wallpapers
python ./download_wallpaper.py
export WALLPAPER_NAME=`ls -lt ./Display| head -n 2 | tail -n 1 | awk '{print $9}'`
echo "Change Wallpaper to $WALLPAPER_NAME"
osascript ./change_wallpaper.scpt $WALLPAPER_NAME
