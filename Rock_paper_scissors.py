import random




def play():
    user= input("what do you choose? 'r' for rock, 'p' for paper , 's' for scissors\n " )
    computer= random.choice(["r", "s", "p"])
    if user not in ["r", "s", "p"]:
        print ("Invalid input")
        exit()
    print("user: ", user)
    print("computer: ", computer)

    if user == computer:
        return "tie"
    if is_win(user,computer):
        return "you won! :)"
    return "you lost :("

def is_win(player, opponent):
    if (player== "r" and opponent== "s") or (player == "p" and opponent== "r") or (player== "s" and opponent== "p"):
        return True
print(play())