# Utils Section
import random
from PIL import Image

def generate_story(name, age, city, animal, genre):
    # Define possible actions, settings, and obstacles based on genre
    if genre == 'adventure':
        actions = ['went on an adventure', 'explored a new land', 'faced their fears', 'discovered a hidden treasure']
        settings = ['a dense jungle', 'a rugged mountain', 'an uncharted island', 'a wild safari']
        obstacles = ['a raging river', 'a dangerous cliff', 'a band of pirates', 'a treacherous storm']
    elif genre == 'mystery':
        actions = ['solved a mystery', 'unraveled a conspiracy', 'cracked a code', 'unveiled a secret']
        settings = ['an old mansion', 'a deserted town', 'a dark alley', 'an abandoned warehouse']
        obstacles = ['a locked door', 'a hidden message', 'a suspicious character', 'a dark secret']
    elif genre == 'fantasy':
        actions = ['went on a magical journey', 'fought a dragon', 'saved a kingdom', 'met a wizard']
        settings = ['a mystical forest', 'an enchanted castle', 'a hidden village', 'a magical kingdom']
        obstacles = ['a wicked sorcerer', 'an evil curse', 'a mythical beast', 'a dark prophecy']
    
    # Select a random action, setting, and obstacle
    action = random.choice(actions)
    setting = random.choice(settings)
    obstacle = random.choice(obstacles)
    
    # Generate the story using the input information and the randomly selected action, setting, and obstacle
    story = f"Once upon a time, there was a young {age}-year-old named {name} who lived in {city}. One day, {name} and their trusty sidekick {animal}, {action} in {setting}. But soon, they discovered {obstacle} blocking their path. With quick thinking and bravery, {name} and {animal} overcame the {obstacle} and continued on their {genre} adventure. In the end, they emerged victorious and returned home as heroes!"
    
    # Generate an image based on the setting
    image_file = f"{setting.lower().replace(' ', '_')}.jpg"
    img = Image.open(image_file)
    img.show()
    
    return story

"""# Use"""

# Use Section
if __name__ == "__main__":
    print("Welcome to the Story Generator!\n")
    name = input("What is the name of the main character? ")
    age = input("What is the age of the main character? ")
    city = input("In which city does the character live? ")
    animal = input("What is the name of the character's trusty sidekick animal? ")
    genres = ['adventure', 'mystery', 'fantasy']
    print("Please select a genre for the story:")
    for i, genre in enumerate(genres):
        print(f"{i+1}. {genre}")
    genre_choice = int(input())
    genre = genres[genre_choice - 1]

    # Generate and print the story using the input information
    story = generate_story(name, age, city, animal, genre)
    print("\nHere is your story:\n")
    print(story)