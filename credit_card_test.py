import credit_card

if credit_card.check(1):
    print("Error:  1 is not valid")

if credit_card.check(240):
    print("Good:  240 is  valid")

if credit_card.check(9548):
    print("Good:  9548 is valid")

if credit_card.check(5490123456789129):
    print("Error:  5490123456789129 is not valid")

if credit_card.check(-2):
    print("Error: -2 is not valid")

if credit_card.check(23.7):
    print("Error: 23.7 is not valid")
