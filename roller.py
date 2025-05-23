import random

def roll_dice(num_dice, num_sides):
    """
    Rolls a specified number of dice with a specified number of sides.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.

    Returns:
        list: A list of integers representing the results of each die roll.
    """
    return [random.randint(1, num_sides) for _ in range(num_dice)]

def roll_dice(num_dice, num_sides, modifier):
    """
    Rolls a specified number of dice with a specified number of sides and applies a modifier.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.
        modifier (int): The modifier to apply to the total roll.

    Returns:
        int: The total result after applying the modifier.
    """
    rolls = roll_dice(num_dice, num_sides)
    return sum(rolls) + modifier

def roll_dice_with_advantage(num_dice, num_sides, advantage):
    """
    Rolls a specified number of dice with a specified number of sides and applies advantage.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.
        advantage (bool): If True, rolls with advantage.

    Returns:
        int: The highest result from the rolls.
    """
    if advantage:
        rolls = [roll_dice(num_dice, num_sides) for _ in range(2)]
        return max([max(roll) for roll in rolls])
    else:
        return max(roll_dice(num_dice, num_sides))