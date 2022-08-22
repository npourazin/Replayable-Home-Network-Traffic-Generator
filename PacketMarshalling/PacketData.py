import datetime


class PacketData:
    invalid = False
    ts = None
    src_ip_addr = None
    src_port = None
    dst_ip_addr = None
    dst_port = None

    # add other attributes like packet sizes
    packet_size = 0
    ip_payload_size = 0
    tcp_payload_size = 0

    def __init__(self, ts, src_ip_addr, src_port, dst_ip_addr, dst_port, packet_size=0, ip_payload_size=0,
                 tcp_payload_size=0):
        self.ts = ts
        self.src_ip_addr = src_ip_addr
        self.src_port = src_port
        self.dst_ip_addr = dst_ip_addr
        self.dst_port = dst_port

        self.invalid = not(self.validate_packet_data())

        self.packet_size = packet_size
        self.ip_payload_size = ip_payload_size
        self.tcp_payload_size = tcp_payload_size

    def validate_packet_data(self):
        if self.ts is None or \
                self.src_ip_addr is None \
                or self.src_port is None \
                or self.dst_ip_addr is None \
                or self.dst_port is None:
            return False
        return True

    # def show_packet_data(self):
    #     pass

    def __str__(self):
        # "  ts: " + str(self.ts) + "\n" + \
        return "Packet:\n" + \
               "  ts:  " + str(datetime.datetime.utcfromtimestamp(self.ts)) + "\n" + \
               "  src: " + str(self.src_ip_addr) + ":" + str(self.src_port) + "\n" + \
               "  dst: " + str(self.dst_ip_addr) + ":" + str(self.dst_port) + "\n" + \
               "  Packet Sizes: " + str(self.packet_size) + " - " + str(self.ip_payload_size) + " - " + str(
                self.tcp_payload_size) + "\n"
