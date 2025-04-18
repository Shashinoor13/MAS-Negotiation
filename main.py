from agent.rule_based_agent import RuleAgent
from utils.utility import UtilityFunction


# Buyer
"""
Buyer weights different features
---
`price` is his highest priority
`warrenty` is is 2nd priority
`delivery_time` is his 3rd priority

Buyer has different ranges for each features
---
`price` min_val=0,max_val=100,inverse=True :He is trying to spend less 
`price` min_val=0,max_val=4,inverse=False :He is trying to get more warrenty 
`price` min_val=0,max_val=3,inverse=True :He is trying to get less delivery_time 
"""
buyer_weights={
    "price":0.6,
    "warrenty":0.3,
    "delivery_time":0.1
}

feature_ranges={
    "price":(0,100,True),
    "warrenty":(0,4,False),
    "delivery_time":(0,3,True)
}


buyer_utility = UtilityFunction(buyer_weights,feature_ranges)

"""
# best offer
offer = {
    "price":0,
    "warrenty":4,
    "delivery_time":0
}
"""
# this is the inital offer by the seller
offer={
    "price":70,
    "warrenty":5,
    "delivery_time":4
}

buyer = RuleAgent("Buyer",buyer_utility)
buyer_response = buyer.accept_offer(offer)
buyer.update_memory(offer=offer,response=buyer_response,agent=buyer)

buyer.show_memory()