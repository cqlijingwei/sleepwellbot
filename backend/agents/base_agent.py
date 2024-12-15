from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, config, db_manager):
        self.config = config
        self.db = db_manager
        self.enabled = True

    @abstractmethod
    def process_query(self, query: str) -> str:
        pass

    def is_enabled(self) -> bool:
        return self.enabled

    def toggle_agent(self, status: bool):
        self.enabled = status