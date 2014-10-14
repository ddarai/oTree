# -*- coding: utf-8 -*-
from __future__ import division
"""Documentation at https://github.com/oTree-org/otree/wiki"""

from otree.db import models
import otree.models
from otree.common import Money, money_range



doc = """
Adapted Copy of lab_results app. Page that shows the results of the session.
"""


class Subsession(otree.models.BaseSubsession):

    name_in_url = 'exp_results'



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

    def set_payoff(self):
        self.payoff = 0
