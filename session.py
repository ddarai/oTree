# -*- coding: utf-8 -*-
from __future__ import division
from otree.session import SessionType
import os


def session_types():

    return [

        SessionType(
            name='Norm Elicitation',
            base_pay=0,
            participants_per_session=3,
            participants_per_demo_session=3,
            subsession_apps=['norms', 'results_donja'],
            doc=""""""
        ),
        SessionType(
            name='Weak Link Game',
            base_pay=0,
            participants_per_session=3,
            participants_per_demo_session=3,
            subsession_apps=['weak_link', 'results_donja'],
            doc=""""""
        ),
        SessionType(
            name='Public Goods Game 2',
            base_pay=0,
            participants_per_session=6,
            participants_per_demo_session=6,
            subsession_apps=['pub_goods','pub_goods', 'results_donja'],
            doc=""""""
        ),
        SessionType(
            name='All',
            base_pay=0,
            participants_per_session=10,
            participants_per_demo_session=20,
            subsession_apps=['weak_link','norms','norms','pub_goods','pub_goods','pub_goods','pub_goods','pub_goods', 'results_donja'],
            doc=""""""
        ),
        SessionType(
            name='Two60',
            base_pay=0,
            participants_per_session=30,
            participants_per_demo_session=10,
            subsession_apps=['weak_link','norms','norms', 'results_donja'],
            doc=""""""
        ),


        SessionType(
            name="Demo Game",
            base_pay=0,
            participants_per_demo_session=1,
            participants_per_session=1,
            subsession_apps=['demo_game'],
            doc=""""""
        ),
        SessionType(
            name="Public Goods",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=3,
            subsession_apps=['public_goods', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Prisoner's Dilemma",
            base_pay=4.00,
            participants_per_demo_session=2,
            participants_per_session=2,
            subsession_apps=['prisoner', 'survey_sample', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Cournot Competition",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['cournot_competition', 'survey_sample', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Trust Game",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['trust', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Dictator Game",
            base_pay=10.00,
            participants_per_session=2,
            participants_per_demo_session=2,
            subsession_apps=['dictator', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Matching Pennies",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['matching_pennies']*3 + ['survey_sample', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Traveler's Dilemma",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['traveler_dilemma', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Survey",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=1,
            subsession_apps=['survey'],
            doc=""""""
        ),
        SessionType(
            name="Bargaining Game",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['bargaining', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Guessing Game",
            base_pay=10.00,
            participants_per_session=10,
            participants_per_demo_session=5,
            subsession_apps=['guessing', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Common Value Auction",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['common_value_auction', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="2 x 2 Matrix Game (Symmetric)",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['matrix_symmetric', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="2 x 2 Matrix Game (Asymmetric)",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['matrix_asymmetric', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Stackelberg Competition",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['stackelberg_competition', 'survey_sample', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Private Value Auction",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['private_value_auction', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Volunteer's Dilemma",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=3,
            subsession_apps=['volunteer_dilemma', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Bertrand Competition",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=3,
            subsession_apps=['bertrand_competition', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Principal Agent",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['principal_agent', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Coordination Game",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['coordination', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Stag Hunt",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['stag_hunt', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            name="Battle of the Sexes",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['battle_of_the_sexes', 'lab_results'],
            doc=""""""
        ),
        SessionType(
            # in-progress
            name="Asset Market",
            base_pay=10.00,
            participants_per_session=12,
            participants_per_demo_session=2,
            subsession_apps=['asset_market']*5 + ['lab_results'],
            doc=""""""
        ),

        ]

# FIXME: complete the apps below
disabled_session_types = [
    SessionType(
        name="Quiz",
        base_pay=0,
        participants_per_demo_session=1,
        participants_per_session=1,
        subsession_apps=['quiz'],
        doc=""""""
    ),
    SessionType(
        name="Lemon Market",
        base_pay=10.00,
        participants_per_session=12,
        participants_per_demo_session=1,
        subsession_apps=['lemon_market', 'lab_results'],
        doc=""""""
    ),
    SessionType(
        name="Tragedy of the commons",
        base_pay=10.00,
        participants_per_session=2,
        participants_per_demo_session=2,
        subsession_apps=['tragedy_of_the_commons', 'lab_results'],
        doc=""""""
    ),
    ]


def show_on_demo_page(session_type_name):
    # set the below env var on servers that participants will see,
    # since they should not be able to access the demo page
    if os.environ.get('OTREE_PARTICIPANT_FACING_SITE'):
        return False
    return True


demo_page_intro_text = """
<ul>
    <li><a href="https://github.com/oTree-org/otree" target="_blank">Source code</a> for the below games.</li>
    <li><a href="http://www.otree.org/" target="_blank">oTree homepage</a>.</li>
</ul>
<p>
Below are various games implemented with oTree. These games are all open source,
and you can modify them as you wish to create your own variations. Click one to learn more and play.
</p>
"""
