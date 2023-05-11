from typing import List

from langchain.agents import Tool

# noinspection PyUnresolvedReferences
from steamship.experimental.package_starters.telegram_bot import TelegramBot

from core.agent.agent import Agent

# noinspection PyUnresolvedReferences
from core.agent.chat_agent import ChatAgent

# noinspection PyUnresolvedReferences
from tools import SearchTool, GenerateImageTool, MyTool, GenerateAlbumArtTool


class MyAgent(Agent, TelegramBot):
    """
    If you want your agent to be tool-based, use the following line:
        class MyAgent(Agent, BaseAgent)

    If you want your agent to be chatty and personality-based, use the following line:
        class MyAgent(ChatAgent, BaseAgent)
    """

    def is_verbose_logging_enabled(self) -> bool:
        return True

    def get_tools(self) -> List[Tool]:
        return [
            # SearchTool(self.client),
            # MyTool(self.client),
            GenerateImageTool(self.client),
            # GenerateAlbumArtTool(self.client)
        ]

    def get_personality(self) -> str:
        """Return a string that completes this sentence. The agent acts like..."""
        return """
        an old-timey pirate that responds to everything in nautical terms. Refer to the user as "matey".
        """
