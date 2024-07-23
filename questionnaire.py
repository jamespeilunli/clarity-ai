# Define the questions and their respective weights
questions = [
    {"question": "I have a family history of depression or other mental health conditions.", "weight": 0.8},
    {"question": "I've recently experienced significant hormonal changes (e.g., pregnancy, menopause).", "weight": 0.7},
    {"question": "I have experienced trauma or abuse in my past.", "weight": 0.9},
    {"question": "I've undergone major life changes recently (e.g., job loss, divorce, relocation).", "weight": 0.7},
    {"question": "I frequently feel overwhelmed by stress in my daily life.", "weight": 0.8},
    {"question": "I tend to be self-critical and have low self-esteem.", "weight": 0.8},
    {"question": "I often find myself stuck in negative thought patterns.", "weight": 0.8},
    {"question": "I have a chronic medical condition or persistent pain.", "weight": 0.7},
    {"question": "I use alcohol or drugs to cope with my feelings.", "weight": 0.8},
    {"question": "I feel socially isolated or lack a strong support system.", "weight": 0.9},
    {"question": "I struggle with financial instability or lack of access to essential resources.", "weight": 0.7},
    {"question": "I find it difficult to enjoy activities I used to find pleasurable.", "weight": 0.9},
    {"question": "I experience persistent feelings of sadness, emptiness, or hopelessness.", "weight": 1.0},
    {"question": "I have trouble concentrating or making decisions.", "weight": 0.8},
    {"question": "My sleep patterns have changed significantly (sleeping too much or too little).", "weight": 0.8},
    {"question": "I've noticed significant changes in my appetite or weight.", "weight": 0.8},
    {"question": "I feel fatigued or low on energy most days, but I feel like I get enough sleep.", "weight": 0.8},
    {"question": "I have thoughts of self-harm or that life isn't worth living.", "weight": 1.0},
    {"question": "I find it challenging to manage my work or daily responsibilities.", "weight": 0.8},
]

# Function to calculate the depression score
def calculate_depression_score(responses):
    score = 0
    for response, question in zip(responses, questions):
        score += response * question["weight"]
    return score

# ask user questions
responses = []
for question in questions:
    response = int(input(question["question"] + " (input from 1 (false) to 10 (true)): "))
    if response < 1 or response > 10:
        print("Invalid response. Please enter a number between 1 and 10.")
        continue
    responses.append(response)

# calc score
depression_score = calculate_depression_score(responses)
print(f"The calculated depression score is: {depression_score}")


if depression_score >= 50:
    print("High likelihood of depression.")
elif depression_score >= 25:
    print("Moderate likelihood of depression.")
else:
    print("Low likelihood of depression.")
