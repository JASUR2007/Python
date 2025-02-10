from abc import ABC, abstractmethod
# Task 8: Sports Tournament
# Define an abstract class Sport with abstract methods:
# play()
# get_winner()

# Create concrete classes Football, Cricket, and Tennis. Write a program to simulate playing these sports and determine the winner.

class Sport(ABC):
    def __init__(self, quantity_players, teams):
        self.quantity_players = quantity_players
        self.teams = teams
        self.scores = {}

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def winner(self):
        pass

class Football(Sport):
    def __init__(self, quantity_players, teams, scores):
        super().__init__(quantity_players, teams)
        self.scores = scores

    def play(self):
        print(f"Футбол, количество:{self.quantity_players} игроками в командах: {self.teams}.")
        print(f"Счет: {self.scores}")

    def winner(self):
        if self.scores[0] > self.scores[1]:
            print(f"Победитель: {self.teams[0]}")
        elif self.scores[0] < self.scores[1]:
            print(f"Победитель: {self.teams[1]}")
        else:
            print("Ничья!")

class Cricket(Sport):
    def __init__(self, quantity_players, teams, scores):
        super().__init__(quantity_players, teams)
        self.scores = scores

    def play(self):
        print(f"Играем в крикет с {self.quantity_players} игроками в командах: {self.teams}.")
        print(f"Счет: {self.scores}")

    def winner(self):
        if self.scores[0] > self.scores[1]:
            print(f"Победитель: {self.teams[0]}")
        elif self.scores[0] < self.scores[1]:
            print(f"Победитель: {self.teams[1]}")
        else:
            print("Ничья!")

class Tennis(Sport):
    def __init__(self, quantity_players, teams, scores):
        super().__init__(quantity_players, teams)
        self.scores = scores

    def play(self):
        print(f"Играем в теннис между игроками: {self.teams}.")
        print(f"Счет: {self.scores}")

    def winner(self):
        if self.scores[0] > self.scores[1]:
            print(f"Победитель: {self.teams[0]}")
        elif self.scores[0] < self.scores[1]:
            print(f"Победитель: {self.teams[1]}")
        else:
            print("Ничья!")


football_game = Football(quantity_players=22, teams=["Chelsi", "Real"], scores=[3, 2])
football_game.play()
football_game.winner()


cricket_game = Cricket(quantity_players=22, teams=["K", "Y"], scores=[250, 200])
cricket_game.play()

# Task 9: File Reader and Writer
# Create an abstract class FileHandler with the following abstract methods:
# read_file()
# write_file(data)
# Implement concrete classes for TextFileHandler and CSVFileHandler. Write a program to read and write data using both classes.

import csv

class FileHandler(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, data):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

class CSVFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def write_file(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

text_handler = TextFileHandler('example.txt')
text_handler.read_file()
print("Text File Read:", text_handler.read_file())


# Task 10: Notification System
# Define an abstract class Notification with abstract methods:
# send_notification(message)
# get_status()
# Implement concrete classes EmailNotification, SMSNotification, and PushNotification. Write a program to send notifications using all types.


from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self):
        self.status = "Pending"

    @abstractmethod
    def send_notification(self, message):
        pass

    def get_status(self):
        return self.status

class EmailNotification(Notification):
    def send_notification(self, message):
        print(f"Sending Email: {message}")
        self.status = "Sent via Email"

class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")
        self.status = "Sent via SMS"

class PushNotification(Notification):
    def send_notification(self, message):
        print(f"Sending Push Notification: {message}")
        self.status = "Sent via Push Notification"

email_not = EmailNotification()
sms_not = SMSNotification()
push_not = PushNotification()

email_not.send_notification("Заказ принят.")
print("Email Status:", email_not.get_status())

sms_not.send_notification("Заказ принят.")
print("SMS Status:", sms_not.get_status())

push_not.send_notification("Заказ принят")
print("Push Notification Status:", push_not.get_status())