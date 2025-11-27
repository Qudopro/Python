"""Turing Test"""
"""
Create a script that plays the part of the independent computer, giving its user a simple medical diagnosis.
The script should prompt the user with 'What is your problem?'
when the user answers and press Enter, the script should simply ignore the user's input, then...
prompt the user again with 'Have you had this problem before (yes or no)?'
If the user enters 'yes', print 'Well, you have it again.'. If the user enters 'no', print 'Well, you have it now.'
"""
input("What is your problem?:\t")

status = input("Have you had this problem before (yes or no)?:\t")
if status == "yes":
    print("Well, you have it again")
elif status == "no":
    print("Well, you have it now")