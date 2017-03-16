from tkinter import *
from gui.display_species import DisplaySpecies
from gui.display import Display
from evolution.constants import SPECIES_MAX_TRAITS_PER_SPECIES
from evolution.player.iplayer import IPlayer
from evo_tests.examples import ExamplePlayerStates

class DisplayPlayer(Display):
    """
    Displays the player
    """
    def __init__(self, master, view_player_state):
        """
        :param master: the containing frame
        :param view_player_state: The view model for player state
        :type view_player_state: ViewPlayerState
        :return: None
        """
        Display.__init__(self, Frame(master, bd=2, relief="groove"))
        view_species = view_player_state.get_species_list()

        Label(self.root, text="Food Bag = %s" % view_player_state.get_food_bag()).grid(row=0)
        Label(self.root, text="ID = %s" % view_player_state.get_id()).grid(row=1)
        Display.make_sub_views(self.root, view_species, DisplaySpecies)
