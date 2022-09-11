from ModelGenerator.list_attributes import ListAttribute
from PacketMarshalling import Flow


class PacketListAttribute(ListAttribute):
    flow: Flow = None

    def __init__(self, flow):
        self.flow = flow
