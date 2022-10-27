#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 25, 2022
# This program sees if the amount spent inputted is over 1000
# dollars then they could have a 10% discount and calculates tax+discount=final price,
# otherwise is calculates tax only.

import random
import math


def main():
# Get the HST rate and the amount spent from the user.
    print("Please Enter the amount spent ($) and the HST rate (%)")
    hst = input("Enter your HST rate: ")
    amount_spent = input("Enter your spent amount: ")
# Tries casting hst and amount_spent from string to int.
    try:
        hst = int(hst)
        amount_spent = int(amount_spent)
# Code executed if hst and amount_spent be converted to int.
    except ValueError:
        print("You did not enter an integer.")
# Loops through code until hst and amount_spent is an integer
        while not isinstance(hst, int)(amount_spent, int):
            print("Please Enter the amount spent ($) and the HST rate (%)")
            hst = input("Enter your HST rate: ")
            amount_spent = input("Enter your spent amount: ")
# Tries casting hst and amount_spent from string to int.
            try:
                hst = int(hst)
                amount_spent = int(amount_spent)
# If hst and amount_spent is an integer, the loop is broken
                break
            except ValueError:
                print("Please try again.")
# Calculate the new price.
    if amount_spent >= 1000:
        discount_price = amount_spent - amount_spent / 10
        new_price = discount_price * (hst / 100 + 1)
        print(f"Your new price + tax and discount would be {new_price}")
# If there would be no discount.
    elif amount_spent < 1000:
        new_price = amount_spent * (hst / 100 + 1)
        print(f"Your new price + tax would be {new_price}")


if __name__ == "__main__":
    main()
