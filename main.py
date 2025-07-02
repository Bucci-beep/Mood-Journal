def welcome_user():
    print("Hi, welcome to your mood journal.")

def get_user_mood():
    # Asks the user how they’re feeling
    mood = input("How are you feeling today? ")
    return mood

def response(mood):
    # Responds with a message based on their input
    print("\nThanks for sharing. Here is something for you.")

    if mood.lower() == "happy":
        poem = """
        Sunshine laughter fills the air,  
        Your joy is something bright and rare.  
        Hold on to that spark so true,  
        And let your happiness carry you.
        """

    elif mood.lower() == "sad":
        poem = """
        Rain may fall, the skies may gray,  
        But storms will always pass away.  
        Hold on gently, take your time,  
        Even sadness has its rhyme.
        """

    elif mood.lower() == "tired":
        poem ="""
        Rest your mind, and close your eyes,  
        You've carried weight, you've reached the skies.  
        Take a break and just be still,  
        Your strength will rise; it always will.
        """
        
    else:
        poem = """
        If all trees die, if all trees go,  
        Where will our beautiful flowers grow?  
        No shade, no shelter,  
        What a shame!
        """

    print(poem)

def main():
    welcome_user()
    mood_today = get_user_mood()
    response(mood_today)
    print("Have a peaceful day!")

main()