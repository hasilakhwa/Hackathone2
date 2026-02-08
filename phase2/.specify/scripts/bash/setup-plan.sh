#!/bin/bash

# Setup implementation plan for a feature

# Parse arguments
JSON_OUTPUT=false
while [[ $# -gt 0 ]]; do
  case $1 in
    -j|--json)
      JSON_OUTPUT=true
      shift
      ;;
    *)
      shift
      ;;
  esac
done

# Get current branch - check environment variable first
if [ -n "$SPECIFY_FEATURE" ]; then
    CURRENT_BRANCH="$SPECIFY_FEATURE"
elif [ -d .git ]; then
    CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || echo "main")
else
    # For non-git repos, try to find the latest feature directory
    if [ -d "specs" ]; then
        LATEST_FEATURE=$(ls -d specs/*/ 2>/dev/null | grep -E 'specs/[0-9]{1,3}-' | sort -t'/' -k3 | tail -1 | xargs basename)
        if [ -n "$LATEST_FEATURE" ]; then
            CURRENT_BRANCH="$LATEST_FEATURE"
        else
            CURRENT_BRANCH="main"
        fi
    else
        CURRENT_BRANCH="main"
    fi
fi

# Get repo root
if [ -d .git ]; then
    REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
else
    REPO_ROOT=$(pwd)
fi

# Define paths
FEATURE_DIR="$REPO_ROOT/specs/$CURRENT_BRANCH"
FEATURE_SPEC="$FEATURE_DIR/spec.md"
IMPL_PLAN="$FEATURE_DIR/plan.md"
TASKS="$FEATURE_DIR/tasks.md"
RESEARCH="$FEATURE_DIR/research.md"
DATA_MODEL="$FEATURE_DIR/data-model.md"
QUICKSTART="$FEATURE_DIR/quickstart.md"
CONTRACTS_DIR="$FEATURE_DIR/contracts"

# Ensure the feature directory exists
mkdir -p "$FEATURE_DIR"

# Copy plan template if it exists, otherwise create empty file
TEMPLATE="$REPO_ROOT/.specify/templates/plan-template.md"
if [ -f "$TEMPLATE" ]; then
    cp "$TEMPLATE" "$IMPL_PLAN"
    echo "Copied plan template to $IMPL_PLAN"
else
    echo "Plan template not found at $TEMPLATE"
    # Create a basic plan file
    touch "$IMPL_PLAN"
fi

# Output results
if [ "$JSON_OUTPUT" = true ]; then
    cat <<EOF
{"FEATURE_SPEC":"$FEATURE_SPEC","IMPL_PLAN":"$IMPL_PLAN","SPECS_DIR":"$FEATURE_DIR","BRANCH":"$CURRENT_BRANCH"}
EOF
else
    echo "FEATURE_SPEC: $FEATURE_SPEC"
    echo "IMPL_PLAN: $IMPL_PLAN"
    echo "SPECS_DIR: $FEATURE_DIR"
    echo "BRANCH: $CURRENT_BRANCH"
fi