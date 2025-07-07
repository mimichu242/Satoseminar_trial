from otree.api import *
import random

doc = """最後通牒ゲーム"""

class C(BaseConstants):
    NAME_IN_URL = "ch10_2_ultimatum"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = 10
    INSTRUCTIONS_TEMPLATE = "ch10_2_ultimatum/instructions.html"
    ADD_TIME = 180

    CHOICE_LIST_SENTE = [
        [0, "あなた0ポイント、相手10ポイント"],
        [1, "あなた1ポイント、相手9ポイント"],
        [2, "あなた2ポイント、相手8ポイント"],
        [3, "あなた3ポイント、相手7ポイント"],
        [4, "あなた4ポイント、相手6ポイント"],
        [5, "あなた5ポイント、相手5ポイント"],
        [6, "あなた6ポイント、相手4ポイント"],
        [7, "あなた7ポイント、相手3ポイント"],
        [8, "あなた8ポイント、相手2ポイント"],
        [9, "あなた9ポイント、相手1ポイント"],
        [10, "あなた10ポイント、相手0ポイント"],
    ]

    CHOICE_LIST_GOTE_TMP = [
        [10, "あなたに10ポイント"],
        [9, "あなた9ポイント"],
        [8, "あなた8ポイント"],
        [7, "あなた7ポイント"],
        [6, "あなた6ポイント"],
        [5, "あなた5ポイント"],
        [4, "あなた4ポイント"],
        [3, "あなた3ポイント"],
        [2, "あなた2ポイント"],
        [1, "あなた1ポイント"],
        [0, "あなた0ポイント"],
    ]

    CHOICE_LIST_GOTE = [[0, "承諾する"], [1, "拒否する"]]

SESSION_FIELDS = ['graph_data']

class Subsession(BaseSubsession):
    num_participants_p1 = models.IntegerField(initial=0)
    num_participants_p2 = models.IntegerField(initial=0)
    num_10 = models.IntegerField(initial=0)
    num_9 = models.IntegerField(initial=0)
    num_8 = models.IntegerField(initial=0)
    num_7 = models.IntegerField(initial=0)
    num_6 = models.IntegerField(initial=0)
    num_5 = models.IntegerField(initial=0)
    num_4 = models.IntegerField(initial=0)
    num_3 = models.IntegerField(initial=0)
    num_2 = models.IntegerField(initial=0)
    num_1 = models.IntegerField(initial=0)
    num_0 = models.IntegerField(initial=0)
    num_accept = models.IntegerField(initial=0)
    num_reject = models.IntegerField(initial=0)

    num_participants = models.IntegerField(initial=0)
    num_10_accept = models.IntegerField(initial=0)
    num_10_reject = models.IntegerField(initial=0)
    num_9_accept = models.IntegerField(initial=0)
    num_9_reject = models.IntegerField(initial=0)
    num_8_accept = models.IntegerField(initial=0)
    num_8_reject = models.IntegerField(initial=0)
    num_7_accept = models.IntegerField(initial=0)
    num_7_reject = models.IntegerField(initial=0)
    num_6_accept = models.IntegerField(initial=0)
    num_6_reject = models.IntegerField(initial=0)
    num_5_accept = models.IntegerField(initial=0)
    num_5_reject = models.IntegerField(initial=0)
    num_4_accept = models.IntegerField(initial=0)
    num_4_reject = models.IntegerField(initial=0)
    num_3_accept = models.IntegerField(initial=0)
    num_3_reject = models.IntegerField(initial=0)
    num_2_accept = models.IntegerField(initial=0)
    num_2_reject = models.IntegerField(initial=0)
    num_1_accept = models.IntegerField(initial=0)
    num_1_reject = models.IntegerField(initial=0)
    num_0_accept = models.IntegerField(initial=0)
    num_0_reject = models.IntegerField(initial=0)

    err_message = models.StringField()
    err_message_pair = models.StringField()

