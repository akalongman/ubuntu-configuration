# Change terminal output

_ROOT_COLOR=31  # red
_USER_COLOR=32  # green
_TS_COLOR=34  # blue

if [ $EUID = 0 ]; then
  #echo "Root logged in\n" >> /tmp/logged.txt
  PS1="\[\033[01;${_ROOT_COLOR}m\]$(hostname)\[\033[01;${_TS_COLOR}m\] \t \w #\[\033[00m\] "
else
  #echo "${USER} logged in\n" >> /tmp/logged.txt
  PS1="\[\033[01;${_USER_COLOR}m\]$(hostname)\[\033[01;${_TS_COLOR}m\] \t \w $\[\033[00m\] "
fi
