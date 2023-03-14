import numpy as np

cash_flows = []
discount_rate = 0.1

npv = np.npv(discount_rate, cash_flows)
print("Net Present Value: ", npv)