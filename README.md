# Atlas

<p align="center">
  <img src="./assets/logo.png" width="140" alt="Atlas Logo">
</p>

<h1 align="center">Atlas</h1>

<p align="center">
<b>The Control Plane for AI Model Decisions.</b>
</p>

<p align="center">
Stop rebuilding AI infrastructure.<br>
Start building AI products.
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square">

<img src="https://img.shields.io/badge/Status-Pre--Alpha-orange?style=flat-square">

<img src="https://img.shields.io/github/stars/KingGester/Atlas?style=flat-square">

<img src="https://img.shields.io/github/issues/KingGester/Atlas?style=flat-square">

<img src="https://img.shields.io/github/license/KingGester/Atlas?style=flat-square">

</p>

---

<p align="center">
<img src="./assets/hero.png" width="100%">
</p>

---

# The Problem

Building an AI product shouldn't require building an AI platform.

Yet every engineering team eventually rebuilds the same infrastructure.

* Model Routing
* Provider Abstraction
* Retry & Fallback
* Policy Enforcement
* Cost Control
* Observability
* Evaluation
* Governance

Different companies.

Different codebases.

The same infrastructure.

Engineering teams spend months rebuilding operational AI infrastructure instead of shipping products.

Atlas exists to standardize this layer.

---

# What is Atlas?

Atlas is **not another model wrapper.**

Atlas is **not another AI framework.**

Atlas is **not another agent library.**

Atlas is an **AI Control Plane**.

Atlas standardizes model routing, provider abstraction, policy enforcement, execution reliability and operational control through a single programmable control plane.

Instead of forcing every company to build an internal AI platform, Atlas provides the missing infrastructure layer.

---

# Vision

Modern software has operating systems.

Cloud computing has Kubernetes.

Microservices have service meshes.

AI applications need a control plane.

Atlas aims to become the operational layer that sits between AI applications and model providers.

---

# What Atlas Solves

| Problem               | Atlas |
| --------------------- | :---: |
| Provider Lock-in      |   ✅   |
| Manual Model Routing  |   ✅   |
| Provider Abstraction  |   ✅   |
| Policy Enforcement    |   ✅   |
| Retry & Fallback      |   ✅   |
| Cost Control          |   ✅   |
| Routing Observability |   ✅   |
| Unified API           |   ✅   |

---

# Why Atlas?

Most existing tools solve only one piece of the problem.

| Tool       | Primary Focus         |
| ---------- | --------------------- |
| OpenAI SDK | Single Provider       |
| LiteLLM    | Provider Abstraction  |
| OpenRouter | Unified API Gateway   |
| LangGraph  | Agent Workflow        |
| CrewAI     | Multi-Agent Framework |
| Atlas      | AI Control Plane      |

Atlas is designed to orchestrate operational decisions across providers instead of becoming another framework.

---

# Architecture

```text
                        Application
                              │
                              ▼
                         Atlas SDK
                              │
                              ▼
                        Atlas Core
        ┌──────────────────────────────────────────┐
        │                                          │
        │  Policy Engine                           │
        │  Router                                  │
        │  Tracing                                 │
        │  Metrics                                 │
        │  Execution Context                       │
        │                                          │
        └──────────────────────────────────────────┘
                              │
                              ▼
                     Provider Adapter
                              │
      ┌───────────┬────────────┬────────────┬────────────┐
      ▼           ▼            ▼            ▼
   OpenAI     Anthropic      Gemini      Ollama
```

---

# Design Principles

Atlas follows several core engineering principles.

* Interface First
* Provider Agnostic
* Single Responsibility
* Explicit Ownership
* Deterministic Execution
* Reliability over Cleverness
* Replaceable Components
* RFC-driven Architecture

---

# Request Lifecycle

```text
Application
      │
      ▼
Atlas SDK
      │
      ▼
Atlas Core
      │
      ▼
Policy Engine
      │
      ▼
Router
      │
      ▼
Provider Adapter
      │
      ▼
Model Provider
      │
      ▼
Normalized Response
      │
      ▼
Application
```

Every request follows the same deterministic lifecycle.

---

# Quick Example

```python
from atlas import Atlas

client = Atlas()

response = client.chat(
    model="atlas://coding",
    messages=[
        {
            "role": "user",
            "content": "Optimize this Python function."
        }
    ]
)

print(response.text)
```

Future migration from existing SDKs should require little more than changing the import and the endpoint.

---

# Core Principles

## Quality

Choose the best model for the workload.

---

## Cost

Optimize successful outcomes instead of token usage.

---

## Reliability

Production-first architecture with predictable execution.

---

## Observability

Every routing decision should be explainable.

---

## Extensibility

Every major subsystem should be replaceable.

---

# RFC Driven Development

Atlas follows an RFC-based engineering process.

Current RFCs:

| RFC      | Description       |
| -------- | ----------------- |
| RFC-0001 | Product Vision    |
| RFC-0002 | Request Lifecycle |
| RFC-0003 | Core Interfaces   |
| RFC-0004 | Core Data Model   |

Future architectural changes are proposed through RFCs before implementation.

---


---

# Current Milestone

## Atlas Alpha

### Completed

* ✅ Market Research
* ✅ Product Vision
* ✅ Architecture Design
* ✅ RFC-0001
* ✅ RFC-0002
* ✅ RFC-0003
* ✅ RFC-0004
* ✅ SDK Architecture

### In Progress

* ⏳ Core Models
* ⏳ Atlas Core
* ⏳ Provider Interface
* ⏳ Mock Provider
* ⏳ Static Router

### Upcoming

* Virtual Models
* Provider Abstraction
* OpenAI Adapter
* Policy Engine
* Routing Engine

---

# Roadmap

## Phase 1 — Foundation

* RFCs
* Core Architecture
* SDK
* Core Data Model

---

## Phase 2 — Alpha

* Virtual Models
* Provider Abstraction
* OpenAI Adapter
* Static Router
* Mock Provider

---

## Phase 3 — Production Foundation

* Policy Engine
* Retry & Fallback
* Tracing
* Metrics
* Reliability
* Cost Policies

---

## Phase 4 — Intelligence

* Smart Routing
* Evaluation Engine
* Routing Analytics
* Model Registry
* Learned Routing

---

## Phase 5 — Enterprise

* Governance
* Multi-Tenant Policies
* Audit Trail
* Budget Enforcement
* Enterprise APIs

---

# Current Status

Atlas is under active development.

Current focus:

* Building the core execution pipeline.
* Establishing stable interfaces.
* Creating a production-ready SDK.
* Preparing the first Alpha release.

The public API is **not yet stable**.

Breaking changes are expected before v1.0.

---

# Philosophy

Atlas is built around one simple belief.

> AI engineers should build AI products.

> They should not spend months rebuilding the same operational AI infrastructure.

---

# Contributing

Atlas is being built in public.

We welcome:

* RFC proposals
* Architecture reviews
* Bug reports
* Documentation improvements
* Feature discussions
* Pull Requests

Please read **CONTRIBUTING.md** before opening an Issue or Pull Request.

---

# License

Apache-2.0 license

---

# Acknowledgements

Atlas is inspired by the engineering practices behind modern infrastructure projects such as Kubernetes, Envoy, Terraform and other cloud-native systems, while focusing on the operational challenges unique to AI applications.

---

<p align="center">

Built with ❤️ for the AI Engineering community and thank you.

</p>
