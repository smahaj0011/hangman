import requests, random

wrong_letters = []  
index = None

def randomWord():
    data = requests.get("https://random-words-api.vercel.app/word").json()
    return {
        "word":data[0]["word"].lower(),
        "definition":data[0]["definition"].lower()
    }
  

def get_index(input, find):
    return [x for x in range(len(input)) if(input[x]==find)]

def main():
    global index
    results = randomWord()
    word = results["word"]
    definition = results["definition"]
    guesses = 0
    random_num = random.randint(0,len(word)-1)
    word_ls = [word[x] if word[x] == word[random_num] else "_" for x in range(len(word))]

    while True:
        if index != None:
            for y in index:
                word_ls[y] = word[y]
            index = None

        for x in word_ls:
            print(x, end=" ")
        print()
        
        if(wrong_letters!=[]):
            print('Wrong letters: ')
            for x in set(wrong_letters):
                print(x, end=" ")
            print()

        if "_" not in word_ls:
            print(f'You won!\nNumber of guesses it took: {guesses}\nFun Fact: The definiton for this word is {definition}')
            break

        guess = input("\nEnter your guess: ").lower()

        while guess.isnumeric():
            print("No numbers please.")
            guess = input("Enter your guess: ").lower()

        guesses += 1

        if(len(guess) > 1) and (guess == word):
            return print(f'Congrats, you got it correct!\nNumber of guesses it took: {guesses}\nDid you know that {word} is {definition}!')

        if(guesses==20):
            print(f'You ran outta guesses. The word was {word} which means {definition}:')
            return

        if(guess in word) and (guess in word_ls):
            print('This letter is already there. Pick a new letter!')


    
        if guess in word:
            if(len(guess) == 1):
                for x in range(len(word)):
                    if word[x] == guess and word_ls[x]=="_":
                        index = get_index(word, word[x])
                        continue
            else:
                print(f"Hint: {guess} is somewhere in the word!")
        else:
            if(len(guess) == 1):
                print('Wrong')
                wrong_letters.append(guess)
            elif(len(guess) > 1):
                print('Incorrect guess')

main()



    
