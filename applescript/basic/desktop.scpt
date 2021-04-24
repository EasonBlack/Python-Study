tell application "Finder" to get the bounds of Finder window 1
tell application "Finder"
    set {0, 0, dtw, dth} to bounds of window of desktop
end tell

tell application "System Events"
    key code 20 using (control down)
end tell
