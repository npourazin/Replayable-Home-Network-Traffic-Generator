from PacketMarshalling.PacketData import PacketData
from typing import List


class Flow:
    # asserts type as a list of PacketData
    pacs: List[PacketData] = []

    # Flow attributes
    duration = 0
    first_flow_packet = None
    last_flow_packet = None

    src_ip_addr = None
    src_port = None
    dst_ip_addr = None
    dst_port = None

    # todo: set appropriate value
    max_flow_duration = 60

    # def __init__(self, pacs):
    #     for pac in pacs:
    #         self.add_new_pac(pac)

    def __init__(self, pac):
        self.pacs = []
        self.duration = 0
        self.first_flow_packet = None
        self.last_flow_packet = None

        self.src_ip_addr = None
        self.src_port = None
        self.dst_ip_addr = None
        self.dst_port = None

        self.add_new_pac(pac)

    def get_first_flow_packet(self):
        return self.first_flow_packet

    def get_last_flow_packet(self):
        return self.last_flow_packet

    def calc_duration(self):
        new_duration = self.last_flow_packet.ts - self.first_flow_packet.ts
        self.duration = new_duration

    def update_with_new_pac(self, pac):

        # first, update attributes if none

        if self.src_ip_addr is None:
            self.src_ip_addr = pac.src_ip_addr

        if self.src_port is None:
            self.src_port = pac.src_port

        if self.dst_ip_addr is None:
            self.dst_ip_addr = pac.dst_ip_addr

        if self.dst_port is None:
            self.dst_port = pac.dst_port

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
        if pac.ts < self.first_flow_packet.ts:
            self.first_flow_packet = pac

        elif pac.ts > self.last_flow_packet.ts:
            self.last_flow_packet = pac

        # after all cases, recalculate the flow duration
        self.calc_duration()

    def add_new_pac(self, pac):
        if not self.check_pac_admissibility(pac):
            return
        self.pacs.append(pac)
        self.update_with_new_pac(pac)
        self.calc_duration()

    def check_pac_admissibility(self, pac):

        # check src and dst addresses and ports

        if self.src_ip_addr is not None:
            if self.src_ip_addr != pac.src_ip_addr:
                return False

        if self.src_port is not None:
            if self.src_port != pac.src_port:
                return False

        if self.dst_ip_addr is not None:
            if self.dst_ip_addr != pac.dst_ip_addr:
                return False

        if self.dst_port is not None:
            if self.dst_port != pac.dst_port:
                return False

        return True

    def check_flow_expiration(self):
        if self.duration >= self.max_flow_duration:
            return True
        # print("limit Exceeded. Saving Flow.")
        # self.create_record()
        return False

    def __str__(self):
        return 'number of packets:' + str(len(self.pacs)) + '\nduration: ' + str(self.duration) + '\nfirst:' + str(
            self.first_flow_packet) + 'last:' + str(
            self.last_flow_packet)
