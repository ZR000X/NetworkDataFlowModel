from ordinal import Ordinal


class Node(Ordinal):
    def __init__(self, area, subordinates=[], widths=[], angles=[], superiors=[], inform_on_init=False) -> None:
        super().__init__(subordinates=subordinates, superiors=superiors, inform_on_init=inform_on_init)

    # TODO - Structure the node to do what we want:
    #      - 