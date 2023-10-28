__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains functions for reloading modules"

# pip3 install gitpython
import git

# modules_repo = 'https://github.com/Younes-Karimi/modules.git'
# git.Repo.clone_from(modules_repo, modules_path)

def reload_modules(modules_path):
    modules = git.Repo(modules_path)
    modules.remotes.origin.pull()
    if modules.is_dirty(untracked_files=True):
        diff = modules.git.diff(modules.head.commit.tree)
        if len(diff) > 0:
            print('>> Detected Changes: <<\n')
            print(diff)
        else:
            print('No changes detected')
