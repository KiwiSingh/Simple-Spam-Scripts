val = int(input(print("Enter a number: ")))
option = {
    "n":"Nae nigga nae \n", "c":"Uohhhhhh :sob::sob::sob: \n",
    "i":"I am living in your walls, oomfie. \n"
    }
userinput = input("Choose your poison: [N]iggas, [C]unny, [I]solation")
with open("outputtings.txt",'w') as f:
    f.write(option[userinput.lower()] * val)
print("Output saved to file. Spam responsibly, fam.")
