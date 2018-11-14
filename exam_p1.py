def text_files(filename):
    red = open(filename)
    elements = [line.split()[0].lower for line in red if line != '']
    return elements

"""trial code please ignore
# text_file = open("roster.txt", "r", encoding="utf8")
# lines = text_file
# lines = text_file.readlines()
# lines = str(lines.split()[0:])
"""

def get_value_dict():
    dict = {}
    val = 1
    for i in range(26):
        dict[chr(97 + 1)] = val
        val += 1
    return dict

def score_name(name):
    score_value = get_value_dict()
    score = 0
    for i in name:
        if i in score_value:
            score += score_value[i]
    return score

def positive_words_match(filename, score):
    red = open(filename)
    elements = [line.split()[0].lower for line in red if line != '']
    words_match = [name for name in name if score_name(name) == score]
    return words_match


def main():
    score_value = get_value_dict()
    scores = score_name('roster.txt')
    print('The person with the most valuable name is:')
    print(max(scores, key = scores.get()))

    words_match = positive_words_match('positive-words.txt', scores['pranjal'] )
    print('The positive words that match my name are:')
    for word in words_match:
        print(word)
if __name__ == '__main__':
    main()
