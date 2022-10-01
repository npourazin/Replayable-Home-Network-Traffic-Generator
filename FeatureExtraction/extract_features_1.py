import datetime
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
            # commented to improve performance
            # print("Non-IP Packet types are not supported.")
            count = count + 1
            continue

        ip_packet = eth.data

        if hasattr(ip_packet, 'p'):
            if ip_packet.p != 6:
                # print(ip_packet.p)
                # non-tcp
                count += 1
                continue

        else:
            # non-ip
            count += 1
            continue
        # print(ip_packet.get)
        # print(type(ip_packet))
        # print(ip_packet.get_proto(ip_packet).__name__)
        # print(ip_packet.data)
        try:
            # print(ip_packet.get_proto(ip_packet).__name__)
            # print(ip_packet.p)
            if print_flag:
                print("packet No.", count, ":")
                print("-- src: ", get_packet_src_ip(ip_packet), ":", get_packet_src_port(ip_packet))
                print("-- dst: ", get_packet_dst_ip(ip_packet), ":", get_packet_dst_port(ip_packet))

            packet_size = len(ip_packet)

            tcp_packet = ip_packet.data
            ip_payload_size = len(tcp_packet)
            tcp_payload_size = len(tcp_packet.data)

            out.append(
                (ts,
                 get_packet_src_ip(ip_packet),
                 get_packet_src_port(ip_packet),
                 get_packet_dst_ip(ip_packet),
                 get_packet_dst_port(ip_packet),
                 packet_size,
                 ip_payload_size,
                 tcp_payload_size,

                 # todo: List Format? Dict format?
                 )
            )
        except Exception as e:
            print(e)
            # commented to improve performance
            # print("Non-TCP Packet types are not supported.")
            continue
    return out


if __name__ == '__main__':
    start_time = time.time()
    out = extract_features_from_pcap_via_dpkt("TestFiles/test5.pcap")
    ts0, *rest = out[0]
    ts1, *rest = out[len(out)-1]
    print(str(datetime.datetime.utcfromtimestamp(ts0)))
    print(ts0)
    print(str(datetime.datetime.utcfromtimestamp(ts1)))
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
