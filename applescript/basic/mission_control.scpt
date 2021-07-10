tell application "System Events"
    tell application "Mission Control" to launch
    tell process "Dock"
      entire contents
    end tell
    tell button "桌面2" of list 1 of group "空间栏" of group 1 of group "调度中心" of application process "Dock"
      delay 1
      click
    end tell 
end tell