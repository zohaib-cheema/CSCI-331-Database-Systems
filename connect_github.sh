#!/bin/bash
# Script to connect local repository to GitHub

echo "🔗 Connecting to GitHub..."
echo ""
echo "Please provide your GitHub repository URL"
echo "Example: https://github.com/yourusername/CSCI-331-Database-Systems.git"
echo ""
read -p "Enter GitHub repository URL: " repo_url

if [ -z "$repo_url" ]; then
    echo "❌ No URL provided. Exiting."
    exit 1
fi

# Check if remote already exists
if git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  Remote 'origin' already exists. Updating..."
    git remote set-url origin "$repo_url"
else
    git remote add origin "$repo_url"
fi

echo "✅ Remote added: $repo_url"
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo "🔒 Your repository is private and will show SQL in the language breakdown"
else
    echo ""
    echo "❌ Push failed. Make sure:"
    echo "   1. The repository exists on GitHub"
    echo "   2. The repository is set to Private"
    echo "   3. You have push access"
    echo "   4. You're authenticated (git credential helper or SSH key)"
fi
