lexicon = {
    'stop': ['the', 'in', 'of'],
    'direction': ['north', 'south', 'east', 'west'],
    'verb' : ['go', 'kill', 'eat'],
    'noun': ['bear', 'princess'],
}


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def get_entries():
    lyst = lexicon.values()
    flat_list = [item for sublist in lyst for item in sublist]
    return flat_list


def scan(str_1):
    lexicon_tuples = []
    # get all of the legit words in a flat list
    entries = get_entries()

    words = str_1.split()

    for word in words:
        # see if word can be parsed into a number
        number = convert_number(word)
        if number:
            lexicon_tuples.append(('number', number))
        elif  word in entries:
            for key in lexicon.keys():
                if word in lexicon[key]:
                    lexicon_tuples.append((key, word))
        else:
            lexicon_tuples.append(('error', word))

    return lexicon_tuples


if __name__ == '__main__':
    print(get_entries())
    print(scan("ASDFADFASDF"))
