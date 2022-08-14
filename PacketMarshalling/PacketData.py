class PacketData:
    invalid = False
    ts = None
    src_ip_addr = None
    src_port = None
    dst_ip_addr = None
    dst_port = None

    # todo: add other attributes like packet size

    def __init__(self, ts, src_ip_addr, src_port, dst_ip_addr, dst_port):
        self.ts = ts
        self.src_ip_addr = src_ip_addr
        self.src_port = src_port
        self.dst_ip_addr = dst_ip_addr
        self.dst_port = dst_port

        self.invalid = self.validate_packet_data()

    def validate_packet_data(self):
        if self.ts is None or \
                self.src_ip_addr is None \
                or self.src_port is None \
                or self.dst_ip_addr is None \
                or self.dst_port is None:
            return True
        return False

    # def show_packet_data(self):
    #     pass

    def __str__(self):
        return "Packet:\n" + \
               "  ts: " + str(self.ts) + "\n" + \
               "  src: " + str(self.src_ip_addr) + ":" + str(self.src_port) + "\n" + \
               "  dst: " + str(self.dst_ip_addr) + ":" + str(self.dst_port) + "\n"
        # todo update with new parameters like packet size
