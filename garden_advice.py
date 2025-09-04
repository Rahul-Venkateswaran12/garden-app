def get_user_input():
    # Function to get user input for season and plant type
    season = input("Enter the current season: ").strip().lower()
    plant_type = input("Enter the type of plant: ").strip().lower()
    return season, plant_type


def generate_advice(season, plant_type):
    # Function to generate gardening advice based on season and plant type
    advice = ""
    # Advice based on season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice


def main():
    season, plant_type = get_user_input()
    advice = generate_advice(season, plant_type)
    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code. (DONE)
# - Refactor the code into functions for better readability and modularity. (DONE)
