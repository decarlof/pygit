import subprocess

from github import Github

def get_sha(repo): 
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo).decode('ascii').strip() 
    return sha

def read_token():
    with open ("access_token.txt", "r") as myfile:
        data=myfile.readlines()
    
    return data[0]

def main():
    #print(get_sha('.'))
    # First create a Github instance:


    # using token instead of username/password
    g = Github(read_token())
    print(g)

    user = g.get_user()
    repos = g.get_user().get_repos()
    print(user.login)
    print(user.name)
    
    repo = g.get_repo("decarlof/pygit")
    print(repo.name)

    contents = repo.get_contents("example.py")
    print(contents)

    # Then play with your Github objects:
    #for repo in g.get_user().get_repos():
    #    print(repo.name)


    #repo = g.get_repo("decarlof/pygit")
    #print(repo.name)

    #contents = repo.get_contents("README.md")
    #print(contents)

    #contents = repo.get_contents("example.py")
    #print(contents)
    #repo.update_file(contents.path, "2018-11/chawla/sample_name", 'xx', contents.sha)    
    
    # or using an access token
    #g = Github("access_token")

    # Github Enterprise with custom hostname
    #g = Github(base_url="https://github.com/PyGithub/PyGithub", login_or_token="access_token")

    # Then play with your Github objects:
    #for repo in g.get_user().get_repos():
    #    print(repo.name)


if __name__ == '__main__':
    main()