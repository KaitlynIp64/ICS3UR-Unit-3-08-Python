#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program uses a nested if statement


def main():
    # this function uses a nested if statement

    # input
    year_int = int(input("Enter the year: "))
    print("")

    # process & output
    if year_int % 4:
        if year_int % 100:
            print("That is a common year.")
        else:
            print("That is a common year.")
    else:
        print("That is a leap year.")


if __name__ == "__main__":
    main()
