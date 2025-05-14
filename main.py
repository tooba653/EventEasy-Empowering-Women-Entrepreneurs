import streamlit as st
from data.dummy_db import platform, user1, user2
from models.event import Event
import datetime

st.set_page_config(page_title="EventEasy", layout="centered")

st.title("🧕 EventEasy - Empowering Women Entrepreneurs")

user_role = st.sidebar.selectbox("Select Role", ["Attendee", "Organizer"])
current_user = user1 if user_role == "Organizer" else user2

st.sidebar.markdown(f"**Logged in as:** `{current_user.username}`")

menu = st.sidebar.radio("Menu", ["View Events", "Create Event", "My Bookings"])

if menu == "View Events":
    st.subheader("📅 Upcoming Events")
    events = platform.get_events()

    if events:
        for event in events:
            with st.expander(f"🎉 {event.title}"):
                st.write(f"**Organizer:** {event.organizer.username}")
                st.write(f"**Date:** {event.date}")
                st.write(f"**Location:** {event.location}")
                st.write(f"**Price:** Rs. {event.price}")
                st.write(event.description)

                if user_role == "Attendee":
                    if st.button(f"Book Now - {event.title}"):
                        event.add_attendee(current_user)
                        current_user.book_event(event)
                        st.success("🎟️ Booking Confirmed!")
    else:
        st.info("No events available.")

elif menu == "Create Event" and user_role == "Organizer":
    st.subheader("📝 Create New Event")

    title = st.text_input("Event Title")
    description = st.text_area("Event Description")
    date = st.date_input("Event Date", min_value=datetime.date.today())
    location = st.text_input("Event Location")
    price = st.number_input("Ticket Price (Rs)", min_value=500)

    if st.button("Create Event"):
        new_event = Event(title, current_user, description, date, location, price)
        platform.create_event(new_event)
        st.success("✅ Event created successfully!")

elif menu == "My Bookings":
    st.subheader("🎟️ My Booked Events")

    if current_user.bookings:
        for e in current_user.bookings:
            st.write(f"- **{e.title}** on {e.date} at {e.location}")
    else:
        st.info("You haven't booked any events yet.")

elif menu == "Create Event" and user_role == "Attendee":
    st.warning("Only organizers can create events.")
