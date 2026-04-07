# LEARNINGS-aariff1

# Checkpoint 1
In checkpoint 1, I used the following commands:
git add tests/test_calculator.py
git commit -m "fix"
git add .gitignore
git commit -m "update"

In this checkpoint I learned how to use the staging area to separate unrelated changes into different commits. With a clean commit history, my teammates and myself can review and debug code a lot easier now.

# Checkpoint 2 
In checkpoint 2, I used the following commands:
git log --oneline
git revert 6ca467b

In checkpoint 2, I learned the usefulness of git revert. With git revert I can safely undo a bad commit without erasing project history unlike git reset. This makes it helpful for my teammates to see where the error occurs.

# Checkpoint 3 

In checkpoint 3, I used the following commands:
git checkout main
git add src/validator.py
git commit -m "Add is_positive helper function"
git log --oneline -1
git reset --hard HEAD~1
git checkout feature/aariff1
git cherry-pick 93ea891
git add src/validator.py
git cherry-pick --continue
git checkout main
git log --oneline -3
git checkout feature/aariff1

In checkpoint 3, I learned how to move a commit from the wrong branch to the correct branch using `git cherry-pick`. I also learned how to resolve a merge conflict while keeping both the existing code and new code added. This is important as developers can easily make mistakes, so knowing how to change the wrong branch to the correct branch can save alot of time and hassle.

# Checkpoint 4
In checkpoint 4, I used the following commands:  
git checkout -b experiment/aariff1  
git add src/calculator.py  
git commit -m "added experiment comment"  
git checkout feature/aariff1  
git branch -D experiment/aariff1  
git reflog --oneline  
git branch recovered/aariff1 75a7769  
git merge --no-ff recovered/aariff1 -m "Merge recovered experiment branch"  

In checkpoint 4, I learned how `git reflog` can help recover work that seems lost after a branch is deleted. This matters because it provides a safeguard when mistakes happen and helps prevent loss of work.

# Checkpoint 5
In checkpoint 5, I used the following commands:  
git remote add upstream https://github.com/mdurrani808/git_project_1.git  
git remote -v  
git fetch upstream  
git checkout main  
git reset --hard upstream/main  
git checkout feature/aariff1  
git rebase main  

In checkpoint 5, I learned how to sync my branch with the original upstream repository by fetching and rebasing onto the updated `main` branch. This is important because it keeps my work current and reduces problems when merging later making my teammates work alot easier.

# Checkpoint 6
In checkpoint 6, I used the following commands:  
git log main..HEAD --oneline  
git rebase -i main  
git log --oneline --graph -10  

In checkpoint 6, I learned how to clean up commit history with rebase by rewording commit messages. This is useful because a clear  commit history makes the project easier for teammates and reviewers to follow along with.



