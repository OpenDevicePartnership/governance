# RFC: `Subsystem Ownership for EC Repositories`

EC repositories currently all list the ec-code-owners team as the code owner, and ec-code-owners has write permission to all the EC repositories. The proposal is to create more EC subsystem teams, make these EC subsystem teams code owners of their subsystem code, and give these subsystem teams write permission to the relevant repositories. EC Subsystem teams can also pull in ec-code-owners for code review as needed to get the 2 approvals required.

## Change Log

- 2025-07-28: Initial RFC created

## Motivation

To give EC subsystem teams more autonomy over their code and to make sure a subject matter expert is always pulled-in for review.

## Technology Background

Not applicable

## Goals

See motivation

## Requirements

Each subsystem should list at least 2 persons.

## Unresolved Questions

Whether to make all the EC subsystem teams child teams of ec-code-owners, the child teams will inherit the write permission to all EC repositories.

## Prior Art

Linux kernel maintainer model where each file has a maintainer. Maintainer owns the file and brings in relevant reviewers as needed for PRs.

## Alternatives

Not applicable

## Rust Code Design

Not applicable

## Guide-Level Explanation

Not applicable
