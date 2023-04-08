# Reference: https://github.com/zzsza/github-action-with-python/blob/master/github_utils.py

import os
from datetime import datetime
from pytz import timezone
from github import Github


def get_github_repo(access_token, repository_name):
    github = Github(access_token)
    return github.get_user().get_repo(repository_name)


def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "github-action"

    # Get GitHub repository
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)

    # Upload GitHub issue
    today = datetime.now(timezone('Asia/Seoul'))
    title = f"Issue of {today.strftime('%Y-%m-%d')}"
    content = f"[This issue is created by github action]"
    content += f"Today is {today.strftime('%Y-%m-%d')}."
    content += f"Have a good day."
    repo.create_issue(title, content)

    print("Done.")
