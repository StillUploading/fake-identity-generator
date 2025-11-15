import time, os, json, random


female_en = "data/female-human-names-en.json"
male_en = "data/male-human-names-en.json"
familly_name = "data/familly_name.json"
female = "error"
male = "error"
familly = "error"
# Variables (for generator)
age = 0
gender = 0
gender_string = "error"
first_name = "error"
last_name = "error"

def loading():
    global female, male, familly
    print("Loading...")
    with open(female_en) as f:
        female = json.load(f)
    with open(male_en) as f:
        male = json.load(f)
    with open(familly_name) as f:
        familly = json.load(f)
    print("Loaded with succes !")



def generator():
    global first_name, last_name, age, gender_string

    print("Informations required")

    gender = input("Enter the gender (1 = male, 2 = female): ")

    # Determine which list to use
    if gender == "1":
        gender_string = "male"
        first_name = random.choice(male)
    elif gender == "2":
        gender_string = "female"
        first_name = random.choice(female)
    else:
        print("Invalid gender.")
        return

    print("What age group?")
    age_1 = int(input("Between: "))
    age_2 = int(input("and: "))

    age = random.randint(age_1, age_2)
    last_name = random.choice(familly)

    print("\nGenerated Identity:")
    print("------------------------")
    print("Gender:", gender_string)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Age:", age)
    print("------------------------")





def main():
    print("""
▗▘▐▘  ▌   ▝▖  ▄▖ ▌    ▗ ▘▗     ▄▖          ▗     
▐ ▜▘▀▌▙▘█▌ ▌  ▐ ▛▌█▌▛▌▜▘▌▜▘▌▌  ▌ █▌▛▌█▌▛▘▀▌▜▘▛▌▛▘
▐ ▐ █▌▛▖▙▖ ▌  ▟▖▙▌▙▖▌▌▐▖▌▐▖▙▌  ▙▌▙▖▌▌▙▖▌ █▌▐▖▙▌▌ 
▝▖        ▗▘               ▄▌                                                                                            
    """)

    loading()
    print("Made by https://github.com/StillUploading, FOR LEGAL/EDUCATIONAL USE ONLY. I am not responsible for any excesses.")
    agree = str(input("I agree to use this tool legally (yes/no): "))
    if agree != "yes":
        print("I'm sorry, but you cannot proceed :(")
    generator()
    

if __name__ == "__main__":
    main()