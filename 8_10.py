def make_great(magicians,modified_magicians):
    for magician in magicians:

        current_magician = magicians.pop()
        current_magician = "The Great "+current_magician
        magicians.insert(0,current_magician)  #
        modified_magicians.append(current_magician)
def show_magicians(magicians):
    while magicians:
        magician=magicians.pop()
        print(magician)
magicians = ["Robert-Houdin","Jasper Maskelyne","Lance Burton"]
modified_magicians = []
make_great(magicians,modified_magicians)
show_magicians(modified_magicians)
print("---")
show_magicians(magicians)
