from repositories.user_repository import (
    get_all_users_from_db,
    get_user_from_db,
    add_user_to_db,
    update_user_in_db,
    remove_user_from_db
)

def get_all_users():
    return get_all_users_from_db()

def get_user_by_id(user_id):
    return get_user_from_db(user_id)

def create_new_user(data):
    return add_user_to_db(data)

def update_user_data(user_id, data):
    return update_user_in_db(user_id, data)

def delete_user_data(user_id):
    return remove_user_from_db(user_id)
