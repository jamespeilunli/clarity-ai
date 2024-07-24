def calculate_depression_likelihood(social_media_score, questionnaire_score):
    """
    Calculate the likelihood of depression based on social media score and questionnaire score.

    Parameters:
    social_media_score (float): The likelihood score from social media analysis (0-100).
    questionnaire_score (float): The likelihood score from a questionnaire (0-100).

    Returns:
    float: The overall likelihood of having depression (0-100).
    """
    
    # Validate inputs
    if not (0 <= social_media_score <= 100) or not (0 <= questionnaire_score <= 100):
        raise ValueError("Both scores must be between 0 and 100.")
    
    # Calculate the weighted average
    # Assuming equal weights for both scores
    overall_likelihood = (social_media_score + questionnaire_score) / 2

    return overall_likelihood

# Example usage:
social_media_score = float(input("Enter the likelihood of depression from social media (0-100): "))
questionnaire_score = float(input("Enter the likelihood of depression from questionnaire (0-100): "))

overall_likelihood = calculate_depression_likelihood(social_media_score, questionnaire_score)
print(f"The overall likelihood of having depression is: {overall_likelihood:.2f}%")


#sources: De Choudhury and Counts (2013) demonstrated that integrating social media data with traditional health metrics enhances predictive accuracy for depressive symptom trajectories . This suggests that both data sources provide valuable, yet distinct, insights into mental health.
#link: https://www.researchgate.net/publication/259948193_Predicting_Depression_via_Social_Media 