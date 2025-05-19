# Menu-driven program
name = input("Enter name: ")

# Display menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get choice
choice = input(">>> ").upper()

# Main loop
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    
    # Display menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

# finish message
print("Finished.")
