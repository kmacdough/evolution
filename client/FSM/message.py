from evo_json.convert_py_json.convert_player import convert_from_pj_player_start, convert_lob_to_lop
from evo_json.convert_py_json.convert_choice import convert_to_new_action4
from evo_json.convert_py_json.convert_state import  convert_from_pj_state
from evo_json.convert_py_json.convert_feeding import convert_player_feeding_choice_to_pj

class Message:
    """
    To represent a message from the server
    """

    @classmethod
    def apply(cls, msg, player, json_stream):
        """
        Applies some action on the player based on msg
        and writes the response to json steam
        :param msg: pyjson
        :param player: Player
        :return: None
        """
        raise NotImplementedError("Method not yet implemented")


class Ok(Message):

    @classmethod
    def apply(cls, msg, player, json_stream):
        return

class StartTurn(Message):

    @classmethod
    def apply(cls, msg, player, json_stream):
        player_state, wh = convert_from_pj_player_start(msg)
        player.start(player_state, wh)

class ChooseCp(Message):

    @classmethod
    def apply(cls, msg, player, json_stream):
        lop_before, lop_after = (convert_lob_to_lop(m) for m in msg)
        choices = player.get_card_choices(lop_before, lop_after)
        json_stream.send_py_json(convert_to_new_action4(choices))

class ChooseFeeding(Message):

    @classmethod
    def apply(cls, msg, player, json_stream):
        wh, other_players, own_player = convert_from_pj_state(msg)
        json_feeding_choice = convert_player_feeding_choice_to_pj(player.choose_feeding(wh, other_players, own_player))
        json_stream.send_py_json(json_feeding_choice)

class BadMsg(Message):
    pass

class GameOver(Message):
    """
    Represents recieving the EndOfStream
    """
    @classmethod
    def apply(cls, msg, player, json_stream):
        pass