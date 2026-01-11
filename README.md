# git-quick

`git-quick` is a small command-line tool that lets you stage, commit, and push changes to a Git repository with a single command.

---

## What it does

When you run:

```bash
a
```

It automatically stages all changes in your current working directory and prompts to enter a commit message:

```bash
enter commit message: _
```

After writing a message and hitting ENTER, the changes are pushed to the remote repo.
Entering an empty commit message results in the program doing `git reset` and exiting.

## How to modify/run locally:

```bash
pip install e .
```

In your project appear:
`build/`
`git_quick.egg-info/`

Now you are ready to run it locally with `a`