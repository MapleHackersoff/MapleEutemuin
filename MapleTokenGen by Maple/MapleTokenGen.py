import pyfiglet
import random
import string
import os

print("contact: invite.gg/Maple")
print("contact: invite.gg/MapleDev")

ascii_banner = pyfiglet.figlet_format("Maple  Token  generator")
print(ascii_banner)

T = input("Whats name of file? \n")


N = input("How many tokens: ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
while(int(count)<int(N)):
    arg = "x"
    firstGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    secondGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    thirdGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fourthGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fifthGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    sixthGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    seventhGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    eightGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    nineGen = arg + "."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    f= open(current_path+"/"+str(T)+str("")+".txt","a")
    f.write(firstGen + "\n" + secondGen + "\n" + thirdGen + "\n" + fourthGen + "\n" + fifthGen + "\n" + sixthGen + "\n" + seventhGen + "\n" + eightGen + "\n" + nineGen)
    print(firstGen)
    print(secondGen)
    print(thirdGen)
    print(fourthGen)
    print(fifthGen)
    print(sixthGen)
    print(seventhGen)
    print(eightGen)
    print(nineGen)
    count+=1