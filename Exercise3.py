# Exercise 4
print("You will get 9 guesses to answer correctly, Good luck\n")
g = 1
n = 10
print("you have total 10 guesses")

while g <= 9:
    print("It was your", g, "guess\n")

    guess = int(input("Enter your guess"))

    if guess < n:
        print("Your input is low, try again")

    elif guess > n:
        print("Your input is large, Try again")

    else:
        print("Hurray! your number is correct")
        break
    g = g + 1

if g > 9:
    print("game over")
