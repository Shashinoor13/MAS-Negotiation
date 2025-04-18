from agent.agent import OFFER_THRESHOLD, Agent

RULE_BASED_OFFER_THRESHOLD = 0.75

class RuleAgent(Agent):
    def propose_offer(self):
        return super().propose_offer()
    
    def evaluate_offer(self,offer):
        return self.utility_func.evaluate(offer)
    
    def accept_offer(self, offer, threshold=RULE_BASED_OFFER_THRESHOLD):
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