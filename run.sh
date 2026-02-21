#!/bin/bash

APP_DIR="$HOME/book-finder"
APP_FILE="book-finder-app.py"
PYTHON="python3.12"
PID_FILE="app.pid"
LOG_FILE="log.txt"

cd "$APP_DIR" || exit 1

echo "=== Deploy started at $(date) ==="

# Stop old process if running
if [ -f "$PID_FILE" ]; then
  OLD_PID=$(cat "$PID_FILE")
  if ps -p $OLD_PID > /dev/null 2>&1; then
    echo "Stopping old process ($OLD_PID)"
    kill $OLD_PID
    sleep 2
  fi
  rm -f "$PID_FILE"
fi

# Start new process
echo "Starting Flask app..."
nohup $PYTHON $APP_FILE > "$LOG_FILE" 2>&1 & echo $! > "$PID_FILE"

echo "New PID: $(cat $PID_FILE)"
echo "=== Deploy finished ==="