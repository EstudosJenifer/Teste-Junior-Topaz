import requests
import unittest

class UserJenifer:
    def __init__(self, name, html_url, public_repos, followers, following):
        self.name = name
        self.html_url = html_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following


def get_user(EstudosJenifer: str) -> UserJenifer:
    url = f"https://api.github.com/users/{EstudosJenifer}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        user = UserJenifer(data['name'], data['html_url'], data['public_repos'], data['followers'], data['following'])
        return user
    else:
        raise Exception(f"Falha ao obter os dados do usuário {EstudosJenifer}. Status: {response.status_code}")


def get_user_repos(EstudosJenifer: str) -> dict:
    url = f"https://api.github.com/users/{EstudosJenifer}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        repo_dict = {repo['name']: repo['html_url'] for repo in repos}
        return repo_dict
    else:
        raise Exception(f"Falha ao obter os repositórios para o usuário {EstudosJenifer}. Status: {response.status_code}")

def user_report(user: UserJenifer, repos: dict) -> None:
    filename = f"EstudosJenifer.txt"
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

    

class TestMethods(unittest.TestCase):
    def test_user_class_has_minimal_parameters(self):
        user = get_user('EstudosJenifer')
        self.assertTrue(hasattr(user, 'name'))
        self.assertTrue(hasattr(user, 'html_url'))
        self.assertTrue(hasattr(user, 'public_repos'))
        self.assertTrue(hasattr(user, 'followers'))
        self.assertTrue(hasattr(user, 'following'))

    def test_get_user(self):
        user = get_user('EstudosJenifer')
        self.assertIsInstance(user, UserJenifer)
    
    def test_get_user_repos(self):
        repos = get_user_repos('EstudosJenifer')
        self.assertIsInstance(repos, dict)
    
    def test_user_report(self):
        user = get_user('EstudosJenifer')
        repos = get_user_repos('EstudosJenifer')
        user_report(user, repos)


if __name__ == "__main__":
    unittest.main()



