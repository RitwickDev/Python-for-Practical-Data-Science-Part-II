from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class ConversationState:
    session_id: str
    user_id: str
    current_intent: str = ""
    context_gathered: Dict[str, Any] = field(default_factory=dict)
    agents_invoked: List[str] = field(default_factory=list)
    pending_actions: List[str] = field(default_factory=list)
    escalation_required: bool = False

@dataclass
class DealState:
    deal_id: str
    client_name: str
    deal_type: str
    stage: str
    documents: List[str] = field(default_factory=list)
    stakeholders: List[str] = field(default_factory=list)
    timeline: Dict[str, Any] = field(default_factory=dict)
    issues: List[str] = field(default_factory=list)
    last_updated: str = "" # Using string for timestamp for simplicity

@dataclass
class KnowledgeState:
    investor_profiles: str = "vector_store_reference"
    market_intelligence: str = "vector_store_reference"
    precedent_transactions: str = "vector_store_reference"
    process_templates: str = "vector_store_reference"
