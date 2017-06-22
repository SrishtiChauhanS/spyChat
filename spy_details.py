from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Srishti', 'Ms.', 20, 4.7)

friend_one = Spy('Anu', 'Ms.', 19, 4.7)
friend_two = Spy('Anna', 'Ms.', 23, 4.8)
friend_three = Spy('Ankita', 'Dr.', 24, 4.8)
friend_four = Spy('Prince', 'Mr..', 22, 4.9)
friend_five = Spy('Pooja', 'Ms.', 25, 4.9)
friend_six = Spy('Varsha', 'Dr.', 24, 4.9)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]