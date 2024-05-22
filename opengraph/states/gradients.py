gradients = []

__all__ = ["State"]


class State:
    def append(self, item):
        gradients.append(item)

    def get(self):
        return gradients
