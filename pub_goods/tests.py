import pub_goods.views as views
from pub_goods._builtin import Bot
from otree.common import Money, money_range
import random

class PlayerBot(Bot):

    def play(self):

        #self.submit(views.Contribution, {"contribution": random.choice(range(0, self.subsession.endowment))})
        self.submit(views.Contribution, {"contribution": 4})

        self.submit(views.Results)