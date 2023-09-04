"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """call out function and print out the statement"""

    data = get_data()
    print(data)

    statements = print_statement(data)

    for statement in statements:
        print(statement)

    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject = input("What subject code: ")
    print(f"{subject_to_data[subject][0]} teaches {subject}")


def convert_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]

    return subject_to_data


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open('subject_data.txt', 'r')

    lists = []

    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        lists.append(parts)

    input_file.close()

    return lists


def print_statement(data):
    """store all the variable in list"""

    statements = []

    for subject_info in data:

        subject_code, lecturer, num_students = subject_info
        statement = f"{subject_code} is taught by {lecturer} and has {num_students}"
        statements.append(statement)

    return statements


main()

