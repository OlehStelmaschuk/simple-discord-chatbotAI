import random
import json


def create_adventure(users_info):
    # Загрузка данных Warhammer 40K
    with open("journey/warhammer_data.json", "r", encoding="utf-8") as file:
        warhammer_data = json.load(file)

    # Создание чарлиста на основе пожеланий игроков
    char_list = []
    for user in users_info:
        char_list.append({'user': user, 'character': random.choice(warhammer_data['characters'])})

    # Создание начального квеста на основе уровней и способностей игроков
    starting_quest = random.choice(warhammer_data['quests'])

    return {'char_list': char_list, 'quest': starting_quest}


def continue_adventure(adventure_state):
    # Загрузка данных Warhammer 40K
    with open("journey/warhammer_data.json", "r", encoding="utf-8") as file:
        warhammer_data = json.load(file)

    # Создание следующего квеста на основе предыдущего квеста и выборов игроков
    next_quest = random.choice(warhammer_data['quests'])

    return {'char_list': adventure_state['char_list'], 'quest': next_quest}
