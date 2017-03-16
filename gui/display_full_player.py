from gui.display_player import DisplayPlayer
from gui.display_card import DisplayCard
from gui.display import Display
from evo_tests.examples import ExamplePlayerStates
from tkinter import *


class DisplayFullPlayer(DisplayPlayer):
    """
    To represent the complete player
    """
    def __init__(self, master, view_player_state):
        DisplayPlayer.__init__(self, master, view_player_state)
        Label(self.root, text="Hand").grid()

        Display.make_sub_views(self.root, view_player_state.get_hand(), DisplayCard)
