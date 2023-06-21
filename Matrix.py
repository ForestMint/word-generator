class Matrix():

    def __init__(self,depth):
        self.depth=depth

    def fill(self, file):
        with open("./lists_of_example_words/"+file) as f:
            for word in f:
                place_in_word=0
                for letter in word:
                    print(letter)
                    if place_in_word==0:
                        if not(table[None][letter]):
                            table[None][letter]=1
                        else:
                            table[None][letter]+=1
                    place_in_word+=1

    def standardize(self):
        pass

    def generate_word(self):
        word=""
        character = get_char(word)
        word = word + character
        while character :
            character = get_char(word)
            if character :
                word = word + character
        return word

def get_char(self,word):
    if word == "" :
        dict_of_possibilities = table [None]
        return pick_char_in_dict_of_possibilities(dict_of_possibilities)  
    else :
        chain = word[self.depth:]
        dict_of_possibilities = table [chain]
        return pick_char_in_dict_of_possibilities(dict_of_possibilities)  

def pick_char_in_dict_of_possibilities(self,dict_of_possibilities):
    keys_of_possibilities = dict_of_possibilities.keys()
    values_of_possibilities = dict_of_possibilities.values()

    sum=0
    for key in keys_of_possibilities:
        key += sum
        sum = key

    random=random(0,1)
    for key, value in zip(keys_of_possibilities, values_of_possibilities):
        if key>random:
            return value