class User:
    
    def __init__(self, id, username):
        self.id = id
        self.username = username
        


user1 = User(1, "MooMan")


print(user1.id)
print(user1.username)