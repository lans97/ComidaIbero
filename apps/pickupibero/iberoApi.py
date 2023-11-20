def ibero_auth(username, password):
    if username == "200490-A" and password == "Contra123$":
        return { 'username': username }
    else:
        return None
