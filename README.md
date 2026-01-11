# git-fast

`git-fast` is a command-line tool that lets you stage, commit, and push changes to a Git repository with a single command - `a`

View at https://pypi.org/project/git-fast/

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

## How to run locally:

```bash
pip install e .
```

In your project appear:
`build/`
`git_fast.egg-info/`

Now you are ready to run it locally with `a`

## How to modify, create your own package from this repo

```bash
git clone https://github.com/OliverIida/git-fast.git
# Modify the code, package names etc
pip install --upgrade build # download/update build tool
python -m build # build the package
pip install --upgrade twine # install/update Twine
twine upload dist/* # upload the package to Pypi
# enter your Pypi API token
# test - pip install {your-package-name}
```