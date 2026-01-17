# WPTC weather the given character is uppercase or lowercase or digit or special char.



while True:
    get_str =input("Enter a character: ")
    if(get_str == ""):
        print("No data Available")
        break
    elif len(get_str)>=2:
        print(len(get_str))
        print('Invalid length')
        break
    elif 'A'<= get_str <='Z':
        print('char is upper')
    elif 'a'<= get_str<= 'z':
        print("char is lower")
    elif '0' <= get_str <= '9':
        print("char is digit")
    else:
        print('char is special')


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

    for i in range(0, 10, 2):
    print(i)

