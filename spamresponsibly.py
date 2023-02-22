def main():
    option = {
        "n":"Nae nikka nae nae nikka nikka nae nae\n", 
        "c":"Uohhhhhh :sob::sob::sob:\n",
        "i":"I am living in your walls, oomfie.\n"
    }

    try:
        val = int(input('Enter a number: '))
        userinput = input('Choose your poison: [N]ae nae, [C]unny, [I]solation: ')

        if userinput.lower() in ['n', 'c', 'i']:
            with open("outputtings.txt",'w') as f:
                f.write(option[userinput.lower()] * val)

            print("Output saved to file. Spam responsibly, fam.")
        else:
            print('Dis no work m8, only N, C and I.')
    except ValueError as ve:
        print('Dis no numbar plis fix.')


if __name__ == '__main__':
    main()
