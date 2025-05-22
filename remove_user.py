import os
import sys
from github import Github

# Github token must be authorized member
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ORG_NAME = os.getenv("ORG_NAME")

def remove_user_from_org(username):
    if not GITHUB_TOKEN or not ORG_NAME:
        print("lack of environment variables GITHUB_TOKEN or ORG_NAME")
        return

    try:
        g = Github(GITHUB_TOKEN)
        org = g.get_organization(ORG_NAME)
        user = g.get_user(username)

        if org.has_in_members(user):
            org.remove_from_members(user)
            print(f" successfully remove user: {username}")
        else:
            print(f" user {username} is not organization member")
    except Exception as e:
        print(f" fail {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(" how to use: python remove_user.py <github_username>")
    else:
        remove_user_from_org(sys.argv[1])

