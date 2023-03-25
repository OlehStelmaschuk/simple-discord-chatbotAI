from journey.adventure_algorithm import create_adventure, continue_adventure


async def handle_create_adventure(users_info):
    adventure_state = create_adventure(users_info)
    return adventure_state


async def handle_continue_adventure(adventure_state):
    updated_adventure_state = continue_adventure(adventure_state)
    return updated_adventure_state
