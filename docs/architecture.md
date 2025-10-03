# 🏗 Plutopia – Architecture Overview

This document explains the high-level architecture of the hybrid simulation project, showing how Python (backend) and Unity (frontend) interact, along with core components for evolution, organisms, and environment.

---

## 1. System Overview

+-------------------+ REST/gRPC +-------------------+
| Unity Frontend | <------------------> | Python Backend |
|-------------------| |-------------------|
| - 3D Environment | | - Evolution Engine|
| - Organism Prefabs| | - DNA/Genome |
| - Resources | | - Organism Logic |
| - Scene Controller| | - Environment |
+-------------------+ +-------------------+


- **Unity Frontend**:  
  - Visualizes organisms, resources, day/night cycles  
  - Requests organism updates from Python backend  
  - Updates organism positions, colors, and status in real-time  

- **Python Backend**:  
  - Handles genome creation, mutation, inheritance  
  - Calculates energy consumption, reproduction, death  
  - Manages environmental factors (sunlight, water, events)  
  - Provides API endpoints for Unity to fetch simulation data  

---

## 2. Core Components

### 2.1 Genetics Module
- Genome representation (string or vector)  
- Mutation & recombination functions  
- Trait mapping (speed, size, energy efficiency)

### 2.2 Organism Module
- Attributes: energy, age, position, genome  
- Behaviors: move, consume resources, reproduce, die  

### 2.3 Environment Module
- Planet parameters: gravity, light, terrain  
- Resources: food, water, sunlight distribution  
- Events: day/night cycles, random environmental changes  

### 2.4 API / Communication Layer
- FastAPI or gRPC server  
- Endpoints for:
  - `/organisms` → fetch organism state  
  - `/resources` → fetch current resources  
  - `/events` → environmental changes  

---

## 3. Data Flow

[Simulation Loop]
Python Backend:

Update environment & resources

Process organism actions & energy

Apply mutation & reproduction rules

Send updated organism data → Unity

Unity Frontend:

Request updated organism states

Update 3D positions & visual traits

Render scene (organisms + environment)

---

## 4. Future Extensions
- Vector database (FAISS, Pinecone) to store genome history  
- LLM / agent integration for decision-making behaviors  
- Multi-cellular organism evolution  
- Predation, cooperation, or complex ecological interactions  

---

## 5. Notes
- Start small: a few hundred organisms with simple genomes  
- Python handles computation-heavy tasks  
- Unity handles real-time visualization and interaction  
- Communication is stateless per update loop, ensuring modularity
