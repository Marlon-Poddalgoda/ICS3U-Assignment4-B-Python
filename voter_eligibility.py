#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program determines if a user is eligible to vote

import constants


def main():
    # this function will determine if a user is of voting age

    print("This program determines if you are eligible to vote.")

    # input
    user_input = input("Enter your age here: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            if user_input_int >= constants.MIN_VOTE_AGE:
                print("You are eligible to vote, congrats!")
            else:
                print("Sorry, you must be at least {} years old to vote."
                      .format(constants.MIN_VOTE_AGE))
        else:
            # output
            print("{} is not a positive number, please try again."
                  .format(user_input_int))
    except Exception:
        # output
        print("'{}' isn't a number! Try again."
              .format(user_input))


if __name__ == "__main__":
    main()