class Group(BaseGroup):
    p1_amount = models.IntegerField()
    p2_amount = models.IntegerField()

    p1_decision = models.StringField(
        choices=C.CHOICE_LIST_SENTE, widget=widgets.RadioSelect, label=""
    )

    p2_decision = models.StringField(
        choices=C.CHOICE_LIST_GOTE, widget=widgets.RadioSelect, label=""
    )

    p1_decision_why = models.LongStringField(label="なぜその選択をしましたか？")

    p2_decision_why = models.LongStringField(label="なぜその選択をしましたか？")

    flg_non_input_p1 = models.IntegerField(initial=0)
    flg_non_input_p2 = models.IntegerField(initial=0)

class Player(BasePlayer):
    tmp_first_player = models.StringField(
        choices=C.CHOICE_LIST_SENTE, widget=widgets.RadioSelect, label=""
    )
    tmp_first_player_why = models.LongStringField(label="なぜその選択をしましたか？")

    tmp_second_player = models.StringField(
        choices=C.CHOICE_LIST_GOTE_TMP, widget=widgets.RadioSelect, label=""
    )
    tmp_second_player_why = models.LongStringField(label="なぜその選択をしましたか？")

def set_P1(player: Player):
    sub = player.subsession
    group = player.group

    if group.p1_decision != "":
        sub.num_participants_p1 += 1
        s = group.p1_decision
        if s == "10":
            sub.num_10 += 1
        elif s == "9":
            sub.num_9 += 1
        elif s == "8":
            sub.num_8 += 1
        elif s == "7":
            sub.num_7 += 1
        elif s == "6":
            sub.num_6 += 1
        elif s == "5":
            sub.num_5 += 1
        elif s == "4":
            sub.num_4 += 1
        elif s == "3":
            sub.num_3 += 1
        elif s == "2":
            sub.num_2 += 1
        elif s == "1":
            sub.num_1 += 1
        elif s == "0":
            sub.num_0 += 1
        else:
            sub.err_message = "エラーあり"
    else:
        group.flg_non_input_p1 = 1
        tmp = random.randint(0, 10)
        group.p1_decision = str(C.CHOICE_LIST_SENTE[tmp][0])
    group.p1_amount = int(group.p1_decision)
    group.p2_amount = C.ENDOWMENT - int(group.p1_decision)

def set_P2(player: Player):
    sub = player.subsession
    group = player.group
    s = group.p2_decision
    if s != "":
        sub.num_participants_p2 += 1
        if s == "0":
            sub.num_accept += 1
        elif s == "1":
            sub.num_reject += 1
        else:
            sub.err_message = "エラーあり"
    else:
        group.flg_non_input_p2 = 1
        tmp = random.randint(0, 1)
        group.p2_decision = str(C.CHOICE_LIST_GOTE[tmp][0])

def set_pair(player: Player):
    sub = player.subsession
    group = player.group
    p1 = group.p1_decision
    p2 = group.p2_decision

    sub.num_participants += 1

    if p1 == "10" and p2 == "0":
        sub.num_10_accept += 1
    elif p1 == "10" and p2 == "1":
        sub.num_10_reject += 1
    elif p1 == "9" and p2 == "0":
        sub.num_9_accept += 1
    elif p1 == "9" and p2 == "1":
        sub.num_9_reject += 1
    elif p1 == "8" and p2 == "0":
        sub.num_8_accept += 1
    elif p1 == "8" and p2 == "1":
        sub.num_8_reject += 1
    elif p1 == "7" and p2 == "0":
        sub.num_7_accept += 1
    elif p1 == "7" and p2 == "1":
        sub.num_7_reject += 1
    elif p1 == "6" and p2 == "0":
        sub.num_6_accept += 1
    elif p1 == "6" and p2 == "1":
        sub.num_6_reject += 1
    elif p1 == "5" and p2 == "0":
        sub.num_5_accept += 1
    elif p1 == "5" and p2 == "1":
        sub.num_5_reject += 1
    elif p1 == "4" and p2 == "0":
        sub.num_4_accept += 1
    elif p1 == "4" and p2 == "1":
        sub.num_4_reject += 1
    elif p1 == "3" and p2 == "0":
        sub.num_3_accept += 1
    elif p1 == "3" and p2 == "1":
        sub.num_3_reject += 1
    elif p1 == "2" and p2 == "0":
        sub.num_2_accept += 1
    elif p1 == "2" and p2 == "1":
        sub.num_2_reject += 1
    elif p1 == "1" and p2 == "0":
        sub.num_1_accept += 1
    elif p1 == "1" and p2 == "1":
        sub.num_1_reject += 1
    elif p1 == "0" and p2 == "0":
        sub.num_0_accept += 1
    elif p1 == "0" and p2 == "1":
        sub.num_0_reject += 1
    else:
        sub.err_message_pair = "エラーあり"

