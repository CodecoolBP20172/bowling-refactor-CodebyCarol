# X means strike
# / means spare
# - means miss
def score(game):
    result = 0
    frame = 1
    in_first_try = True
    game=game.lower()
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_try:
            frame += 1
        if game[i] == 'x':
            in_first_try = True
            frame += 1
        else:
            in_first_try = not in_first_try
    return result

def get_value(char):
    if char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    elif int(char) > 0 and int(char) < 10:
        return int(char)
