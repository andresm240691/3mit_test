import logging
import requests
from treemittest.settings import API_URL
from bs4 import BeautifulSoup
from coins.models import (
    Coin as CoinModel,
    BriefCase,
    Operation
)


class CoinApi:

    def __init__(self):
        self.api_url = API_URL

    def _get_html_page(self):
        html = None
        try:
            response = requests.get(self.api_url)
            if str(response.status_code).startswith('2'):
                html = response.content
        except Exception:
            logging.exception('Exception in utils/CoinApi.get_html_page')
        finally:
            return html

    def _formatter_html(self, str_html):
        response = None
        try:
            response = BeautifulSoup(str_html, 'lxml')
        except Exception:
            logging.exception('Exception in utils/CoinApi._formatter_html')
        finally:
            return response

    def _get_records(self, soap):
        rows = []
        try:
            tag_table = soap.find('table')
            tag_body = tag_table.find('tbody')
            tag_tr_all = tag_body.find_all('tr')

            for tag_tr in tag_tr_all:
                try:
                    new_coin = {}
                    tag_td_all = tag_tr.find_all('td')

                    # Table index field
                    table_index = int(tag_td_all[0].get_text())
                    new_coin.update(table_index=table_index)

                    # Image src
                    img_src = tag_td_all[1]
                    img_src = img_src.find('img')
                    img_src = img_src['src']
                    new_coin.update(img_src=img_src)

                    # Name
                    name = tag_td_all[1].find(
                        'span', class_='tw-hidden d-lg-block font-bold'
                    ).get_text()
                    new_coin.update(name=name)

                    # Symbol
                    symbol = tag_td_all[2].find('span').get_text()
                    new_coin.update(symbol=symbol)

                    # Price
                    str_price = tag_td_all[3].find('span').get_text()
                    price = float(str_price.replace('$', '').replace(
                        '.', '').replace(',', '.'))
                    new_coin.update(price=price)

                    # Percentage 1 hour
                    percentage = tag_td_all[4].find('span').get_text()
                    new_coin.update(percentage_one_hour=percentage)

                    # Percentage 24 hour
                    percentage = tag_td_all[5].find('span').get_text()
                    new_coin.update(percentage_twentyfour_hour=percentage)

                    # Percentage 7 days
                    percentage = tag_td_all[6].find('span').get_text()
                    new_coin.update(percentage_seven_days=percentage)

                    # Percentage 38 days
                    percentage = tag_td_all[7].find('span').get_text()
                    new_coin.update(percentage_thirtyeight_days=percentage)

                    # Volume
                    value = tag_td_all[8].find('span').get_text()
                    value = float(value.replace('$', '').replace(
                        '.', '').replace(',', '.'))
                    new_coin.update(volume=value)

                    # Circulating Quantity
                    value = tag_td_all[9].find('div').get_text()
                    value = float(value.strip().replace('.', '').replace(
                        ',', '.'))
                    new_coin.update(circulating_quantity=value)

                    # Total Quantity
                    value = tag_td_all[10].find('div').get_text()
                    value = value.strip()
                    new_coin.update(total_quantity=value)

                    rows.append(new_coin)
                except Exception:
                    logging.exception('Error processing coin')
                    continue
        except Exception:
            logging.exception('Exception in utils/CoinApi._get_records')
        finally:
            return rows

    def _save(self, rows):
        flag = False
        try:
            for row_coin in rows:
                coin = CoinModel.objects.filter(symbol=row_coin.get('symbol'))
                if coin.exists():
                    coin = coin.first()
                    coin.price = row_coin.get('price')
                    coin.percentage_one_hour = row_coin.get(
                        'percentage_one_hour')
                    coin.percentage_twentyfour_hour = row_coin.get(
                        'percentage_twentyfour_hour')
                    coin.percentage_seven_days = row_coin.get(
                        'percentage_seven_days')
                    coin.percentage_thirtyeight_days = row_coin.get(
                        'percentage_thirtyeight_days')
                    coin.volume = row_coin.get('volume')
                    coin.circulating_quantity = row_coin.get(
                        'circulating_quantity')
                    coin.total_quantity = row_coin.get('total_quantity')
                    coin.save()
                else:
                    new_coin = CoinModel(**row_coin)
                    new_coin.save()
            flag = True
        except Exception:
            logging.exception('Exception in utils/CoinApi._save')
        finally:
            return flag

    def execute(self):
        flag = False
        try:
            str_html = self._get_html_page()
            if str_html:
                soap_content = self._formatter_html(str_html=str_html)
                if soap_content:
                    rows = self._get_records(soap=soap_content)
                    if rows:
                        print("Processing #{} coins records".format(
                            str(len(rows))))
                        if self._save(rows=rows):
                            flag = True
            if not flag:
                flag = False
        except Exception:
            logging.exception('Exception in utils/CoinApi.execute')
        finally:
            return flag


def register_operation(user, data):
    flag = True
    try:
        coin_query = CoinModel.objects.filter(id=data.get('coin_id')).first()
        quantity = float(data.get('quantity'))
        amount = float(data.get('amount'))

        # Register in Briefcase
        bc_query = BriefCase.objects.filter(user=user, coin=coin_query).first()
        if bc_query:
            bc_query.total_quantity = bc_query.total_quantity + quantity
            average = amount / quantity
            str_trend = 'NEGATIVE' if average < coin_query.price \
                else 'POSITIVE'
            bc_query.average_purchase = average
            bc_query.trend = str_trend
            bc_query.save()
        else:
            bc_query = BriefCase()
            bc_query.coin = coin_query
            bc_query.user = user
            bc_query.total_quantity = quantity
            average = amount / quantity
            str_trend = 'NEGATIVE' if average < coin_query.price \
                else 'POSITIVE'
            bc_query.average_purchase = average
            bc_query.trend = str_trend
            bc_query.save()

        # Register the purchase
        operation_query = Operation()
        operation_query.coin = coin_query
        operation_query.user = user
        operation_query.total_quantity = quantity
        operation_query.amount = amount
        operation_query.briefcase = bc_query
        operation_query.save()
    except Exception:
        logging.exception('Exception in register_operation')
        flag = False
    finally:
        return flag