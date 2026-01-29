#!/usr/bin/env python3
"""
Setup script to configure automatic daily commits
This will set up a cron job or launchd agent to run auto_commit.py daily
"""

import subprocess
import os
import platform
from pathlib import Path

def setup_macos_launchd():
    """Set up launchd agent for macOS (runs daily at 11:59 PM)"""
    home = Path.home()
    launch_agents = home / "Library/LaunchAgents"
    launch_agents.mkdir(exist_ok=True)
    
    script_path = "/Users/zohaibcheema/Desktop/CSCI 331L/auto_commit.py"
    log_path = "/Users/zohaibcheema/Desktop/CSCI 331L/auto_commit.log"
    
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.csci331.autocommit</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>{script_path}</string>
    </array>
    <key>StandardOutPath</key>
    <string>{log_path}</string>
    <key>StandardErrorPath</key>
    <string>{log_path}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>59</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>"""
    
    plist_path = launch_agents / "com.csci331.autocommit.plist"
    
    try:
        with open(plist_path, 'w') as f:
            f.write(plist_content)
        
        # Load the launchd agent
        subprocess.run(['launchctl', 'load', str(plist_path)], check=True)
        print(f"✅ Launchd agent installed successfully!")
        print(f"📅 Auto-commit will run daily at 11:59 PM")
        print(f"📝 Logs will be saved to: {log_path}")
        print(f"\nTo stop auto-commit, run:")
        print(f"   launchctl unload {plist_path}")
        return True
    except Exception as e:
        print(f"❌ Error setting up launchd: {e}")
        return False

def setup_cron():
    """Set up cron job as fallback"""
    script_path = "/Users/zohaibcheema/Desktop/CSCI 331L/auto_commit.py"
    log_path = "/Users/zohaibcheema/Desktop/CSCI 331L/auto_commit.log"
    
    cron_line = f"59 23 * * * /usr/bin/python3 {script_path} >> {log_path} 2>&1\n"
    
    try:
        # Get current crontab
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_cron = result.stdout if result.returncode == 0 else ""
        
        # Check if already exists
        if "auto_commit.py" in current_cron:
            print("⚠️  Auto-commit cron job already exists")
            return False
        
        # Add new cron job
        new_cron = current_cron + cron_line
        subprocess.run(['crontab', '-'], input=new_cron, text=True, check=True)
        
        print("✅ Cron job installed successfully!")
        print(f"📅 Auto-commit will run daily at 11:59 PM")
        print(f"📝 Logs will be saved to: {log_path}")
        print(f"\nTo view cron jobs: crontab -l")
        print(f"To remove: crontab -e (then delete the line)")
        return True
    except Exception as e:
        print(f"❌ Error setting up cron: {e}")
        return False

def main():
    print("🔧 Setting up automatic daily commits...\n")
    
    # Try launchd first (macOS preferred method)
    if platform.system() == "Darwin":
        if setup_macos_launchd():
            return
    
    # Fallback to cron
    if setup_cron():
        return
    
    print("\n❌ Failed to set up automatic commits")
    print("💡 You can manually run: python3 auto_commit.py")

if __name__ == "__main__":
    main()
