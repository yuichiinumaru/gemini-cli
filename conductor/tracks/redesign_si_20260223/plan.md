# Implementation Plan: System Instruction Re-design

## Phase 1: Analysis & Scaffolding

- [x] Task: Analyze current System Instruction (SI) and identify modular
      components.
  - [x] Map out existing workflows: Software Engineering, New Applications,
        Operational Guidelines.
  - [x] Audit tool usage instructions for redundancies.
- [x] Task: Define the new modular structure.
  - [x] Design the "Core SI" skeleton.
  - [x] Define the interface for skill-based workflow injection.
- [x] Task: Set up the testing environment for SI variations.
  - [x] Create a utility to swap SI versions during local development/testing.
  - [x] Identify key evals to use for baseline comparison.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Analysis &
      Scaffolding' (Protocol in workflow.md)

## Phase 2: Modularization & Skill Migration

- [x] Task: Extract Software Engineering workflow to a dedicated skill.
  - [x] Create `packages/core/src/skills/builtin/software-engineering/`.
  - [x] Port the logic from SI to the new skill as an Instruction Delta.
  - [x] Write unit tests for the skill (covered by existing tests).
- [x] Task: Extract New Application workflow to a dedicated skill.
  - [x] Create `packages/core/src/skills/builtin/new-application/`.
  - [x] Port the logic from SI to the new skill as an Instruction Delta.
  - [x] Write unit tests for the skill (covered by existing tests).
- [x] Task: Refactor tool usage instructions.
  - [x] Simplify tool definitions in the SI.
  - [x] Improve descriptions for high-use tools (e.g., `grep_search`,
        `read_file`, `run_shell_command`).
- [x] Task: Conductor - User Manual Verification 'Phase 2: Modularization &
      Skill Migration' (Protocol in workflow.md)

## Phase 3: Core SI Implementation

- [x] Task: Implement the new, minimized Core SI for `gemini-3-flash-preview`.
      (High Priority)
  - [x] Rewrite the SI to be capability-driven and concise (Ultra-Minimal).
  - [x] Implement the logic to dynamically inject active skills into the prompt.
- [x] Task: Integrate the new skills into the harness.
  - [x] Update `packages/core/src/prompts/promptProvider.ts` to handle
        skill-based prompt construction.
- [x] Task: (Low Priority) Implement the model-specific SI selection logic.
  - [x] Update prompt providers to select SI based on the model family (Gemini 3
        Flash Preview).
- [x] Task: Conductor - User Manual Verification 'Phase 3: Core SI
      Implementation' (Protocol in workflow.md)

## Phase 4: Validation & Optimization

- [x] Task: Run evaluations focused on `gemini-3-flash-preview`.
  - [x] Execute relevant evals and compare against baseline.
  - [x] Use evals as indicators of quality/behavior; specific failures are
        acceptable if the behavior isn't explicitly mandated by the SI.
  - [x] Prioritize overall experience and what works best for the model.
- [x] Task: Optimize for token usage and performance.
  - [x] Perform final token count audit.
  - [x] Refine prompts for maximum clarity with minimum tokens.
- [x] Task: Conductor - User Manual Verification 'Phase 4: Validation &
      Optimization' (Protocol in workflow.md)
