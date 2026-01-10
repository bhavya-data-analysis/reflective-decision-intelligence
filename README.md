# Reflective Decision Intelligence (RDI)

Reflective Decision Intelligence (RDI) is a system for **evaluating decision quality and cognitive risk**.

It does not tell people what to do.  
It does not give advice.  
It does not judge decisions by outcomes.

RDI looks at **how a decision is formed** — how clear the thinking is, where reasoning breaks down, and how cognition changes when someone is forced to slow down and reflect.

Questions are only the entry point.  
The goal is to turn human decisions into **structured, comparable objects** that can be measured and learned from over time.

---

## Core Idea

Outcomes are noisy and often misleading.

A decision can fail despite good reasoning, and succeed despite bad reasoning.  
RDI focuses on the **structure of the decision itself**:

- Is the decision clearly defined?
- What cognitive failures are present?
- Is the thinking stable or fragile under pressure?
- Does reflection actually improve the reasoning, or make it worse?

The system treats human thinking as something that can be **observed, compared, and improved**, not something to be generated.

---

## What This Is Not

RDI is not:
- a chatbot  
- a reflection or journaling app  
- a questionnaire  
- an advice engine  

The system never decides for the user.  
It evaluates **decision formation**, not decision content.

---

## What Exists Right Now

### Level 1 — Structured Reflection
- Decision clarity classification:
  - `NONE / EMERGING / DEFINED / COMMITTED`
- High-stakes detection (career, income, health, relationships, identity, immigration)
- Cognitive failure detection:
  - deflection
  - overconfidence
  - emotional pressure
  - irritation / resistance
  - low specificity
- Follow-up questions chosen based on cognitive state
- Local-first CLI with a modular core

---

### Level 2 — Comparison & Patterning
- Decisions are comparable across:
  - time
  - different decisions
- The system tracks:
  - recurring cognitive patterns
  - reflection depth trends
  - decision fragility over time

This is behavior modeling, not conversation.

---

### Level 3 — Prediction
- Baseline ML model (TF-IDF + Logistic Regression)
- Predicts decision fragility **before** reflection starts
- ML is kept outside the core system
- Rule-based and ML predictions are explicitly compared

This adds anticipation without replacing judgment.

---

### Level 4 — Measuring Improvement and Control

#### Level 4.1 — Reflection Effect (Complete)
The system computes:
- `reflection_effect ∈ {helped, no_change, hurt}`

This answers a simple but important question:  
**Did reflection actually improve decision quality?**

This is the first true control signal in the system.

---

#### Level 4.2 — Intervention Attribution (Complete)
- Questions are treated as **interventions**
- Changes in decision fragility are attributed to specific questions
- The system logs which interventions help, hurt, or produce no change
- Effects are tracked under different cognitive states

Reflection is no longer subjective — it is measurable.

---

#### Level 4.3 — Measurement-Aware Probing (Complete)
- The system adapts **within a session** based on observed effects
- Interventions that empirically worsen thinking are not repeated
- Neutral or helpful probes are allowed to continue

This introduces **control without learning a policy**.

---

## How Machine Learning Is Used

ML is used to:
- replace brittle heuristics over time
- predict cognitive risk
- estimate decision fragility
- model intervention effects

ML is not used to:
- generate advice
- decide outcomes
- replace human judgment

The goal is measurement and learning — not automation.

---

## Why This Project Exists

Most systems optimize answers.

RDI focuses on **decision quality under uncertainty** — something people experience constantly but rarely measure.

This project is intentionally built slowly:
- the same system grows deeper over time
- new capabilities are added only when they are earned
- explanations remain local and inspectable
  
It is an attempt to build a **learning system around human decision-making**.

---

## Status

Current state: **Level 4 complete (4.1–4.3)**  

**Next phase beginning:**  
**Level 5 — Intervention Learning (RL-lite)**  
Learning an intervention policy from observed `(state, question, effect)` data — without advice, without outcome optimization, and without replacing human judgment.

---
## 👤 Author
**Bhavya Pandya**  
LinkedIn: https://www.linkedin.com/in/bhavya-91p/
