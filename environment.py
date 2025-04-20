from agent.agent import Agent
from typing import Optional, Dict, Any, List

class NegotiationEnvironment:
    def __init__(self, agents: list[Agent], rounds: int) -> None:
        print("-" * 30)
        print(f"Negotiation Environment setup for {rounds} rounds with {len(agents)} agents")
        self.agents = agents
        self.rounds = rounds
        self.current_round = 0
        self.history = []
        self.agreement = None
        self.agreement_round = None
        
        # Validate we have enough agents
        if len(agents) < 2:
            raise ValueError("Need at least 2 agents for negotiation")
            
    def run_negotiation(self, start_agent: int = 0):
        """Run multi-agent negotiation where the starting agent makes an offer and others respond sequentially."""
        print("-" * 30)
        print(f"Starting negotiation with {len(self.agents)} agents using sequential protocol...")
        print("Participating agents:", ", ".join([agent.name for agent in self.agents]))

        offer = self.agents[start_agent].propose_offer(
            self.agents[start_agent].utility_func.weights,
            self.agents[start_agent].utility_func.feature_ranges
        )
        print(f"\nInitial offer by {self.agents[start_agent].name}: {offer}")

        for round_num in range(1, self.rounds + 1):
            self.current_round = round_num
            print(f"\nRound {round_num}:")

            all_accepted = True

            for i, agent in enumerate(self.agents):
                if i == start_agent:
                    continue  # Skip the proposer

                accepted = agent.accept_offer(offer)
                print(f"{agent.name} {'accepted' if accepted else 'rejected'} the offer.")
                agent.update_memory(offer=offer,response=accepted,agent=agent)
                if not accepted:
                    all_accepted = False
                    counter_offer = agent.propose_counter_offer(offer)
                    print(f"{agent.name} proposed counter offer: {counter_offer}")
                    offer = counter_offer
                    start_agent = i  # New proposer becomes the one who rejected and countered
                    break  # Restart from new proposer in next round

            if all_accepted:
                print(f"All agents accepted the offer: {offer}")
                self.agreement = offer
                self.agreement_round = round_num
                return offer

        print("Negotiation ended without agreement.")
        return None
