# -*- coding: utf-8 -*-
from __future__ import division
import pub_goods.models as models
from pub_goods._builtin import Page, WaitPage
from json import dumps

def variables_for_all_templates(self):
    return {
        'endowment': self.subsession.endowment,
        'round_number': self.subsession.round_number,
        'num_of_rounds': self.subsession.number_of_rounds,
        'group': self.group.id
    }

class Contribution(Page):

    form_model = models.Player
    form_fields = ['contribution']

    template_name = 'pub_goods/Contribution.html'

class ResultsWaitPage(WaitPage):

    scope = models.Group

    def after_all_players_arrive(self):
        self.group.sum_avg()
        self.group.set_payoffs()

    def body_text(self):
        return "Waiting for other players to decide."


class Results(Page):

    template_name = 'pub_goods/Results.html'

    def variables_for_template(self):
        round_labels = range(1,self.subsession.number_of_rounds+1)
        avg_list = [None]*self.subsession.number_of_rounds
        for i, p in enumerate(self.player.me_in_all_rounds()):
            avg_list[i]=float(p.group.avg_contribution)


        return {
            'sum_contribution': self.group.sum_contribution,
            'avg_contribution': self.group.avg_contribution,
            'avg_contribution_list': dumps(avg_list),
            'contribution': self.player.contribution,
            'payoff': self.player.payoff,
            'round_labels':  round_labels
        }


def pages():
    return [
        Contribution,
        ResultsWaitPage,
        Results
    ]