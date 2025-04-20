import math
import random
from agent.agent import  Agent

OFFER_ACCEPTANCE_THRESHOLD = 0.70

class RuleAgent(Agent):
    def propose_offer(self,weight,feature_ranges):
        """
        Only called if the agent offers first else call `propose_counter_offer(self,offer)`
        """
        BIAS_RATE = 0.60
        offer = {}
        for key in weight.keys():
            if key not in feature_ranges:
                continue
            min_val,max_val,inv = feature_ranges[key]
            # provide a bais according to inverse
            if inv:
                max_val = math.ceil((1-BIAS_RATE)*max_val)
                off_val = random.randint(min_val,max_val)
                offer[key] = off_val
            else:
                min_val = math.floor((1+BIAS_RATE)*min_val)
                off_val = random.randint(min_val,max_val)
                offer[key] = off_val
        return offer
                
    def propose_counter_offer(self, offer):
        shift_rate = 0.15
        counter_offer = {}

        for key in offer:
            if key not in self.utility_func.feature_ranges:
                continue

            min_val, max_val, inverse = self.utility_func.feature_ranges[key]
            current_val = offer[key]

            # Move the offer slightly toward what this agent prefers
            range_span = max_val - min_val
            shift = max(1, int(shift_rate * range_span))

            if inverse:
                # Agent prefers smaller values
                new_val = current_val - shift
            else:
                # Agent prefers higher values
                new_val = current_val + shift

            # Clamp to allowed range
            new_val = max(min_val, min(new_val, max_val))
            counter_offer[key] = new_val

        # Only return if it's better than the current one
        if self.evaluate_offer(counter_offer) > self.evaluate_offer(offer):
            offer = counter_offer

        print(f"[{self.name}] Counter offer: {offer} (Score: {self.evaluate_offer(offer):.2f})")
        return offer



            
    
    def evaluate_offer(self,offer):
        return self.utility_func.evaluate(offer)
    
    def accept_offer(self, offer, threshold=OFFER_ACCEPTANCE_THRESHOLD):
       return self.evaluate_offer(offer) >= threshold
    
    def update_memory(self, offer, response, agent: 'Agent'):
        self.memory.append({
            'id': len(self.memory),
            'offer': offer,
            'response': response,
            'agent': agent
        })
    
    def show_memory(self):
        if not self.memory:
            print("Memory is empty.")
            return
        
        print(f"Negotiation Memory for {self.name}:")
        for entry in self.memory:
            print(f"ID: {entry['id']}")
            print(f"Offer: {entry['offer']}")
            print(f"Response: {entry['response']}")
            print(f"With Agent: {entry['agent'].name} ({entry['agent'].__class__.__name__})")
            print("-" * 30)

    def learn_from_outcome(self):
        return super().learn_from_outcome()