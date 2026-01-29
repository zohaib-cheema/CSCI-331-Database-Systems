#!/bin/bash
# Start auto-commit script in background

SCRIPT_DIR="/Users/zohaibcheema/Desktop/CSCI 331L"
LOG_FILE="$SCRIPT_DIR/auto_commit.log"

echo "🚀 Starting auto-commit service..."
echo "📝 Logs will be saved to: $LOG_FILE"
echo ""
echo "This will run auto_commit.py every day at 11:59 PM"
echo "Press Ctrl+C to stop"
echo ""

# Run the auto-commit script with schedule
cd "$SCRIPT_DIR"

# Check if schedule is installed
if ! python3 -c "import schedule" 2>/dev/null; then
    echo "📦 Installing schedule library..."
    pip3 install schedule
fi

# Create a simple scheduler script
cat > "$SCRIPT_DIR/run_scheduler.py" << 'EOF'
import schedule
import time
import subprocess
import sys
from pathlib import Path

script_path = Path(__file__).parent / "auto_commit.py"

def run_commit():
    subprocess.run([sys.executable, str(script_path)])

# Schedule daily at 11:59 PM
schedule.every().day.at("23:59").do(run_commit)

print("✅ Auto-commit scheduler started!")
print("📅 Will commit daily at 11:59 PM")
print("Press Ctrl+C to stop\n")

try:
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
except KeyboardInterrupt:
    print("\n👋 Stopping scheduler...")
EOF

# Run in background
nohup python3 "$SCRIPT_DIR/run_scheduler.py" >> "$LOG_FILE" 2>&1 &
PID=$!

echo "✅ Auto-commit started (PID: $PID)"
echo "📋 To stop: kill $PID"
echo "📋 To view logs: tail -f $LOG_FILE"
