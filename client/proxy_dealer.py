from collections import defaultdict

from client.FSM.state import State, dead_state
from client.FSM.fsm import FSM
from client.FSM.message import *
from evo_json.json_stream import EndOfStream


class ProxyDealer:
    """
    To represent a Proxy for the Dealer
    """

    def __init__(self, json_stream, player):
        """
        :param json_stream: the stream to read/write from/to
        :type json_stream: JSONStream
        :param player: the external Player to query
        :type player: Player

        self.fsm is an FSM that stores which messages it received
        last from the player and can determine which messages to
        expect.

        :return: None
        """
        self.json_stream = json_stream
        self.player = player
        self.fsm = FSM(State.START, TRANSITIONS)

    def wait_for_msg(self):
        """
        Waits for messages from the proxy dealer.
        :return: None
        """

        #send sign up msg to the server
        self.json_stream.send_py_json("Hi")

        while self.fsm.state is not State.GAME_OVER:
            msg = self.json_stream.receive_py_json()
            decoded_msg_cls = self.decode_msg(msg)
            self.fsm.transition(decoded_msg_cls)
            if self.fsm.state is State.DEAD_STATE:
                raise BadDealerError
            else:
                decoded_msg_cls.apply(msg, self.player, self.json_stream)
        print("Game Over")


    def decode_msg(self, json_msg):
        """
        Decodes the json msg to the appropriate message class for FSM
        :param json_msg: PyJSON or EndOfStream
        :return: Message
        """
        if isinstance(json_msg, EndOfStream):
            return GameOver
        if json_msg == "ok":
            return Ok

        elif isinstance(json_msg, list):
            if len(json_msg) == 4:
                return StartTurn
            if len(json_msg) == 2:
                return ChooseCp
            if len(json_msg) == 5:
                return ChooseFeeding

        return BadMsg

TRANSITIONS = {
    State.START:        defaultdict(dead_state, {Ok: State.TURN}),
    State.TURN:         defaultdict(dead_state, {StartTurn: State.CHOOSE_CARDS}),
    State.CHOOSE_CARDS: defaultdict(dead_state, {ChooseCp: State.FEED_NEXT}),
    State.FEED_NEXT:    defaultdict(dead_state,
                                 {ChooseFeeding: State.FEED_NEXT,
                                  StartTurn: State.CHOOSE_CARDS,
                                  GameOver: State.GAME_OVER}),
    State.GAME_OVER:    defaultdict(dead_state, {}),
    State.DEAD_STATE:   defaultdict(dead_state, {})
}

class BadDealerError(BaseException):
    """
    Represents an error for bad message sent
    by the dealer
    """
    pass



