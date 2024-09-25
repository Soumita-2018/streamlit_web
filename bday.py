import streamlit as st
import random
from datetime import datetime, timedelta

# Set the title and description
st.set_page_config(page_title="🎉 Epic Birthday Bash 🎉", page_icon="🎂", layout="wide")

st.title("🎂 Celebrate Like Never Before! 🎉")
st.subheader("Make the most of this special day with surprises and joy!")

# Sidebar Music Player
# Sidebar Music Player
def play_music():
    music_file = 'bday.mp3'
    st.sidebar.markdown("**🎶 Add some birthday vibes!**")
    st.sidebar.audio(music_file, format="audio/mp3", start_time=0)

play_music()



# GIF Animation to kick things off
st.image("birthday.gif", caption="Let the party begin! 🎉", use_column_width=True)





# Get the birthday person's name
name = st.text_input("Enter the birthday person's name:")

# Add Birthday Countdown
birthday = st.date_input("Select the birthday date:", min_value=datetime.today())
days_to_go = (birthday - datetime.today().date()).days
if days_to_go > 0:
    st.info(f"Only {days_to_go} days until {name}'s birthday! 🎉")

# Add a live countdown timer until midnight of their birthday
if birthday == datetime.today().date():
    current_time = datetime.now().time()
    birthday_midnight = datetime.combine(birthday, datetime.min.time())
    remaining_time = birthday_midnight - datetime.now()
    st.metric("Time left to celebrate", str(remaining_time))

# Rotating Birthday Quotes Carousel
birthday_quotes = [
    "“Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!”",
    "“The more you praise and celebrate your life, the more there is in life to celebrate.” – Oprah Winfrey",
    "“Today you are you! That is truer than true! There is no one alive who is you-er than you!” – Dr. Seuss",
    "“You are never too old to set another goal or to dream a new dream.” – C.S. Lewis",
    "“A birth-date is a reminder to celebrate the life as well as to update the life.” – Amit Kalantri"
]
quote = random.choice(birthday_quotes)
st.subheader(f"💬 Birthday Quote of the Moment:")
st.write(quote)

# Personalized Video Surprise
st.video("https://www.youtube.com/watch?v=piWcA289stE")
st.write("🎥 Special Birthday Video Just for You!")


# Add gift ideas
st.markdown("### 🎁 Need some gift ideas?")
gift_suggestions = [
    "🎁 Personalized photo album of special moments",
    "🎁 A subscription to their favorite streaming service",
    "🎁 A handmade scrapbook with messages from friends",
    "🎁 A surprise weekend getaway",
    "🎁 Custom jewelry with initials or birthstone"
]
for gift in gift_suggestions:
    st.markdown(gift)

# Show celebration progress
progress = ((datetime.now() - datetime.combine(datetime.today(), datetime.min.time())).seconds) / 86400 * 100
st.progress(int(progress))

# Display a fun birthday message
def generate_wish(name):
    wishes = [
        f"🎉 Woohoo, {name}! Let's make this birthday one for the books! 🎉",
        f"🎂 Happy Birthday, {name}! Here's to loads of fun, laughter, and celebration! 🎂",
        f"🎁 {name}, the world is celebrating YOU today! Let's make it epic! 🎁",
        f"💃 Let's dance all day, {name}! Celebrate YOU in every way! 💃",
        f"🎉 {name}, it's your day to shine. Make it spectacular! 🎉"
    ]
    return random.choice(wishes)

if st.button("Generate Birthday Wish"):
    if name:
        st.subheader(f"Dear {name},")
        st.write(generate_wish(name))
        st.balloons()  # Fire off some celebratory balloons
        st.snow()  # Add some extra festive fun
    else:
        st.warning("Please enter a name to generate a birthday wish.")

# Display current date and time
st.write("🎈 Wish generated on:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
