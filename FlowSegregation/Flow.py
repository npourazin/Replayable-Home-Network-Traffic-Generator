from FlowSegregation.PacketData import PacketData


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
        pass

    def get_last_flow_packet(self):
        pass

    def calc_duration(self):
        # todo: first pac ts to last pac ts
        # first = get_first_flow_packet
        # last = get_last_flow_packet

        new_duration = 0
        # calc it
        self.duration = new_duration

    def create_record(self):
        # todo: save the flow as a record on disk
        pass

    def add_new_pac(self, pac):
        self.pacs.append(pac)
        # todo: might need to check ts and update first and last ones
        # todo: if at least one of first and last are None, we need to update (make update func maybe)

        self.calc_duration()

