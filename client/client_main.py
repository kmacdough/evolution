import socket
import sys
from evolution.player.player import Player
from client.proxy_dealer import ProxyDealer
from evo_json.json_stream import JSONStream

HOST = "localhost"
PORT = 45678

def main(argv):
    """
    Runs the client main
    :param argv: a list of host and port
    :return: None
    """
    (host, port) = parse_args(argv)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    json_stream = JSONStream(client_socket)
    player = Player()
    proxy_dealer = ProxyDealer(json_stream, player)
    proxy_dealer.wait_for_msg()

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


if __name__ == '__main__':
    main(sys.argv[1:])