import os
import sys
from limbo import FakeServer

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from or_plugin import on_message


def test_poll():
    # since it's a random selection, lets run this 3 times to have change to select bettween the two
    for i in range(3):
        ret = on_message({"text": u"!or A B or B"}, None)
        assert ret is not None
        assert ret in ["A B", "B"]
