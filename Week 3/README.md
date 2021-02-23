## Command line statement for Gitlab setup

# git installation check
      - git --version

# git configuration 
      - git config --global user.name "your_username"
      - git config --global user.email "you_email_address@example.com"
      - git config --global --list

# git authentication (using SSH or https)
      - 

# Clone a repository command (cloning is different from download) 
      - git clone "repository_url"

# Pulling repository (If any changes are made in repository, first pull)
      - git pull origin master 

# To view remote repository
      - git remote -v 

# Branching (if you want to add code to a project or collaborating with others)
      - Feature branch and Switch branch 
      - git checkout -b test_branch 

# Command to switch to the master branch or feature branch 
      - git checkout master
      - git checkout test_branch

# To view the changes made
      - git status

# To view differences between local, upstages changes and repository version 
      - git diff

# Add and commit local changes
      - git add file_name
      - git commit -m “git comment”

# Add all changes to commit
      - git add .
      - git commit -m “git comment"

# Send changes to gitlab server using push
      - Git push origin master
      - Git push origin test_branch (to push to test_branch)

# push command
      - git init
      - git status
      - git add .
      - git commit -m “msg”
      - git push -u “url” master

# Forking 

# Rebasing 