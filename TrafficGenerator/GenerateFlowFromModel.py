from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.layers import *

from ModelGenerator.Modelify import Modelify
from ModelGenerator.packet_list_attributes import PacketListAttribute

from scapy.all import *


class FlowGenerator:
    pla: PacketListAttribute = None

    def __init__(self, pla=None):
        self.pla = pla
        if pla is None:
            self.fill_pla()

    def generate_flow(self):
        pacs = []
        # for i, packet_size, ip_payload_size, tcp_payload_size in self.pla.pac_sizes_complete:
        #     print(i, packet_size, ip_payload_size, tcp_payload_size)

        for size in self.pla.item_size_list:
            l2 = Ether()
            # l3 = IP(dst='8.8.8.8/30')
            l3 = IP()
            # l4 = TCP(dport=53, flags='S')
            l4 = TCP()
            packet = l2 / l3 / l4 / ("X" * size)

            # packet.payload.dst = '8.8.8.8/30'
            # packet.dport = 80
            packet.show()
            pacs.append(packet)
        print(pacs)

    def fill_pla(self):
        pass


if __name__ == '__main__':
    addr = "../PacketMarshalling/FlowRecords/test5-2.obj"
    m = Modelify()
    fla, pla = m.create_model(addr=addr)
    FlowGenerator(pla).generate_flow()
