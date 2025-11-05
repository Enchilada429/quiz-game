"""A CLI quiz game implemented in Python"""

from requests import get
from html import unescape
from random import shuffle

BASE_URL = "https://opentdb.com/api.php"


class Question:
    """A class that represents a single question."""

    def __init__(self, question_dict: dict):
        """Create a new question instance."""

        self.question_type = question_dict["type"]
        self.difficulty = question_dict["difficulty"]

        # Load with correct punctuation
        self.category = unescape(question_dict["category"])
        self.question_text = unescape(question_dict["question"])
        self.correct_answer = unescape(question_dict["correct_answer"])
        self.incorrect_answers = unescape(question_dict["incorrect_answers"])

        self.answers = self.incorrect_answers
        self.answers.append(self.correct_answer)
        shuffle(self.answers)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"""
              <Question Class
              Question: {self.question_text}
              Question Type: {self.question_type}
              Category: {self.category}
              Correct Answer: {self.correct_answer}
              Incorrect Answers: {self.incorrect_answers}
              >"""

    def display(self):
        """Display the question details."""
        print(self.question_text)
        for i in range(0, len(self.answers)):
            print(f"{i + 1}. {self.answers[i]}")

    def answer(self, guess: str) -> bool:
        """Return if a given answer is correct."""
        return guess == self.correct_answer


def get_questions(number: int = 5,
                  difficult: str = "medium") -> list[Question]:
    response = get(f"{BASE_URL}?amount={number}&difficulty={difficult}").json()[
        "results"]
    return [Question(question) for question in response]


if __name__ == "__main__":
    get_questions(7, "medium")[0].display()
