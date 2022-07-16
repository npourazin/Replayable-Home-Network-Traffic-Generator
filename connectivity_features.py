import socket


def get_packet_src_ip(pac):
    if hasattr(pac, 'src'):
        return socket.inet_ntoa(pac.src)


def get_packet_dst_ip(pac):
    if hasattr(pac, 'dst'):
        return socket.inet_ntoa(pac.dst)


def get_packet_src_port(pac):
    if hasattr(pac, 'data') and hasattr(pac.data, 'sport'):
        return pac.data.sport


def get_packet_dst_port(pac):
    if hasattr(pac, 'data') and hasattr(pac.data, 'dport'):
        return pac.data.dport


def duration(pac):
    if hasattr(pac, 'ttl'):
        return pac.ttl
