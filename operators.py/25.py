
#Create a Score Update Program.
#➜ Initial Score = 50
#➜ Add Bonus
#➜ Subtract Penalty
#➜ Double the Score
#➜ Display Final Score

score = 50

bonus = int(input("Enter bonus"))
penalty = int(input("Enter penalty"))

score += bonus
score -= penalty
score *= 2


print("Final Score:", score)