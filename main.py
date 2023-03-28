import pathlib
from typing import Final

import git

link_for_test_repo = "https://github.com/Alex-Matveenko/test_for_gitpython"
PATH_TO_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parent
PATH_TO_REPO_DIR: Final[pathlib.Path] = PATH_TO_DIR.joinpath("my_test")
try:
    repository = git.Repo.clone_from(url=link_for_test_repo, to_path=PATH_TO_REPO_DIR, branch="master")
except git.exc.GitCommandError:
    repository = git.Repo(PATH_TO_REPO_DIR)

last_commit = repository.head.commit
last_changed_files = last_commit.stats.files

# changed_files = []
# for file in last_changed_files:
#     file = PATH_TO_REPO_DIR.joinpath(file)
#     changed_files.append(file)

some = repository.index.diff(None)
repository.remotes.origin.fetch()
repository.remotes.origin.pull()

commits = []

for commit in list(repository.iter_commits(rev='master')):
    commits.append(commit)
    if commit.hexsha == "5b4149f92b3d5f6b05d08c0b27d837b2617e8ca7":
        break

for item in commits:
    x = 1
    item = item.stats.files
    i=1
