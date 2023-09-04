"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
<<<<<<< HEAD
state_names = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
=======
state_names = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
>>>>>>> origin/master

print(state_names)

max_length = max(len(state) for state in list(state_names.keys()))

for state in state_names:
    print(f"{state:{max_length}} is {state_names[state]}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", state_names[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
