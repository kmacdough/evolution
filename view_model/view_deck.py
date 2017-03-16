class ViewDeck:
    """
    To represent a view model for the deck
    """

    def __init__(self, deck):
        """
        :param deck: the deck
        :rtype deck: Deck
        :return: None
        """
        self._deck = deck

    def get_cards(self):
        """
        Gets the view model for the cards in the deck
        :rtype: [ViewCard, ...]
        """
        return [card.view_model() for card in self._deck.loc]


