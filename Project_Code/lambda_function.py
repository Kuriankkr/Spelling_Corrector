import json
from collections import Counter
import re
from Utilities  import *


def lambda_handler(event,context):
    
    #word = 'somthing'
    word = event['rawQueryString']
    
    first_combinations= possible_combinations_of_words(word)
    big_text = open('big.txt').read()
    list_of_words_in_big_text = convert_file_to_lower_caps(big_text)
    count_of_words_in_big_text =  Counter(list_of_words_in_big_text)
    
    
    second_combinations = scnd_possible_combinations(first_combinations)
    first_matched_words_from_big_text = known_words_from_big_text(first_combinations,count_of_words_in_big_text)
    second_matched_words_from_big_text = known_words_from_big_text(second_combinations,count_of_words_in_big_text)
    
    possible_candidates = candidates(word,first_matched_words_from_big_text,second_matched_words_from_big_text,count_of_words_in_big_text)
    final_candidate = correction(possible_candidates,count_of_words_in_big_text)

    return{
        'statusCode' :200,
        'body': json.dumps(final_candidate)
        
    }