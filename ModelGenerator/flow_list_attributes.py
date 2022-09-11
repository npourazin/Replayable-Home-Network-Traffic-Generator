from ModelGenerator.LoadFlows import LoadFlows
from ModelGenerator.list_attributes import ListAttribute
from PacketMarshalling import Flow


class FlowListAttribute(ListAttribute):
    flow_list: [Flow] = None

    def __init__(self, flow_list, flow_obj_addr=None):

        self.flow_list = flow_list
        if flow_list is None and flow_obj_addr is not None:
            lf = LoadFlows(flow_obj_addr)
            self.flow_list = lf.flow_list

