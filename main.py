from agent.rule_based_agent import RuleAgent
from environment import NegotiationEnvironment
from utils.utility import UtilityFunction

# Buyer
"""
Buyer weights different features ---
`price` is his highest priority
`warrenty` is is 2nd priority
`delivery_time` is his 3rd priority

Buyer has different ranges for each features ---
`price` min_val=0,max_val=100,inverse=True :He is trying to spend less
`warrenty` min_val=0,max_val=4,inverse=False :He is trying to get more warrenty
`delivery_time` min_val=0,max_val=3,inverse=True :He is trying to get less delivery_time
"""
buyer_weights={
    "price": 0.6,
    "warrenty": 0.3,
    "delivery_time": 0.1
}

buyer_feature_ranges = {
    "price": (0, 100, True),
    "warrenty": (0, 4, False),
    "delivery_time": (0, 3, True)
}

# Seller
"""
Seller weights different features ---
`price` is highest priority
`warrenty` is 2nd priority
`delivery_time` is 3rd priority

Seller has different ranges for each features ---
`price` min_val=50,max_val=150,inverse=False :Seller wants higher price
`warrenty` min_val=1,max_val=5,inverse=True :Seller wants to give less warranty
`delivery_time` min_val=1,max_val=5,inverse=False :Seller prefers longer delivery time
"""
seller_weights = {
    "price": 0.7,
    "warrenty": 0.2,
    "delivery_time": 0.1
}



seller_feature_ranges = {
    "price": (50, 150, False),
    "warrenty": (1, 5, True),
    "delivery_time": (1, 5, False)
}

# Create utility functions for both agents
buyer_utility = UtilityFunction(buyer_weights, buyer_feature_ranges)
seller_utility = UtilityFunction(seller_weights, seller_feature_ranges)

# Create agents
buyer = RuleAgent("Buyer", buyer_utility)
seller = RuleAgent("Seller", seller_utility)
    
environment= NegotiationEnvironment([buyer,seller],5)
environment.run_negotiation()

# count =0
# for i in range(100):
#     agreement = environment.run_negotiation()
#     if agreement is not None:
#         count +=1

# print(f"Agreed {count} times")