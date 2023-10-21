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

echo -e "${GREEN}Done"
