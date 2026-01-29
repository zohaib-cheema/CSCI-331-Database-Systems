#!/bin/bash
# Quick script to connect to GitHub

echo "🔗 GitHub Connection Setup"
echo "=========================="
echo ""
echo "Step 1: Create a private repository on GitHub"
echo "   Go to: https://github.com/new"
echo "   - Name: CSCI-331-Database-Systems (or your choice)"
echo "   - Select: Private"
echo "   - DO NOT initialize with README, .gitignore, or license"
echo "   - Click 'Create repository'"
echo ""
read -p "Press Enter after you've created the repository..."

echo ""
echo "Step 2: Enter your repository URL"
echo "   Example: https://github.com/yourusername/CSCI-331-Database-Systems.git"
read -p "Repository URL: " repo_url

if [ -z "$repo_url" ]; then
    echo "❌ No URL provided. Exiting."
    exit 1
fi

echo ""
echo "🔗 Connecting to GitHub..."

# Add remote
if git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  Remote 'origin' already exists. Updating..."
    git remote set-url origin "$repo_url"
else
    git remote add origin "$repo_url"
fi

echo "✅ Remote configured: $repo_url"
echo ""
echo "📤 Pushing to GitHub..."

# Push to GitHub
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅✅✅ SUCCESS! ✅✅✅"
    echo ""
    echo "Your repository is now connected to GitHub!"
    echo "🔒 Repository is private"
    echo "📊 SQL will show in language breakdown"
    echo "🔄 Auto-commit is running (will push daily at 11:59 PM)"
    echo ""
    echo "View your repo at: $repo_url"
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo "   1. Repository doesn't exist or URL is wrong"
    echo "   2. Not authenticated (run: git config --global user.name 'Your Name')"
    echo "   3. Need to set up GitHub authentication"
    echo ""
    echo "Try again or set up authentication first."
fi
