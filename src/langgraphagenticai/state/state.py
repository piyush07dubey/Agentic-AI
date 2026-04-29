from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """The state of the application"""
    messages:Annotated[List,add_messages]