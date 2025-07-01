def welcome_user():
    print("Hi, welcome to your mood journal.")

def get_user_mood():
    # Asks the user how they’re feeling
    mood = input("How are you feeling today? ")
    return mood

def response(mood):
    # Responds with a message based on their input
    print("\nThanks for sharing. Here is something for you.")

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