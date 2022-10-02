import pickle

from ModelGenerator.Modelify import Modelify
from PacketMarshalling.PacketMarshaller import PacketMarshaller
from TrafficGenerator.Generator1 import Generator1
from TrafficGenerator.Generator2 import Generator2

if __name__ == '__main__':
    save_flows = 0
    state = int(input("new pcap? enter 0 - reload? enter 1\n"))
    if state == 0:
        input("pcap address?\n")
        # todo set the value
        input_pcap_file = '../FeatureExtraction/TestFiles/test4.pcap'

        pm = PacketMarshaller(input_pcap_file)
        print(pm.recorded_flow_list)
        # m = Modelify(None, flow_list=pm.recorded_flow_list)
        addr = "../PacketMarshalling/FlowRecords/test4-1.obj"

        save_flows = int(input("save detected flows? enter 0 - dont? enter 1\n"))
        # todo: ask for the address to save

        if save_flows == 0:
            filehandler = open(addr, 'wb')
            pickle.dump(pm.recorded_flow_list, filehandler)
            m = Modelify(addr)

        else:
            m = Modelify(None, flow_list=pm.recorded_flow_list)

        fla = m.create_traffic_model()
        print(fla)

        generation_type = int(input("generate flows into separate files? enter 0 - dont (same file)? enter 1\n"))

        if generation_type == 0:
            gen = Generator2(fla)
            gen.generate_traffic()

        else:
            gen = Generator1(fla)
            gen.generate_traffic()
