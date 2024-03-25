def calculate_score(participants):
    # Initialize an empty list to store scores for each participant
    scores = []
    
    # Iterate over each participant in the list
    for participant in participants:
        # Calculate the total score for the participant based on the points assigned to each type of food
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        
        # Create a dictionary containing the participant's name and score and append it to the scores list
        scores.append({'name': participant['name'], 'score': score})
    
    # Sort the list of scores based on the score (descending) and alphabetically by name if scores are equal
    sorted_scores = sorted(scores, key=lambda x: (-x['score'], x['name']))
    
    # Return the sorted list of scores
    return sorted_scores

# Example usage:
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

# Call the calculate_score function with the list of participants
scoreboard = calculate_score(participants)

# Print the resulting scoreboard
print(scoreboard)