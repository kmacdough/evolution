import socket
from evo_json.json_stream import JSONStream
from server.proxy_player import ProxyPlayer
from evolution.timeout import timeout
from dealer.dealer import Dealer
from dealer.deck import Deck
from main import print_score

import time

HOST = "localhost"
PORT = 45678
CONNECTIONS = 5
MAX_NUM_PLAYERS = 8
MIN_NUM_PLAYERS = 3
MAX_TIME = 10
ACCEPT_TIMEOUT = 2


def main(argv):
    #create socket
    host, port = parse_args(argv)
    server_socket = make_socket(port)
    start_time = time.time()
    players = []

    add_player(players, server_socket, start_time)

    dealer = Dealer(players, Deck.make_deck())
    dealer.run_game()

    score = dealer.get_sorted_scores()
    print_score(score)


def parse_args(argv):
    """
    parses arguments
    :param argv: string arguments
    :return: (host, port)
    """
    host, port = HOST, PORT
    if len(argv) >=1:
        host = argv[0]
    if len(argv) >=2:
        port = int(argv[1])

    return host, port

@timeout()
def accept_player(clientsocket):
    """
    Waits for a message from client socket and responds
    to the player with an "ok"
    :param clientsocket: socket
    :return: ProxyPlayer or False
    """
    stream = JSONStream(clientsocket)
    info = stream.receive_py_json()
    if not verify_info(info):
        return False
    else:
        stream.send_py_json("ok")
        return ProxyPlayer(stream, info)

def verify_info(info):
    """
    Verifies that the player info is a string
    :param info: player info
    :type info: Pyjson
    :rtype: Boolean
    """
    return isinstance(info, str)

def make_socket(port):
    """
    Creates a server socket
    :return:
    """
    #create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind socket to host
    server_socket.bind((HOST, port))

    #become a server socket
    server_socket.listen(CONNECTIONS)
    server_socket.settimeout(ACCEPT_TIMEOUT)
    return server_socket

def add_player(curr_players_list, server_socket, start_time):
    """
    Add a new player to the current list of players
    :param curr_players_list: [ProxyPlayer, ...]
    :return: None
    """
    while   (len(curr_players_list) < MIN_NUM_PLAYERS or
            (len(curr_players_list) < MAX_NUM_PLAYERS and
            (time.time() - start_time) < MAX_TIME)):
            #accept connections from remote client

            try:
                (clientsocket, address) = server_socket.accept()
            except socket.timeout:
                pass

            else:

                try:
                    possible_player = accept_player(clientsocket)
                    if possible_player:
                        curr_players_list.append(possible_player)

                except TimeoutError:
                    pass


if __name__ == '__main__':
    main()
