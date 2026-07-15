# Atlas RFCs

This directory contains Architecture Decision Records and Request for Comments (RFCs) for Atlas.

Atlas is not just an SDK or model router. Atlas is a control plane for model decisions.  
These RFCs define the core architecture, boundaries, interfaces, and data contracts before implementation begins.

## Purpose

The RFC process exists to help Atlas make deliberate architectural decisions before code is written.

We use RFCs to:

- define system boundaries clearly
- document major design decisions
- reduce ambiguity before implementation
- prevent architectural drift
- align product, architecture, and engineering

## Principles

Every RFC in Atlas should support at least one of these outcomes:

- improve quality
- reduce cost
- improve reliability

If a proposal does not improve one of those dimensions, it should be challenged.

## Rules

- Every major architectural decision should be documented in an RFC.
- Every RFC must explain which user pain it solves.
- Every RFC should clearly define goals and non-goals.
- Every RFC should keep Atlas aligned with its core identity: a control plane for model decisions.
- RFCs should be reviewed before implementation starts.

## RFC Status

Each RFC must include one of the following statuses:

- `Draft` — under discussion, not yet approved
- `Accepted` — approved and ready to guide implementation
- `Rejected` — considered but not approved
- `Superseded` — replaced by a newer RFC

## Recommended Reading Order

Read these RFCs in order:

1. `0001-architecture-foundation.md`
2. `0002-request-lifecycle.md`
3. `0004-data-model.md`
4. `0003-core-interfaces.md`

This order matters:

- Architecture Foundation defines what Atlas is.
- Request Lifecycle defines how Atlas behaves.
- Data Model defines the language and objects of the system.
- Core Interfaces define the contracts between components.

## RFC Template

Use the following structure for new RFCs:
```md
# RFC-XXXX: Title

Status: Draft
Owner: TBD
Last Updated: YYYY-MM-DD

## Summary

## Motivation

## User Pain

## Goals

## Non-Goals

## Proposal

## Architecture Impact

## Data Model Impact

## Interface Impact

## Error Handling

## Observability

## Alternatives Considered

## Open Questions

## Decision
