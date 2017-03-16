from evo_json.convert_py_json.convert_player import convert_to_pj_player_start, \
    convert_lop_to_lob
from evo_json.convert_py_json.convert_step4 import convert_new_action4
from evo_json.convert_py_json.convert_state import convert_to_pj_state
from evo_json.convert_py_json.convert_feeding import \
    convert_from_pj_feeding_choice


class ProxyPlayer:
    """
    To represent a proxy player
    """

    def __init__(self, json_stream, info):
        """
        :param json_stream: The JSON stream to read/write from/to
        :type json_stream: JSONStream
        :param info: Player info
        :type info: String
        :return: None
        """
        self.json_stream = json_stream
        self.info = info

    def start(self, player_state, wh):
        """
        updates the player state
        :type: player_state: PlayerState
        :param wh: watring hole
        :type wh: Nat
        :return: None
        """
        py_json = convert_to_pj_player_start(player_state, wh)
        self.json_stream.send_py_json(py_json)

    def get_card_choices(self, c, d):
        """
        Gets the card choices from the players
        :param c: the states of the players before this player
        :type c: [PlayerState, ...]
        :param d: the states of the players after this player
        :type d: [PlayerState, ...]
        :return: A tuple containing both choices
        :rtype: (Nat, [CardPlay, ...])
        """
        py_json = [convert_lop_to_lob(lop) for lop in (c, d)]
        self.json_stream.send_py_json(py_json)
        response = self.json_stream.receive_py_json()
        return convert_new_action4(response)

    def choose_feeding(self, watering_hole, other_players, own_player):
        """
        Choose the next species for this player to feed. Must have at least 2 choices for feedings.
        :param watering_hole: the number of tokens at the watering hole
        :type watering_hole: Nat+
        :param players: the states of all players in the game (not including this player)
        :type players: [PlayerState, ...]
        :param own_player: This player's state
        :type own_player: Player
        :return: The player's evolution choice
        :rtype: PlayerFeedingChoice or None
        """
        py_json = convert_to_pj_state(watering_hole, other_players, own_player)
        self.json_stream.send_py_json(py_json)
        response = self.json_stream.receive_py_json()
        return convert_from_pj_feeding_choice(response)

    def get_player_info(self):
        """
        Gets the player info
        :return: String
        """
        return self.info