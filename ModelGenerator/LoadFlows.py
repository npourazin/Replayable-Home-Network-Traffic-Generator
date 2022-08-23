import pickle
from typing import Dict

from PacketMarshalling import Flow


class LoadFlows:
    # flow_list: Dict[Flow] = {}
    flow_list = []

    # todo create a model using the detected flows

    def __init__(self, filename):
        self.flow_list = self.load_flows(filename)

    def load_flows(self, filename):
        # todo: open the file with the recorded flows and load the flows in a list (:flow_list)
        filehandler = open(filename, 'rb')
        # pm: PacketMarshaller = None
        flows = pickle.load(filehandler)
        print(flows)
        print(type(flows))
        # for flow in flows:
        #     print(flows[flow])
        return flows

    def get_flows(self):
        return self.flow_list


if __name__ == '__main__':
    lf = LoadFlows("../PacketMarshalling/FlowRecords/test5-2.obj")
    pac = None
    print(lf.flow_list)
    print(lf.flow_list[0])
    # for f in lf.flow_list:
    #     if lf.flow_list[f].first_flow_packet.src_ip_addr != lf.flow_list[f].last_flow_packet.src_ip_addr:
    #         print(lf.flow_list[f])
    #         print(lf.flow_list[f].first_flow_packet.src_ip_addr)
    #         print(lf.flow_list[f].last_flow_packet.src_ip_addr)
    #
    #         # todo check why there are none of this
    # print(str(hash((1, 2))))
    # print(str(hash((2, 1))))
    # from collections import Counter
    # print(str(hash(frozenset(Counter([pac.src_ip_addr, pac.src_port, pac.dst_ip_addr, pac.dst_port]).items()))))
    # print(str(hash(frozenset(Counter([pac.dst_ip_addr, pac.dst_port, pac.src_ip_addr, pac.src_port]).items()))))
