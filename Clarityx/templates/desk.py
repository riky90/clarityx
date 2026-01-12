import datetime

class User:
    def __init__(self, name):
        self.name = name

class Desk:
    def __init__(self, number):
        self.number = number
        self.booked = False
        self.booked_by = None
        self.date_booked = None

class BookingSystem:
    def __init__(self):
        self.desks = [Desk(i) for i in range(1, 12)]
        self.users = []

    def create_user(self, name):
        new_user = User(name)
        self.users.append(new_user)
        return new_user

    def book_desk(self, user, date):
        if date < datetime.date.today() or date > (datetime.date.today() + datetime.timedelta(days=30)):
            return "Invalid date, please choose a date between today and one month ahead."
        for desk in self.desks:
            if not desk.booked:
                desk.booked = True
                desk.booked_by = user
                desk.date_booked = date
                return f"Desk {desk.number} has been successfully booked for {user.name} on {date}."
        return "All desks are booked for the chosen date."

    def check_availability(self, date):
        available_desks = []
        for desk in self.desks:
            if not desk.booked or desk.date_booked != date:
                available_desks.append(desk.number)
        return available_desks