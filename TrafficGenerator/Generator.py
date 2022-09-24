from ModelGenerator.Modelify import Modelify
from TrafficGenerator.GenerateFlowFromModel import FlowGenerator


class Generator:
    def __init__(self):
        pass

    def create_general_traffic(self):
        pass

    def generate_traffic(self):
        addr = "../PacketMarshalling/FlowRecords/test5-2.obj"
        m = Modelify()
        fla, pla = m.create_model(addr=addr)
        FlowGenerator(pla).generate_flow()
