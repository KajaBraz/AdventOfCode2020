from day4 import get_list
from day23 import str_to_list


def first_bigger(card1: int, card2: int) -> bool:
    return card1 > card2


def combat(cards_player1: [int], cards_player2: [int]) -> [int]:
    while len(cards_player1) > 0 and len(cards_player2) > 0:
        card_player1 = cards_player1.pop(0)
        card_player2 = cards_player2.pop(0)
        if first_bigger(card_player1, card_player2):
            cards_player1 += [card_player1, card_player2]
        else:
            cards_player2 += [card_player2, card_player1]
    if len(cards_player1) > 0:
        return cards_player1
    return cards_player2


def resursive_combat(cards_player1: [int], cards_player2: [int], cards_previous_rounds: set) -> ([int]):
    while len(cards_player1) > 0 and len(cards_player2) > 0:
        if (tuple(cards_player1), tuple(cards_player2)) in cards_previous_rounds:
            return cards_player1 + cards_player2, []
        cards_previous_rounds.add((tuple(cards_player1), tuple(cards_player2)))
        card_player1 = cards_player1.pop(0)
        card_player2 = cards_player2.pop(0)

        if len(cards_player1) >= card_player1 and len(cards_player2) >= card_player2:
            new_cards_player1 = cards_player1[:card_player1]
            new_cards_player2 = cards_player2[:card_player2]
            combat_result = resursive_combat(new_cards_player1, new_cards_player2, set())
            if not combat_result[1]:
                cards_player1 += [card_player1, card_player2]
            else:
                cards_player2 += [card_player2, card_player1]
        elif first_bigger(card_player1, card_player2):
            cards_player1 += [card_player1, card_player2]
        else:
            cards_player2 += [card_player2, card_player1]

    if len(cards_player1) == 0:
        return [], cards_player2
    return cards_player1, []


def count_result(cards: [int]) -> int:
    return sum([cards[ind] * (len(cards) - ind) for ind in range(len(cards))])


if __name__ == '__main__':
    cards = get_list('input22.txt')
    player1 = str_to_list(cards[1:len(cards) // 2])
    player2 = str_to_list(cards[len(cards) // 2 + 2:])
    winner_cards = combat(player1, player2)
    print(count_result(winner_cards))

    player1_r = str_to_list(cards[1:len(cards) // 2])
    player2_r = str_to_list(cards[len(cards) // 2 + 2:])
    recursive_winner = resursive_combat(player1_r, player2_r, set())
    if recursive_winner[0] != []:
        print(count_result(recursive_winner[0]))
    else:
        print(count_result(recursive_winner[1]))
