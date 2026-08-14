def response(hey_bob):
    msg = hey_bob.strip()
    
    if not msg:
        return "Fine. Be that way!"
    
    is_question = msg.endswith("?")
    is_yelling = msg.upper() == msg and msg.lower() != msg
    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."