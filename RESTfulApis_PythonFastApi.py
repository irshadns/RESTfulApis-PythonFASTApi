from fastapi import FastAPI
from pydantic import BaseModel  # used for in-memory database

cool_app = FastAPI()


class User(BaseModel):
    id: int
    name: str


root_msg = {
    'success': True,
    'message': 'Custom Server Running'
}


@cool_app.get('/')
def root():
    return root_msg


data = [
    {
        'id': 1,
        'name': 'Irshad'
    },
    {
        'id': 2,
        'name': 'Ashfaq'
    },
    {
        'id': 3,
        'name': 'Waqar'
    },
    {
        'id': 4,
        'name': 'Israr'
    }
]


@cool_app.get('/api/users')
def get_all_users():
    return data


@cool_app.get('/api/users/{id}')
def get_user(user_id: int):
    for ent in data:
        if user_id == ent['id']:
            return ent
    return "Invalid ID - ID doesn't exist"


@cool_app.post('/api/users/')
def add_user(user: User):
    data.append(user)
    return data


@cool_app.put('/api/users/{id}')
def update_user(user: User):
    for i in range(len(data)):
        if user.id == data[i]['id']:
            data[i]['name'] = user.name
            return 'Record Updated', data[i]

    else:
        return 'Invalid ID - Try with another ID'


@cool_app.delete('/api/users/{id}')
def delete_user(user_id: int):
    for i in range(len(data)):
        if user_id == data[i]['id']:
            deleted_rec = data[i]
            del data[i]
            return 'Deleted Record', deleted_rec, 'Updated Records:', data
    else:
        return 'Invalid ID - Try with another ID'
