from ModelGenerator.LoadFlows import LoadFlows
from ModelGenerator.flow_list_attributes import FlowListAttribute
from ModelGenerator.packet_list_attributes import PacketListAttribute
from PacketMarshalling.Flow import Flow


class Modelify:
    flow_list: [Flow] = []
    loader: LoadFlows = None
    pass

    def __init__(self, addr):
        self.load_flow_list(addr)

    def load_flow_list(self, addr):
        self.loader = LoadFlows(addr)
        self.flow_list = self.loader.flow_list

    def create_traffic_model(self):
        # self.load_flow_list(addr)

        fla = FlowListAttribute(flow_list=self.flow_list, flow_obj_addr=self.loader.file_addr)
        # print("*******")
        # print(fla.item_size_list)
        # print(fla.item_intervals_list)
        # # num, sizes, inters = fla.train_list('Pareto', 'Gamma')
        # size, inter = fla.get_new_size('Pareto'), fla.get_new_interval('Gamma')
        # print(size, inter)
        #
        # sizes, inters = fla.train_list('Pareto', 'Gamma', len(fla.item_size_list))
        # sizes, inters = fla.train_list('Gamma', 'Pareto', len(fla.item_size_list))
        # fla.inter_arrival_histogram()
        # fla.dist_histogram(inters)
        # fla.dist_histogram(sizes)

        return fla

    def create_a_random_flow_model(self):
        pla = PacketListAttribute(flow=self.loader.get_a_random_flow())
        return pla

    def create_flow_model(self, flow):
        pla = PacketListAttribute(flow=flow)
        return pla


if __name__ == '__main__':
    address = "../PacketMarshalling/FlowRecords/test5-2.obj"
    m = Modelify(address)
    m.create_traffic_model()
