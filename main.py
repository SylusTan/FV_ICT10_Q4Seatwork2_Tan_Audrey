# Define a class named "Classmate"
class Classmate:
    # Constructor method that initializes the attributes of each classmate
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    # Method to introduce the classmate
    def introduce(self):
        print(f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}.")


# Create at least 5 Classmates objects with unique data
c1 = Classmate("Andrea", "Emerald", "Math")
c2 = Classmate("Jean", "Topaz", "Science")
c3 = Classmate("John", "Sapphire", "English")
c4 = Classmate("Asher", "Ruby", "Math")
c5 = Classmate("Melody", "Emerald", "History")


# Store all classmate objects inside a list
classmates = [c1, c2, c3, c4, c5]

# Display list
print("\nClassmate List:\n")
for c in classmates:
    c.introduce()


# Ask the user to input details for a new classmate
print("\nAdd a new classmate:")
name = input("Enter name: ")
section = input("Enter section (Emerald/Topaz/Sapphire/Ruby): ")
fav_sub = input("Enter favorite subject: ")

# Create a new Classmate object using user input
new_classmate = Classmate(name, section, fav_sub)
# Add the new object to the classmates list
classmates.append(new_classmate)

print("\nUpdated Classmate List:\n")
# Loop again to display all classmates including the new one
for c in classmates:
    c.introduce()
