#group the words based on the word families 
def group_words(words, guess):
    groups = {}
    for word in words:
        #add each word to the group based on the location of the guessed characters
        pattern = ''.join([char if char in guess else '*' for char in word])
        if pattern not in groups:
            groups[pattern] = []
        groups[pattern].append(word)
    return groups

def main():
    #store all words in an array
    with open('dictionary.txt', 'r') as file:
        words = [line.strip() for line in file]

    #parameters to initialize game
    word_len = int(input("Enter word length: "))

    while(word_len not in [len(word) for word in words]):
        word_len = int(input("There are no words of that length. Choose a different length: "))
    
    tot_guesses = int(input("Enter number of guessses: "))

    curr_num_guesses = 0
    candidates = [word for word in words if len(word) == word_len]
    guessed_letters = set()
    letters_left = list('abcdefghijklmnopqrstuvwxyz')
    while(curr_num_guesses < tot_guesses):
        print(' '.join(letters_left))
        guess = (input("\nGuess a letter: ").lower())
        while(guess in guessed_letters):
            guess = (input("You already guessed this letter. Try again: ").lower())
        guessed_letters.add(guess)
        curr_num_guesses += 1
        letters_left.remove(guess)
        groups = group_words(candidates, guessed_letters)
        candidates = max(groups.values(), key=len)
        
        for key, value in groups.items():
            if value == candidates:
                guessed_word = key     
        print(f"\n {guessed_word}\n")
        
        if(len(candidates) == 1 and '*' not in guessed_word):
            print(f"You win!")
            return
    print(f"You lose... the word was {candidates[0]}")

main()