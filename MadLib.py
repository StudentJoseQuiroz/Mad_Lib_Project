# Jose Quiroz aka Mister Sweet
# Mad Lib Story Program
# Very first question
print("")
name = input("Greetings, what do we call you?: ")
# Greeting
def greeting():
    print("")
    print("Welcome to Mister Sweet's Mad Lib Story Telling Journey " + name + " :)")
    print("")
greeting()
introAnswer = input("Would you like to board the story telling journey?: Yes or no?: ")
if introAnswer == "yes" or introAnswer == "Yes":
    print("\n")
    print("GREAT! Let us begin!")
    print("")
# Story choice
    def stories():
        madLibQ = input("Now there are three mad lib stories you can journey through, which story would you like to choose? 1, 2, or 3?: ")
# Mad Lib Story #1
        if madLibQ == "1":
            def madLib1():
                print("\n")
                print("Alrighty! First let me ask you a few questions to get the story telling started.")
                print("")
                question1 = input("Choose any female name for your main character. Please capitalize the name: ")
                question2 = input("Choose any male name for your second main character. Please capitalize the name: ")
                question3 = input("Choose one of the following verbs: run, smash, or explode: ")
                question4 = input("Choose one of the following adjectives: smelly, hairy, or shiny: ")
                question5 = input("Choose one of the following verbs: tripped, tumbled, or collided: ")
                question6 = input("Choose any number from 2-100: ")
                question7 = input("Choose one of the following nouns: chicken-nugget, fork, or jollyrancher: ")
                question8 = input("Choose one of the following names: Toby From HR, ToeJam, or McLovin: ")
                question9 = input("Choose one of the following verbs: launch, toss, kick: ")
                question10 = input("Choose one of the following adjectives: god-like, mystic, or superhuman: ")
                question11 = input("Choose one of the following nouns: hot air balloon, walrus, or category 5 hurricane: ")
                question12 = input("Choose one of the following adjectives: baffled, drunk, dehydrated: ")
                print("")
                print("EXCELLENT, Let the story telling commence.")
                print("\n")
                print("ONCE UPON A TIME...")
                print("There was a young grasshopper named", question1, "that loved to", question3, "through walls.")
                print(question1, "had incredible super grasshopper strength and always hopped as if nothing around her mattered.\nOne day", question1, "ran into a very", question4, "frog named", question2+'.')
                print(question1, "only knew this frog's name because he had a nametag on.")
                print(question2, "was so startled by", question1+"'s approach that he", question5, "against a nearby mushroom causing him to spin out of control and completely collapse on the ground.")
                print("As", question2, "laid there completely unconscious,", question1, "tried her best to get it together and see if", question2, "was alright.")
                print(question1, "got closer to", question2, "and for whatever reason started to get the sense that something harmful was approaching them.")
                print("Without hesitation", question1, "quickly grabbed", question2, "with her super strength and started to hop away from whatever she sensed.")
                print(question1, "only got to hop away", question6, "times before she ran into a wall that for some reason she couldn't", question3,"through.")
                print(question1, "desperately tried to go around the wall that seemed to be as long as the Wall of China, but it was too late...it had caught up to them.\nShe turned around still carrying an unconscious", question2+',', "to make eye-contact with a...", question7+'...', "who had keyboards for hands and coded for fun.")
                print(question1, "was so surprised she hopped straight up in the air", question6, "times. SHE COULDN'T BELIEVE IT, it was...IT WAS...the one and only..."+question8+',', "her arch nemesis.")
                print("Before she could use her super strength to power", question9, question2, "to safety, a sudden...ribbit interrupted her.")
                print(question2, "had finally woken up and looked", question10+", for an amphibian that is.")
                print("As", question2, "got up on his froglegs, he let out another roar-like ribbit and started huffing and puffing like your stereotypical big bad wolf.\nHe grew as big as a", question11, "and turned directly to", question8, "while standing in a karate fighting stance.")
                print(question8, "looked extremely", question12, "at the sight of", question2+"'s appearance that he turned around and ran for his", question7+"-like life.")
                print(question1+" and "+question2, "looked at each other, knowing exactly what had to be done next.\nThey combined their super power abilities to destroy the wall in a matter of minutes, incase anyone else without the blessing of super power abilities ever got in the situation they were just in.\nAfterwards they decided they would journey together and spread peace across their existing worlds.\nThey hopped into the setting sun horizon and disappeared for eternity.")
                print("")
                print("THE END.")
                print("\n")
                def outro():
                    outroAnswer = input("Did you like Mister Sweet's Mad Lib journey #1?: Yes or no?: ")
                    if outroAnswer == "yes" or outroAnswer == "Yes":
                        print("")
                        print("Mister Sweet appreciates your positive feedback! :)")
                        print("")
                        outroAnswer2 = input("Did you want to journey through another Mister Sweet mad lib story?: Yes or no?: ")
                        if outroAnswer2 == "yes" or outroAnswer2 == "Yes":
                            print("")
                            stories()
                        else:
                            print("")
                            print("Well swing back around for another story telling journey whenever you please! :)")
                    elif outroAnswer == "no" or outroAnswer == "No":
                        print("")
                        print("How unfortunate, please come by another time for a different story telling journey.")
                    else:
                        print("")
                        print("Invalid entry. Please try again.")
                        print("")
                        outro()
                outro()
            madLib1()
# Mad Lib Story #2
        elif madLibQ == "2":
            print("")
            print("This mad lib journey is still under cyber-construction, please come again later after an update has been issued, thank you! :)")
# Mad Lib Story #3
        elif madLibQ == "3":
            print("")
            print("This mad lib journey is still under cyber-construction, please come again later after an update has been issued, thank you! :)")
        else:
            print("")
            print("Invalid entry. Please try again.")
            print("")
            stories()
    stories()
else:
    print("")
    print("How unfortunate! Very well my friend, farewell and stay swell", name+'!')
# Nothing else beyond this point
