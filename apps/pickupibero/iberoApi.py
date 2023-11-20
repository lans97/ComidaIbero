def ibero_auth(username, password):
    if username == "200490-A" and password == "Contra123$":
        return { 'username': username }
    else:
        return None
    # Your logic to authenticate with the external API
    # Return user information if authentication is successful, else return None
    # Example:
    # api_response = make_api_request(username, password)
    # if api_response and api_response.get('authenticated'):
    #     return {'username': username, 'other_data': api_response['other_data']}
    # else:
    #     return None
