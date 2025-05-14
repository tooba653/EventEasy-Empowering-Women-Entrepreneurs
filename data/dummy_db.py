from models.platform import EventPlatform
from models.user import User
from models.event import Event
import datetime

platform = EventPlatform()


user1 = User("Tooba", "yameentooba653@gmail.com", role="organizer")
user2 = User("Alisha", "yameenAlisha897@gmail.com", role="attendee")
platform.register_user(user1)
platform.register_user(user2)

event1 = Event(
    title="Women Entrepreneurs Meetup",
    organizer=user1,
    description="A networking event for local women-led startups.",
    date=datetime.date(2025, 5, 25),
    location="Karachi, Pakistan",
    price=500
)

platform.create_event(event1)
