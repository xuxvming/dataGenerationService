from faker import Faker
from flaskWebApp.users.user import User
def generate_user(nums):
    user_list = []
    fake = Faker()
    id = 0;
    while id <= nums:
        user = User(id, fake.name(), fake.address(), fake.job())
        user_list.append(user)
        id += 1
    return user_list