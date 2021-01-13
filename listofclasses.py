classes = []

print('what classes are you taking this semester?')

name_of_class = input ('Enter what class(Press Enter to stop): ')

while name_of_class: 
    classes.append(name_of_class)
    name_of_class = input ('Enter what class(Press Enter to stop): ') 

    print('Your classes this semester are: ')

    for index, c in enumerate(classes):
        print(f'{index+1} {c}')