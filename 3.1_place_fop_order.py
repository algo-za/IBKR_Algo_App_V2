from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *

import threading
import time

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print('The next valid order id is: ', self.nextorderId)

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
              'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


def run_loop():
    app.run()


# Function to create FX Order contract
def options_order(symbol):
    contract = Contract()
    contract.symbol = "ES"
    contract.secType = 'FOP'
    contract.exchange = 'CME'
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = '20230221'
    contract.strike = 4100
    contract.right = 'C'
    contract.multiplier = '50'
    return contract


app = IBapi()
app.connect('127.0.0.1', 4002, 123)

app.nextorderId = None

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

# Check if the API is connected via orderid
while True:
    if isinstance(app.nextorderId, int):
        print('connected')
        break
    else:
        print('waiting for connection')
        time.sleep(1)

# Create order object
order = Order()
order.action = 'BUY'
order.totalQuantity = 1
order.orderType = 'MKT'
order.eTradeOnly = ''
order.firmQuoteOnly = ''

# Place order
app.placeOrder(app.nextorderId, options_order('TSLA'), order)
# app.nextorderId += 1

time.sleep(3)

# Cancel order
print('cancelling order')
app.cancelOrder(app.nextorderId)

time.sleep(3)
app.disconnect()