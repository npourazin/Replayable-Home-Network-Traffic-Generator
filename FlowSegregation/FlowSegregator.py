from FlowSegregation.Flow import Flow


class FlowSegregator:
    flows = []

    def __init__(self, pacs):
        self.flows = self.segregate_flows(pacs)

    def segregate_flows(self, pacs):
        # todo: implement basic segregation
        if self.flows in []:
            # todo: well the whole thing is useless annnnndddd
            #  it isn't even what it should be sooo
            flows = [Flow(pacs)]
            return flows
        else:
            flows = [self.flows, Flow(pacs)]
            return flows
            # raise Exception("FlowAlreadyFull")
