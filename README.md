# Git Learning Lab

A hands-on repo for practicing core git commands.

## Exercises

### 1. git merge
**Goal:** Combine two diverged branches.

```bash
# See the branches available
git branch -a

# Checkout main and merge the feature branch into it
git checkout main
git merge feature/add-multiply

# Inspect the result
git log --oneline --graph --all
```

### 2. git rebase
**Goal:** Replay a feature branch on top of the latest main.

```bash
# Switch to the rebase feature branch
git checkout feature/add-divide

# Rebase it on top of main
git rebase main

# Inspect the linear history
git log --oneline --graph --all
```

### 3. git cherry-pick
**Goal:** Apply only specific commits from another branch.

```bash
# Find the commit hashes you want on the extras branch
git log --oneline feature/extras

# Cherry-pick one or more specific commits onto main
git checkout main
git cherry-pick <commit-hash>

# Try cherry-picking multiple commits
git cherry-pick <hash1> <hash2>
```

## Files
- `calculator.py` — grows as features are added across branches
