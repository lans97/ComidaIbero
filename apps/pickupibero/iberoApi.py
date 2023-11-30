import re

def ibero_auth(username, password):
    user_patern = r'^\d{6}-[A-Z0-9]$'
    password_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{10}$'
    if re.match(user_patern, username) and re.match(password_pattern, password):
        return { 'username': username }
    else:
        return None
