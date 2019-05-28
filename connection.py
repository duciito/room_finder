class Connection:
    """Клас, описващ връзките м/у стаите."""

    def __init__(self, to, link_type, cost, bidirectional=True):
        self.to = to
        self.link_type = link_type
        self.cost = cost
        self.bidirectional = bidirectional
