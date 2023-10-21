NAME="heaterpi"

SESSION=$(tmux list-session | grep $NAME)
if [ "$SESSION" ]
then
  echo "Stopping any HeaterPi TMUX instances"
  tmux kill-session -t $NAME
else
  echo "No HeaterPI TMUX instances detected"
fi

echo "Done"
