text = """
CP1404
CP1409
CP2403
CP2408
"""

my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'CC2511', 'EG1012'}
example = []

print(", ".join(set(text.split())))
print(set(text.split()))
print(f"{'union':>21}: ", my_subjects | your_subjects)
print(f"{'intersection':>21}: ", my_subjects & your_subjects)
print(f"{'different':>21}: ", my_subjects - your_subjects)
print(f"{'symmetric_difference':>21}: ", my_subjects ^ your_subjects)

in_file = open('../data/wimbledon.txt')
lines = [line.strip for line in in_file.readline()]
winners = set(lines)
print(winners)
print(set(lines))
print(len(set(winners)))
in_file.close()

example.add(1)
print(example)