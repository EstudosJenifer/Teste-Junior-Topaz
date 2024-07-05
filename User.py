import requests
import unittest

class User:
    def __init__(self, name, html_url, public_repos, followers, following):
        self.name = name
        self.html_url = html_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following


def get_user(gitubuser: str) -> User:
    url = f"https://api.github.com/users/{gitubuser}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        user = User(data['name'], data['html_url'], data['public_repos'], data['followers'], data['following'])
        return user
    else:
        raise Exception(f"Falha ao obter os dados do usuário {gitubuser}. Status: {response.status_code}")


def get_user_repos(gitubuser: str) -> dict:
    url = f"https://api.github.com/users/{gitubuser}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        repo_dict = {repo['name']: repo['html_url'] for repo in repos}
        return repo_dict
    else:
        raise Exception(f"Falha ao obter os repositórios para o usuário {gitubuser}. Status: {response.status_code}")

def user_report(user: User, repos: dict) -> None:
    filename = f"gitubuser.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Nome: {user.name}\n")
        file.write(f"Perfil: {user.html_url}\n")
        file.write(f"Número de repositórios publicos: {user.public_repos}\n")
        file.write(f"Número de seguidores: {user.followers}\n")
        file.write(f"Número de usuários seguidos: {user.following}\n\n")
        
        file.write("Repositórios:\n")
        for repo_name, repo_url in repos.items():
            file.write(f"{repo_name}: {repo_url}\n")
    
    print(f"Relatório gerado: {filename}")

    # Observação: após relatório gerado, número atual de seguidores é de 11 pessoas


class TestMethods(unittest.TestCase):
    def test_user_class_has_minimal_parameters(self):
        user = get_user('githubuser')
        self.assertTrue(hasattr(user, 'name'))
        self.assertTrue(hasattr(user, 'html_url'))
        self.assertTrue(hasattr(user, 'public_repos'))
        self.assertTrue(hasattr(user, 'followers'))
        self.assertTrue(hasattr(user, 'following'))

    def test_get_user(self):
        user = get_user('githubuser')
        self.assertIsInstance(user, User)
    
    def test_get_user_repos(self):
        repos = get_user_repos('githubuser')
        self.assertIsInstance(repos, dict)
    
    def test_user_report(self):
        user = get_user('githubuser')
        repos = get_user_repos('githubuser')
        user_report(user, repos)


if __name__ == "__main__":
    unittest.main()



