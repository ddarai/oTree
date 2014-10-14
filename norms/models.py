# -*- coding: utf-8 -*-
from otree.db import models
import otree.models
from otree.common import Money, money_range
import random
import collections
from otree import widgets

author = 'Donja Darai'

doc = """
This app is used to conduct an experiment for norm elicitation (see Krupka & Weber).
"""

RATING_CHOICES = [(1, 'very inappropriate'), (2, 'somewhat inappropriate'), (3, 'somewhat appropriate'), (4, 'very appropriate')]

class Subsession(otree.models.BaseSubsession):
    name_in_url = 'exp2'

    most_common_rating = models.IntegerField(
        default=None,
        choices=RATING_CHOICES,
        doc="rating given most often among players"
    )

    def most_common_rating_choices(self):
        return self.RATING_CHOICES

    def set_payoffs(self):
        for p in self.get_players():
            # if p.rating == p.random_rating:
            if p.rating == self.most_common_rating:
                p.payoff = self.match_payoff
            else:
                p.payoff = 0

    def most_common(self):
        ratings = [p.rating for p in self.get_players()]
        self.most_common_rating = collections.Counter(ratings).most_common(1)[0][0]
        # at the moment, the program does not take care of ties

    match_payoff = models.MoneyField(
        default=200,
        doc="payoff if answer matches most common answer"
    )


class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_group = 1

class Player(otree.models.BasePlayer):
    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>


    rating = models.IntegerField(
        default=None,
        choices=RATING_CHOICES,
        doc="Players enter norm rating",
        widget = widgets.RadioSelect()
    )


    # random_player = models.IntegerField(
    #         default = None,
    #         doc="number of random player"
    #     )
    #
    #     random_rating = models.CharField(
    #         default = None,
    #         doc="rating of random player"
    #     )
    #
    #     def random(self):
    #          self.random_player = random.choice(self.other_players_in_subsession())
    #          self.random_rating = self.random_player.rating




