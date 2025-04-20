"""
## Agent
Agent is the unit in code that will perform any action.
It will have Goals,Utility Functions and Strategies.

## Goals

## Utility Functions

## Strategies

It is also able to store negotiation details and learn from it.(TODO implement later)
"""

from utils.utility import UtilityFunction
OFFER_THRESHOLD:float = 0.75


class Agent:
    def __init__(self,name,utility_func):
        self.name = name
        self.utility_func : UtilityFunction = utility_func
        self.memory = [] #{id,offer,response,agent}
    
    def propose_offer(self,weight,feature_ranges):
        # have a random offer generator
        pass

    def propose_counter_offer(self,offer):
        pass

    def evaluate_offer(self,offer)->float:
        pass

    def accept_offer(self,offer,threshold=OFFER_THRESHOLD):
        pass
    
    def update_memory(self, offer, response, agent: 'Agent'):
        pass

    def show_memory(self):
        pass

    def learn_from_outcome(self):
        pass