import sys
import os
import pytest

# Add project root to the Python path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rdco_agent_system.src.agents.orchestration_agent import OrchestrationAgent

@pytest.fixture
def orchestrator():
    """Pytest fixture to create an OrchestrationAgent instance for tests."""
    return OrchestrationAgent()

def test_intent_classification_research(orchestrator):
    """
    Tests that queries with research-related keywords are correctly classified.
    """
    research_query = "Can you research the competitive landscape for Indian fintech?"
    # Accessing the private method for unit testing purposes
    intent = orchestrator._classify_intent(research_query)
    assert intent == "research"

def test_intent_classification_unclassified(orchestrator):
    """
    Tests that queries without specific keywords are marked as unclassified.
    """
    unclassified_query = "What is the current time?"
    intent = orchestrator._classify_intent(unclassified_query)
    assert intent == "unclassified"

def test_escalation_flow_for_recommendation_query(orchestrator):
    """
    Tests that a query asking for a recommendation correctly triggers the escalation flow.
    """
    recommendation_query = "Should we invest in the fintech market? Give a recommendation."
    response = orchestrator.handle_request(recommendation_query)

    # Check that the response is a formatted escalation message
    assert "<escalation>" in response
    assert "ESCALATION REQUIRED" in response
    assert "STRATEGIC_INTERPRETATION_REQUESTED" in response

    # Check that the agent's internal state reflects the escalation
    assert orchestrator.state.escalation_required is True
