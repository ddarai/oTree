# -*- coding: utf-8 -*-
from __future__ import division
import norms.models as models
from norms._builtin import Page, WaitPage
from models import RATING_CHOICES
from json import dumps
from collections import Counter

def variables_for_all_templates(self):
    return {
         'round_number': self.subsession.round_number
    }

class Question(Page):

    template_name = 'norms/Question.html'

    form_model = models.Player
    form_fields = ['rating']


class ResultsWaitPage(WaitPage):

    scope = models.Subsession

    # THIS SOLUTION WORKS
    def after_all_players_arrive(self):
        for p in self.subsession.get_players():
            #p.random()
            p.subsession.most_common()
            p.subsession.set_payoffs()

    def body_text(self):
        return "Waiting for other players to decide."


class Results(Page):

    template_name = 'norms/Results.html'

    def variables_for_template(self):

        options = [ele[0] for ele in RATING_CHOICES]
        option_labels = [ele[1] for ele in RATING_CHOICES]

        players = self.subsession.get_players()
        counter = Counter([p.rating for p in players])
        popularity_counts = [counter[option] for option in options]

        return {
            'rating': self.player.get_rating_display(),
            'payoff': self.player.payoff,
            #'random_player' : self.player.random_player,
            #'random_rating' : self.player.random_rating,
            'most_common_rating' : self.subsession.get_most_common_rating_display,
            'option_labels': dumps(option_labels),
            'popularity_counts': dumps(popularity_counts)
        }

def pages():
    return [
        Question,
        ResultsWaitPage,
        Results
    ]