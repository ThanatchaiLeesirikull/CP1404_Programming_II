import random

statement_true = True
statement_false = False

statement_list = [statement_true, statement_false]


def main():

    result_statement_1 = generate_random_boolean_v1(statement_list)
    print(result_statement_1)

    result_statement_2 = generate_random_boolean_v2()
    if result_statement_2 == 1:
        print(True)
    else:
        print(False)

    result_statement_3 = generate_random_boolean_v3()


def generate_random_boolean_v1(statement_list):
    return random.choice(statement_list)


def generate_random_boolean_v2():
    return random.randint(0, 1) == 1


def generate_random_boolean_v3():
    return random.random() < 0.5


main()
