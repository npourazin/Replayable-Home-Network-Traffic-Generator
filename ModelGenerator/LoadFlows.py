import pickle
import random
from typing import Dict

from PacketMarshalling import Flow


class LoadFlows:
    flow_list: [Flow] = []
    file_addr = ""

    def __init__(self, filename):
        self.flow_list = self.load_flows(filename)
        self.file_addr = filename

    def load_flows(self, filename):
        # todo: open the file with the recorded flows and load the flows in a list (:flow_list)
        try:
            file_handler = open(filename, 'rb')
            flows = pickle.load(file_handler)
        except:
            print("Failed to reload. returning previous value for flow_list")
            return self.flow_list

        return flows

    def get_a_random_flow(self):
        return random.choice(self.flow_list)

    def get_flows(self):
        return self.flow_list


if __name__ == '__main__':
    lf = LoadFlows("../PacketMarshalling/FlowRecords/test5-2.obj")
    pac = lf.flow_list[0]
    print(lf.flow_list)
    print(lf.flow_list[0])

    # for f in lf.flow_list:
    #     if f.first_flow_packet.src_ip_addr != f.last_flow_packet.src_ip_addr:
    #         print(f)
    #         print(f.first_flow_packet.src_ip_addr)
    #         print(f.last_flow_packet.src_ip_addr)
    #
    #         # todo check why there are none of this
    # print(str(hash((1, 2))))
    # print(str(hash((2, 1))))
    # from collections import Counter
    # print(str(hash(frozenset(Counter([pac.src_ip_addr, pac.src_port, pac.dst_ip_addr, pac.dst_port]).items()))))
    # print(str(hash(frozenset(Counter([pac.dst_ip_addr, pac.dst_port, pac.src_ip_addr, pac.src_port]).items()))))
