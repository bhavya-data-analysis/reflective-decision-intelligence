# Reflective Decision Intelligence (RDI)
### A system for measuring decision quality and cognitive risk - not giving advice.

![Status](https://img.shields.io/badge/Status-Level%204%20Complete-brightgreen?style=flat)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20CLI%20%7C%20ML-3776AB?style=flat&logo=python&logoColor=white)
![Approach](https://img.shields.io/badge/Approach-Rule--based%20%2B%20ML-orange?style=flat)

---

## What It Does

RDI evaluates **how a decision is formed** - not whether it's right.

It doesn't tell you what to do. It doesn't judge by outcomes. It measures the structure of your thinking: where reasoning breaks down, how cognition shifts under pressure, and whether reflection actually helps or makes things worse.

Questions are the entry point. The real output is a **structured, comparable decision object** - something that can be measured, tracked, and learned from over time.

---

## The Core Insight

Outcomes are noisy. A decision can fail despite good reasoning, and succeed despite bad reasoning.

RDI cuts through that by focusing on the decision itself:

- Is it clearly defined?
- What cognitive failures are present?
- Is the thinking stable or fragile?
- Does reflection improve reasoning - or entrench it?

Human thinking, treated as something **observable and measurable**.

---

## What This Is Not

- Not a chatbot
- Not a journaling or reflection app
- Not an advice engine
- Not a questionnaire

The system never decides for the user. It evaluates **decision formation**, not decision content.

---

## System Architecture - 5 Levels

### Level 1 - Structured Reflection ✅
The foundation. Every decision is analyzed before anything else runs.

- **Clarity classification:** `NONE -> EMERGING -> DEFINED -> COMMITTED`
- **High-stakes detection:** career, income, health, relationships, identity, immigration
- **Cognitive failure detection:** deflection, overconfidence, emotional pressure, irritation, low specificity
- Follow-up questions chosen based on detected cognitive state
- Local-first CLI with a modular, inspectable core

---

### Level 2 - Comparison & Patterning ✅
Decisions become comparable - across time and across different choices.

- Recurring cognitive pattern tracking
- Reflection depth trends over sessions
- Decision fragility measured longitudinally

This is behavior modeling, not conversation history.

---

### Level 3 - Prediction ✅
Baseline ML layer (TF-IDF + Logistic Regression) that predicts decision fragility **before** reflection begins.

- ML sits outside the rule-based core - kept deliberately separate
- Rule-based and ML predictions are explicitly compared, not merged
- Anticipation without replacing judgment

---

### Level 4 - Measurement & Control ✅

#### 4.1 - Reflection Effect
Computes `reflection_effect ∈ {helped, no_change, hurt}`

The first true control signal: **did slowing down actually help?**

#### 4.2 - Intervention Attribution
Questions are treated as interventions. Changes in fragility are attributed to specific probes, logged by cognitive state.

Reflection is no longer subjective - it's measurable.

#### 4.3 - Measurement-Aware Probing
The system adapts **within a session** based on observed effects. Interventions that empirically worsen thinking are not repeated.

Control without learning a policy.

---

### Level 5 - Intervention Learning (In Progress) 🔄
Learning an intervention policy from observed `(state, question, effect)` data.

RL-lite. No advice. No outcome optimization. No replacing human judgment.

---

## How ML Is Used

| Used for | Not used for |
|----------|-------------|
| Replacing brittle heuristics over time | Generating advice |
| Predicting cognitive risk | Deciding outcomes |
| Estimating decision fragility | Replacing human judgment |
| Modeling intervention effects | |

The goal is measurement and learning - not automation.

---

## Why This Exists

Most systems optimize answers.

RDI focuses on **decision quality under uncertainty** - something people experience constantly but rarely measure. The system grows intentionally: new capabilities are added only when earned, explanations stay local and inspectable.

It's an attempt to build a learning system around human decision-making - from the inside out.

---

**Bhavya Pandya** · [LinkedIn](https://www.linkedin.com/in/bhavya-91p/) · M.S. Data Analytics, LIU Brooklyn
