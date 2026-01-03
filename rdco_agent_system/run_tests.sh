#!/bin/bash

# This script runs the pytest suite with the correct Python path.
# It ensures that the 'rdco_agent_system' package can be found by the interpreter.

# Add the 'src' directory to the PYTHONPATH.
# This allows the interpreter to find the 'rdco_agent_system' package within it.
export PYTHONPATH=$(pwd)/src

# Run pytest. Pytest will automatically discover the 'tests' directory.
pytest
