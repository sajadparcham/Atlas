
This glossary defines the canonical language of Atlas.

Atlas is a control plane for model decisions.  
To keep the architecture consistent, these terms should be used precisely and consistently across RFCs, code, docs, and product messaging.

## Why This Exists

Most architecture problems start as language problems.

If the team uses the same word to mean different things, the implementation will drift.  
This glossary exists to create a shared vocabulary for Atlas.

## Core Terms

## Atlas

Atlas is a control plane for model decisions.

It standardizes how model requests are evaluated, routed, executed, controlled, and observed across providers.

Atlas is not a model provider.  
Atlas is not a model itself.  
Atlas is not just a router.

## Atlas Core

Atlas Core is the main execution and control runtime of Atlas.

It is responsible for:

- receiving standardized requests
- invoking policy evaluation
- invoking routing
- coordinating provider execution
- collecting traces, metrics, logs, and cost data

Atlas Core does not generate model responses by itself.

## Control Plane

The control plane is the part of the system that makes decisions about execution.

In Atlas, the control plane determines:

- what is allowed
- what is preferred
- where a request should run
- how execution is observed

## Data Plane

The data plane is the part of the system that performs the actual request execution against a provider.

In Atlas, provider adapters sit close to the data plane boundary.

## Virtual Model

A Virtual Model is a stable logical model name exposed to users.

It does not necessarily map to one fixed provider model.  
Instead, Atlas resolves it at runtime based on policy, routing rules, and available candidates.

Example:

- `atlas/smart-chat`
- `atlas/fast-chat`
- `atlas/cheap-chat`

## Provider

A Provider is an external system that offers model inference APIs.

Examples include:

- OpenAI
- Anthropic
- Google
- Azure OpenAI

A provider may expose one or more models.

## Model

A Model is a concrete inference endpoint or model offering exposed by a provider.

Examples:

- `gpt-4.1`
- `claude-3-5-sonnet`
- `gemini-1.5-pro`

A model has capabilities, cost characteristics, latency characteristics, and operational behavior.

## Provider Adapter

A Provider Adapter is the integration layer between Atlas and a specific provider.

It is responsible for:

- translating Atlas requests into provider-specific API calls
- translating provider responses into Atlas-standard responses
- normalizing provider errors
- exposing provider metadata in a standard way

A Provider Adapter does not make routing or policy decisions.

## Router

The Router chooses the best execution target for a request.

It evaluates candidate models, providers, or regions against:

- constraints
- objectives
- capabilities
- cost considerations
- latency considerations

The Router returns a decision.  
It does not execute the request itself.

## Route Decision

A Route Decision is the output of the Router.

It typically includes:

- selected target
- candidate set
- rejected candidates
- reason codes
- decision metadata

A Route Decision explains why Atlas chose a specific execution path.

## Policy

A Policy is a declarative rule that defines what is allowed, preferred, or forbidden.

Policies may express things like:

- provider allowlists
- region restrictions
- budget limits
- latency preferences
- capability requirements

Policies should be declarative, not hardcoded in execution logic.

## Policy Engine

The Policy Engine interprets policies and converts them into executable constraints and objectives.

It does not choose the final route directly.  
It defines the rules within which routing happens.

## Constraint

A Constraint is a hard requirement that must be satisfied.

If a candidate violates a constraint, it must be excluded.

Examples:

- provider must be OpenAI
- region must be EU
- tool calling must be supported
- max cost per request must not exceed a threshold

## Objective

An Objective is a preferred optimization target, not a hard rule.

Examples:

- minimize cost
- minimize latency
- maximize quality
- prefer lower-risk providers

Objectives influence ranking, but do not behave like hard filters.

## Capability

A Capability is a feature or property that a model or provider supports.

Examples:

- chat
- JSON output
- tool calling
- image input
- streaming
- function calling
- long context

Capabilities are used in both policy evaluation and routing.

## Candidate

A Candidate is a possible execution target considered during routing.

A candidate may represent:

- a model
- a provider-model pair
- a provider-model-region combination

Candidates are evaluated before one target is selected.

## Execution Target

An Execution Target is the final destination chosen for the request.

It may include:

- provider
- model
- region
- adapter

This is the concrete target that will actually execute the request.

## Chat Request

A Chat Request is the standardized Atlas request for conversational model execution.

It may include fields such as:

- virtual model
- messages
- tools
- policy context
- budget context
- tenant
- metadata
- trace context
- objectives

The exact schema belongs in the Data Model RFC.

## Response

A Response is the standardized Atlas output returned after execution.

It includes the normalized model output and related execution metadata.

A Response should be provider-neutral from the caller's perspective.

## Trace

A Trace is the structured record of what happened during request processing.

A trace may include:

- request metadata
- policy evaluation results
- route decision
- provider execution details
- latency measurements
- cost measurements
- error information

Trace exists for observability, debugging, evaluation, and governance.

## Reason Code

A Reason Code is a machine-readable explanation attached to a routing or policy decision.

Examples:

- `capability_missing`
- `provider_blocked`
- `budget_exceeded`
- `latency_preferred`
- `lowest_cost_selected`

Reason codes help make decisions explainable.

## Tenant

A Tenant is the logical customer, team, project, or workspace on whose behalf a request is executed.

Policies, budgets, and routing behavior may vary by tenant.

## Budget

Budget is the limit or spending context applied to model execution.

Budget may be expressed at different levels, such as:

- per request
- per tenant
- per environment
- per time window

Budget enforcement may evolve over time; v0.1 should keep it simple.

## Reliability

Reliability refers to Atlas's ability to execute requests consistently and recover safely from failures.

This may include:

- timeout handling
- fallback behavior
- retry strategy
- provider health awareness

Reliability is a system concern, not just a provider concern.

## Observability

Observability is the ability to inspect and understand how Atlas behaves in production.

In Atlas, observability includes:

- logs
- metrics
- traces
- cost visibility
- route visibility
- policy visibility

## Plugin

A Plugin is an extendable Atlas component that adds a focused control-plane capability without changing the identity of Atlas Core.

Examples may include:

- Router
- Policy Engine
- Budget
- Reliability
- Eval
- Trace
- Registry
- Governance

The exact plugin model must be defined in a dedicated RFC.

## Registry

A Registry is the source of truth for known models, providers, capabilities, and related metadata.

In v0.1, the registry may be static or curated rather than dynamic.

## Governance

Governance refers to organizational control over how models may be used.

Examples include:

- approved providers
- restricted regions
- disallowed capabilities
- compliance constraints

Governance is broader than routing and broader than provider integration.

## Non-Goals

A Non-Goal is something Atlas intentionally does not solve in a given version.

Defining non-goals is a first-class design activity.  
They protect focus and reduce accidental scope creep.

## Canonical Distinctions

Use these distinctions consistently:

- Atlas is not a provider
- Atlas Core is not the Router
- Router does not execute requests
- Policy Engine does not choose the final target
- Provider Adapter does not enforce policy
- Constraints are hard requirements
- Objectives are optimization preferences
- Virtual Models are logical names, not fixed provider models

## Temporary Terms

The following terms may be used during design, but should be stabilized through RFCs before implementation depends on them heavily:

- Execution Profile
- Decision Context
- Provider Health
- Reliability Policy
- Budget Policy

## Notes

If a term becomes important in code, API, or documentation, it should be added here before it spreads informally.