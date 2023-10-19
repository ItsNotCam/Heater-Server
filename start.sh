cd app

# Install Dependencies
sudo apt install tmux python3 python3-pip
pip3 install -r requirements.txt

# Kill TMUX windows running the heater app
WINDOW_NAME="heaterpi"

if [ $(tmux list-sessions | grep "$WINDOW_NAME") ];
then
  tmux kill-session -t $WINDOW_NAME
fi

# Start servers in new TMUX sessions
tmux new-session -d -s $WINDOW_NAME python3 WebServer.py
tmux split-window -h -t $WINDOW_NAME
tmux send-keys -t $WINDOW_NAME "python3 SocketServer.py" C-m
