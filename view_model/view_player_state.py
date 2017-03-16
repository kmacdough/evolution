class ViewPlayerState:
    """
    To represent the view model for the player state
    """

    def __init__(self, player_state):
        """
        :param player_state: the player state
        :type player_state: PlayerState
        :return: None
        """
        self._player_state = player_state

    def get_hand(self):
        """
        Gets the view model for the cards in the player's hand
        :rtype: [ViewCard, ...]
        """
        return [card.view_model() for card in self._player_state.hand]

    def get_species_list(self):
        """
        Gets the view model for species list for the player
        :return: [ViewSpecies, ...]
        """
        return [species.view_model() for species in self._player_state.species_list]

    def get_food_bag(self):
        """
        Gets the food bag
        :rtype: Nat
        """
        return self._player_state.food_bag

    def get_id(self):
        """
        Gets the id for the player
        :rtype: Nat+
        """
        return self._player_state.id