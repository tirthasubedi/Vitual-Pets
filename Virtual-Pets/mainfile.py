from Owner import*
from pets import*
# importing both file owner and pets
import sys

def main():
    """
    this is main function calling all the activities;


    :return:
    """
    o= Owner()
    p= Pets()
    owner_name= input("what's your name?")          # this is asking for name
    pet_name= input("what's your pet name?")        # asking for pet name
    # p.current_hunger = 0
    while True:
        tasks= input("what do you want to do with pet? choose from eat, play, run, ignore, unhealthy food, sleep:")
        if tasks == "eat":                              # this ask for user to do activities which impact energy of pet
            o.feed(p)
            print("Your Pet energy level:", + p.current_hunger)         # feeding by 4 by eat
        elif tasks=="play":                                         # playing will decrease energy
            o.activities(p)
            print("Your Pet energy level:", + p.current_hunger)
        elif tasks=="run":                                          # this will make pet run and decrease energy
            o.run(p)
            print("Your Pet energy level:", +p.current_hunger)
        elif tasks=="ignore":                                          # ignore if owner dont care than pet will die eventually
            o.careless(p)
            print("Your Pet energy level:", + p.current_hunger)
        elif tasks=="sleep":
            o.rest(p)                                                   # calling rest by typing sleep
            print("Your Pet energy level:", +p.current_hunger)

        if p.current_hunger <=10:                                       # this will warn owner to feed pet
            print("Feed your pet, else your pet will die soon")

        if p.current_hunger <=0:                                        # if the energy is less than zero than pet will die
            print("Sorry!! Your Pet is Dead")
            sys.exit()                          # I also could break to break the loop


main()
