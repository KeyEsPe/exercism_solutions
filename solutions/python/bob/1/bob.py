def response(hey_bob):
    """
    This code determines answers depending on different 
    types of queries.
    """
    # To make conditions more readable we define two basic variables.
    # We have to remove white characters using strip() and check if the string even has any letters with isalpha()
    is_a_yell = hey_bob.strip().isupper() and any(c.isalpha() for c in hey_bob)
    # We remove empty characters from the beginning and the end and check if last character is "?"
    ends_with_q = hey_bob.rstrip().endswith("?")
    
    if is_a_yell and ends_with_q:
        return "Calm down, I know what I'm doing!"
    elif not hey_bob.strip():
        return "Fine. Be that way!"
    elif is_a_yell:
        return "Whoa, chill out!"
    elif ends_with_q:
        return "Sure."
    else:
        return "Whatever."
        