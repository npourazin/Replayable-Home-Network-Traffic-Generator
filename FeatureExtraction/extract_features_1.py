import time

import dpkt

# import pandas as pd
# import json
# from scapy.all import *
# from connectivity_features import get_packet_src_ip, get_packet_dst_ip, get_packet_dst_port, get_packet_src_port
from FeatureExtraction.connectivity_features import *


def extract_features_from_pcap_via_dpkt(pcap_file, print_flag=0):
    f = open(pcap_file, 'rb')
    pcap = dpkt.pcap.Reader(f)
    # Using SCAPY for Zigbee and blutooth ##
    # scapy_pak = rdpcap(pcap_file)
    count = 0
    out = []
    for ts, buf in pcap:
        if print_flag:
            print("-----------------------------------------------------------------------")

        try:
            eth = dpkt.ethernet.Ethernet(buf)
            count = count + 1
        except:
            print("Non-IP Packet types are not supported.")
            count = count + 1
            continue
        ip_packet = eth.data
        # print(ip_packet.data)
        try:
            if print_flag:
                print("packet No.", count, ":")
                print("-- src: ", get_packet_src_ip(ip_packet), ":", get_packet_src_port(ip_packet))
                print("-- dst: ", get_packet_dst_ip(ip_packet), ":", get_packet_dst_port(ip_packet))
            out.append(
                (ts,
                 get_packet_src_ip(ip_packet),
                 get_packet_src_port(ip_packet),
                 get_packet_dst_ip(ip_packet),
                 get_packet_dst_port(ip_packet),
                 # todo: packet size
                 # todo: List Format? Dict format?
                 )
            )
        except:
            continue
    return out


if __name__ == '__main__':
    start_time = time.time()
    extract_features_from_pcap_via_dpkt("TestFiles/test2.pcap")
    print("time elapsed: {:.2f}s".format(time.time() - start_time))