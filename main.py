from art import logo
from art import vs
from game_data import data
import random
import replit


print(logo)
# Get list length
data_length = len(data)

# Generate random starting point
random_digit = random.randint(0, data_length - 1)

# user score
score =  0
game_over = False

# Generate second random number and make sure its different from the first
def second_rand_generator(first_rand):
    second_rand = random.randint(0, data_length - 1)
    if first_rand == second_rand:
        second_rand = random.randint(0, data_length - 1)
        return second_rand
    else:
        return second_rand



def check_answer(a_count,b_count, answer):
	global score
	global game_over
	
	print(f"{a_count} vs {b_count} {answer}")

	if a_count > b_count: #true
		if answer == "a":
			replit.clear()
			score += 1
			print(logo)
			print(f"You're right! Current score: {score}.")
			
			
		elif answer == "b":
			replit.clear()
			print(logo)
			print(f"Sorry, that's wrong. Final score: {score}")
			game_over = True
			
	else:
		if answer == "b":
			replit.clear()
			score += 1
			print(logo)
			print(f"You're right! Current score: {score}.")
			
		elif answer == "a":	
			replit.clear()
			print(logo)
			print(f"Sorry, that's wrong. Final score: {score}")
			game_over = True


	
			

	
while not game_over:		
	# Get the second number
	second_digit = second_rand_generator(random_digit)	
	
	
	# A profile
	a_name = data[random_digit]['name']
	a_followers = data[random_digit]['follower_count']
	a_description = data[random_digit]['description']
	a_country = data[random_digit]['country']
	
	# B Profile
	b_name = data[second_digit]['name']
	b_followers = data[second_digit]['follower_count']
	b_description = data[second_digit]['description']
	b_country = data[second_digit]['country']
	
	
	# Show the the comparisons
	print(f"Compare A: {a_name}, {a_description} from {a_country}")
	
	print(vs)
	
	print(f"Against B: {b_name}, {b_description} from {b_country}")
	
	# Get user's answer
	user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
	
	
	check_answer(a_followers, b_followers, user_answer)
	# print(user_answer)

	random_digit = second_digit

 

		

	
