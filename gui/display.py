from tkinter import Frame

class Display:
    """
    Displays an object in the game
    """
    def __init__(self, root):
        self.root = root

    def grid(self, *args, **kwargs):
        self.root.grid(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self.root.pack(*args, **kwargs)

    @staticmethod
    def make_sub_views(root, loi, func):
        """
        Applies the display function on the list of
        items
        :param root: parent container
        :type root: ???
        :param loi: List of items
        :type loi: [i, ...]
        :param func: function to apply on list of items
        :type func: frame, i -> None
        :return: None
        """
        item_frame = Frame(root)
        item_frame.grid()
        for i, item in enumerate(loi):
            func(item_frame, item).pack(side="left", fill="y")