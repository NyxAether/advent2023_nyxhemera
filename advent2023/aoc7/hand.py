class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.joker = False

    def hand_type(self, hand: str) -> str:
        cards = self.count_cards(hand)
        match len(cards):
            case 1:
                return 6  # Five of a kind
            case 2:
                if 4 in cards.values():
                    return 5  # Four of a kind
                return 4  # Full house
            case 3:
                if 3 in cards.values():
                    return 3  # Three of a kind
                return 2  # Two pairs
            case 4:
                return 1  # One pair
            case 5:
                return 0  # High card

    def card_type(self, card: str) -> int:
        match card:
            case "A":
                return 14
            case "K":
                return 13
            case "Q":
                return 12
            case "J":
                return 1
            case "T":
                return 10
            case _:
                return int(card)

    def count_cards(self, hand: str) -> int:
        cards = {}
        for card in hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1
        return cards

    def best_hand(self, hand1: str, hand2: str) -> int:
        """Compare two hands. If hand1 is better return 1, if hand2 is better return -1, else return 0

        Args:
            hand1 (str): First hand
            hand2 (str): Second hand

        Returns:
            int: 1 if hand1 is better, -1 if hand2 is better, 0 if equal
        """
        if self.joker:
            save_hand1 = hand1
            save_hand2 = hand2
            hand1 = self.best_replacement(hand1)
            hand2 = self.best_replacement(hand2)

        if self.hand_type(hand1) > self.hand_type(hand2):
            return 1
        elif self.hand_type(hand1) < self.hand_type(hand2):
            return -1
        else:
            if self.joker:
                hand1 = save_hand1
                hand2 = save_hand2
            for card1, card2 in zip(hand1, hand2):
                if self.card_type(card1) > self.card_type(card2):
                    return 1
                elif self.card_type(card1) < self.card_type(card2):
                    return -1
            return 0

    def best_replacement(self, hand: str) -> str:
        cards = self.count_cards(hand)
        if "J" in cards and cards["J"] < 5:
            cards["J"] = 0
            return hand.replace("J", max(cards, key=cards.get))
        return hand

    def __lt__(self, other):
        return self.best_hand(self.hand, other.hand) < 0

    def __gt__(self, other):
        return self.best_hand(self.hand, other.hand) > 0

    def __ge__(self, other):
        return self.best_hand(self.hand, other.hand) >= 0

    def __le__(self, other):
        return self.best_hand(self.hand, other.hand) <= 0

    def __eq__(self, other):
        return self.best_hand(self.hand, other.hand) == 0

    def __ne__(self, other):
        return self.best_hand(self.hand, other.hand) != 0
    
    def __str__(self) -> str:
        return self.hand
    
    def __repr__(self) -> str:
        return self.hand
