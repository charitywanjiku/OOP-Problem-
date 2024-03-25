# OOP-Problem-
Competitive Eating Competition Scoreboard
You are the judge at a competitive eating competition and you need to choose a winner! Participants earn points based on the amount of each type of food they consume. Chicken wings are worth 5 points, hamburgers are worth 3 points, and hotdogs are worth 2 points.

This Python function helps you create a scoreboard for the competition. It takes a list of participant objects as input, where each participant object contains their name along with the quantity of each type of food they consumed. The function returns a list of objects containing the name and score of each participant, sorted by score in descending order. If multiple participants have the same score, they are sorted alphabetically by name.

Function Signature
python

def create_scoreboard(participants: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    
Parameters
participants: A list of participant objects, where each participant object is a dictionary containing the following key-value pairs:
'name' (str): The name of the participant.
'chickenwings' (int): The quantity of chicken wings consumed by the participant.
'hamburgers' (int): The quantity of hamburgers consumed by the participant.
'hotdogs' (int): The quantity of hotdogs consumed by the participant.
Returns
A list of participant objects, where each participant object is a dictionary containing the following key-value pairs:
'name' (str): The name of the participant.
'score' (int): The total score of the participant calculated based on the quantities of each type of food consumed.