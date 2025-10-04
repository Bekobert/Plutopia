import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from typing import Dict, Any

# Importing Our Models
from models import BehaviorStrategy, SimulationState

# Importing LLM libs
from langchain_google_genai import ChatGoogleGenerativeAI

# Loading variables in .env file
load_dotenv()

app = FastAPI(
    title="GENAI Evolution Simulation API",
    description="Adaptive behavior strategies service driven by LLM Agent."
)

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

print(f"DEBUG: GEMINI_API_KEY yüklendi mi? {'GEMINI_API_KEY' in os.environ}")
# Run LLM globally
# It works only if GEMINI_API_KEY is set in .env file
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0, api_key = GEMINI_KEY)
except Exception as e:
    # If this error is caught in the Lambda environment, check the environment variable.
    print(f"LLM not initialized: {e}")
    llm = None


@app.get("/health", response_model=Dict[str, str])
def health_check():
    """Check if the API is running"""
    return {"status": "ok", "message": "API is running"}

@app.post("/generate-strategy", response_model=BehaviorStrategy)
async def generate_strategy(state: SimulationState):
    """
    Requests a new strategy from the LLM Agent based on the simulation status received from Unity.
    """
    if not llm:
        raise HTTPException(status_code=500, detail="LLM Agent not initialized. Check API key")
    
    try:
        # **In next steps there will be LangChain Agent Logic**

        # For now, we only use an example prompt for testing
        prompt = f"""
        Current State for Organism {state.organism_id}:
        Energy: {state.energy_level},
        Threats: {state.nearby_threats},
        Resources: {state.nearby_resources},
        Based on this state, generate the optimal BehaviorStrategy JSON.
        """
    
        # This is a temporary call; RAG and Agent logic will be added later.
        # We want structured JSON output directly from LLM (LangChain's capability).
        # However, this part is a bit more complex and we'll detail it in the next step.

        # For now, let's return a successful test response:
        return BehaviorStrategy(
            decision="SEARCH",
            target=state.nearby_resources[0] if state.nearby_resources else "Random Area",
            priority_score=85,
            reasoning="Low Energy and there are resources nearby. Go to resource first."
        )

    except Exception as e:
        print(f"Error in Strategy Generation: {e}")
        raise HTTPException(status_code=500, details=f"Internal error in Strategy Generation: {e}")


# Main function to run server (For local dev)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
