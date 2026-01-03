import uuid
from typing import Dict, Any
from .research_agent import ResearchIntelligenceAgent
from ..models.state import ConversationState

class OrchestrationAgent:
    """
    Master coordinator for all specialist agents.
    """

    def __init__(self, user_id: str = "default_user"):
        """
        Initializes the orchestrator, its specialist agents, and the conversation state.
        """
        self.specialist_agents = {
            "research": ResearchIntelligenceAgent()
        }
        # Initialize the state for this session
        self.state = ConversationState(
            session_id=str(uuid.uuid4()),
            user_id=user_id
        )
        print(f"OrchestrationAgent initialized for user '{user_id}'. Session ID: {self.state.session_id}")
        print("Specialists loaded: research")


    def _classify_intent(self, user_query: str) -> str:
        """
        Classifies user intent based on keywords from the design spec.
        """
        query = user_query.lower()
        research_keywords = ["research", "market", "competitor", "industry", "trend", "news", "landscape", "recommendation"]

        if any(keyword in query for keyword in research_keywords):
            return "research"

        # In the future, we can check previous intents from self.state
        return "unclassified"

    def handle_request(self, user_query: str) -> str:
        """
        Handles a user request by classifying intent, updating state, and routing.
        """
        print(f"--- Orchestrator: Received request: '{user_query}' ---")

        intent = self._classify_intent(user_query)
        print(f"--- Orchestrator: Classified intent as '{intent}' ---")

        # Update the conversation state
        self.state.current_intent = intent
        self.state.context_gathered['last_query'] = user_query

        if intent == "unclassified":
            return self._format_clarification_response()

        specialist = self.specialist_agents.get(intent)
        if not specialist:
            return f"Error: No specialist agent found for intent '{intent}'."

        # Update state before routing
        self.state.agents_invoked.append(intent)

        # Route the task to the specialist agent
        result = specialist.handle_task(user_query)

        # Assemble the final response
        return self._assemble_response(result)

    def _assemble_response(self, agent_result: Dict[str, Any]) -> str:
        """
        Formats the final response for the user, handling success or escalation.
        """
        if agent_result.get("status") == "success":
            print("--- Orchestrator: Specialist agent returned 'success'. Formatting output. ---")
            return agent_result.get("output", "No output received.")

        elif agent_result.get("status") == "escalation":
            print("--- Orchestrator: Specialist agent triggered 'escalation'. Formatting for human review. ---")
            self.state.escalation_required = True
            return self._format_escalation_handoff(agent_result)

        return "An unexpected error occurred."

    def _format_clarification_response(self) -> str:
        """
        Returns a message asking for clarification.
        """
        return "I am not sure how to handle your request. Please specify if you need 'research', 'financial_analysis', etc."

    def _format_escalation_handoff(self, details: Dict[str, Any]) -> str:
        """
        Formats an escalation message for a human professional.
        """
        return (
            f"<escalation>\n"
            f"ESCALATION REQUIRED\n"
            f"Type: {details.get('type', 'N/A')}\n"
            f"Urgency: Medium\n"
            f"Reason: {details.get('details', 'N/A')}\n"
            f"</escalation>"
        )
