from pydantic import BaseModel, Field
from enum import Enum

# 1. Possible decisions for the organism
class ActionType(str, Enum):
    SEARCH = "SEARCH"
    FIGHT = "FIGHT"
    REPRODUCE = "REPRODUCE"

#2. Structured output for the LLM
class BehaviorStrategy(BaseModel):
    """
    New Adaptive Behavior Strategy by LLM
    """
    decision: ActionType = Field(
        description="Basic action most appropriate to the environmental conditions (SEARCH, FIGHT, REPRODUCE)."
    )
    target: str = Field(
        description="Target of the action (e.g.: 'nearest source', 'weakest enemy', 'safe zone')."
    )
    priority_score: int = Field(
        description="The priority score of the action (0-100). This simulation engine will execute the action based on this score."
    )  
    reasoning: str = Field(
        description="A concise Chain-of-Thought (CoT) explanation of why LLM made this decision."
    )


class SimulationState(BaseModel):
    current_cycle: int = Field(
        description="The current simulation cycle number."
    )
    organism_id: str = Field(
        description="Unique identifier for the organism."
    )
    energy_level: float = Field(
        description="Current energy level of the organism (0.0-1.0)."
    )
    nearby_threats: list[str] = Field(
        description="List of nearby threats (e.g.: 'predator', 'resource', 'other organism')."
    )
    nearby_resources: list[str] = Field(
        description="List of nearby resources (e.g.: 'food', 'water', 'shelter') and distances."
    )