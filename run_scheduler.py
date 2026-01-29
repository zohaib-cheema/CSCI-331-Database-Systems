#!/usr/bin/env python3
"""
Auto-commit scheduler - runs auto_commit.py daily at 11:59 PM
"""
import schedule
import time
import subprocess
import sys
from pathlib import Path
from datetime import datetime

script_path = Path(__file__).parent / "auto_commit.py"

def run_commit():
    """Run the auto-commit script"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running auto-commit...")
    subprocess.run([sys.executable, str(script_path)])

# Schedule daily at 11:59 PM
schedule.every().day.at("23:59").do(run_commit)

print("✅ Auto-commit scheduler started!")
print("📅 Will commit daily at 11:59 PM")
print("📝 Logs: auto_commit.log")
print("Press Ctrl+C to stop\n")

try:
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
except KeyboardInterrupt:
    print("\n👋 Stopping scheduler...")
