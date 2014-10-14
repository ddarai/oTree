import norms.views as views
from norms._builtin import Bot
from otree.common import Money, money_range
import random

class PlayerBot(Bot):

    def play(self):

        self.submit(views.Question, {"rating": random.choice([1,2,3,4])})

        self.submit(views.Results)