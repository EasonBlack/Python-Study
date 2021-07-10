(* osascript desktop_one.scpt *)

tell application "Finder"
    set {0, 0, dtw, dth} to bounds of window of desktop
end tell

log(dtw & dth)
log("cccc")
log("dddd")

tell application "Finder"
    set screen_resolution to bounds of window of desktop
end tell
log(screen_resolution)
set screenWidth to (do shell script "system_profiler SPDisplaysDataType | awk '/Resolution/{print $2}'")
log(screenWidth)

(* 
tell application "Visual Studio Code"
    activate
    -- set the bounds of the first window to {55, 0,  (dtw / 2) - 55, dth}
end tell
*)

(*
tell application "Notes"
    activate
    set the bounds of the first window to {(dtw / 2) - 55, 0,  (dtw / 2) , dth}
end tell
*)