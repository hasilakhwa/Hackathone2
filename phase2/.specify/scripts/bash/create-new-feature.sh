#!/bin/bash

# Parse arguments
DESCRIPTION=""
NUMBER=""
SHORT_NAME=""

while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--description)
      DESCRIPTION="$2"
      shift 2
      ;;
    --number)
      NUMBER="$2"
      shift 2
      ;;
    --short-name)
      SHORT_NAME="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

# Create the feature branch
BRANCH_NAME="${NUMBER}-${SHORT_NAME}"
echo "Creating branch: $BRANCH_NAME"

# Create and checkout the new branch
git checkout -b "$BRANCH_NAME" || git checkout -B "$BRANCH_NAME"

# Create the specs directory structure
SPEC_DIR="specs/$BRANCH_NAME"
mkdir -p "$SPEC_DIR"

# Create the spec file
SPEC_FILE="$SPEC_DIR/spec.md"
touch "$SPEC_FILE"

# Output the result as JSON
printf '{"BRANCH_NAME":"%s","SPEC_FILE":"%s"}\n' "$BRANCH_NAME" "$SPEC_FILE"