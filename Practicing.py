from tokenize import Double


print('Hello World!')

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# How many voters did you get?

my_votes = int(input('How many votes were for you?'))
total_votes = int(input('How many people voted in total?'))
my_percent = (my_votes/total_votes)*100

print(f'You got {my_percent}% of the total votes cast.')

#Simple If
counties = ['arapahoe','denver','jefferson']
if counties[1] != 'jefferson':
    print(counties[2])

# If - Else Temps
temperature = int(input('What is the temperature outside?'))

if temperature > 80:
    print('Turn on that A/C!!!')
else:
    print('No A/C needed')

#Nested Ifs

score = int(input('What was your test score?'))

if score >= 90:
    print('You got an A!')
else:
    if score>= 80:
        print('You got a B')
    else:
        if score >= 70:
            print('You got a C...')
        else:
            if score >= 60:
                print('You got a D')
            else:
                print('You failed and you should feel bad.')

#Nested Ifs w/ Elif

score = int(input('What was your test score?'))

if score >= 90:
    print('You got an A!')
elif score>= 80:
    print('You got a B')
elif score >= 70:
    print('You got a C...')
elif score >= 60:
    print('You got a D')
else:
    print('You failed and you should feel bad.')

# Using In
counties = ['arapahoe', 'denver', 'jefferson']

if 'el paso' in counties or 'jefferson' in counties:
    print('True')
else:
    print('False')

# While loops

x = -4

while x<=5:
    print(x)

    x = x + 1

# For loops

for county in counties:
    print(county)

counties_dict = {'arapahoe':422829,'denver': 463353,'jefferson':432438}

for key, value in counties_dict.items():
    print(key, value)

for county_diction in voting_data:
    for value in county_diction.items():
        print(value)

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters')


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters')

for county_diction in voting_data:
        print(f'{"county"} county has {"registered_voters":,} registered voters')