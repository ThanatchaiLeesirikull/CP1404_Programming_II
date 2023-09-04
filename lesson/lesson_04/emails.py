user_emails = {}

email = input("Email: ")

ask_for_name = input(f"Is your name {email}? (Y/n)")

user_emails[email] = ask_for_name

while email != "":
    try:
        print(f"{email}")
    except KeyError:
        print("Invalid color")
    state_code = input("Enter Name: ")

