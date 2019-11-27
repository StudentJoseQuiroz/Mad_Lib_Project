"""
This is my main file for this story telling program
__author__= Jose Quiroz
"""


# Jose Quiroz aka Mister Sweet
# Mad Lib Story Program


def get_name():
    """Demonstrates get_name function and asks for name input, also returns
    name"""
    print("")
    name = input("Greetings, what do we call you?: ")
    return name


# Greeting
def greeting(name):
    """Demonstrates greeting function with name input"""
    print("")
    print(
        "Welcome to Mister Sweet's Mad Lib Story Telling Journey " + name +
        " :)")
    print("")


# Story choice
def choose_story():
    """Demonstrates choose_story function when called and asks for story
    option input to then call one of the three story choices"""
    madLibQ = input(
        "Now there are two mad lib stories you can journey through, "
        "which story would you like to choose? 1 or 2?: ")
    # Mad Lib Story #1
    if madLibQ == "1":
        madlib1()
    # Mad Lib Story #2
    elif madLibQ == "2":
        madlib2()
    else:
        print("")
        print("Invalid entry. Please try again.")
        print("")
        choose_story()


# Mad Lib Story #1
def madlib1():
    """Demonstrates madlib1 function, which is primarily called by the user's
    choice, and it asks the user to input answers for their correlating
    questions to fill in the blanks for the story it is going to print. In this
    example, story choice #1"""
    print("\n")
    print(
        "Alright! First let me ask you a few questions to get the story "
        "telling started.")
    print("Please make sure to not misspell your answers.")
    print("")
    question1 = input(
        "Choose any female name for your main character. Please capitalize "
        "the name: ")
    question2 = input(
        "Choose any male name for your second main character. Please "
        "capitalize the name: ")
    question3 = input(
        "Choose one of the following verbs: run, smash, or explode: ")
    question4 = input(
        "Choose one of the following adjectives: smelly, hairy, or shiny: ")
    question5 = input(
        "Choose one of the following verbs: tripped, tumbled, or collided: ")
    question6 = input("Choose any number from 2-100: ")
    question7 = input(
        "Choose one of the following nouns: chicken-nugget, fork, "
        "or jolly-rancher: ")
    question8 = input(
        "Choose one of the following names: Toby From HR, ToeJam, or McLovin: ")
    question9 = input(
        "Choose one of the following verbs: launch, toss, kick: ")
    question10 = input(
        "Choose one of the following adjectives: god-like, mystic, "
        "or superhuman: ")
    question11 = input(
        "Choose one of the following nouns: hot air balloon, walrus, "
        "or category 5 hurricane: ")
    question12 = input(
        "Choose one of the following adjectives: baffled, drunk, "
        "or dehydrated: ")
    print("")
    print("EXCELLENT, Let the story telling commence.")
    print("\n")
    print("ONCE UPON A TIME...")
    print("There was a young grasshopper named", question1, "that loved to",
          question3, "through walls.")
    print(question1,
          "had incredible super grasshopper strength and always hopped as if "
          "nothing around her mattered.\nOne day",
          question1, "ran into a very", question4, "frog named",
          question2 + '.')
    print(question1, "only knew this frog's name because he had a nametag on.")
    print(question2, "was so startled by", question1 + "'s approach that he",
          question5,
          "against a nearby mushroom causing him to spin out of control and "
          "completely collapse on the ground.")
    print("As", question2, "laid there completely unconscious,", question1,
          "tried her best to get it together and see if", question2,
          "was alright.")
    print(question1, "got closer to", question2,
          "and for whatever reason started to get the sense that something "
          "harmful was approaching them.")
    print("Without hesitation", question1, "quickly grabbed", question2,
          "with her super strength and started to hop away from whatever she "
          "sensed.")
    print(question1, "only got to hop away", question6,
          "times before she ran into a wall that for some reason she couldn't",
          question3, "through.")
    print(question1,
          "desperately tried to go around the wall that seemed to be as long "
          "as the Wall of China, but it was too late...it had caught up to "
          "them.\nShe turned around still carrying an unconscious",
          question2 + ',', "to make eye-contact with a...", question7 + '...',
          "who had keyboards for hands and coded for fun.")
    print(question1, "was so surprised she hopped straight up in the air",
          question6,
          "times. SHE COULDN'T BELIEVE IT, it was...IT WAS...the one and "
          "only..." + question8 + ',',
          "her arch nemesis.")
    print("Before she could use her super strength to power", question9,
          question2,
          "to safety, a sudden...ribbit interrupted her.")
    print(question2, "had finally woken up and looked",
          question10 + ", for an amphibian that is.")
    print("As", question2,
          "got up on his froglegs, he let out another roar-like ribbit and "
          "started huffing and puffing like your stereotypical big bad "
          "wolf.\nHe grew as big as a",
          question11, "and turned directly to", question8,
          "while standing in a karate fighting stance.")
    print(question8, "looked extremely", question12, "at the sight of",
          question2 + "'s appearance that he turned around and ran for his",
          question7 + "-like life.")
    print(question1 + " and " + question2,
          "looked at each other, knowing exactly what had to be done "
          "next.\nThey combined their super power abilities to destroy the "
          "wall in a matter of minutes, incase anyone else without the "
          "blessing of super power abilities ever got in the situation they "
          "were just in.\nAfterwards they decided they would journey "
          "together and spread peace across their existing worlds.\nThey "
          "hopped into the setting sun horizon and disappeared for eternity.")
    print("")
    print("THE END.")
    print("\n")
    outro()


