# How to change your wallpaper dynamically

## 0. Prerequisites

For image downloads, we use python packages `requests`. And we use `json` to process your data from `requests.get`.

For local wallpaper change, we use `applescript` grammar, which is ugly and documentation missing.

For script manipulation, we use `bash` grammar.

## 1. Project Tree
```text
~/Pictures/Wallpapers
├── Display
│   ├── your_downloaded_pictures1.jpg
│   └── your_downloaded_pictures2.jpg
├── README.md
├── change_wallpaper.scpt
├── download_wallpaper.py
└── run.sh
```

## 2. Deployment Flow

### 2.1 Download Pics From `Bing`

Bing provides API for picture link's uri at `https://www.bing.com/HPImageArchive.aspx?format=js&idx={}&n={}`. So we can just get the picture storage link from this and directly download pictures from `https://s.cn.bing.net/" + uri`.

### 2.2 Employ `applescript` to manipulate wallpaper-related API 

> Talk is cheap, show you the code.

The truth is: I'm not familiar with `applescript` either...

```applescript
on run argv
	set wallpaperName to item 1 of argv
	set wallpaperPath to POSIX path of "~/Pictures/Wallpapers/Display/" & (wallpaperName as string) 
	log wallpaperPath
  tell application "System Events"
      set theDesktops to a reference to every desktop
      repeat with x from 1 to (count theDesktops)
          set picture of item x of the theDesktops to wallpaperPath
      end repeat
  end tell
end run
```

### 2.3 Write a script to pipeline the download and change

To get the latest picture, we should sort files at picture hall, and that is `ls -lt` where parameter `-t` means sort the results by descending time order.

To get the file name from `ls` result, we use `awk`. `awk {print $i}` prints the `ith` element from the raw text, sepped by spacing by default.

`ls -lt ./Display| head -n 2 | tail -n 1 | awk '{print $9}'`


### 2.4 Use `Crontab` to set Timed Task

Firstly, we use this command

```bash
crontab -e
```

Argument `-e` means automatically create a file (for example, my crontab script is saved at `/tmp/crontab.GLqTBkM4Fb`), and open the editor to write instruction.

And we type this in `vim`.

```bash
0 * * * * /path/to/your/run.sh
``` 

`num1(*) num2(*) num3(*) num4(*) num5(*)` is divided into five fields, each representing minutes, hours, day of month, month, and day of week.

* num1 (minutes): Indicates the start of each hour.
* num2 (hours): Means every hour.
* num3 (day of month): Indicates every day of the month.
* num4 (month): Means every month.
* num5 (day of week): Represents every day of the week.

Symbol `*` means that the script is executed every minute (hours, ...)