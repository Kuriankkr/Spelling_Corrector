import re

def possible_combinations_of_words(word):
        '''
        Input: 
        word: The input word for which the combinations have to be tried
        
        Output: 
        All possible combinations of the input word
        
        Description: 
        This function takes input word and calculates all possible combinations of the input word and returns the set of combinations
        '''
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)
        

def convert_file_to_lower_caps(text): 
    
        '''
        Input:
        text: Input file to convert to lower text
        
        Output:
        Returns the file converted to lower case
        
        Description:
        Takes an input file and converts to lower case        
        '''
        return re.findall(r'\w+', text.lower())
        
def known_words_from_big_text(combination,count_of_words_in_big_text): 
    
        '''
        Input:
        combination: All possible words in the list of combinations that are in the dictionary of count of words from the big file
        count_of_words_in_big_text: Dictionary of count of words within the input file
        
        Output:
        Returns a dictionary of words that are present in the larger file (big_text)
        
        Description:
        The function returns a dictionary of words present in big_text
        
        '''
        return set(w for w in combination if w in count_of_words_in_big_text)
        
def scnd_possible_combinations(combinations):
    
        '''
        Input:
        combinations: The combinations of words that are one degree of change from the original input word
        
        Output:
        Returns the sets of words that are two degrees away from the input word
        
        Description:
        The function returns a list of words that are two degree of differences from the input word
        
        
        '''
        scnd_degree_of_words = []
        for e1 in combinations:
            for e2 in possible_combinations_of_words(e1):
                scnd_degree_of_words.append(e2)
        return scnd_degree_of_words

def candidates(*args):
    
    '''
    Input: Multiple arguments
    word: Initial word that was typed by user
    first_matched_words_from_big_text: Words that are one degree change away form the input word
    second_matched_words_from_big_text: Words that are two degrees changes away from the input word
    count_of_words_in_big_text: Dictionary of words with the count of occurences for each word
    
    Output:
    Returns the first valid matches that is the most similar to the input word
    
    Description:
    Matches potential candidates for the input word and finds the closest match
    
    '''
    return (known_words_from_big_text([args[0]],args[3]) or  
            args[1] or 
            args[2] or 
            [args[0]])
            

def correction(possible_candidates,count_of_words_in_big_text):
    
    '''
    Input:
    possible_candidates: Final list of possible candidates 
    count_of_words_in_big_text: Dictionary of words with count for each word
    
    Output:
    Returns the possible word 
    
    Description:
    Find the word that has the max probability with the input word and returns that
    
    '''
    return max(possible_candidates, key = lambda k: count_of_words_in_big_text[k]/sum(count_of_words_in_big_text.values()))