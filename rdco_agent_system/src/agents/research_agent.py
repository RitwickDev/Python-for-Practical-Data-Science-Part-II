from typing import Dict, Any

# We'll use relative imports once the project is structured as a package.
# For now, to make it runnable, we might need to adjust sys.path later.
from ..mocks import apis

class ResearchIntelligenceAgent:
    """
    Market research, competitor analysis, and data aggregation specialist.
    """

    def __init__(self):
        """
        Initializes the agent with access to necessary tools.
        In a real implementation, this would involve dependency injection.
        """
        self.tools = {
            "web_search": apis.web_search,
            "financial_database_query": apis.financial_database_query,
            "news_search": apis.news_search,
        }

    def handle_task(self, task_description: str) -> Dict[str, Any]:
        """
        Handles a research task based on a textual description.
        """
        print(f"--- ResearchAgent: Handling task: '{task_description}' ---")

        # --- Escalation Trigger Check ---
        if "recommendation" in task_description.lower() or "should we" in task_description.lower():
            return {
                "status": "escalation",
                "type": "STRATEGIC_INTERPRETATION_REQUESTED",
                "details": f"The request '{task_description}' asks for a strategic recommendation, which requires human judgment.",
                "research_completed": None
            }

        # --- Simple Tool Selection & Execution ---
        # A real agent would have more sophisticated logic here.
        web_results = self.tools["web_search"](task_description)
        news_results = self.tools["news_search"](task_description)

        # Basic entity extraction to find a company to profile
        company_profile = None
        # TODO: Replace this hardcoded logic with a more dynamic
        # named entity recognition (NER) model or a regex-based approach.
        potential_company = "Razorpay" # Hardcoded for this example
        if potential_company.lower() in task_description.lower():
            company_profile = self.tools["financial_database_query"](potential_company)

        # --- Synthesize Output ---
        report = self._synthesize_report(task_description, web_results, news_results, company_profile)

        return {
            "status": "success",
            "output": report
        }

    def _synthesize_report(self, query, web_results, news_results, company_profile):
        """Creates a structured text report from the gathered data."""
        report = f"## Research Report: {query}\n\n"

        report += "### Web Intelligence Summary\n"
        if web_results:
            for item in web_results:
                report += f"- **{item['title']}**: {item['snippet']} *(Source: {item['source']})*\n"
        else:
            report += "- No relevant web results found.\n"

        report += "\n### Recent News Articles\n"
        if news_results:
            for item in news_results:
                report += f"- **{item['headline']}** *(Source: {item['source']}, {item['date']})*\n"
        else:
            report += "- No recent news found on this topic.\n"

        if company_profile:
            report += f"\n### Profile: {company_profile['company_name']}\n"
            report += f"- **Valuation**: ${company_profile['valuation_usd_billions']}B\n"
            report += f"- **Business Model**: {company_profile['business_model']}\n"
            report += f"- **Total Funding**: ${company_profile['total_funding_usd_millions']}M\n"
            report += f"- **Key Investors**: {', '.join(company_profile['key_investors'])}\n"

        return report
