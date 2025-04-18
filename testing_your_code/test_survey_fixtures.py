import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to test all functions."""
    question = "What language ded you first learn?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored prreyrly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that a three responses are stored prreyrly."""
    responses = ['English', 'Igbo', 'Hausa']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
