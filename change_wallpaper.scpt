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
