#generate paasword for users

import random as passi
import string

while(True):
    lenth_n = int(input("give me the lenth of pass? "))

    if (lenth_n < 6):
        print ("your pass should be bigger than 6 digit.")
    else:
        upper = int(input("give me the uppercase of pass? "))
        lower = int(input("give me the lowecase of pass? "))
        digit_number = int(input("give me the digits of pass? "))
        for_if = upper + lower + digit_number
        if (for_if != lenth_n):
            print ("bro! the sum of your letter isn't equal to lenth.")
            ques = input("wanna try again? ")
            if (ques == "yes"):
                continue
            else:
                break
        else:
             result = ''.join(passi.choices(string.ascii_uppercase , k = upper)
             + passi.choices(string.ascii_lowercase , k = lower) + passi.choices(string.digits , k = digit_number))
             print ("your pass is: " , result)
             ques2 = input("wanna try again? ")
             if (ques2 == "yes"):
                 continue
             else:
                break