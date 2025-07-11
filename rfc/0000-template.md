# RFC: `<Title>`

Provide a one paragraph description of the RFC.

## Change Log

This text can be modified over time. Add a change log entry for every change made to the RFC.

- YYYY-MM-DD: Initial RFC created
- YYYY-MM-DD: Updated RFC item (x) based on feedback from the community

## Motivation

Why are we doing this? What use cases does it support? What is the expected outcome?

## Technology Background

Explain and provide references to technologies that are relevant to the proposal. In particular, an explanation of
how hardware or existing technologies influence the design of the proposal. This section should be written for a
technical audience and should not assume that the reader is familiar with the technology.

## Goals

Provide a succinct ordered list of the the goals for this change/feature. It should be easy to associate design choices with goals.

## Requirements

Provide a succinct ordered list of the requirements for this change/feature. It should be easy to associate design choices with
requirements. This does not need to be exhaustive, but should cover the most important requirements that influenced
design decisions.

## Unresolved Questions

- What parts of the design do you expect to resolve through the RFC process before this gets merged?
- What related issues do you consider out of scope for this RFC that could be addressed in the future independently of
  the solution that comes out of this RFC?

## Prior Art

Briefly describe and/or link to existing documentation about the same functionality in existing code or similar processes. This only needs to be present if such functionality exists and it was particularly influential in the design
of this RFC or this RFC deviates in a significant way from the existing implementation that feature users should be
aware of.

## Alternatives

- Why is this design the best in the space of possible designs?
- What other designs have been considered and what is the rationale for not choosing them?

## Rust Code Design

Include diagrams, process flows, code snippets, and other design artifacts that are relevant to the proposal. If relevant, all public facing
APIs should be included in this section. Rationale for the interfaces chosen should be included here as relevant.

## Guide-Level Explanation

For RFCs affecting code design, explain the proposal as if it was already included in code documentation and you were teaching it to another Rust
programmer. That generally means:

- Introducing new named concepts
- Explaining the feature largely in terms of examples
- Explaining how Rust programmers should *think* about the feature, and how it should impact the way they interact
  with this feature. It should explain the impact as concretely as possible
- If applicable, describe the differences between teaching this to existing firmware programmers and those learning
  the feature the first time in the Rust codebase
