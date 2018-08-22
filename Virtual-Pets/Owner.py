

class Owner:

    """this is owner class all functions are called from the pets file; owner is in control of the pet; and owner only have access to their pet.

    """
    # def __init__(self, name, pet, ownership_time):
    #     self.name= input("What's your name?")
    #     self.pet=0
    #     self.ownership_time=ownership_time

    def feed(self, pet):            # this function to feed or increase the energy level of pet
        pet.eat()

    def activities(self, p):           # this is for the play or the acticities for the pet.
        p.play()

    def food_type(self, p):             # if the owner keep feeding junk food than your pet will die sooner than not feeding at all
        p.unhealthy_food()

    def run(self, p):                   # this function to make pet run
        p.run()

    def careless(self, p):          # this function is for the ignorance purpose if owner careless about their pet than pet will die
        p.ignore()

    def rest(self, p):              # making pet sleep and if it sleep for long period than it will die by hunger
        p.sleep()


def main():
    pass

if __name__ == '__main__':
    main()

