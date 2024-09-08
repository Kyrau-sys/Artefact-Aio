import git
import os


def fetch_update():
    # URL du dépôt distant
    repo_url = 'https://github.com/Kyrau-sys/Artefact-Aio'

    # Chemin actuel du script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Remonter d'un dossier
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Définir le chemin où le dépôt sera cloné
    repo_path = os.path.join(parent_dir, 'Artefact AIO Dashboard')

    # Si le dépôt n'existe pas localement, on le clone
    if not os.path.exists(repo_path):
        print(f"Clonage du dépôt {repo_url}...")
        repo = git.Repo.clone_from(repo_url, repo_path)
    else:
        # Si le dépôt existe déjà, on l'ouvre
        repo = git.Repo(repo_path)

    origin = repo.remotes.origin
    origin.fetch()

    local_commit = repo.head.commit
    remote_commit = repo.refs['origin/main'].commit

    return local_commit, remote_commit, repo_url, repo

