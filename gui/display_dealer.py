from tkinter import Frame, Label, Tk
from gui.display_full_player import DisplayFullPlayer
from gui.display_card import DisplayCard
from gui.display import  Display
from evo_tests.examples import ExampleDealers

class DisplayDealer(Display):
    """
    To represent displaying a dealer
    """
    def __init__(self, master, view_dealer):
        """
        :param master: the containing frame
        :param view_dealer: The view model for the dealer
        :type view_dealer: ViewDealer
        :return: None
        """
        Display.__init__(self, Frame(master))

        player_states = view_dealer.get_player_states()
        deck = view_dealer.get_deck()
        wateringhole = view_dealer.get_wateringhole()

        Label(self.root, text="Wateringhole = %s" % wateringhole).grid()
        Label(self.root, text="Players").grid()
        Label(self.root, text="Deck").grid()

        Display.make_sub_views(self.root, player_states, DisplayFullPlayer)
        Display.make_sub_views(self.root, deck.get_cards(), DisplayCard)
