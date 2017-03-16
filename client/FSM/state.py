import enum


class State(enum.Enum):
    START = 0
    TURN = 1
    CHOOSE_CARDS = 2
    FEED_NEXT = 3
    GAME_OVER = 4
    DEAD_STATE = 5

dead_state = lambda : State.DEAD_STATE