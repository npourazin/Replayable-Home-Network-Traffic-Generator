from PacketMarshalling.PacketData import PacketData


class Flow:
    # todo assert type as a list of PacketData
    pacs = []

    # Flow attributes
    duration = 0
    first_flow_packet = None
    last_flow_packet = None

    def __init__(self, pacs):
        self.pacs = pacs

    def get_first_flow_packet(self):
        return self.first_flow_packet

    def get_last_flow_packet(self):
        return self.last_flow_packet

    def calc_duration(self):
        new_duration = self.last_flow_packet.ts - self.first_flow_packet.ts
        self.duration = new_duration

    def create_record(self):
        # todo: save the flow as a record on disk
        pass

    def update_with_new_pac(self, pac):

        # we check different cases for  first_flow_packet and last_flow_packet

        # first case: at least one of them is none
        none_flag = False
        if self.first_flow_packet is None:
            self.first_flow_packet = pac
            none_flag = True
        if self.last_flow_packet is None:
            self.last_flow_packet = pac
            none_flag = True
        if none_flag:
            return

        # second case: both are the same but different from this pac
        if self.first_flow_packet == self.last_flow_packet and self.first_flow_packet != pac:
            if pac.ts < self.first_flow_packet.ts:
                self.first_flow_packet = pac
                return
            else:
                self.last_flow_packet = pac
                return

        # third case: none of them is none, and the are different from each other
        if pac.ts < self.first_flow_packet:
            self.first_flow_packet = pac

        elif pac.ts > self.last_flow_packet:
            self.last_flow_packet = pac

        # after all cases, recalculate the flow duration
        self.calc_duration()

    def add_new_pac(self, pac):
        self.pacs.append(pac)
        self.update_with_new_pac(pac)

        self.calc_duration()
