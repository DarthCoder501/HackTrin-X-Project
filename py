answer = input("You see a deal for a flight to Spain, do you buy the ticket?(yes/no): ")
if answer.lower() == "yes":
    answer = input("On your flight the wings of your plane breaks, do you put your oxygen mask on? (yes/no): ")
    if answer.lower() == "yes":
        answer = input("You wake up on an island, do you check for any survivors?(yes/no): ")
        
        if answer.lower() == "yes":
            answer = input("You found a man with a piece of the plane impaled in their chest, do you put them out misery or try to save him?(kill/save): ")
            
            if answer.lower() == "kill":
                answer = input("The man thanks you and gives you a pocket knife as a part gift, do you go into the wilderness or try to fish?(Wilderness/fish): ")
                
                if answer.lower() == "wilderness":
                    answer = input("You come acorss a wild boar, do you kill it or run away?(kill/run): ")
                    
                    if answer.lower() == "kill":
                        answer = input("You manage to kill the boar but you got some scrapes. Do you cook the whole boar or part of it?(whole/part): ")
                        if answer.lower() == "whole":
                            answer = input ("You had a very good meal to replenished your enery, but now you are sleepy, do you sleep on the beach or in the wilderness?(beach/wilderness): ")
                            if answer.lower() == "beach":
                                print("The waves dragged you into the ocean where you drowned!")

                            elif answer.lower() == "wilderness":
                                answer = input("You wake up well rested and decide to make a SOS message, do you make it out of stones or write it into the sand?(stones/sand): ")
                                if answer.lower() == "stones":
                                    answer = input("You manage to find enough stones to make a large SOS message but the family of the boar come to get revenge and mess up your SOS and then turn onto you, do you kill the boar family or run away?(kill/run): ")
                                    if answer.lower() == "kill":
                                        answer = input("You manage to kill all but one of the boars and now you have enough food to last you two weeks, but you see a plane, do you try to get the pliot's attention on the beach or on the top of the mountain?(beach/mountain): ")
                                        if answer.lower() == "beach":
                                            print("The pilot doesn't see you and you fall into depression and die!")
                                        elif answer.lower() == "mountain":
                                            answer = input("You run up to the top of the mountain where you encouter the last member of the boar family, do you fight it or run away?(fight/run): ")
                                            if answer.lower() == "fight":
                                                answer = input("You and the boar get into a grueling battle, but you manage to come out on top, but now you're having second thought about leaving the island, do you use the boar tusks to start a fire or stay on the island?(fire/island): ")
                                                if answer.lower() == "fire":
                                                    print("You managed to get the pilot's attention to leave the island and return back to your family!")
                                                elif answer.lower() == "island":
                                                    print("You slip and fall 100ft to your death!")
                                            if answer.lower() == "run":
                                                print("The boar impales you and you both fall off the side of the mountain!")

                                    elif answer.lower() == "run":
                                        print("You trip on one of your SOS rocks and boar family uses that oppununity to eat you alive!")
                                elif answer.lower() == "sand":
                                    print("The waves wash away your message and you fall into a depressive state and you eventually die from malnutrition!") 

                        elif answer.lower() == "part":
                            print("The children of the boar sees that you killed their mother and they stampede you to death!")
                    
                    elif answer.lower() == "run":
                        answer = input("The boar sees you and impales you with its tusk, do you move to the beach or lie on the ground?(beach/ground): ")
                        if answer.lower() == "beach":
                            print("You die on the beach watching a beauiful sunset")
                        elif answer.lower() == "ground":
                            print("The boar eats you alive!")

                elif answer.lower() == "fish":
                    answer = input("You manage to catch three medium sized fish, do you eat them raw or look for materials to make a fire?(raw/fire): ")
                    
                    if answer.lower() == "raw":
                        print("You die due to food poisoning!")

                    elif answer == "fire":
                        answer = input("You managed to make a fire to have a very good meal to replenished your enery, but now you are sleepy, do you sleep on the beach or in the wilderness?(beach/wilderness): ")
                        if answer.lower() == "beach":
                            print("The waves dragged you into the ocean where you drowned!")

                        elif answer.lower() == "wilderness":
                            answer = input("You wake up well rested and decide to make a SOS message, do you make it out of stones or write it into the sand?(stones/sand): ")
                            if answer.lower() == "stones":
                                answer = input("You manage to find enough stones to make a large SOS message but the family of the boar come to get revenge and mess up your SOS and then turn onto you, do you kill the boar family or run away?(kill/run): ")
                                if answer.lower() == "kill":
                                    answer = input("You manage to kill all but one of the boars and now you have enough food to last you two weeks, but you see a plane, do you try to get the pliot's attention on the beach or on the top of the mountain?(beach/mountain): ")
                                    if answer.lower() == "beach":
                                        print("The pilot doesn't see you and you fall into depression and die!")
                                    elif answer.lower() == "mountain":
                                        answer = input("You run up to the top of the mountain where you encouter the last member of the boar family, do you fight it or run away?(fight/run): ")
                                        if answer.lower() == "fight":
                                            answer = input("You and the boar get into a grueling battle, but you manage to come out on top, but now you're having second thought about leaving the island, do you use the boar tusks to start a fire or stay on the island?(fire/island): ")
                                            if answer.lower() == "fire":
                                                print("You managed to get the pilot's attention to leave the island and return back to your family!")
                                            elif answer.lower() == "island":
                                                print("You slip and fall 100ft to your death!")
                                        if answer.lower() == "run":
                                            print("The boar impales you and you both fall off the side of the mountain!")

                                elif answer.lower() == "run":
                                    print("You trip on one of your SOS rocks and boar family uses that oppununity to eat you alive!")
                            elif answer.lower() == "sand":
                                print("The waves wash away your message and you fall into a depressive state and you eventually die from malnutrition!") 

            
            elif answer.lower() == "save":
                print("The man kills you for trying to save his life and then dies from his injuries!")
        
        elif answer.lower() == "no":
            print("You get killed by the other remaining surviors that were hiding for trying to leave them!")

    elif answer.lower() == "no":
        print("You died in the plane crash!")

elif answer.lower() == "no":
    print("You slip and died due to head trauma!")
