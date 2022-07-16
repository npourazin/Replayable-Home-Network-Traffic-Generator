import dpkt
# import pandas as pd
# import json
# from scapy.all import *
import socket


def get_packet_src(pac):
    if hasattr(pac, 'src'):
        # print("source_ip", socket.inet_ntoa(ip.src))
        return socket.inet_ntoa(pac.src)


def get_packet_dst(pac):
    if hasattr(pac, 'dst'):
        # print("destination_ip", socket.inet_ntoa(ip.src))
        return socket.inet_ntoa(pac.dst)


def extract_features_from_pcap(pcap_file):
    f = open(pcap_file, 'rb')
    pcap = dpkt.pcap.Reader(f)
    # Using SCAPY for Zigbee and blutooth ##
    # scapy_pak = rdpcap(pcap_file)
    count = 0

    for ts, buf in pcap:
        print("-----------------------------------------------------------------------")
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            count = count + 1
        except:
            count = count + 1
            continue  # If packet format is not readable by dpkt,
        ip = eth.data
        src = get_packet_src(ip)
        dst = get_packet_dst(ip)
        print("packet No.", count)
        print("src: ", src)
        print("dst: ", dst)


if __name__ == '__main__':
    extract_features_from_pcap("test.pcap")
