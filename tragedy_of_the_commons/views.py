# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Money, money_range
from .models import Constants


class Introduction(Page):

    def participate_condition(self):
        return True

    template_name = 'tragedy_of_the_commons/Introduction.html'

    def variables_for_template(self):

        return {'common_gain': Constants.common_gain,
                'common_loss': Constants.common_loss,
                'common_cost': Constants.individual_gain - Constants.defect_costs,
                'defect_gain': Constants.common_gain - Constants.defect_costs}


class Decision(Page):

    def participate_condition(self):
        return True

    template_name = 'tragedy_of_the_commons/Decision.html'

    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    scope = models.Group

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    template_name = 'tragedy_of_the_commons/Results.html'

    def variables_for_template(self):
        return {'payoff': self.player.payoff}


def pages():

    return [Introduction,
            Decision,
            ResultsWaitPage,
            Results]
