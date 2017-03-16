class ViewSpecies:
    """
    To represent the view model for the species
    """

    def __init__(self, species):
        """
        :param species: Species
        :return: None
        """
        self._species = species

    def get_num_food_tokens(self):
        """
        gets the view model for number of food tokens
        :rtype: Nat
        """
        return self._species.num_food_tokens

    def get_body_size(self):
        """
        gets the body size
        :rtype: Nat
        """
        return self._species.body_size

    def get_population(self):
        """
        gets the population
        :return: Nat
        """
        return self._species.population

    def get_played_cards(self):
        """
        gets the view models for the cards for the species
        :return: [ViewCard, ...]
        """
        return [card.view_model() for card in self._species.get_active_cards()]
