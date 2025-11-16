import json
import random

# Paths
FEMALE_EN = "data/female-human-names-en.json"
MALE_EN = "data/male-human-names-en.json"
FAMILY_NAME = "data/familly_name.json"


def load_json(path):
    """Load a JSON file safely."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None


def loading():
    print("Loading...")

    female = load_json(FEMALE_EN)
    male = load_json(MALE_EN)
    familly = load_json(FAMILY_NAME)

    if not female or not male or not familly:
        print("❌ Failed to load data. Exiting.")
        exit()

    print("Loaded successfully!")
    return female, male, familly


def generator(female, male, familly):
    """Generate an identity."""
    print("Informations required")

    gender = input("Enter the gender (1 = male, 2 = female): ")

    if gender == "1":
        gender_string = "male"
        first_name = random.choice(male)
    elif gender == "2":
        gender_string = "female"
        first_name = random.choice(female)
    else:
        print("Invalid gender.")
        return

    # Age range
    try:
        age_1 = int(input("Between: "))
        age_2 = int(input("and: "))
        if age_1 > age_2:
            age_1, age_2 = age_2, age_1
    except ValueError:
        print("Invalid number.")
        return

    age = random.randint(age_1, age_2)
    last_name = random.choice(familly)

    # Output
    print("\nGenerated Identity:")
    print("------------------------")
    print(f"Gender: {gender_string}")
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Age: {age}")
    print("------------------------")


def main():

    print("""
▗▘▐▘  ▌   ▝▖  ▄▖ ▌    ▗ ▘▗     ▄▖          ▗     
▐ ▜▘▀▌▙▘█▌ ▌  ▐ ▛▌█▌▛▌▜▘▌▜▘▌▌  ▌ █▌▛▌█▌▛▘▀▌▜▘▛▌▛▘
▐ ▐ █▌▛▖▙▖ ▌  ▟▖▙▌▙▖▌▌▐▖▌▐▖▙▌  ▙▌▙▖▌▌▙▖▌ █▌▐▖▙▌▌ 
▝▖        ▗▘               ▄▌
    """)

    female, male, familly = loading()

    print("Made by https://github.com/StillUploading, FOR LEGAL/EDUCATIONAL USE ONLY.")
    agree = input("I agree to use this tool legally (yes/no): ").lower()

    if agree != "yes":
        print("You cannot proceed.")
        return

    generator(female, male, familly)


if __name__ == "__main__":
    main()
