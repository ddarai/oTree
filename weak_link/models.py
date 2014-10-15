# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-otree-docs/wiki"""

from otree.db import models
import otree.models
from otree.common import Money, money_range
from otree import widgets

author = 'Donja Darai'

doc = """
This app is a weak link coordination game played among all participants
of the session, there are no subgroups.
"""

CHOICES = [(1, '100 %'),(0.8, '80 %'),(0.6, '60 %'), (0.4, '40 %'), (0.2, '20 %'), (0, '0 %')]

class Subsession(otree.models.BaseSubsession):

    name_in_url = 'exp1'

    min_value = models.FloatField(
        default=None,
        choices=CHOICES,
        doc="minimum of all decisions")

    def minimum(self):
        self.min_value = min(p.decision for p in self.get_players())

    def set_payoffs(self):
        for p in self.get_players():
            assert p.decision
            assert self.min_value
            p.payoff = self.a + self.b * self.min_value - self.c * p.decision


    a = models.FloatField(default=200.0,doc="a+b*(minimum of all)-c*(own choice)")

    b = models.FloatField(default=400.0,doc="a+b*(minimum of all)-c*(own choice)")

    c = models.FloatField(default=200.0,doc="a+b*(minimum of all)-c*(own choice)")


class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_group = 1


class Player(otree.models.BasePlayer):
    # <built-in>
    group = models.ForeignKey(Group, null = True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>
    
    decision = models.FloatField(
        default=None,
        choices=CHOICES,
        doc="degree to which capital requirement is accomodated",
        widget = widgets.RadioSelect()
    )
