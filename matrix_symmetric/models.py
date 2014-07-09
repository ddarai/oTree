# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-ptree-docs/wiki"""

from ptree.db import models
import ptree.models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

doc = """
Matrix Symmetric is a game in which the identity of the player does not change the resulting game facing that player.
Each player earns the same payoff when making the same choice against similar choices of his competitors.

<p>Source code <a href="https://github.com/wickens/ptree_library/tree/master/matrix_symmetric">here</a></p>
"""


class Subsession(ptree.models.BaseSubsession):

    name_in_url = 'matrix_symmetric'


class Treatment(ptree.models.BaseTreatment):
    subsession = models.ForeignKey(Subsession)

    self_1_other_1 = models.PositiveIntegerField()
    self_1_other_2 = models.PositiveIntegerField()
    self_2_other_1 = models.PositiveIntegerField()
    self_2_other_2 = models.PositiveIntegerField()


class Match(ptree.models.BaseMatch):

    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)

    participants_per_match = 2


class Participant(ptree.models.BaseParticipant):

    match = models.ForeignKey(Match, null = True)
    treatment = models.ForeignKey(Treatment, null = True)
    subsession = models.ForeignKey(Subsession)

    def other_participant(self):
        """Returns other participant in match"""
        return self.other_participants_in_match()[0]

    decision = models.PositiveIntegerField(
        null=True,
        doc='either 1 or 2',
    )

    def set_payoff(self):

        payoff_matrix = {
            1: {
                1: self.treatment.self_1_other_1,
                2: self.treatment.self_1_other_2,
            },
            2: {
                1: self.treatment.self_2_other_1,
                2: self.treatment.self_2_other_2,
            }
        }

        self.payoff = payoff_matrix[self.decision][self.other_participant().decision]


def treatments():

    treatment_list = []

    treatment = Treatment(
        self_1_other_1=10,
        self_1_other_2=0,
        self_2_other_1=30,
        self_2_other_2=40
    )

    treatment_list.append(treatment)

    return treatment_list