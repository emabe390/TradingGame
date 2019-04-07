import logging
from Helpers import IdentifierGenerator
logger = logging.getLogger("mainLogger")


def fix_name(name, prefix, suffix, id):
    if name is None:
        if prefix is None:
            prefix = ""
        if suffix is None:
            suffix = ""
        return "%s%s%s" % (prefix, id, suffix)
    else:
        return name


class Agent(object):
    def __init__(self, name=None, prefix=None, suffix=None, money=100, inside=None):
        self.alive = True
        self.inside = inside
        self.money = money
        self.id = IdentifierGenerator.next_id()
        self.name = fix_name(name, prefix, suffix, self.id)
        logger.info("Created agent %s with id %d" % (self.name, self.id))

    def step(self, dt, batch):
        if self.alive is False:
            return False
        

        return True