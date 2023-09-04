from operator import itemgetter

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """get every an instruction"""

    records = get_records()

    champion_to_count, countries = get_process(records)

    print_records(champion_to_count, countries)


def print_records(champion_to_count, countries):
    """print the statement"""
    print("Wimbledon Champions: ")
    sorted_champions = sorted(champion_to_count.items(), key=itemgetter(1), reverse=True)
    for name, count in sorted_champions:
        print(f"{name} {count}")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_process(records):
    """count the champions won by a different country"""
    champions_won = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champions_won[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champions_won[record[INDEX_CHAMPION]] = 1
    return champions_won, countries


def get_records():
    """read the file and extract the statement"""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        records = []
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
