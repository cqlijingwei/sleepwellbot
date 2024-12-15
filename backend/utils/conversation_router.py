class ConversationRouter:
    def __init__(self, agents):
        self.agents = agents
        self.fallback_response = "I apologize, I'm unable to help with that right now."

    def route_query(self, query: str) -> str:
        # More sophisticated routing
        for agent in self.agents:
            if agent.is_enabled():
                response = agent.process_query(query)
                if response and response != "Could not process your request.":
                    return response
        
        return self.fallback_response