#!/bin/bash
# Setup script for GitHub repository

REPO_PATH="/Users/zohaibcheema/Desktop/CSCI 331L"
cd "$REPO_PATH"

echo "🚀 Setting up GitHub repository..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "📝 Adding files..."
git add .

# Initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: CSCI 331 Database Systems assignments"

echo ""
echo "✅ Local repository initialized!"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Create a NEW repository (name it something like 'CSCI-331-Database-Systems')"
echo "3. Make sure to select 'Private'"
echo "4. DO NOT initialize with README, .gitignore, or license"
echo "5. Copy the repository URL (e.g., https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)"
echo ""
echo "6. Then run this command (replace with your actual repo URL):"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git push -u origin main"
echo ""
echo "7. To set up auto-commit, run:"
echo "   python3 setup_auto_commit.py"
