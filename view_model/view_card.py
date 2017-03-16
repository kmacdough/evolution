class ViewCard:
    """
    To represent the viewmodel for the card
    """

    def __init__(self, card):
        """
        :param card: Card
        :return: None
        """
        self._card = card

    def get_name(self):
        """
        Gets the card name
        :rtype: String
        """
        return self._card.get_name()

    def get_food_tokens(self):
        """
        Gets the number of food tokens
        :rtype: int
        """
        return self._card.get_num_tokens_as_food_card()

    def get_description(self):
        """
        Gets the description of the card
        :return: String
        """
        return self._card.description

