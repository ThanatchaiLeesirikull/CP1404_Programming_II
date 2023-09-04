def main():
    email_dict = {}

    email = input("Email: ").strip()

    while email != "":
        name = extract_name(email)
        confirm_name = input(f"Is your name {name}? (Y/n): ")

        if confirm_name.upper() != "Y" and confirm_name != "":
            name = input("Name: ").title()

        email_dict[email] = name
        email = input("Email: ").strip()

    print_emails(email_dict)


def extract_name(email):
    parts = email.split('@')[0]
    name_parts = parts.split('.')
    name = " ".join(name_parts).title()
    return name


def print_emails(email_dict):
    for email, name in email_dict.items():
        print(f"{name} ({email})")


main()
