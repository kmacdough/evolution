from cardplay.cardplay import CardPlay


class ReplaceCards(CardPlay):
    def __init__(self, played_card_index, species_index, replaced_card_index):
        """
        :param played_card_index: the card to replace with
        :type played_card_index: Nat
        :param species_index: the species
        :type species_index: Nat
        :param replaced_card_index: replaced card index
        :type replaced_card_index: Nat
        :return: None
        """
        CardPlay.__init__(self, played_card_index)
        self.species_index = species_index
        self.replaced_card_index = replaced_card_index

    def apply(self, player_state):
        species = player_state.species_list[self.species_index]
        played_card = player_state.hand[self.played_card_index]
        species.played_cards[self.replaced_card_index] = played_card


    def verify_self(self, player_state, food_card_index, card_plays_before_this):
        return super(ReplaceCards, self).verify_self(player_state, food_card_index, card_plays_before_this) and\
         player_state.validate_species_index(self.species_index, card_plays_before_this) and\
         player_state.validate_species_trait_index(self.species_index, self.replaced_card_index, card_plays_before_this)


    def update_trait_counts(self, species_trait_count):
        return species_trait_count

    def __eq__(self, other):
        if not isinstance(other, ReplaceCards):
            return false
        else:
            return self.played_card_index == other.played_card_index and \
                   self.species_index == other.species_index and \
                   self.replaced_card_index == other.replaced_card_index

    def __repr__(self):
        return "ReplaceCards(%s, %s, %s)" % \
               (repr(self.played_card_index), repr(self.species_index), repr(self.replaced_card_index))
