import dpkt

# import pandas as pd
# import json
# from scapy.all import *
# from connectivity_features import get_packet_src_ip, get_packet_dst_ip, get_packet_dst_port, get_packet_src_port
from FeatureExtraction.connectivity_features import *


def extract_features_from_pcap_via_dpkt(pcap_file):
    f = open(pcap_file, 'rb')
    pcap = dpkt.pcap.Reader(f)
    # Using SCAPY for Zigbee and blutooth ##
    # scapy_pak = rdpcap(pcap_file)
    count = 0
    out = []
    for ts, buf in pcap:
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

    return out


if __name__ == '__main__':
    extract_features_from_pcap_via_dpkt("TestFiles/test.pcap")
