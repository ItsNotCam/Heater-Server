echo ""

GREEN='\033[1;32m'
WHITE='\033[1;37m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'

cd app

#Install Dependencies
echo -e "${GREEN}Installing Dependencies${WHITE}"
sudo apt install tmux python3 python3-pip
pip3 install -r requirements.txt
echo ""

# Kill TMUX windows running the heater app
WINDOW_NAME="heaterpi"
SESSION=$(tmux list-session | grep $WINDOW_NAME)
if [ "$SESSION" ]
then
  echo -e "${YELLOW}Killing any old HeaterPi instances"
  tmux kill-session -t $WINDOW_NAME
  echo ""
fi

# Start servers in new TMUX sessions
echo -e "${CYAN}Starting up HeaterPi in TMUX..."
tmux new-session -d -s $WINDOW_NAME python3 WebServer.py
tmux split-window -h -t $WINDOW_NAME
tmux send-keys -t $WINDOW_NAME "python3 SocketServer.py" C-m
echo ""

echo -e "${GREEN}All done!${WHITE}"
echo ""

echo "Just type \"tmux attach -t heaterpi\" to view the running app!" 
echo "To visit it in your browser, just find your pi's IP address and paste it into your web browser along with the port \":5000\" after it!"
echo ""
