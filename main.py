# class is a blueprint. To create a class, you use the class keyword followed by the name.
# We are building a class for a website.

# """class User:
#     pass  # we use this to have an empty function
#
#
# # create an object using the blueprint
#
# user_1 = User()
#
# # Note that pascal case is used for class case and snake case is used for everything else.
#
# # how do we create attribute for the class. An attribute is a variable that is associated with an object.
# user_1.id = '001'
# user_1.username = 'promise'
# print(user_1.username)
#
#
# # I can i specify statrting pieces of information when i create my class? I will use a constructor. A constructor helps us specify
# # wha should happen . We use the def __init__(self) which is use to initialise our attributes. Attributes are wha the variables will have."""
#


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        # print('new user being created')
        self.username = username
        self.followers = 0
        self.following = 0
        # we can set a default number

        # let's say we want to notify our followers when they get a new follower
        self.followers = 0
        self.following = 0

    # methods
    def follow(self, user):
        user.followers += 1
        user.following += 1

    # attributes are what the object have and method is what the methods are what the object does.
    # when a function is added to an object, it's called a method.


# now using the construct, we can pass in the attributes
#

user_1 = User('001', 'promise')
user_2 = User('002', 'Jack')

# lets say user1 decided to follow user2
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
print(user_2.followers)
print(user_2.following)
