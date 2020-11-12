import random

random.seed(1)
biden_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trump_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
biden_win_pct = 69.13
trump_win_pct = 29.28
number_of_sims = 1000
total_wards = 0
total_trump_votes = 0
total_biden_votes = 0
total_votes = 0
for i in range(number_of_sims):
    my_input = open('milwaukee_total_voters.txt')
    for line in my_input:
        total_wards += 1
        fields = line.strip().split()
        num_voters = int(fields[0])
        trump_votes_in_ward = 0
        biden_votes_in_ward = 0
        for j in range(num_voters):
            random_num = random.random() * 100
            if random_num <= biden_win_pct:
                biden_votes_in_ward += 1
                total_biden_votes += 1
            elif random_num <= (biden_win_pct + trump_win_pct) :
                trump_votes_in_ward += 1
                total_trump_votes += 1
            total_votes += 1
        trump_digit = int(str(trump_votes_in_ward)[0])
        biden_digit = int(str(biden_votes_in_ward)[0])
        trump_digits[trump_digit] += 1
        biden_digits[biden_digit] += 1
    if i % 100 == 0:
        print('done with sim', i)

trump_win_pct = 100.0 * total_trump_votes / total_votes
biden_win_pct = 100.0 * total_biden_votes / total_votes
print('biden win pct:', biden_win_pct)
print('trump win pct:', trump_win_pct)


for i in range(10):
    print_info = "biden " +  str(biden_digits[i] * 100.0 / total_wards)
    print(print_info)

for i in range(10):
    print_info = "trump " +  str(trump_digits[i] * 100.0 / total_wards)
    print(print_info)
