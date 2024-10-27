from nada_dsl import *

def nada_main():
    user_1 = Party(name="User 1")
    user_2 = Party(name="User 2")

    # Secret inputs from each user representing hobbies and red flags
    user_1_hobby = SecretInteger(Input(name="user_1_hobby", party=user_1))
    user_1_red_flag = SecretInteger(Input(name="user_1_red_flag", party=user_1))
    user_2_hobby = SecretInteger(Input(name="user_2_hobby", party=user_2))
    user_2_red_flag = SecretInteger(Input(name="user_2_red_flag", party=user_2))

    # Check if hobbies match and if red flags match
    hobby_match = user_1_hobby == user_2_hobby
    red_flag_match = user_1_red_flag == user_2_red_flag

    # Convert match results to integers (1 for True, 0 for False)
    hobby_match_result = hobby_match.if_else(Integer(1), Integer(0))
    red_flag_match_result = red_flag_match.if_else(Integer(1), Integer(0))

    # Both categories must match for the final result to be 1
    total_match = hobby_match_result * red_flag_match_result

    # Output the result to both users
    return [
        Output(total_match, "match_result", user_1),
        Output(total_match, "match_result", user_2)
    ]
