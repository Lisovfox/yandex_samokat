import requests
import configuration
def create_order(order):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=order)
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(track))