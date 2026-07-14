import random

question = input("Shake the Magic 8 Ball with a question: ")
answer = random.randint(1, 8)

if answer == 1:
    print("It is certain.")
elif answer == 2:
    print("Heaven's Blessing is upon you.")
elif answer == 3:
    print("Without a doubt.")
elif answer == 4:
    print("The devil is not idle, but you will be fine.")
elif answer == 5:
    print("You may rely on it.")
elif answer == 6:
    print("Definitely try again.")
elif answer == 7:
    print("Most likely.")
elif answer == 8:
    print("Yes.")

else:
    print("Signs point to yes.")
print("Ask another question to see what the Magic 8 Ball has to say!")
