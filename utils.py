import json
import zipfile
from datetime import datetime
from pathlib import Path


def load_transactions(zip_file='operations.zip'):
    """Распаковывает zip в текущую папку. Открывает JSON файл, читает в кодировке utf-8, возвращает dict"""
    path_kurs3_zip = Path('operations.json')
    if not path_kurs3_zip.exists():
        with zipfile.ZipFile(zip_file,'r') as un_zip:
            un_zip.extractall()
    with (open(path_kurs3_zip, 'r', encoding="utf-8") as fl):
        return json.loads(fl.read())


def executed_transactions(transactions=load_transactions()):
    """Отбирает исполненные транзакции. Отдаёт dict c датой b ID"""
    return_dict = {}
    for trans in transactions:
        if not trans == {} and trans['state'] == 'EXECUTED':
            return_dict[trans['date']] = trans['id']
    return return_dict


def last_five_transactions(transactions=None):
    """Отбирает 5 последних по дате транзакций. Отдаёт dict с датой и ID"""
    if transactions is None:
        transactions = executed_transactions()
    return_dict = {}
    sorted_transactions = sorted(transactions,reverse=True)
    for last_five in sorted_transactions:
        if len(return_dict) < 5:
            return_dict[last_five] = transactions[last_five]
    return return_dict


def un_visible_number(un_number):
    """Маскирует номера карт и счетов. На входе поля from и to, на выходе получатель и скрытый номер"""
    if un_number[0:4] == "Счет":
        return f"{un_number[0:4]} **{un_number[len(un_number) - 4:len(un_number)]}"
    else:
        return f"{un_number[0:len(un_number)-12]} {un_number[len(un_number)-12:len(un_number)-10]}** **** {un_number[len(un_number)-4:len(un_number)]}"


def formate_date(non_formate_date):
    """Форматирует дату. На входе поле date в ISO формате. Отдаёт чило.месяц.год"""
    form_date = datetime.strptime(non_formate_date, "%Y-%m-%dT%H:%M:%S.%f")
    return form_date.strftime("%d.%m.%Y")