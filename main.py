import random

#Mengenal pasti fungsi main
def main():
    """Start a element guessing game."""
    print("Guess the element!")

#Memasukkan data string ke dalam pembolehubah
    element = [
        "hydrogen",
        "helium",
        "beryllium",
        "fluorine",
        "neon"
        ]

#Mengeluarkan element secara rawak
    x = random.choice(element)
    
    guess = None
    
#Mencipta gelung yang melaksanakan pernyataan
    while x != guess:

        guess = str(input("What element am I thinking of? "))
        
        if x == guess:
            print("Congratulations, you are correct!".format(guess))
            break
        else:
            if x == "neon":
                print("This element is  the second lightest noble gas")
            elif x == "fluorine":
                print("This element is the most reactive element")
            elif x == "hydrogen":
                print("This element is the lightest element")
            elif x == "helium":
                print("This element is the second lightest element")
            elif x == "beryllium":
                print("This element is a silvery-white metal")
                
#Bertindak sebagai titik pelaksanaan untuk mana-mana program
main()
