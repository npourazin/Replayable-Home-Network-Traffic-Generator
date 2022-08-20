import random
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from FeatureExtraction.extract_features_1 import extract_features_from_pcap_via_dpkt
from PacketMarshalling.Flow import Flow
from PacketMarshalling.PacketData import PacketData


class PacketMarshaller:
    flows = {}
    packets = []

    def __init__(self, filename):
        self.create_packets(filename)
        self.marshall_packets()

    def marshall_packets(self):

        for pac in self.packets:
            f_id = str(hash(frozenset(Counter([pac.src_ip_addr, pac.src_port, pac.dst_ip_addr, pac.dst_port]).items())))
            if f_id in self.flows:
                self.flows[f_id].add_new_pac(pac)

            else:
                new_flow = Flow(pac)
                self.flows[f_id] = new_flow
                # print(new_flow)
                # print(f_id)

        # # todo: implement basic segregation
        # if self.flows in []:
        #     # todo: well the whole thing is useless annnnndddd
        #     #  it isn't even what it should be sooo
        #     flows = [Flow(pacs)]
        #     return flows
        # else:
        #     flows = [self.flows, Flow(pacs)]
        #     return flows
        #     # raise Exception("FlowAlreadyFull")

        # todo: check check_flow_duration for every flow in a loop

    def create_packets(self, filename):
        data = extract_features_from_pcap_via_dpkt(filename)
        for d in data:
            self.packets.append(PacketData(*d))

        print(len(self.packets))


if __name__ == '__main__':
    # PacketMarshaller("TestFiles/test.pcap")
    pm = PacketMarshaller("../FeatureExtraction/TestFiles/test3.pcap")
    # print(pm.flows)
    # print(len(pm.flows))
    # k = random.choice(list(pm.flows.keys()))
    # print(pm.flows[k])
    # k = random.choice(list(pm.flows.keys()))
    # print(pm.flows[k])
    # print(pm.packets[0])
    # print(dir(pm.packets[0]))
    # print(type(pm.packets[0].ts))
    # print(type(pm.packets[0].dst_ip_addr))
    # print(type(pm.packets[0].src_ip_addr))
    # print(type(pm.packets[0].src_port))
    # print(type(pm.packets[0].dst_port))
    # print(pm.packets[1])

    dur_sum = 0
    dur_arr = []
    for f in pm.flows:
        print(pm.flows[f])
        dur_sum += pm.flows[f].duration
        dur_arr.append(pm.flows[f].duration)

    print("------------------")
    print("number of packets:", len(pm.packets))
    print("number of flows:", len(pm.flows))
    print("duration average: ", (dur_sum / len(pm.flows)))
    print(dur_arr)

    dur_arr = sorted(dur_arr)
    plt.plot(dur_arr)
    plt.show()
