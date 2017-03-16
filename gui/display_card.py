from gui.display import Display
from tkinter import *
from evolution.trait_cards import CarnivoreCard
from gui.constants import *


class DisplayCard(Display):
    def __init__(self, master, view_card):
        """
        Displays view_card
        :param master: the containing frame
        :param view_card: the view model of the card
        :type view_card: ViewCard
        :return: None
        """
        Display.__init__(self,
                         Frame(master,
                               bg=CARD_BG,
                               width=CARD_WIDTH,
                               height=CARD_HEIGHT))

        self.root.grid_propagate(False)

        self.make_label_with_text(view_card.get_name(), self.root)
        self.make_label_with_text(view_card.get_food_tokens(), self.root)
        self.make_label_with_text(view_card.get_description(), self.root)

    @staticmethod
    def make_label_with_text(txt, root):
        Label(root, text=txt, bg=CARD_BG, fg=CARD_TEXT, wraplength=CARD_WIDTH).grid()
