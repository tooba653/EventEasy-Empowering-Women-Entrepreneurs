class User:
    def __init__(self, username, email, role="attendee"):
        self.username = username
        self.email = email
        self.role = role 
        self.bookings = []

    def book_event(self, event):
        self.bookings.append(event)
