# area_rug.py
# This program follows the IPO (input, process, output) technique.
# A user will input the size of a room in feet, and the cost of a rug in square feet.
# The rug will be 1.5 ft shorter in width and 2 ft shorter in length than the room.
# The program will output the room's dimension and the rug's dimension, area, and cost.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 3

# Author: Adam Zieman
# Date: February 25, 2021

def main():
    # Print a heading and description of the program
    print("Area Rub Calculation Program")
    print("----------------------------")
    print("This program will determine the size and cost of")
    print("an area rug for an entered room size and cost")
    print("per square foot.\n")
    
    # Retrieve user input
    room_width = eval(input("Enter the room width (in feet): "))
    room_length = eval(input("Enter the room length (in feet): "))
    cost_SquareFoot = eval(input("Enter cost per square foot for rug material: "))
    print()
    
    # Calculate the rug size. The rug will have a 1.5 ft shorter width, and a 2 ft shorter length
    rug_width = room_width - 1.5
    rug_length = room_length - 2

    # Calcualte the cost of the rug (area * cost)
    rug_cost = rug_width * rug_length * cost_SquareFoot
    
    # Print a heading 
    print("Area Rug Details")
    print("============================")

    # Print the room's dimensions
    print("Room dimensions:")
    print(room_width, "feet wide x", room_length, "feet long")
    print("----------------------------")

    # Print the rug's dimensions
    print("Rug dimensions:")
    print(rug_width, "feet wide x", rug_length, "feet long")
    print("----------------------------")

    # Print the rug's squarefeet
    print("Total square feet:", rug_width * rug_length)

    # Print the cost of the rug
    print("Your rug will cost $", rug_width * rug_length * cost_SquareFoot, sep='')
    
main() # Calls the main() function
