from PacketMarshalling.Flow import Flow


class ModelFlow:
    flow_list = []

    # todo create a model using the detected flows

    def model_a_flow(self, flow: Flow):
        pac_intervals = []
        pac_sizes = []

        for i in range(len(flow.pacs)):
            pac = flow.pacs[i]
            pac_sizes.append((i, pac.packet_size, pac.ip_payload_size, pac.tcp_payload_size))

            if i == 0:
                continue

            prev_pac = flow.pacs[i - 1]

            dist = pac.ts - prev_pac.ts
            pac_intervals.append(((i - 1, i), dist))

        return pac_intervals, pac_sizes
