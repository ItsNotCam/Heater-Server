# Get interface name for IP
if [ "$1" = "" ]
then
  echo "Usage: $0 <interface name>"
  exit
fi;

# Install TMUX to run the app
sudo apt install tmux python3 python3-pip

# Install python dependencies
pip3 install -r app/requirements.txt

# Kill TMUX windows running the heater app
if [ $(tmux list-sessions | grep "heaterpi-web") ];
then
  tmux kill-session -t heaterpi-web
fi

if [ $(tmux list-sessions | grep "heaterpi-socket") ];
then 
  tmux kill-session -t heaterpi-socket
fi

# Start servers in new TMUX sessions
tmux new-session -d -s heaterpi-web python3 app/WebServer.py
tmux new-session -d -s heaterpi-web python3 app/SocketServer.py