SESSION_NAME="clash"
COMMAND="cd ~/.config/clash && ./clash"
tmux new-session -d -s "$SESSION_NAME" "$COMMAND"
