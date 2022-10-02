import datetime
import random
import time

import dpkt

sys_random = random.SystemRandom()

class PcapEditor:
    file_addr = ""
    pcap_file = None
    mtu = 1500
    samples = []

    def __init__(self, file_addr, handle_type="wb+"):
        self.file_addr = file_addr
        # todo: check type
        self.pcap_file = open(file_addr, handle_type)
        self.load_basic_tcp_packet("./TestFiles/samples.pcap")

    def publish_packet(self, desired_packet_size):
        if desired_packet_size < 40:
            desired_packet_size = 40
        if desired_packet_size > self.mtu:
            desired_packet_size = self.mtu

        rand_buf = sys_random.choice(self.samples)
        eth = dpkt.ethernet.Ethernet(rand_buf)
        ip_layer = eth.data
        previous_packet_size = len(ip_layer)
        tcp_layer = ip_layer.data
        app_layer = tcp_layer.data

        new_pac = rand_buf

        # print(app_layer)
        # print(len(app_layer))
        # print(type(app_layer))
        #
        # print(rand_buf)
        # print(eth)
        # print(type(eth))
        # print(type(rand_buf))
        # print(ip_layer)
        # print(type(ip_layer))
        # print(tcp_layer)
        # print(type(tcp_layer.__str__()))
        # print(type(tcp_layer))
        # print(len(tcp_layer.__str__()))
        # print((tcp_layer.__str__()))
        # tcp = tcp_layer.__str__()
        # print(tcp[:-1])
        # print(tcp[:-4])
        # print((tcp[:-8]))
        # print(list(tcp_layer))
        # print(app_layer)
        #
        # print(len(rand_buf))
        # print(len(eth))
        # print(len(ip_layer))
        # print(len(tcp_layer))
        # print(len(app_layer))

        if previous_packet_size > desired_packet_size:
            # todo: remove something from the payload
            print("oops too much ")
            cutoff = previous_packet_size - desired_packet_size

        elif previous_packet_size < desired_packet_size:
            # todo: add some bullshit in the packet
            print("whoops gotta fill it up")
            addon = desired_packet_size - previous_packet_size

            # print(ip_layer.__hdr__)
            # print(ip_layer.pack_hdr())
            eth_hdr_len = len(eth) - len(ip_layer)
            raw_ip = rand_buf[eth_hdr_len:]
            eth_hdr = rand_buf[0:eth_hdr_len]
            # print(rand_buf)
            # print(raw_ip)

            # raw_ip[2:3] = int(desired_packet_size).to_bytes(2, 'big')
            # print(raw_ip[2:3])

            # fix ip len
            new_rawip = raw_ip[0:2] + int(desired_packet_size).to_bytes(2, 'big') + raw_ip[4:]
            # print(new_rawip)

            ip_hdr_len = len(ip_layer) - len(tcp_layer)
            new_rawip_hdr = new_rawip[0:ip_hdr_len]
            raw_tcp = new_rawip[ip_hdr_len:]

            # todo fix checksum

            # now you can just cat
            new_app_layer = b'\x00' * addon
            # print(new_app_layer)
            new_pac = eth_hdr + new_rawip + new_app_layer
            # print(new_pac)
            # print(rand_buf[:])
            # for (attr, type, val) in ip_layer.__hdr__:
            #     if attr == 'len':
            #         iplen = val
            #         break

            # new_app_layer = "hello world".encode('ascii')
            # print(new_pac)
            # dpkt.ethernet.Ethernet(new_pac).data.data.data
            # print(b'\x00' * addon)
            # print(dpkt.ethernet.Ethernet(new_pac).data.data.data)
            # print(new_pac)
            # print(new_app_layer)

        # todo have a packet that you change the payload to set it's size
        return new_pac

    def load_basic_tcp_packet(self, sample_file):
        f = open(sample_file, 'rb')
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            self.samples.append(buf)


if __name__ == '__main__':
    pe = PcapEditor("./TestFiles/empty.pcap")
    writer = dpkt.pcap.Writer(pe.pcap_file)
    for i in range(0, 10):

        ts = datetime.datetime.now().timestamp()
        pac = pe.publish_packet(desired_packet_size=64)
        # print("The whole length: ", len(pac))
        # print("The ip length: ", len(dpkt.ethernet.Ethernet(pac).data))
        # print(pac)
        new_dpkt_pac = dpkt.ethernet.Ethernet(pac)
        print(new_dpkt_pac)
        # new_pac2 = dpkt.ip.IP(new_dpkt_pac[14:])
        # print(new_pac2)
        writer.writepkt(new_dpkt_pac, ts=ts)
        time.sleep(3)
        # writer.close()
        # pe.pcap_file.close()
    # print("'''''''''''''''''''''''''''''''''''''''''''")
    # print(type(pac))
    # print(pac)
    # print(dpkt.ethernet.Ethernet(pac).data.pack_hdr())
    # pac = b'\xf0\x18\x98\x0c\xaa\xaf<\x18\xa0A\xc3\xa0\x08\x00E\x00\x00(\x98\x85@\x00\xee\x06\x82y\x11!\x17\x02\xc0\xa8\x89\x05\x01\xbb\xc3\xbf\x93\x00=\x8cB_4\xc8P\x10\x01\xf5.\xe0\x00\x00'
    # print(pac)
    # print(dpkt.ethernet.Ethernet(pac).data.pack_hdr())
    # print("*******************************************************")
    # print(dpkt.ethernet.Ethernet(pac).data)
    #
    # print(dpkt.ethernet.Ethernet(pac).data.pack_hdr())
    # print(dpkt.ethernet.Ethernet(pac).data.data)
    # # print(dpkt.ethernet.Ethernet(pac).data.__bytes__()[:-22])
    # print(dpkt.ethernet.Ethernet(pac).data.data.pack_hdr())
    # print(dpkt.ethernet.Ethernet(pac).data.data)
    # dpkt.ethernet.Ethernet(pac).data.data.__hdr__ = b'\x00\x00\x00\x00'
    # print(dpkt.ethernet.Ethernet(pac).data.__hdr__)

    # pac_n = dpkt.Packet(pac)
    # print(pac_n)
