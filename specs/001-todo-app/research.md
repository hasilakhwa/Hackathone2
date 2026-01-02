# Research Notes: Phase I — In-Memory Python Console Todo App

**Date**: 2026-01-02
**Feature**: 001-todo-app
**Status**: Complete

## Research Summary

This research document captures all technical decisions, alternatives considered, and rationale for the Phase I in-memory Python console todo application.

## Decisions Made

### 1. Project Structure
- **Decision**: Use a modular Python package structure with distinct layers (models, services, cli)
- **Rationale**: Follows separation of concerns principle from constitution, enables testability, and provides clear boundaries between data model, business logic, and presentation
- **Alternatives considered**:
  - Single file script (rejected - doesn't follow modularity principle)
  - Flat directory structure (rejected - doesn't provide clear separation)

### 2. Python Version
- **Decision**: Target Python 3.13+
- **Rationale**: Uses latest Python features and ensures compatibility with future phases
- **Alternatives considered**:
  - Python 3.8+ (rejected - too conservative, missing modern features)
  - Python 3.12 (rejected - Python 3.13 is the latest stable)

### 3. Dependency Management
- **Decision**: Use `uv` for dependency management as specified in requirements
- **Rationale**: Fast, modern Python package installer and resolver that meets project requirements
- **Alternatives considered**:
  - pip + requirements.txt (rejected - less efficient than uv)
  - Poetry (rejected - uv was specified in requirements)

### 4. Testing Framework
- **Decision**: Use pytest for testing
- **Rationale**: Widely adopted, feature-rich testing framework with good support for parameterized tests and fixtures
- **Alternatives considered**:
  - unittest (rejected - more verbose, less flexible)
  - nose2 (rejected - pytest is more actively maintained)

### 5. Data Storage Approach
- **Decision**: In-memory storage using Python data structures (list/dict)
- **Rationale**: Meets Phase I constraint of no persistence, simple implementation, and fast access
- **Alternatives considered**:
  - File-based storage (rejected - violates in-memory only constraint)
  - SQLite in-memory (rejected - overkill for Phase I requirements)

### 6. CLI Framework
- **Decision**: Use Python's built-in input() function with a menu-driven approach
- **Rationale**: No external dependencies required, simple to implement and maintain
- **Alternatives considered**:
  - argparse (rejected - for command-line arguments, not interactive menu)
  - click (rejected - violates "no external dependencies" constraint)
  - rich (rejected - violates "no external dependencies" constraint)

### 7. Task Identification
- **Decision**: Use integer-based auto-incrementing IDs for tasks
- **Rationale**: Simple, efficient, and intuitive for users to reference tasks
- **Alternatives considered**:
  - UUID strings (rejected - too complex for simple console app)
  - String-based names (rejected - potential conflicts, harder to reference)

## Technical Unknowns Resolved

1. **Storage mechanism**: Resolved as in-memory Python list/dict
2. **Task identification**: Resolved as integer auto-incrementing IDs
3. **CLI interface**: Resolved as menu-driven with input() function
4. **Project structure**: Resolved as modular package with models/services/cli layers
5. **Testing approach**: Resolved as pytest with unit and integration tests

## Implementation Approach

The implementation will follow the architecture plan with three distinct layers:
1. **Models layer**: Task data model and in-memory storage
2. **Services layer**: Business logic for task operations (add, update, delete, etc.)
3. **CLI layer**: Interactive command-line interface

Each layer will have clear interfaces and responsibilities, following the separation of concerns principle from the constitution.