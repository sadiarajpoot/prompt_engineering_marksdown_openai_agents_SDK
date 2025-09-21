# 🤖 OpenAI Agents SDK - Study Notes

This repository contains my study notes and practice work on **OpenAI Agents SDK** concepts, configurations, and advanced features. The goal is to provide a structured overview of all key topics I have covered.

---

## 📌 Topics Covered

### ⚙️ 1. Agents & Configuration

* Basics of creating an **Agent**
* `Agent` configuration parameters
* Defining **instructions** and **output types**
* Using `Runner` to execute agents

### 🧠 2. Contexts (Local & Global)

* **Local Context**: Data available only inside the agent, not passed to the LLM
* **Global/LLM Context**: Data passed to the LLM for reasoning
* `Context` object usage for managing state

### 🏗️ 3. Dataclasses vs Pydantic Classes

* **Pydantic** for validation and schema generation
* **Dataclasses** for lightweight structured data
* When to prefer each in Agent SDK

### 🔄 4. Dynamic Instructions

* Modifying agent instructions at runtime
* Example: adjusting behavior based on user input or system state

### 🛡️ 5. Guardrails

* **Input Guardrails**: validate or restrict incoming data
* **Output Guardrails**: validate or enforce safe responses
* Practical examples of applying guardrails in SDK

### 🤝 6. Handoffs

* **Basic Handoff**: Passing control between agents
* **Advanced Handoff**: With conditions and callbacks
* **Custom Handoff**: Define your own transfer logic

### ⏱️ 7. Conversation Controls

* **Max Turns**: Limiting the number of conversational steps
* Exception handling with `MaxTurnsExceeded`

### 🎲 8. Sampling & Generation Parameters

* `temperature` → randomness control
* `top_p` → nucleus sampling
* `top_k` → restrict to top-k tokens

### 🛠️ 9. Tools & Tool Behavior

* Tool definition and registration
* **Tool Choice** (automatic vs forced)
* Tool behavior configuration and error handling

### ✨ 10. Markdown Usage

* Proper structuring with **lists, images, and code blocks**
* Best practices for readable agent responses

### 📑 11. Data Schema

* Defining structured outputs using **Pydantic Models**
* Enforcing type safety with schemas
* Integration with `output_type`

### 🪝 12. Hooks

* **RunHooks** and **AgentHooks**
* Pre-run and post-run customizations
* Logging, analytics, and debugging with hooks

### ⚡ 13. Model Settings

* Configuring model behavior per run or globally
* Example: setting `max_tokens`, `temperature`

### 🔍 14. Tracing & Output Types

* **Tracing**: Understanding traces and spans
* **Output Types**: Forcing structured responses from agents
* Debugging agent execution with tracing

### 📝 15. Type Hinting

* Using Python **type hints** for better schema validation
* Integration with Pydantic and dataclasses

---

## 🛠️ Example Snippets

```python
from agents import Agent, Runner
from pydantic import BaseModel

class Weather(BaseModel):
    temperature: float
    city: str

agent = Agent(
    name="weather_agent",
    instructions="Provide weather updates",
    output_type=Weather
)

response = Runner.run(agent, input="Weather in Karachi")
print(response)
```

---

## 🚀 What I Learned

* How **contexts** affect data flow (local vs global)
* Writing **dynamic instructions** for flexible agents
* Using **guardrails** for safe input/output
* Implementing **handoffs** between multiple agents
* Fine-tuning responses with **temperature, top\_p, top\_k**
* Structuring responses with **schemas and type hints**
* Observing agent activity via **tracing**

---

## 📖 Next Steps

* Explore **Sessions** for long-running conversations
* Learn about **multi-agent collaboration patterns**
* Experiment with **custom tools and external APIs**

---

📌 *This README is part of my personal study notes while learning the OpenAI Agents SDK.*
