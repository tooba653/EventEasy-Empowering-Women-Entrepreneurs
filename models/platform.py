class EventPlatform:
    def __init__(self):
        self.users = []
        self.events = []

    def register_user(self, user):
        self.users.append(user)

    def create_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events
