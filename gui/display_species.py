from tkinter import *
from gui.display_card import DisplayCard
from gui.display import Display
from evolution.constants import SPECIES_MAX_TRAITS_PER_SPECIES
from gui.constants import SPECIES_BORDER

class DisplaySpecies(Display):
    """
    Displays species
    """
    def __init__(self, master, view_species):
        """
        :param master: the containing frame
        :param view_species: The view_species
        :type view_species: Species
        :return: None
        """
        Display.__init__(self, Frame(master, bd=2, relief='groove'))

        Label(self.root, text="Population = %s" % view_species.get_population()).grid()
        Label(self.root, text="Body size = %s" % view_species.get_body_size()).grid()
        Label(self.root, text="Food Tokens = %s" % view_species.get_num_food_tokens()).grid()
        Display.make_sub_views(self.root, view_species.get_played_cards(), DisplayCard)
