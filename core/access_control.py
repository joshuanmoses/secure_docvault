from config.settings import ROLES
import json

def get_user_role(username):
    with open('data/users.json') as f:
        users = json.load(f)
    return users.get(username, {}).get('role')

def can_access(username, permission):
    role = get_user_role(username)
    if role and permission in ROLES.get(role, []):
        return True
    return False
