import weak_link.views as views
from weak_link._builtin import Bot
from otree.common import Money, money_range
import random

class PlayerBot(Bot):

    def play(self):

        self.submit(views.Decision, {"decision": random.choice([0,0.2,0.4,0.6,0.8,1])})

        self.submit(views.Results)