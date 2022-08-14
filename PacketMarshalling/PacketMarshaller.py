from FeatureExtraction.extract_features_1 import extract_features_from_pcap_via_dpkt
from PacketMarshalling.Flow import Flow
from PacketMarshalling.PacketData import PacketData


class PacketMarshaller:
    flows = []
    packets = []

    def __init__(self, filename):
        self.create_packets(filename)
        self.flows = self.marshall_packets(self.packets)

    def marshall_packets(self, pacs):
        # todo: implement basic segregation
        if self.flows in []:
            # todo: well the whole thing is useless annnnndddd
            #  it isn't even what it should be sooo
            flows = [Flow(pacs)]
            return flows
        else:
            flows = [self.flows, Flow(pacs)]
            return flows
            # raise Exception("FlowAlreadyFull")

    def create_packets(self, filename):
        data = extract_features_from_pcap_via_dpkt(filename)
        for d in data:
            self.packets.append(PacketData(*d))

        print(len(self.packets))


if __name__ == '__main__':
    # PacketMarshaller("TestFiles/test.pcap")
    pm = PacketMarshaller("../FeatureExtraction/TestFiles/test.pcap")
    print(pm.flows)
    print(pm.packets[0])