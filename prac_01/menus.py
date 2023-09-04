#pseudocode
"""
get name

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

print MENU

get choice

while choice != Q

   if choice == H
       print name

   elif choice == G
       print name

   else
       print Invalid choice

   print MENU

   get choice

print Finished.
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ").capitalize()

print(MENU)

choice = input(">>> ").upper()

while choice != 'Q':

   if choice == 'H':
       print("Hello", name)

   elif choice == 'G':
       print("Goodbye", name)

   else:
       print("Invalid choice")

   print(MENU)

   choice = input(">>> ").upper()

print("Finished.")

