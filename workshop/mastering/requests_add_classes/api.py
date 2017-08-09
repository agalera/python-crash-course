from bottle import get, post, put, delete, request, run, HTTPError


users = {}


@get('/')
def hello():
    return {'hello': 'world'}


@post('/headers')
def headers():
    return {'post': request.json, 'headers': request.headers}


@get('/users')
def get_users():
    return users


@get('/user/<username>')
def get_user(username):
    if username in users:
        return users[username]
    return HTTPError(404, {'msg': 'user not found'})


@post('/user')
def create_user():
    if 'username' not in request.json:
        return HTTPError(400, {'msg': 'key username is required'})

    if request.json['username'] not in users:
        users[request.json['username']] = request.json
        return request.json
    return HTTPError(400, {'msg': 'user exists'})


@put('/user/<username>')
def update_user(username):
    users[username] = request.json
    return users[username]


@delete('/user/<username>')
def delete_user(username):
    try:
        users.pop(username)
    except KeyError:
        return HTTPError(404, {'msg': 'User %s not exists' % username})


if __name__ == "__main__":
    run(bind='0.0.0.0', port=8008)
