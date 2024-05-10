from utils import last_five_transactions
from utils import load_transactions
from utils import formate_date
from utils import un_visible_number


for key_, value_ in last_five_transactions().items():
    for trans in load_transactions():
        if not trans == {} and trans['id'] == value_:
            print(f"{formate_date(trans['date'])} {trans['description']}")
            if 'from' in trans.keys(): print(f"{un_visible_number(trans['from'])} -> ", end='')
            if 'to' in trans.keys(): print(f"{un_visible_number(trans['to'])}")
            print(f"{trans['operationAmount']['amount']} {trans['operationAmount']['currency']['name']}\n")
