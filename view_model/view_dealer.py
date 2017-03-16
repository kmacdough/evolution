class ViewDealer:
    """
    To represent the view-model for the dealer
    """

    def __init__(self, dealer):
        """
        :param dealer:
        :type dealer: Dealer
        :return: None
        """
        self._dealer = dealer

    def get_deck(self):
        """
        Gets the view model for the deck
        :rtype: ViewDeck
        """
        return self._dealer.deck.view_model()

    def get_player_states(self):
        """
        Gets the view model for the player states
        :rtype: [ViewPlayerState, ...]
        """
        return [player_state.view_model() for player_state in self._dealer.player_states]

    def get_wateringhole(self):
        """
        Gets the view model for the wateringhole
        :rtype: int
        """
        return self._dealer.wateringhole