# Mad Lib Story #2
def madlib2():
    """Demonstrates madlib2 function, which is primarily called by the user's
    choice, and it asks the user to input answers for their correlating
    questions to fill in the blanks for the story it is going to print. In this
    example, story choice #1"""
    print("\n")
    print(
        "Alright! First let me ask you a few questions to get the story "
        "telling started.")
    print("Please make sure to not misspell your answers.")
    print("")
    question1 = input("Choose any male name for your protagonist: Please "
                      "capitalize the name: ")
    question2 = input("Choose any male name for your antagonist: Please "
                      "capitalize the name: ")
    question3 = input("Choose one of the following verbs: jump, squat, "
                      "or spin: ")
    question4 = input("Choose one of the following adjectives: kooky, "
                      "fluffy, or confused: ")
    question5 = input("Choose one of the following nouns: toothbrush, "
                      "shoe, "
                      "or bottle-cap: ")
    question6 = input("Choose one of the following verbs: tickled, poked, "
                      "or tackled: ")
    question7 = input("Choose one of the following nouns: Please "
                      "capitalize the noun: Diaper, Dandelion, "
                      "or Diva: ")
    question8 = input("Choose one of the following adjectives: aggressive, "
                      "attentive, or affordable: ")
    question9 = input("Choose one of the following items: AAA battery, "
                      "Q-tip, or USB: ")
    question10 = input("Choose one of the following adjectives: blank, "
                       "happy, "
                       "or sideways: ")
    question11 = input("Choose one of the following adjectives: noisy, "
                       "stinky, or deadly: ")
    print("")
    print("EXCELLENT, Let the story telling commence.")
    print("\n")
    print("ONCE UPON A TIME...")
    print("There was a young king named", question1 + ',' + " who ruled a "
                                                            "magical "
                                                            "land called",
          question7, "Desert.\nThis piece of land's name was a sort of "
                     "misnomer "
                     "because it wasn't a desert at all, it was in fact an "
                     "island.\nBut having been deserted for centuries by it's "
                     "past inhabitants, "
                     "king",
          question1, "decided to name the land over it's loneliness.")
    print("The other reason king", question1, "named the land", question7,
          "Desert was because it was full of them.", question7 + 's' + " "
                                                                       "that "
                                                                       "is.")
    print("As king", question1, "woke up one day, he practiced his morning "
                                "routine where he would", question3,
          "for 2 full hours before "
          "eating breakfast.")
    print("But this morning struck king", question1, "differently.\nHe was "
                                                     "feeling rather",
          question4, "for whatever unknown reason.\nTherefore he concluded "
                     "that "
                     "only one person was to blame for this...it had to "
                     "have "
                     "been because of lord", question2 + ',' + " HAD TO HAVE "
                                                               "BEEN, "
                                                               "the king "
                                                               "thought to "
                                                               "himself.")
    print("He decided to confront lord",
          question2 + ',' + " his evil twin brother "
                            "who ruled Vapor "
                            "Valley. A land full of "
                            "vapor.")
    print("The king decided he was going to get to the bottom of this issue "
          "and use his ultimate weapon, which was a", question5 + ',' +
          " to destroy "
          "his twin "
          "for making "
          "him feel",
          question4 + '.')
    print("As the king walked over to his ship to sail to Vapor Valley, "
          "he was suddenly", question6, "by someone.")
    print("He regained his altered focus and turned to his girlfriend,",
          question8, "Ashley.\nShe had rushed to him to tell him that it "
                     "wasn't "
                     "his evil twin that made him feel", question4 + ',' +
          " it as "
          "was "
          "something"
          " else.")
    print("She continued to explain that it was because he forgot to carry "
          "his lucky", question9, "while he slept.")
    print("King", question1, "looked at", question8, "Ashley with "
                                                     "disbelief. He "
                                                     "couldn't entirely "
                                                     "believe it.")
    print("The king turned turned back to his ship, and there he "
          "was...lord",
          question2, "surrounded by his loyal", question11, "minions.")
    print("The king looked at his twin with a", question10, "facial "
                                                            "expression "
                                                            "knowing what "
                                                            "was about to "
                                                            "happen.")
    print("The king hit one single", question3, "and his ship exploded into "
                                                "a million pieces...")
    print(question7, "Desert remained untouched by his evil twin and king",
          question1, "continued ruling the land until eventually his son took "
                     "over.\nWho was named after himself and the land, Sir",
          question1,
          question7,
          "Jr.")
    print("")
    print("THE END.")
    print("\n")
    outro()


