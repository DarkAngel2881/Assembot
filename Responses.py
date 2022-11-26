from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "what's up"):
        
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        
        return "You can call me AssemBot and I am the way you can manage a request for a class assembly!"

    if user_message in ("what time is it?", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y", "%h:%m:%s")

        return str(date_time)

    else:
        return "I didn't understand try again!"
