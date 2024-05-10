import json
import zipfile
from datetime import datetime


def load_transactions(zip_file='operations.zip', file_name='operations.json'):
    with zipfile.ZipFile(zip_file,'r') as un_zip:
        un_zip.extractall()
    with (open(file_name, 'r', encoding="utf-8") as fl):
        return json.loads(fl.read())


def executed_transactions(transactions=load_transactions()):
    return_dict = {}
    for trans in transactions:
        if not trans == {} and trans['state'] == 'EXECUTED':
            return_dict[trans['date']] = trans['id']
    return return_dict


def last_five_transactions(transactions=None):
    if transactions is None:
        transactions = executed_transactions()
    return_dict = {}
    sorted_transactions = sorted(transactions,reverse=True)
    for last_five in sorted_transactions:
        if len(return_dict) < 5:
            return_dict[last_five] = transactions[last_five]
    return return_dict


def un_visible_number(un_number):
    if un_number[0:4] == "Счет":
        return un_number[0:4] + " **" + un_number[len(un_number) - 4:len(un_number)]
    else:
        return un_number[0:len(un_number)-12] + " " + un_number[len(un_number)-12:len(un_number)-10] + "** **** " + un_number[len(un_number)-4:len(un_number)]


def formate_date(non_formate_date):
    form_date = datetime.strptime(non_formate_date[0:len(non_formate_date)-7], "%Y-%m-%dT%H:%M:%S")
    return form_date.strftime("%d.%m.%Y")



# class Transactions:
#     def __init__(self, id_trans, date_trans, description_trans, from_trans, to_trans, amount_trans, currency_trans):
#         self.id_trans = id_trans
#         self.date_trans = date_trans
#         self.description_trans = description_trans
#         self.from_trans = from_trans
#         self.to_trans = to_trans
#         self.amount_trans = amount_trans
#         self.currency_trans = currency_trans
#
#     def __repr__(self):
#         return (f"Transactions ('{self.date_trans}', '{self.description_trans}', '{self.from_trans}', '{self.to_trans}', '{self.amount_trans}', '{self.currency_trans}')")
#
#     def append(self, date_trans, description_trans, from_trans, to_trans, amount_trans, currency_trans):
#          self.append(Transactions(date_trans, description_trans, from_trans, to_trans, amount_trans, currency_trans)
#

# for fl_ln in load_transactions():
#     if not fl_ln == {} and fl_ln['state'] == 'EXECUTED':
#         Transactions.append(fl_ln['date'], fl_ln['description'], )



#datetime(year, month, day [, hour] [, min] [, sec] [, microsec])
#for a, b in last_executed_transactions(load_transactions()).items(): print(a, b)
#last_five_transactions(last_executed_transactions(load_transactions()))

    # return_dict[file_line_dict] = file_line[file_line_dict]
            # #print(file_line_dict, file_line[file_line_dict])

        # #дальше вообще не изящно, подумаю потом как сделать красиво
        # try:
        #     return_dict['state'] = file_line['state']
        # except LookupError:
        #     return_dict['state'] = ''
        # try:
        #     return_dict['date'] = file_line['date']
        # except LookupError:
        #     return_dict['date'] = ''
        # try:
        #     return_dict['description'] = file_line['description']
        # except LookupError:
        #     return_dict['description'] = ''
        # try:
        #     return_dict['from'] = file_line['from']
        # except LookupError:
        #     return_dict['from'] = ''
        # try:
        #     return_dict['to'] = file_line['to']
        # except LookupError:
        #     return_dict['to'] = ''
        # try:
        #     return_dict['amount'] = file_line['operationAmount']['amount']
        # except LookupError:
        #     return_dict['amount'] = ''
        # try:
        #     return_dict['currency'] = file_line['operationAmount']['currency']['name']
        # except LookupError:
        #     return_dict['currency'] = ''
