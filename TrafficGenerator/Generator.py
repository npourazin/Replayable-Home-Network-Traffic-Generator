import random
import time

from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from ModelGenerator.Modelify import Modelify
from ModelGenerator.flow_list_attributes import FlowListAttribute
from ModelGenerator.packet_list_attributes import PacketListAttribute
from PacketMarshalling import Flow
from TrafficGenerator.EditPcap import PcapEditor
from TrafficGenerator.GenerateFlowFromModel import FlowGenerator


class Generator:
    fla: FlowListAttribute = None

    def __init__(self, fla):
        self.fla = fla

    def create_new_flow(self):
        flow_packet_number = self.fla.get_new_size(distr="Pareto")
        print("Got number of packets: ", flow_packet_number)
        flows_pacs = []
        flow_interval_list = []
        print("Chose a random flow to replicate statistically")
        chosen_flow = random.choice(self.fla.flow_list)
        for i in range(flow_packet_number):
            print("     Creating a new Packet")

            # pac, next_ts = None, None

            # print(chosen_flow)
            pac, next_ts = self.generate_new_packet(chosen_flow)
            print("     Got the packet")
            flows_pacs.append(pac)
            flow_interval_list.append(next_ts)

        # print("yeeet")
        return flows_pacs, flow_interval_list

    def generate_traffic(self):
        print("Start Generating traffic...")
        while True:
            pacs, idles = self.create_new_flow()
            print("Created flow.")
            interarrival = self.fla.get_new_interval(distr="Gamma")
            self.launch_flow(pacs, idles)
            print("Launched flow.")
            # TODO NO dont sleep in between, make threads
            time.sleep(interarrival)
            print("slept for ", interarrival)

    def generate_new_packet(self, flow: Flow, base_time=0):
        pla = PacketListAttribute(flow)
        # if not pla.item_size_list:
        #     print("no size? ****************************")
        # if not pla.item_intervals_list:
        #     print("no inter? ****************************")
        packet_ts = pla.get_new_interval("Gamma")
        packet_size = pla.get_new_size("Pareto")
        # l2 = Ether()
        # # l3 = IP(dst='8.8.8.8/30')
        # l3 = IP()
        # # l4 = TCP(dport=53, flags='S')
        # l4 = TCP()
        # packet = l2 / l3 / l4 / ("X" * packet_size)
        # TODO CREATE THE PACKETS!!!
        pe = PcapEditor("./TestFiles/empty.pcap")
        pe.publish_packet(ts=(packet_ts + base_time), desired_packet_size=packet_size)
        packet = None
        return packet, packet_ts

    def launch_flow(self, pacs, idles):
        # Todo the moment you are invoked, create a connection an start sending packets
        #  for the connection, create a new thread so the can be simultaneous
        print("launching flow:")
        print("     Sending out ", len(pacs), "packets!!")

        # TODO create a connection
        # you might make client and server classes, then have them as objects and randomly pass packets to them
        for pac in pacs:
            continue


if __name__ == '__main__':
    addr = "../PacketMarshalling/FlowRecords/test5-2.obj"
    m = Modelify(addr)
    fla = m.create_traffic_model()
    print(fla)
    gen = Generator(fla)
    gen.generate_traffic()
