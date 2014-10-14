# -*- coding: utf-8 -*-
from __future__ import division
import weak_link.models as models
from weak_link._builtin import Page, WaitPage
from weak_link.models import CHOICES
from json import dumps


# def variables_for_all_templates(self):
#     return {
#         # example:
#         #'my_field': self.player.my_field,
#     }

class Decision(Page):

#     def participate_condition(self):
#         return True

    template_name = 'weak_link/Decision.html'

    form_model = models.Player
    form_fields = ['decision']
        

class ResultsWaitPage(WaitPage):

    scope = models.Subsession

    def after_all_players_arrive(self):
        for p in self.subsession.get_players():
            p.subsession.minimum()
            p.subsession.set_payoffs()
    
    def body_text(self):
        return "Waiting for other players to decide."

class Results(Page):

    template_name = 'weak_link/Results.html'
    
    def variables_for_template(self):
        options = [ele[0] for ele in CHOICES]
        option_labels = [ele[1] for ele in CHOICES]

        players = self.subsession.get_players()
        popularity_counts = []
        for option in options:
            popularity_counts.append(sum([1 for p in players if p.decision == option]))

        return{
            'decision': self.player.get_decision_display,
            'payoff': self.player.payoff,
            'min_value': self.subsession.get_min_value_display,
            'option_labels': dumps(option_labels),
            'popularity_counts': dumps(popularity_counts),
        }

def pages():
    return [
        Decision,
        ResultsWaitPage,
        Results
    ]