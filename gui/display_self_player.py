from tkinter import Frame, Label, Tk
from gui.display_full_player import DisplayFullPlayer
from gui.display_player import DisplayPlayer
from gui.display import Display
from evo_tests.examples import ExampleDealers


class DisplaySelfPlayer(Display):
    def __init__(self, master, view_dealer, self_index):
        """
        :param master: the containing frame
        :param view_dealer: The view_dealer
        :type view_dealer: Dealer
        :return: None
        """
        Display.__init__(self, Frame(master))

        view_player_states = view_dealer.get_player_states()
        self_view_player = view_player_states[self_index]
        other_view_players = view_player_states[:self_index] + \
                        view_player_states[self_index + 1:]

        Label(self.root, text="Watering Hole = %s" % view_dealer.get_wateringhole()).grid()
        Label(self.root, text="Other Players").grid()

        Display.make_sub_views(self.root, other_view_players, DisplayPlayer)

        Label(self.root, text="You ;)").grid()
        DisplayFullPlayer(self.root, self_view_player).grid()

