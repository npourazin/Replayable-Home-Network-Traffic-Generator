import datetime
import os
import random
import time

import dpkt
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from ModelGenerator.Modelify import Modelify
from ModelGenerator.flow_list_attributes import FlowListAttribute
from ModelGenerator.packet_list_attributes import PacketListAttribute
from PacketMarshalling import Flow
from TrafficGenerator.EditPcap import PcapEditor
from TrafficGenerator.GenerateFlowFromModel import FlowGenerator
from TrafficGenerator.MergePcap import PcapMerger


class Generator1:
    fla: FlowListAttribute = None
    start_time = None

    def __init__(self, fla):
        self.fla = fla
        self.start_time = datetime.datetime.now().timestamp()

    def create_new_flow(self):
        flow_packet_number = self.fla.get_new_size(distr="Pareto")
        print("Got number of packets: ", flow_packet_number)
        flows_pac_sizes = []
        flow_interval_list = []
        print("Chose a random flow to replicate statistically")
        chosen_flow = random.choice(self.fla.flow_list)
        for i in range(flow_packet_number):
            print("     Creating a new packet model:")
            pac_size, next_ts = self.generate_new_packet(chosen_flow)
            print("     Got the packet size and int")
            flows_pac_sizes.append(pac_size)
            flow_interval_list.append(next_ts)

        # print("yeeet")
        return flows_pac_sizes, flow_interval_list

    def generate_traffic(self):
        print("Start Generating traffic...")
        passed_time = 0
        file_counter = 1
        filename1 = "../TrafficGenerator/TestFiles/temp.pcap"
        filename2 = "../TrafficGenerator/TestFiles/out1.pcap"
        if not os.path.exists('../TrafficGenerator/TestFiles/out1.pcap'):
            with open('../TrafficGenerator/TestFiles/out1.pcap', 'wb'):
                pass
        if not os.path.exists('../TrafficGenerator/TestFiles/temp.pcap'):
            with open('../TrafficGenerator/TestFiles/temp.pcap', 'wb'):
                pass

        pm = PcapMerger(filename1, filename2)
        while True:
            interarrival = self.flow_single_generation(passed_time=passed_time, file_counter=file_counter)
            passed_time += interarrival
            file_counter += 1
            pm.merge()

    def flow_single_generation(self, passed_time, file_counter):
        sizes, idles = self.create_new_flow()
        print("Created flow.")
        interarrival = self.fla.get_new_interval(distr="Gamma")
        flow_launch_time = self.start_time + passed_time
        self.launch_flow(sizes, idles, flow_launch_time, file_counter)
        print("Launched flow.")
        return interarrival

    def generate_new_packet(self, flow: Flow, base_time=0):
        pla = PacketListAttribute(flow)
        packet_ts = pla.get_new_interval("Gamma")
        packet_size = pla.get_new_size("Pareto")
        # if not pla.item_size_list:
        #     print("no size? ****************************")
        # if not pla.item_intervals_list:
        #     print("no inter? ****************************")

        # l2 = Ether()
        # # l3 = IP(dst='8.8.8.8/30')
        # l3 = IP()
        # # l4 = TCP(dport=53, flags='S')
        # l4 = TCP()
        # packet = l2 / l3 / l4 / ("X" * packet_size)
        # TODO CREATE THE PACKETS!!!
        # pe = PcapEditor("./TestFiles/empty.pcap")
        # pe.publish_packet(ts=(packet_ts + base_time), desired_packet_size=packet_size)
        # packet = None
        return packet_size, packet_ts

    def launch_flow(self, sizes, idles, flow_launch_time, outputfile_id):
        # Todo the moment you are invoked, create a connection an start sending packets
        #  for the connection, create a new thread so the can be simultaneous
        print("launching flow:")
        print("     Sending out ", len(sizes), "packets!!")

        # make a thread and a pcap file with thread id name to write in
        # filename = "./TestFiles/temp" + str(outputfile_id) + ".pcap"
        filename = "../TrafficGenerator/TestFiles/temp.pcap"
        pe = PcapEditor(file_addr=filename, handle_type="wb+")
        passed_time_in_flow = 0
        writer = dpkt.pcap.Writer(pe.pcap_file)
        print(idles)
        for i in range(len(sizes)):
            # we make a packet
            pac = pe.publish_packet(desired_packet_size=sizes[i])
            ts = flow_launch_time + passed_time_in_flow
            passed_time_in_flow += idles[i]
            writer.writepkt(pac, ts)
            print(ts)

        writer.close()


if __name__ == '__main__':
    addr = "../PacketMarshalling/FlowRecords/test5-2.obj"
    m = Modelify(addr)
    fla = m.create_traffic_model()
    print(fla)
    gen = Generator1(fla)
    gen.generate_traffic()
