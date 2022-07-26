class PacketData:
    invalid = False
    src_ip_addr = None
    src_port = None
    dst_ip_addr = None
    dst_port = None

    # todo: add other attributes like packet size

    def __init__(self, src_ip_addr, src_port, dst_ip_addr, dst_port):
        self.src_ip_addr = src_ip_addr
        self.src_port = src_port
        self.dst_ip_addr = dst_ip_addr
        self.dst_port = dst_port

        self.invalid = self.validate_packet_data()

    def validate_packet_data(self):
        if self.src_ip_addr is None or self.src_port is None or self.dst_ip_addr is None or self.dst_port is None:
            return True
        return False

    def show_packet_data(self):
        # todo: make some pretty printing format
        pass
