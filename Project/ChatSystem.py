# This is a Mini Chat System using OOP in Python.

# ----------------------
# Message Class
# ----------------------
class Message:
    # message ID
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    # dunder function
    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"

# ----------------------
# User Class
# ----------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)

# ----------------------
# Chatroom Class
# ----------------------
class Chatroom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\nChat history of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()

# ----------------------
# Demo / Testing
# ----------------------
chat = Chatroom("Python Room")

u1 = User("Aditya")
u2 = User("Rohan")

u1.join_chatroom(chat)
u2.join_chatroom(chat)

u1.send_message("Hello everyone!")
u2.send_message("Hi Aditya!")

u1.leave_chatroom()
u2.send_message("Looks like Aditya left!")

chat.show_chat_history()