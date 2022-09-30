import random

import dpkt


class PcapEditor:
    file_addr = ""
    pcap_file = None
    mtu = 1500
    samples = []

    def __init__(self, file_addr, handle_type="wb"):
        self.file_addr = file_addr
        # todo: check type
        self.pcap_file = open(file_addr, handle_type)
        self.load_basic_tcp_packet("./TestFile")

    def publish_packet(self, ts, packet_size):
        if packet_size < 40:
            packet_size = 40
        if packet_size > self.mtu:
            packet_size = self.mtu

        rand_pac = random.choice(self.samples)
        eth = dpkt.ethernet.Ethernet(rand_pac)
        ip_layer = eth.data
        previous_packet_size = len(ip_layer)
        tcp_layer = ip_layer.data
        app_layer = tcp_layer.data

        if previous_packet_size < packet_size:
            # todo: remove something from the payload
            print("oops too much ")
            cutoff = packet_size - previous_packet_size

        elif previous_packet_size > packet_size:
            # todo: add some bullshit in the packet
            print("whoops gotta fill it up")
            addon = previous_packet_size - packet_size

        # todo have a packet that you change the payload to set it's size
        return rand_pac

    def load_basic_tcp_packet(self, sample_file):
        f = open(sample_file, 'rb')
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            self.samples.append(buf)


if __name__ == '__main__':
    pe = PcapEditor("./TestFiles/empty.pcap")
    pe.publish_packet(ts=22.477363, packet_size=60)
