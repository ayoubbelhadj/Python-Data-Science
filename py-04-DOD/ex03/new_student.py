import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15 character lowercase id."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student with auto-generated login and ID."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Sets login as first letter of name (capitalized) + surname."""
        self.login = self.name[0].upper() + self.surname
