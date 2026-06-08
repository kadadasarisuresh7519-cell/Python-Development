:: Create project folder
mkdir python-starter
cd python-starter

:: Create virtual environment
python -m venv .venv

:: Activate virtual environment
.venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Create Python file
echo print("Hello World") > app.py

:: Create README file
echo # Python Starter Project > README.md

:: Initialize Git
git init

:: Configure Git (replace with your details)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

:: Add files to Git
git add .

:: First commit
git commit -m "Initial project setup"

:: Connect GitHub repository (replace with your repository URL)
git remote add origin https://github.com/YOUR_USERNAME/python-starter.git

:: Rename branch to main
git branch -M main

:: Push to GitHub
git push -u origin main