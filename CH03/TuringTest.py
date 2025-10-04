"""Turing Test"""

input("What is your problem?:\t")

status = input("Have you had this problem before (yes or no)?:\t")
if status == "yes":
    print("Well, you have it again")
elif status == "no":
    print("Well, you have it now")