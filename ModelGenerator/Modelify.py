from ModelGenerator.LoadFlows import LoadFlows
from ModelGenerator.flow_list_attributes import FlowListAttribute
from ModelGenerator.packet_list_attributes import PacketListAttribute
from PacketMarshalling.Flow import Flow


class Modelify:
    flow_list: [Flow] = []
    # todo create a model
    pass

    # todo
    #  what to do:
    #     load some flows
    #     train flow list
    #     choose a random flow
    #     train the random flow

    def create_model(self, addr):
        loader = LoadFlows(addr)
        self.flow_list = loader.flow_list

        fla = FlowListAttribute(flow_list=self.flow_list, flow_obj_addr=addr)
        print("*******")
        print(fla.item_size_list)
        print(fla.item_intervals_list)
        # num, sizes, inters = fla.train_list('Pareto', 'Gamma')
        size, inter = fla.get_new_size('Pareto'), fla.get_new_interval('Gamma')
        print(size, inter)

        sizes, inters = fla.train_list('Pareto', 'Gamma', len(fla.item_size_list))
        # sizes, inters = fla.train_list('Gamma', 'Pareto', len(fla.item_size_list))
        fla.inter_arrival_histogram()
        fla.dist_histogram(inters)
        fla.dist_histogram(sizes)

        pla = PacketListAttribute(flow=loader.get_a_random_flow())


if __name__ == '__main__':
    addr = "../PacketMarshalling/FlowRecords/test5-2.obj"
    m = Modelify()
    m.create_model(addr=addr)
