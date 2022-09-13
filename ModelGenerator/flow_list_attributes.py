from ModelGenerator.LoadFlows import LoadFlows
from ModelGenerator.list_attributes import ListAttribute
from PacketMarshalling import Flow
import matplotlib.pyplot as plt


class FlowListAttribute(ListAttribute):
    flow_list: [Flow] = None

    def __init__(self, flow_list, flow_obj_addr=None):

        self.flow_list = flow_list
        if flow_list is None and flow_obj_addr is not None:
            lf = LoadFlows(flow_obj_addr)
            self.flow_list = lf.flow_list

        item_size_list = self.get_flow_size_list()
        item_intervals_list = self.get_flow_intervals_list()

        super().__init__(item_size_list=item_size_list, item_intervals_list=item_intervals_list)

        # super().__init__(number_of_items=len(self.flow_list), item_size_list=item_size_list,
        #                  item_intervals_list=item_intervals_list)

    def get_flow_size_list(self):
        sl = []
        for flow in self.flow_list:
            sl.append(len(flow.pacs))
        return sl

    def get_flow_intervals_list(self):
        inter_arr_ts = []

        for f in self.flow_list:
            inter_arr_ts.append(f.first_flow_packet.ts)

        inter_arr_ts = sorted(inter_arr_ts)
        # now we have relative arrival time, we want inter arrivals
        inter_arr_rel = inter_arr_ts
        inter_arr = []
        for i in range(1, len(inter_arr_rel)):
            inter_arr.append((inter_arr_rel[i] - inter_arr_rel[i - 1]))
        return inter_arr

    def inter_arrival_histogram(self):
        inter_arr = self.get_flow_intervals_list()
        for inter in range(len(inter_arr)):
            inter_arr[inter] *= 60  # put in minutes
        print(inter_arr)
        print(print())
        print(len(inter_arr))
        m = int(max(inter_arr))
        # num = 1000*3
        # num = 6 * 1000
        num = 10
        print(range(-1 * num, m, num)[1:])
        print(range(-1 * num, m, num))
        plt.hist(inter_arr, bins=range(0, m, num), density=True)
        plt.show()


if __name__ == '__main__':
    ooo = FlowListAttribute(flow_list=None, flow_obj_addr="../PacketMarshalling/FlowRecords/test5-2.obj")
    ooo.inter_arrival_histogram()
