for i in range(5):
    word = input(f"Enter the {i+1}th word: ")
    j=0
    for letter in word:
        print(f"{j+1}th letter of {word} is: {letter}")
        j+=1
    print()
