# CSCI 331 — Database Systems

Database Systems course assignments (Winter 2026)

## Featured case study

[Assignment 14: SQL Query Optimization](https://zohaib-cheema.github.io/CSCI-331-Database-Systems/) compares equivalent MySQL query forms and index states, then audits the experiment's own measurement pipeline. The portfolio view links directly to the SQL, Python runner, and unchanged raw output.

**Demonstrates:** non-trivial SQL, Python database automation, indexing, execution-plan analysis, query telemetry, and data-quality reasoning.

## Setup Instructions

### 1. Initialize Git Repository

Run the setup script:
```bash
./setup_github.sh
```

### 2. Create Private GitHub Repository

1. Go to https://github.com/new
2. Repository name: `CSCI-331-Database-Systems` (or your preferred name)
3. Select **Private**
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

### 3. Connect to GitHub

After creating the repo, run (replace with your actual repo URL):
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 4. Set Up Automatic Daily Commits

Run the auto-commit setup:
```bash
python3 setup_auto_commit.py
```

This will automatically commit and push changes daily at 11:59 PM.

### Manual Commit (Optional)

To manually commit and push at any time:
```bash
python3 auto_commit.py
```

## Repository Structure

- `Assignment##.py` - Python source code for each assignment
- `Assignment##.sql` - SQL queries for each assignment
- `Assignment##.html` - HTML output files
- `DBUtil.py` - Database utility functions
- `OutputUtil.py` - HTML output utility functions

## Technologies

- Python
- SQL (MySQL)
- HTML
