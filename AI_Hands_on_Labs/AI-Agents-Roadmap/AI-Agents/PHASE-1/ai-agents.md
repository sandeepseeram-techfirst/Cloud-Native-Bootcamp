# ✅ Phase 1: AI Agents – Theory Deep Dive

---

## 🔹 1. What Exactly Is an AI Agent?

An **AI agent** is a system that:
- **Perceives** its environment (via inputs).
- **Thinks** using logic, rules, or learned behavior.
- **Acts** to achieve specific goals.

## 🔹 2. The AI Agent Loop

[Perception] → [Reasoning / Decision-Making] → [Action] → (Feedback / Learning)

### Example:
**Input**: "Turn on the lights"  
**Agent**:
- Understands the command (Perception)
- Decides what to do (Reasoning)
- Calls a smart-home API (Action)

---

## 🔹 3. Components of an AI Agent

| Component      | Description |
|----------------|-------------|
| **Sensor/Input**     | Receives data (text, image, API, sensor) |
| **Perception** | Interprets the input |
| **Reasoning / Planning** | Chooses actions based on logic, ML, rules |
| **Memory**     | Stores context or history |
| **Action**     | Executes a function, command, or output |

---

## 🔹 4. Agent Environments

Agents operate in **environments**, which can be:

- **Fully Observable**: The agent has access to all relevant data (e.g., chess).
- **Partially Observable**: Some data is hidden or uncertain (e.g., autonomous driving).
- **Deterministic**: Actions have predictable results.
- **Stochastic**: Outcomes are uncertain.
- **Episodic**: Each input is independent (e.g., spam filter).
- **Sequential**: Actions affect future states (e.g., chatbots, games).

---

## 🔹 5. Types of AI Agents

| Type                        | Description                                | Example                        |
|-----------------------------|--------------------------------------------|--------------------------------|
| **Simple Reflex Agent**     | Responds to current input using rules      | Basic rule-based chatbot       |
| **Model-Based Reflex Agent**| Maintains internal state                   | Self-driving car logic         |
| **Goal-Based Agent**        | Uses goal-driven logic for decision-making | Pathfinding or game AI         |
| **Utility-Based Agent**     | Maximizes a utility function               | Recommendation systems         |
| **Learning Agent**          | Learns and improves over time              | GPT, AlphaGo, ML models        |

---

## 🔹 6. Reactive vs Deliberative Agents

| Category          | Description                                                  |
|------------------|--------------------------------------------------------------|
| **Reactive Agent**     | Quick responses, no internal model or planning              |
| **Deliberative Agent** | Thinks ahead, plans based on outcomes, slower but smarter |

---