# Intro
def intro():
    """Demonstrates intro function, that asks the user to pick a story,
    either 1 or 2"""
    introAnswer = input(
        "Would you like to board the story telling journey?: Yes or no?: ")
    if introAnswer == "yes" or introAnswer == "Yes":
        print("\n")
        print("GREAT! Let us begin!")
        print("")
        choose_story()
    elif introAnswer == "no" or introAnswer == "No":
        print("")
        print("How unfortunate! Very well my friend, farewell and stay swell",
              name + '!')
    else:
        print("")
        print("Invalid entry. Please try again.")
        print("")
        intro()


# Outro
def outro():
    """Demonstrates outro function, that asks for feedback from user and
    whether or not they want to choose another story"""
    outroAnswer = input(
        "Did you like Mister Sweet's Mad Lib journey?: Yes or no?: ")
    if outroAnswer == "yes" or outroAnswer == "Yes":
        print("")
        print("Mister Sweet appreciates your positive feedback! :)")
        print("")
        outroAnswer2 = input(
            "Did you want to journey through another Mister Sweet mad lib "
            "story?: Yes or no?: ")
        if outroAnswer2 == "yes" or outroAnswer2 == "Yes":
            print("")
            choose_story()
        else:
            print("")
            print(
                "Well swing back around for another story telling journey "
                "whenever you please! :)")
    elif outroAnswer == "no" or outroAnswer == "No":
        print("")
        print(
            "How unfortunate, please come by another time for a different "
            "story telling journey.")
    else:
        print("")
        print("Invalid entry. Please try again.")
        print("")
        outro()


name = get_name()
greeting(name)
intro()
