# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-otree-docs/wiki"""

from otree.db import models
import otree.models
from otree.common import Money, money_range

author = 'Donja Darai'

PLAYERS_PER_GROUP = 10

doc = """
Public goods game with groups of {} and an marginal per capita return of 0.2
""".format(PLAYERS_PER_GROUP)

class Subsession(otree.models.BaseSubsession):

    name_in_url = 'exp3'

    endowment = models.MoneyField(
        default=20.00,
        doc="payoff = p(endowment-contribution)+a/N*sum(contribution)"
    )

    a = models.FloatField(
        default=2.0,
        doc="payoff = p(endowment-contribution)+a/N*sum(contribution)"
    )

class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_group = PLAYERS_PER_GROUP
    
    sum_contribution = models.MoneyField(
        default=None,
        doc="sum of contributions per group"
    )
    
    avg_contribution = models.MoneyField(
        default=None,
        doc="average contribution of all players in group"
    )
    
    def sum_avg(self):
        self.sum_contribution = sum(p.contribution for p in self.get_players())
        self.avg_contribution = self.sum_contribution / self.players_per_group
    
    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = (self.subsession.endowment - p.contribution) + self.subsession.a/self.players_per_group * self.sum_contribution

class Player(otree.models.BasePlayer):
    # <built-in>
    group = models.ForeignKey(Group, null = True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    contribution = models.MoneyField(
        default=None,
        doc="player's own contribution"
    )

    def contribution_choices(self):
        return money_range(0,self.subsession.endowment,1.00)
