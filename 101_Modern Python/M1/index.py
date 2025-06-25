# Module 1: Python Fundamentals & Modern Typing

# Q1: Pet store count

# def store():
#     pet = {
#         "Cats": 5,
#         "Dogs": 7,
#         "Birds": 9
#     }

#     print(f"List of Pets in store: {pet}")
#     sum = 0
#     for i in pet:
#         sum += pet[i]
#     print(f"Total number of pets: {sum}")


# store()


# Question 2: Greeting My Friends

# def friends():
#     buddies = ['Ali', 'Asif', 'Baqir', 'Kashif', 'Amin']
#     for i in buddies:
#         print(f"Welcome to the party, {i}!")


# friends()


# Question 3: Is It Hot Enough for Ice Cream?

# def ice_cream():
#     temp = 30
#     if temp > 20:
#         print(f"It's enough for an ice cream!")
#     else:
#         print(f"It's not enough for an ice cream!")


# ice_cream()


# Question 4: Finding the Longest Word

# from typing import List


# def longest_word(words_list: List[str]) -> str:

#     word_found = ""

#     for current_word in words_list:

#         if len(current_word) > len(word_found):

#             word_found = current_word

#     return word_found


# my_words = ["cat", "banana", "dog", "elephant"]
# winner = longest_word(my_words)
# print(f"The longest word in {my_words} is: {winner}")


# Question 5: Student Scores Analysis
# from typing import Dict


# def score_analysis():
#     details: dict = {
#         "Ali": 76,
#         "Bashir": 92,
#         "Kashif": 72,
#         "Ubaid": 93
#     }
#     count: int = 0
#     for i in details:
#         if details[i] >= 80:
#             count += 1

#     return count


# final_count = score_analysis()
# print(f"{final_count} student(s) scored above 80")


# Question 6: Simple Action Log (Conceptual Decorator Use)

import functools


def action_logger(func):
    @functools.wraps(func)
    def wrapper_log_action(*args, **kwargs):
        print(f"Agent is starting action: '{func.__name__}'...")
        result = func(*args, **kwargs)
        return result

    return wrapper_log_action


@action_logger
def move(direction: str, steps: int):
    """Simulates the agent moving."""
    print(f" --> Agent moves {steps} steps towards {direction}.")


@action_logger
def collect_item(item_name: str):
    """Simulates the agent collecting an item."""
    print(f" --> Agent picks up the {item_name}.")


print("Testing agent actions:")
move("north", 10)
print("-" * 20)
collect_item("ancient artifact")
