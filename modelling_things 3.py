class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["doom","tak","tss"])

    def count_to_four(self):
        print("1, 2, 3, 4")

    def mr_im_on_fire(self):
        print("ahhh, i'm on fire!!")
        
#------- don't know what to do here
        
class Band(Drummer):
    def fire_musician(self):
        whoToFire = input("Who should we kick out? ")
        replacementMusician = input("Who is the new guy taking their place? ")

                          
#-------------------------
        
theBand = Band()
nigel = Guitarist()
dean = Drummer()
derek = Bassist()

theBand.fire_musician()

print("sound check:")
print("")
print("*nigel*")
print(nigel.sounds)
print("")
print("*derek*")
print(derek.sounds)
print("")
print("*dean*")
print(dean.sounds)
print("")

print("*nigel tuning*")
nigel.tune()

print("")
dean.count_to_four()
dean.solo(4)

"""
Extend the example code to add a Drummer class.
Drummers should be able to solo, count to four, and spontaneously combust.

Then add a Band class. Bands should be able to hire and fire musicians,
and have the musicians play their solos after the drummer has counted time.
"""
