
def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertilizer to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Ask the user for details and display gardening advice."""
    # Ask the user to enter the season and plant type
    season = input("Enter the season (summer or winter): ").lower()
    plant_type = input(
        "Enter the plant type (flower or vegetable): "
    ).lower()

    # Get advice from both functions
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display the gardening advice
    print(advice)


if __name__ == "__main__":
    main()
