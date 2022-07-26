

class PacketData:
    invalid = False
    src_ip_addr = None
    src_port = None
    dst_ip_addr = None
    dst_port = None
    # todo: add other attributes like packet size

    def __init__(self, src_ip_addr, src_port, dst_ip_addr, dst_port):
        if src_ip_addr is None or src_port is None or dst_ip_addr is None or dst_port is None:
            self.invalid = True
            return
        self.src_ip_addr = src_ip_addr
        self.src_port = src_port
        self.dst_ip_addr = dst_ip_addr
        self.dst_port = dst_port
        self.invalid = False
