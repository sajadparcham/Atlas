# RFC-0003: Core Interfaces

Status: Draft

Authors: Atlas Team

Owner: CTO

Created: 2026-07-17

Last Updated: 2026-07-17

Target Release: v0.1

Related RFCs:
- RFC-0001 Product Vision
- RFC-0002 Request Lifecycle

---

# Summary

This RFC defines the core architectural contracts of Atlas.

Rather than specifying implementation details, this document defines the responsibilities, ownership boundaries, and interaction rules between the major components of the Atlas Control Plane.

These interfaces are intended to remain stable even if the internal implementation changes over time.

---

# Motivation

Atlas is not an SDK.

Atlas is not an LLM wrapper.

Atlas is a control plane responsible for model decisions.

To keep the architecture modular, replaceable, and maintainable, every component must expose a well-defined contract with a single responsibility.

Without explicit contracts:

- responsibilities become ambiguous
- coupling increases
- implementations become difficult to replace
- testing becomes harder
- plugin architecture becomes impossible

---

# Design Principles

The following principles apply to every core interface.

## Interface First

Components communicate only through contracts.

Implementation details remain private.

---

## Single Responsibility

Every component has one primary responsibility.

Responsibilities must never overlap.

---

## Replaceability

Every component should be replaceable without affecting other components.

---

## Dependency Inversion

High-level components depend on contracts, not implementations.

---

## Explicit Ownership

Every piece of data has exactly one owner.

---

## Stateless Components

Whenever possible, components remain stateless.

Execution state belongs to Atlas Core.

---

# Core Components

Atlas v0.1 contains five primary interfaces.

- SDK
- Atlas Core
- Policy Engine
- Router
- Provider Adapter

---

# SDK Contract

## Responsibility

Translate application requests into Atlas requests.

Translate Atlas responses back into application responses.

## Owns

- SDK configuration
- Client API

## Must

- Validate user input
- Normalize requests
- Return standardized responses

## Must Not

- Execute routing
- Execute provider logic
- Apply policies

---

# Atlas Core Contract

## Responsibility

Coordinate the complete request lifecycle.

Atlas Core is the only orchestration entry point.

## Owns

- Request Context
- Execution State
- Trace
- Metrics
- Lifecycle

## Must

- Build execution context
- Invoke Policy Engine
- Invoke Router
- Invoke Provider Adapter
- Record traces
- Return standardized responses

## Must Not

- Decide routing
- Execute provider-specific logic
- Define policies

---

# Policy Engine Contract

## Responsibility

Convert declarative policies into executable constraints.

## Owns

- Policy evaluation

## Input

- Request Context

## Output

- Constraints
- Objectives
- Execution Rules

## Must

- Validate policies
- Generate routing constraints

## Must Not

- Select providers
- Rank models
- Execute requests

---

# Router Contract

## Responsibility

Select the best execution target.

## Owns

- Route Decision

## Input

- Request Context
- Candidate Targets
- Constraints

## Output

- Route Decision

## Must

- Evaluate eligible candidates
- Produce deterministic routing decisions
- Explain routing decisions

## Must Not

- Execute requests
- Retry providers
- Apply policies
- Modify responses

---

# Provider Adapter Contract

## Responsibility

Execute requests against external providers.

## Owns

- Provider Translation
- API Compatibility

## Input

- Provider Request

## Output

- Provider Response

## Must

- Translate requests
- Normalize responses
- Normalize provider errors

## Must Not

- Perform routing
- Evaluate policies
- Modify routing decisions

---

# Component Dependencies

```
SDK
 │
 ▼
Atlas Core
 │
 ├───────────────┐
 ▼               ▼
Policy Engine   Router
                    │
                    ▼
           Provider Adapter
                    │
                    ▼
              External Provider
```

Dependencies are strictly one-directional.

No component may bypass Atlas Core.

---

# Data Ownership

| Data | Owner |
|------|-------|
| Request Context | Atlas Core |
| Execution State | Atlas Core |
| Route Decision | Router |
| Constraints | Policy Engine |
| Provider Request | Provider Adapter |
| Provider Response | Provider Adapter |
| Trace | Atlas Core |
| Metrics | Atlas Core |

---

# Invariants

The following rules must always remain true.

- Atlas Core is the only orchestration entry point.
- Router never executes requests.
- Router never retries providers.
- Policy Engine never selects providers.
- Provider Adapter never changes routing decisions.
- SDK never contains routing logic.
- Every request has exactly one Request Context.
- Every execution produces exactly one Trace.

These invariants are architecture rules and must never be violated.

---

# Extension Points

The following interfaces may be extended in future releases.

- Budget Engine
- Reliability Engine
- Evaluation Engine
- Registry
- Governance
- Memory
- Streaming
- Agent Runtime

Extensions must integrate through Atlas Core.

---

# Stability

The interfaces defined in this RFC are considered Stable.

Internal implementations may change.

Interface contracts must remain backward compatible whenever possible.

Breaking changes require a new RFC.

---

# Future Work

Future RFCs will define:

- Request Data Model
- Error Model
- Plugin Architecture
- Event System
- Streaming
- Reliability
- Budget Enforcement
- Evaluation Pipeline

These topics are intentionally outside the scope of RFC-0003.