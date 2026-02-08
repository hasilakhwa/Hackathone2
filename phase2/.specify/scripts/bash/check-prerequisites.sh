#!/bin/bash

# Check prerequisites script - outputs JSON with paths

FEATURE_DIR="specs/1-db-schema"
AVAILABLE_DOCS=()

# Check for required documents
if [ -f "$FEATURE_DIR/plan.md" ]; then
    AVAILABLE_DOCS+=("plan.md")
fi
if [ -f "$FEATURE_DIR/spec.md" ]; then
    AVAILABLE_DOCS+=("spec.md")
fi
if [ -f "$FEATURE_DIR/data-model.md" ]; then
    AVAILABLE_DOCS+=("data-model.md")
fi
if [ -f "$FEATURE_DIR/research.md" ]; then
    AVAILABLE_DOCS+=("research.md")
fi
if [ -f "$FEATURE_DIR/quickstart.md" ]; then
    AVAILABLE_DOCS+=("quickstart.md")
fi
if [ -d "$FEATURE_DIR/contracts" ] && [ -n "$(ls -A $FEATURE_DIR/contracts)" ]; then
    AVAILABLE_DOCS+=("contracts/")
fi

# Convert array to JSON format
docs_json="["
for i in "${!AVAILABLE_DOCS[@]}"; do
    if [ $i -eq 0 ]; then
        docs_json+="\"${AVAILABLE_DOCS[$i]}\""
    else
        docs_json+=", \"${AVAILABLE_DOCS[$i]}\""
    fi
done
docs_json+="]"

echo "{\"FEATURE_DIR\":\"$FEATURE_DIR\",\"AVAILABLE_DOCS\":$docs_json}"