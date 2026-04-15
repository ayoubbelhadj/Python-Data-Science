from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King, combining Baratheon and Lannister."""
    def __init__(self, first_name):
        """Initialize King character."""
        super().__init__(first_name)

    def get_eyes(self):
        """Return eye color."""
        return self.eyes

    def set_eyes(self, val):
        """Set eye color."""
        self.eyes = val

    def get_hairs(self):
        """Return hair color."""
        return self.hairs

    def set_hairs(self, val):
        """Set hair color."""
        self.hairs = val
