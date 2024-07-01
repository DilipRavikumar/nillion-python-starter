from nada_dsl import *

# Function to determine the stage based on some conditions
def journey_to_hackerhouse(status):
    if status == "selected":
        party = Party(name="Hackerhouse Goa")
        return [Output(SecretInteger(0), "selected", party)]
    elif status == "improve":
        party = Party(name="Improvement Phase")
        return [Output(SecretInteger(0), "improve", party)]
    else:
        party = Party(name="Waiting Phase")
        return [Output(SecretInteger(0), "waiting", party)]

# Main story flow
def main_story(status):
    print("Once upon a time, in the land of coding challenges, a brave developer set out on a quest to conquer Hackerhouse Goa...")

    # Determine the current stage of the journey
    results = journey_to_hackerhouse(status)

    # Print the outcome of the journey using nada_dsl Outputs
    for result in results:
        print(f"Outcome: {result.party.name} - {result.name}")

# Example usage
status = "selected"  # Change this value to "selected", "improve", or any other status
main_story(status)