def set_P2s(subsession: Subsession):
    for p in subsession.get_players():
        set_P2(p)

def set_P1s(subsession: Subsession):
    for p in subsession.get_players():
        set_P1(p)

def set_pairs(subsession: Subsession):
    for p in subsession.get_players():
        set_pair(p)
    graph(subsession=subsession)

def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    if group.p2_decision == "0":
        p1.payoff = int(group.p1_decision)
        p2.payoff = C.ENDOWMENT - int(group.p1_decision)
    else:
        p1.payoff = 0
        p2.payoff = 0

def graph(subsession: Subsession):
    sub = subsession
    session = sub.session
    graph_list_accept = []
    graph_list_reject = []
    ch10_2_result = []

    # 割合計算(拒否)
    for i in range(0, 11):
        reject_count = getattr(sub, f'num_{i}_reject')
        if reject_count > 0:
            tmp = round((reject_count / sub.num_participants) * 100, 2)
            graph_list_reject.append(tmp)
        else:
            graph_list_reject.append(0)
    # 割合計算(承諾)
    for i in range(0, 11):
        accept_count = getattr(sub, f'num_{i}_accept')
        if accept_count > 0:
            tmp = round((accept_count / sub.num_participants) * 100, 2)
            graph_list_accept.append(tmp)
        else:
            graph_list_accept.append(0)

    for player in subsession.get_players():
        group = player.group
        participant = player.participant
        p2_decision = "承諾" if group.p2_decision == "0" else "拒否"
        participant.vars["ch10_2_result"] = (
            "++++++++++++++++++++++++++++++++++++++++++++++++++<br>"
            "最後通牒ゲーム：あなたの結果："
            "プレイヤー1（先手）は、プレイヤー1に"
            + str(group.p1_amount)
            + "ポイント、プレイヤー2に"
            + str(group.p2_amount)
            + "という提案をしました。<br>"
            "プレイヤー2（後手）は、プレイヤー1の提案を" + (p2_decision) + "しました。<br>"
            "++++++++++++++++++++++++++++++++++++++++++++++++++"
        )
        ch10_2_result.append(participant.vars["ch10_2_result"])

    # 最終結果用（修正点！session.varsを使うこと）
    if "graph_data" not in session.vars:
        session.vars["graph_data"] = {}
    session.vars["graph_data"]["ch10_2"] = {
        "num_participants": sub.num_participants,
        "graph_list_accept": graph_list_accept,
        "graph_list_reject": graph_list_reject,
        "ch10_2_result": ch10_2_result,
    }

class Introduction(Page):
    timeout_seconds = 60

class Strategy(Page):
    timeout_seconds = 120 + C.ADD_TIME
    form_model = "player"
    form_fields = [
        "tmp_first_player",
        "tmp_first_player_why",
        "tmp_second_player",
        "tmp_second_player_why",
    ]

class Send(Page):
    timeout_seconds = C.ADD_TIME
    form_model = "group"
    form_fields = ["p1_decision", "p1_decision_why"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class WaitForP1(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_P1s

class SendBack(Page):
    timeout_seconds = C.ADD_TIME
    form_model = "group"
    form_fields = ["p2_decision", "p2_decision_why"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

class WaitForP2(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_P2s

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class ResultWaitPair(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_pairs

class Results(Page):
    @staticmethod
    def js_vars(player: Player):
        print("js_vars")
        # session.graph_data ではなく session.vars['graph_data']
        return player.session.vars.get("graph_data", {})

page_sequence = [
    Introduction,
    Strategy,
    Send,
    WaitForP1,
    SendBack,
    WaitForP2,
    ResultsWaitPage,
    ResultWaitPair,
    Results,
]
