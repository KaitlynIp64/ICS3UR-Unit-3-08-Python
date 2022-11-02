#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program uses a nested if statement


def main():
    # this function uses a nested if statement

    # input
    year_int = input("Enter the year: ")
    print("")

    # process & output
    try:
        year_int = int(year_int)
        print("That is a valid input.")

        if year_int % 4 != 0 and year_int % 400 != 0:
            if year_int % 100 != 0:
                print("That is a common year.")
            else:
                print("That is a leap year.")
        else:
            print("That is a leap year.")

    except ValueError:
        print("That is not a valid input.")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
