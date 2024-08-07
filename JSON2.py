import json
from json import JSONEncoder
class User():
    def __init__(self, name, age):
        self.name=name
        self.age=age
user=User("Max", 23)
def encode_user(o):
    if isinstance(o, user):
        return {"name":o.name, "age":o.age, o.__class__.__name__:True}
    else:
        raise TypeError("ERRRR")

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name":o.name, "age":o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
#M1
userJSON=json.dumps(user, cls=UserEncoder)
#M2
userJSON1=UserEncoder().encode(user)
print(userJSON1)
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct
user=json.loads(userJSON1, object_hook=decode_user)
print(type(user))
print(user.name)
print(user.age)