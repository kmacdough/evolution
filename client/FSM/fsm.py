class FSM(object):
    """
    To represent a Finite State Machine
    """

    def __init__(self, start_state, transitions):
        """
        Creates a FSM with states of type X and transitions of type Y
        :param start_state: The initial state of the FSM
        :type start_state: X
        :param transitions: The transitions of the FSM
        :type transitions: {X: {Y: X, ...}, ...}
        :return:
        """
        self.state = start_state
        self.transitions = transitions

    def transition(self, message):
        """
        Transition this FSM based on the given message
        :param message: message to transition with
        :return:
        """
        curr_transitions = self.transitions[self.state]
        self.state = curr_transitions[message]