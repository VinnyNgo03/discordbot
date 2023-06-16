import random
import numpy as np

names_bd = np.array([['vinny', 'jennifer', 'nicole', 'brandon', 'remi', 'justin', 'wayne'],
                     ['March 14', 'July 18', 'May 20', 'February 17', 'August 22', 'August ?', 'August 24']])


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return "!dice : roll a dice"

    if p_message == '!dice':
        return str(random.randint(1, 6))

    if p_message == '!coin':
        result = random.randint(1, 2)
        if result == 1:
            return 'heads'
        return 'tails'

    if p_message[:3] == '!bd':
        person_name = p_message[4:]
        for x in range(len(names_bd[0])):
            if person_name == names_bd[0][x]:
                return names_bd[1][x]

    return '???'
