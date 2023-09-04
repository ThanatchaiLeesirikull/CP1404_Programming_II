def main():

    in_file = open('temps_input.txt', 'r')
    out_file = open('temps_output.txt', 'w')

    for line in in_file:

        celsius = float(line.strip())

        fahrenheit = convert_celsius_to_fahrenheit(celsius)

        out_file.write(str(fahrenheit) + "\n")

    in_file.close()
    out_file.close()


def convert_celsius_to_fahrenheit(Celsius):
    return (Celsius * 9 / 5) + 32


main()
