#!/usr/bin/env python3
"""
Auto-commit script for CSCI 331 assignments
Automatically commits and pushes changes to GitHub daily
"""

import subprocess
import os
import sys
from datetime import datetime

def commit_and_push():
    """Commit and push changes to GitHub if there are any"""
    repo_path = "/Users/zohaibcheema/Desktop/CSCI 331L"
    
    try:
        os.chdir(repo_path)
        
        # Check if there are changes
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        
        if result.stdout.strip():  # If there are changes
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Changes detected, committing...")
            
            # Add all changes
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Commit with timestamp
            commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            
            # Push to GitHub
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            print(f"✅ Successfully committed and pushed at {datetime.now()}")
            return True
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ⏭️  No changes to commit")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Run once if called directly
    commit_and_push()
