if [ "$1" = "" ]
then
  echo "Usage: $0 <interface name>"
  exit
fi;

sudo apt install tmux

CWD=$(pwd)
cd $CWD/app/client

IP=$(ip -f inet addr show $1 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')
echo "
// This file is edited by the 'start.sh' script - the IP is pulled from the interface specified in the script arguments before building the app
export const IP: string = \"$IP\";
" > IP.ts;

npm install --force
npm run build

if [ ! -d "$CWD/app/server/static" ];
then
  mkdir "$CWD/app/server/static"
fi

mv build/* $CWD/app/server/static

cd $CWD

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

if [ $(tmux list-sessions | grep "heaterpi-web") ];
then
  tmux kill-session -t heaterpi-web
fi

if [ $(tmux list-sessions | grep "heaterpi-socket") ];
then 
  tmux kill-session -t heaterpi-socket
fi

tmux new-session -d -s heaterpi-web python3 app/server/WebServer.py
tmux new-session -d -s heaterpi-web python3 app/server/ThermostatServer.py