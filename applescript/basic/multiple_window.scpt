tell application "System Events"
    tell application "Mission Control" to launch
   
    tell group 2 of group 1 of group 1 of process "Dock"
        click (every button whose value of attribute "AXDescription" is "add desktop")
        tell list 1
            set countSpaces to count of buttons
            delay 0.5
            log(countSpaces)
            click button (countSpaces)
        end tell
    end tell

    delay 0.5
    tell application "Calendar" to launch
    tell application "Reminders" to launch
end tell