import random
from collections import Counter
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from FeatureExtraction.extract_features_1 import extract_features_from_pcap_via_dpkt
from PacketMarshalling.Flow import Flow
from PacketMarshalling.PacketData import PacketData
import pickle


class PacketMarshaller:
    flows = {}
    recorded_flow_list = []
    packets: List[PacketData] = []
    expiration_black_list = set()

    def __init__(self, filename):
        self.create_packets(filename)
        self.marshall_packets()

    def marshall_packets(self):

        loop_counter = 0
        for pac in self.packets:
            loop_counter += 1
            if not pac.validate_packet_data():
                continue

            if loop_counter % 1000 == 0:
                self.check_all_flows_life()

            f_id = str(hash(frozenset(Counter([pac.src_ip_addr, pac.src_port, pac.dst_ip_addr, pac.dst_port]).items())))
            if f_id in self.flows:
                if f_id in self.expiration_black_list:
                    # this flow was previously expired and needs to be renewed
                    self.expiration_black_list.remove(f_id)
                    self.recorded_flow_list.append(self.flows[f_id])
                    self.flows[f_id] = Flow(pac)
                else:
                    # this flow has not expired and the packet can be added to it
                    self.flows[f_id].add_new_pac(pac)

            else:
                new_flow = Flow(pac)
                self.flows[f_id] = new_flow
                # print(new_flow)
                # print(f_id)

        # record leftover flows
        for k in self.flows:
            self.recorded_flow_list.append(self.flows[k])

    def create_packets(self, filename):
        data = extract_features_from_pcap_via_dpkt(filename)
        for d in data:
            self.packets.append(PacketData(*d))

        print(len(self.packets))

    def check_all_flows_life(self):
        for k in self.flows:
            if self.flows[k].check_flow_expiration():
                self.expiration_black_list.add(k)


if __name__ == '__main__':
    # PacketMarshaller("TestFiles/test.pcap")
    pcap_file = "../FeatureExtraction/TestFiles/test5.pcap"
    pm = PacketMarshaller(pcap_file)
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
    print("std duration: ", np.std(dur_arr))

    print(dur_arr)

    filehandler = open("FlowRecords/test5-2.obj", 'wb')
    pickle.dump(pm.recorded_flow_list, filehandler)
    # filehandler = open("FlowRecords/test5-1.obj", 'rb')
    # pppmmm = pickle.load(filehandler)
    # # print(pppmmm.flows)
    # print(pppmmm)

    dur_arr = sorted(dur_arr)
    plt.plot(dur_arr)
    plt.show()
