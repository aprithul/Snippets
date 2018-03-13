import math

prefs = {
    "Pri": {
        "Inception": 9.0,
        "Mummy": 6.1,
        "Star Wars": 7.9,
        "Shawshank": 9.8,
        "Prestige": 8.8
    },
    "Ani": {
        "Inception": 8.0,
        "Mummy": 7.6,
        "Star Wars": 5.5,
        "Shawshank": 8.0,
        "Prestige": 10.0
    },
    "Nov": {
        "Inception": 7.0,
        "Mummy": 5.1,
        "Star Wars": 7.4,
        "Shawshank": 7.8,
        "Prestige": 7.3
    },
    "Rai": {
        "Inception": 6.7,
        "Mummy": 4.8,
        "Star Wars": 8.0,
        "Shawshank": 7.9,
        "Prestige": 9.2
    },
    "Fai": {
        "Inception": 8.7,
        "Mummy": 5.7,
        "Star Wars": 9.0,
        "Shawshank": 8.3,
        "Prestige": 9.9
    },
    "Tan": {
        "Inception": 8.1,
        "Mummy": 6.6,
        "Star Wars": 8.8,
        "Shawshank": 8.9,
        "Prestige": 8.2
    }
}


def similarity_eucledian(person_1, person_2, prefs):
	person_1_pref = prefs[person_1]
	person_2_pref = prefs[person_2]

	dist = math.sqrt(
	    sum([(person_1_pref[key] - person_2_pref[key])**2
	         for key in person_1_pref if key in person_2_pref]))

	return 1.0 / (1.0 + dist)


def main():
	print(similarity_eucledian("Pri", "Nov", prefs))


main()
