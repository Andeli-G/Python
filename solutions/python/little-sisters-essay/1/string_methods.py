"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """
    t= title.split()
    a=""
    for item in t:
        new = chr(ord(item[0])-32)
        new += item[1:]
        a+=f"{new} " 
    a=a[:-1]
    return(a)


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """
    return(sentence[-1] in {".","?","!"})

    pass


def clean_up_spacing(sentence):    
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.
    
    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """
    s= sentence.split()
    a=""
    a=" ".join(s)
    return(a)
    pass


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """
    if check_sentence_ending(sentence):
        sentence=sentence[:-1]
    
    s=sentence.split(" ")
    if old_word not in s:
       return(sentence+".")
    print(s)
    print(s.index(old_word))
    s[s.index(old_word)]=new_word
    a=""
    a=" ".join(s)
    if not check_sentence_ending(a):
        a+="."
    return(a)
