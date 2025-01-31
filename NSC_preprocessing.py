import re

def apply_rules(sentence, min_char):
    '''
    To chain all rules together
    '''
    
    if not other_languages_rule(sentence):
        return  "REJECT"
    
    sentence = filler_word_rule(sentence)
    sentence = singlish_filler_word_rule(sentence)
    sentence = singlish_exclamation_rule(sentence)
    sentence = singlish_lingo_rule(sentence)
    sentence = acronyms_rule(sentence)
    sentence = shortforms_rule(sentence)
    
    if minimum_char_rule(sentence, min_char):
        return sentence
    else:
        return "REJECT"
    

def filler_word_rule(sentence):
    '''
    For words like etc. (uh), (mm), (pbo)
    
    REMOVE THESE WORDS
    '''
    
    pattern = r'\((.*?)\)'
    sentence = re.sub(pattern, r'', sentence)
    
    return sentence

def singlish_filler_word_rule(sentence):
    '''
    For words like etc. [ah], [leh], [orh]
    
    REMOVE the []
    '''
    
    pattern = r'\[(.*?)\]'
    sentence = re.sub(pattern, r'\1', sentence)
    
    return sentence

def other_languages_rule(sentence):
    '''
    For words like etc. <mandarin>…</mandarin>
    
    REMOVE WHOLE THING
    '''
    
    pass_rule = True
    
    pattern = r'\<(\w+)\>(.*?)\<\/\1\>'
    sentence = re.findall(pattern, sentence)
    
    if sentence:
        pass_rule = False
    
    return pass_rule
    

def singlish_exclamation_rule(sentence): 
    '''
    For words like etc. !aiyo!, !haiya!, !huh!
    
    REMOVE the []
    '''
    
    pattern = r'\!(.*?)\!'
    sentence = re.sub(pattern, r'\1', sentence)
    
    return sentence

def singlish_lingo_rule(sentence):
    '''
    For words like etc. #kor#, #pa#, #Hougang#
    
    REMOVE the ##
    '''
    
    pattern = r'\#(.*?)\#'
    sentence = re.sub(pattern, r'\1', sentence)
    
    return sentence

def acronyms_rule(sentence):
    '''
    For words like etc. U_E
    
    REPLACE the _ with blank space
    '''
    
    pattern = r'_'
    sentence = re.sub(pattern, r' ', sentence)
    
    return sentence

def shortforms_rule(sentence):
    '''
    For words like etc. U_E
    
    REPLACE the _ with blank space
    '''
    
    pattern = r'~'
    sentence = re.sub(pattern, r'', sentence)
    return sentence

def minimum_char_rule(sentence, minimum_char):
    """
    Minimum number of characters to meet if not remove
    """
    
    return len(sentence) >= minimum_char