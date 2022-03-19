val = int(input(print("Enter a number: ")))
option = {
    "N":"Nae nigga nae \n", "n":"Nae nigga nae \n", "C":"Uohhhhhh :sob::sob::sob: \n", "c":"Uohhhhhh :sob::sob::sob: \n",
    "I":"I am living in your walls, oomfie. \n", "i":"I am living in your walls, oomfie. \n"
    }
userinput = input("Choose your poison: [N]iggas, [C]unny, [I]solation")
f = open('outputtings.txt','w')
print(option[userinput] * val, file=f)
print("Output saved to file. Spam responsibly, fam.")