# import pandas as pd
# import json
from scapy.all import *
# from connectivity_features import get_packet_src_ip, get_packet_dst_ip, get_packet_dst_port, get_packet_src_port
from scapy.layers.inet import TCP
from scapy.utils import PcapReader

scapy_pcap_reader = None
packet_number = 0

start_time = time.time()


def get_next_n_packets(count=0, store=1, timeout=None):
    # f = open(pcap_file, 'rb')
    # pcap = dpkt.pcap.Reader(f)
    # if offline is None:
    #     if L2socket is None:
    #         L2socket = conf.L2listen
    #     s = L2socket(type=ETH_P_ALL, *arg, **karg)
    # else:
    #     s = PcapReader(offline)

    global scapy_pcap_reader
    global packet_number
    prev_c = -1
    c = 0

    lst = []
    if timeout is not None:
        stoptime = time.time() + timeout
    remain = None

    while True:
        # print(prev_c, c)
        if prev_c == c:
            # End of File
            break
        prev_c = c
        try:
            if timeout is not None:
                remain = stoptime - time.time()
                if remain <= 0:
                    break

            try:
                p = scapy_pcap_reader.recv(MTU)
            # except PcapTimeoutElapsed:
            except:
                continue
            if p is None:
                break
            if store:
                lst.append(p)

            c += 1
            packet_number += 1

            if packet_number == int(count / 10):
                print("time elapsed: {:.2f}s".format(time.time() - start_time))
                print(packet_number)
            if packet_number == int(2 * count / 10):
                print("time elapsed: {:.2f}s".format(time.time() - start_time))
                print(packet_number)
            if packet_number == int(3 * count / 10):
                print("time elapsed: {:.2f}s".format(time.time() - start_time))
                print(packet_number)

            if 0 < count <= c:
                break
        except KeyboardInterrupt or EOFError:
            break

    if prev_c == c:
        scapy_pcap_reader.close()
        print("all data parsed already")

    return lst


def get_next_packet(store=1, timeout=None):
    lst = get_next_n_packets(count=1, store=store, timeout=timeout)
    if len(lst) == 1:
        return lst[0]
    else:
        print("Something went wrong. Wrong number of packets returned. expected 1, got", len(lst))
        return None


def get_ip_and_port_of_packet_src_and_dst(pacs):
    for i in range(len(pacs)):
        pac = pacs[i]
        print("packet No.", i, ":")
        # pac.show()
        if hasattr(pac.payload, 'src') and hasattr(pac.payload, 'sport'):
            print("-- src: ", pac.payload.src, ":", pac.payload.sport)
        else:
            print("-- Not an IP Packet")
            continue
        if hasattr(pac.payload, 'dst') and hasattr(pac.payload, 'dport'):
            print("-- dst: ", pac.payload.dst, ":", pac.payload.dport)
        else:
            print("-- Not an IP Packet")
            continue


def extract_features_from_pcap_via_scapy_iterator(pcap_file, buff_size=1):
    global scapy_pcap_reader
    scapy_pcap_reader = PcapReader(pcap_file)
    pacs = get_next_n_packets(count=buff_size)
    out = []

    for pac in pacs:
        # pac.show()
        if not pac.payload.haslayer(TCP):
            continue
            # print("***********************************************************************")
            # print(pac.layers())
        if hasattr(pac.payload, 'src') \
                and hasattr(pac.payload, 'sport') \
                and hasattr(pac.payload, 'dst') \
                and hasattr(pac.payload, 'dport') \
                and hasattr(pac, 'time'):
            out.append(
                (pac.time,
                 pac.payload.src,
                 pac.payload.sport,
                 pac.payload.dst,
                 pac.payload.dport,

                 len(pac.payload),
                 len(pac.payload.payload),
                 len(pac.payload.payload.payload),

                 # todo: List Format? Dict format?
                 )
            )

    return out


if __name__ == '__main__':
    pcap_file = "TestFiles/test.pcap"
    scapy_pcap_reader = PcapReader(pcap_file)
    # pacs = get_next_n_packets(count=10)
    pacs = extract_features_from_pcap_via_scapy_iterator(pcap_file, buff_size=70)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    print("\n\n\n\n\n\n")
    # pass real packets
    # get_ip_and_port_of_packet_src_and_dst(pacs)

    print("\n\n\n\n\n\n")
    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    # pacs = extract_features_from_pcap_via_scapy_iterator(pcap_file, 100)
    # print(pacs)
# print(pac.layers()[1])
