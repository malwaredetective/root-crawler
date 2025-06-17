#!/usr/bin/python3
import os
import sys

def read_character_sheet(uid, character_name):
    try:
        os.setuid(uid)
        print(f"\n*** Accessing {character_name}'s Character Sheet ***")
        os.system(f"cat /home/{character_name}/character_sheet.md")
    except PermissionError:
        print(f"Permission denied! Could not access {character_name}'s character sheet!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome, Dungeon Master (DM)!")
    print("Select a character to review their character sheets.\n")
    print("Available options:")
    print("1. Read Tav's Character Sheet")
    print("2. Read Shadowheart's Character Sheet")
    print("3. Read Lae'zel's Character Sheet")
    print("4. Read Astarion's Character Sheet")
    print("5. Quit\n")

    while True:
        try:
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                read_character_sheet(1002, "tav")
            elif choice == 2:
                read_character_sheet(1003, "shadowheart")
            elif choice == 3:
                read_character_sheet(1004, "laezel")
            elif choice == 4:
                read_character_sheet(1005, "astarion")
            elif choice == 5:
                print("Exiting the DM's terminal. Happy adventuring!")
                sys.exit()
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
