from ModelGenerator.list_attributes import ListAttribute
from PacketMarshalling import Flow


class PacketListAttribute(ListAttribute):
    flow: Flow = None

    def __init__(self, flow):
        self.flow = flow

        if Flow is None:
            super().__init__()
            return

        item_intervals_list, item_size_list = self.get_packet_intervals_and_sizes()
        super().__init__(number_of_items=len(self.flow.pacs), item_size_list=item_size_list,
                         item_intervals_list=item_intervals_list)

    def get_packet_intervals_and_sizes(self):
        pac_intervals = []
        pac_sizes = []

        if self.flow is None:
            return None, None

        for i in range(len(self.flow.pacs)):
            pac = self.flow.pacs[i]
            pac_sizes.append((i, pac.packet_size, pac.ip_payload_size, pac.tcp_payload_size))

            if i == 0:
                continue

            prev_pac = self.flow.pacs[i - 1]

            dist = pac.ts - prev_pac.ts
            pac_intervals.append(((i - 1, i), dist))

        return pac_intervals, pac_sizes
