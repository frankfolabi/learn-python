from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language ded you first learn?"
language_survey = AnonymousSurvey(question)

# Show the question, and store the responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

