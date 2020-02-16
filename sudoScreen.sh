#/bin/sh
loginwindowpid=`ps axo pid,comm | grep '[l]oginwindow' | sed -n 's# *\([^ ]*\).*$#\1#p'`
sudo launchctl bsexec $loginwindowpid screencapture -m ~/screen.png
