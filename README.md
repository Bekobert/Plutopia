🧬 GenAI-Driven Evolution Simulation: Adaptive Artificial Life
<div align="center">
<img src="https://img.shields.io/badge/Tech-Python_3.11+-blue?style=for-the-badge&logo=python" alt="Python Badge">
<img src="https://img.shields.io/badge/LLMs-LangGraph_Agent-red?style=for-the-badge&logo=openai" alt="LLM Agent Badge">
<img src="https://img.shields.com/badge/Deployment-AWS_Serverless-orange?style=for-the-badge&logo=amazon-aws" alt="AWS Serverless Badge">
<img src="https://img.shields.com/badge/Data-VectorDB_RAG-green?style=for-the-badge&logo=qdrant" alt="Vector DB Badge">
</div>

🚀 Project Overview
This project elevates the classic evolutionary simulation engine by integrating Large Language Models (LLMs) and Agent Systems to generate adaptive organism behaviors. We separate the organisms' fixed genetic traits (Python Backend) from their strategic decision-making (LLM Agent).

The core goal is to observe emergent behaviors in complex, dynamic virtual environments, driven by an LLM Agent, and to deploy this system using production-grade GenAI engineering practices.

🌟 Key Competencies and Technology Showcase
This project demonstrates the full-stack GenAI Engineer skill set, directly addressing key requirements from modern job postings:

LLM Orchestration: Built a LangGraph/LangChain Agent structure to generate intelligent, context-aware strategies for organisms.

RAG Architecture: Implemented Retrieval-Augmented Generation (RAG) by storing past evolutionary successes in a Vector Database (FAISS/Qdrant), creating an "Evolutionary Memory."

Prompt Engineering: Utilized advanced prompting techniques like Chain-of-Thought (CoT) and ReAct to enhance the Agent's reasoning and decision-making capabilities.

Serverless Deployment: Deployed the Python Backend's Agent API using AWS Lambda and API Gateway, showcasing practical AWS Serverless experience.

MLOps Fundamentals: Integrated monitoring with CloudWatch, ensured secure access with IAM, and containerized the backend using Docker.

Data Proficiency: Used SQL (PostgreSQL) for statistical data and a Vector Database for unstructured memory storage.

🏗️ Architecture Diagram: End-to-End Flow
The simulation consists of three main components and communicates via a RESTful API.

Kod snippet'i

graph TD
    A[Unity Frontend] -->|1. Request Strategy| B(AWS API Gateway);
    B --> C{AWS Lambda: Python Agent};
    C -->|2. Fetch Stats (SQL Tool)| D[SQL DB/PostgreSQL];
    C -->|3. Retrieve Past Successes (RAG)| E[Vector DB / Evolutionary Memory];
    C -->|4. Prompt & CoT/ReAct| F(LLM Provider);
    F -->|5. New Strategy (JSON)| C;
    C -->|6. Logging & Monitoring| G[AWS CloudWatch & DynamoDB];
    C -->|7. Return Response| B;
    B --> A;
⚙️ Technical Implementation Details
1. Backend and GenAI Core
Feature	Description
Tech Stack	Python 3.11, FastAPI, LangGraph (Orchestration), HuggingFace Transformers (Embedding)
Agent Flow	Designed with a Tool Using pattern. When an organism reaches a critical decision point, the Agent is triggered, utilizing a SQL Executor Tool to fetch current stats and a Vector DB Retriever Tool to fetch relevant past strategies.
Advanced Prompting	Applied the Chain-of-Thought (CoT) technique to make the LLM's reasoning traceable. Example Prompt: "You are a survival strategist. Analyze the current state (population: X, resources: Y) and the historical successful strategies provided below to formulate a new, optimal survival rule. Think step-by-step (Chain-of-Thought) before outputting the final JSON."
Data Management	PostgreSQL for population and resource statistics (demonstrating SQL proficiency), and FAISS/Qdrant for the Evolutionary Memory vector store.

E-Tablolar'a aktar
2. AWS Serverless Deployment
Containerization: The entire FastAPI service (including LangChain, numpy dependencies) is packaged using Docker and deployed via AWS ECR using Lambda Container Image Support.

API Gateway: Serves as the single RESTful API endpoint, triggering the Lambda function for strategy generation.

Security (IAM): The Lambda Execution Role is configured according to the principle of least privilege, with only essential permissions like s3:GetObject and cloudwatch:PutMetricData.

Monitoring: Critical API latency and error rates are actively monitored using AWS CloudWatch metrics.

🛠️ Setup and Execution
Prerequisites
Python 3.11+

Unity 2022+

AWS CLI configured

LLM API Key (OpenAI, Anthropic, Gemini, etc.)

Backend Setup
Bash

# 1. Set up the environment and install dependencies
cd backend
pip install -r requirements.txt

# 2. Run in Development Mode (for API testing)
uvicorn main:app --reload

# 3. Build the Docker Image
docker build -t evolution-agent-backend .

# 4. AWS Deployment (using Serverless Framework, AWS CLI, or CDK)
# Deployment steps will be detailed in the docs/ folder.
🎮 Unity Integration
The EvolutionManager.cs script in the Unity Frontend prepares the simulation state as a JSON payload and sends a POST request to the configured AWS API Gateway endpoint. The returned JSON rule set dynamically updates the organisms' adaptive behaviors.

🤝 Contribution and License
While designed as a personal project, contributions are welcome! Please open an issue or submit a Pull Request.

License: This project is licensed under the MIT License.