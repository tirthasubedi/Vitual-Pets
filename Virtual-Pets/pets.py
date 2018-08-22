
class Pets:

    def __init__(self ):
        """
        this class is for the pet and it have all the activities such as Eat, play, unhealthy food, Run, Ignore, and sleep

        """
        self.current_hunger =20         # pet has initial energy level of 20

    def eat(self):                      # this function let increase energy level by typing eat
        self.current_hunger += 4

    def play(self):                     # this function decrease energy level by playing

        self.current_hunger -= 3
        print("your pet is playing")
        # if self.current_hunger ==0:
        #     print("Your pet is dead")
        # else:
    def unhealthy_food(self):               # unhealthy food hurt the health of pet so it decrease energy level
        self.current_hunger -= 2
        print("Feeding Junk Food will have huge Negative impact on your pet.")
        # if self.current_hunger ==0:
        #     print("Your pet is dead")
        # else:
    def run (self):
                        # this is to make your pet run
        self.current_hunger -= 4
        print("Your Pet is Running (Feed as soon as Possible):")
    def ignore(self):           # if you careless your pet than it will eventually die one day

        self.current_hunger -=1

    def sleep(self):                # if your pet is keep sleeping for long period of time then it will die after long period of time
        self.current_hunger -=.5



def main():
    pass

if __name__ == '__main__':

    main()



