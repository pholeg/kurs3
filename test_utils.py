from utils import last_five_transactions
from utils import load_transactions
from utils import formate_date
from utils import un_visible_number
from utils import executed_transactions


def test_last_five_transactions():
    assert not last_five_transactions(executed_transactions()) != {'2019-12-08T22:46:21.935582': 863064926,
                                                                   '2019-12-07T06:17:14.634890': 114832369,
                                                                   '2019-11-19T09:22:25.899614': 154927927,
                                                                   '2019-11-13T17:38:04.800051': 482520625,
                                                                   '2019-11-05T12:04:13.781725': 801684332}


def test_load_transactions():
    assert len(load_transactions()) == 101


def test_formate_date():
    assert formate_date('2018-06-30T02:08:58.425572') == '30.06.2018'


def test_un_visible_number():
    assert un_visible_number('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert un_visible_number('Счет 35383033474447895560') == 'Счет **5560'
