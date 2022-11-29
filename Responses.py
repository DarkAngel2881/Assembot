#functions for date needings
from datetime import datetime

#filters for the responses based on the user text message
def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "what's up"):

        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        
        return "You can call me AssemBot and I am the way you can manage a request for a class assembly!"

    if user_message in ("date?", "date", "what day is it", "what day is it?", "day", "day?"):
        now = datetime.now()
        date_time = "Today is " + (now.strftime("%A %d of %B %Y"))

        return str(date_time)
    
    if user_message in ("time?", "time", "what time is it", "what time is it?"):
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S")

        return str(date_time)

    else:
        return "I didn't understand try again!"
