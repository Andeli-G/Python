"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """
    return("un" + word)
    pass


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    words = [vocab_words[0]]
    for i in vocab_words[1:]:
        words.append(vocab_words[0]+i )
    return " :: ".join(words)
    pass


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    sep = word.split("ness")
    if sep[0][-2] in {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','t','s','v','w','z'} and sep[0][-1]=='i':
        return(sep[0][:-1]+"y")
    else:
        return sep[0]
    pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.
https://assets.exercism.org/assets/icons/run-tests-7259457020c0ad37ed70454416e07956cb5d40cf.svg
    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    sen = sentence.split()
    adj= sen[index].split(".")
    return(adj[0]+"en")
    