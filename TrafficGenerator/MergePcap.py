import dpkt


class PcapMerger:
    pcap_file_1 = None
    addr_pcap_file_1 = ""
    pcap_file_2 = None
    addr_pcap_file_2 = ""
    all_data = []

    def __init__(self, addr_pcap_file_1, addr_pcap_file_2):
        self.addr_pcap_file_1 = addr_pcap_file_1
        self.addr_pcap_file_2 = addr_pcap_file_2

        self.pcap_file_1 = open(addr_pcap_file_1, 'rb')
        self.pcap_file_2 = open(addr_pcap_file_1, 'rb')

        reader_1 = dpkt.pcap.Reader(self.pcap_file_1)
        for ts, buf in reader_1:
            self.all_data.append((ts, buf))

        reader_2 = dpkt.pcap.Reader(self.pcap_file_2)
        for ts, buf in reader_2:
            self.all_data.append((ts, buf))

        # sort by timestamp
        self.all_data = sorted(self.all_data, key=lambda x: x[0])

        writer = dpkt.pcap.Writer(open("./TestFiles/out1.pcap", 'wb+'))
        for (ts, buf) in self.all_data:
            writer.writepkt(buf, ts)


if __name__ == '__main__':
    pm = PcapMerger("./TestFiles/single2.pcap", "./TestFiles/single1.pcap")