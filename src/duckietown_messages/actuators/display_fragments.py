from typing import List

from .display_fragment import DisplayFragment
from ..base import BaseMessage
from ..standard.header import Header, AUTO


class DisplayFragments(BaseMessage):
    # header
    header: Header = AUTO

    # ID of the fragment, used to update fragments that repeat over time
    fragments: List[DisplayFragment]
