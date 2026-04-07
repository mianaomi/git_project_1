# Learnings - ngangise

## Checkpoint 1: Staging Is Not Committing

**Commands:**
```
git add src/calculator.py
git commit -m "fix"
git add src/validator.py
git commit -m "update"
git push origin feature/ngangise
```

**Reflection:** I learned that the staging area lets you control exactly which changes go into each commit. By staging files separately, you can make two unrelated changes in one working session but record them as distinct, focused commits.

---

## Checkpoint 2: Undo Without Erasing History

**Commands:**
```
git revert 4dc20fb --no-edit
```

**Reflection:** I learned that `git revert` undoes a commit by creating a new commit, leaving the original bad commit still in history. This is safer than deleting history because it keeps a clear record of what happened and why it was undone.

---

## Checkpoint 3: Moving a Commit to the Right Branch

**Commands:**
```
git checkout main
git add src/validator.py
git commit -m "Add is_positive helper function"
git log --oneline
git reset --hard HEAD~1
git checkout feature/ngangise
git cherry-pick <commit-hash>
git add src/validator.py
git cherry-pick --continue
```

**Reflection:** I learned that `git cherry-pick` lets you apply a specific commit from one branch onto another. This is useful when you accidentally commit to the wrong branch and need to move that work without merging the entire branch.

---

## Checkpoint 4: Recovering Lost Work with Reflog

**Commands:**
```
git checkout -b experiment/ngangise
git add src/calculator.py
git commit -m "Add experiment comment"
git checkout feature/ngangise
git branch -D experiment/ngangise
git reflog
git checkout -b recovered/ngangise <commit-hash>
git checkout feature/ngangise
git merge recovered/ngangise
```

**Reflection:** I learned that `git reflog` tracks every movement of HEAD, even after branches are deleted. This means that as long as you haven't garbage collected, you can recover almost any commit that seemed lost.

---

## Checkpoint 5: Syncing with Upstream

**Commands:**
```
git remote add upstream git@github.com:mdurrani808/git_project_1.git
git fetch upstream
git checkout main
git merge upstream/main
git checkout feature/ngangise
git rebase main
git push --force-with-lease origin feature/ngangise
```

**Reflection:** I learned how to keep a forked repository in sync with the original upstream repo using two remotes. Rebasing onto the updated main keeps a linear history instead of adding unnecessary merge commits.

---

## Checkpoint 6: Interactive Rebase to Clean Up History

**Commands:**
```
git rebase -i main
git push --force-with-lease origin feature/ngangise
```

**Reflection:** I learned that interactive rebase lets you rewrite commit history before submitting for review — rewording vague messages like "fix" into descriptive ones makes the history much easier for teammates to understand.