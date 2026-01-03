from typing import Dict, Any
from ..mocks import apis

class FinancialAnalysisAgent:
    """
    Financial modelling, valuation, and quantitative analysis specialist.
    """

    def __init__(self):
        """
        Initializes the agent with access to necessary tools.
        """
        self.tools = {
            "comparable_data_api": apis.comparable_data_api,
            # In the future, we would add precedent_data_api, etc.
        }

    def handle_task(self, task_description: str) -> Dict[str, Any]:
        """
        Handles a financial analysis task based on a textual description.
        """
        print(f"--- FinancialAnalysisAgent: Handling task: '{task_description}' ---")

        # --- Escalation Trigger Check ---
        if "recommendation" in task_description.lower() or "what value should we recommend" in task_description.lower():
            return {
                "status": "escalation",
                "type": "VALUATION_RECOMMENDATION",
                "details": f"The request '{task_description}' asks for a valuation recommendation, which requires human judgment.",
                "analysis_completed": "Preliminary analysis complete, pending recommendation."
            }

        # --- Simple Tool Selection & Execution ---
        # A real agent would parse the company name from the query.
        # For this demo, we'll assume a target company is implicit.
        target_company = "TargetCo"
        comparables = self.tools["comparable_data_api"](target_company)

        # --- Synthesize Output ---
        report = self._synthesize_valuation_summary(task_description, comparables)

        return {
            "status": "success",
            "output": report
        }

    def _synthesize_valuation_summary(self, query, comparables):
        """Creates a structured text summary of the valuation analysis."""
        report = f"## Valuation Summary: {query}\n\n"

        if not comparables:
            report += "Could not retrieve comparable company data to perform valuation."
            return report

        report += "### Comparable Company Analysis (Trading Comps)\n"
        report += "| Company | EV/Revenue | EV/EBITDA |\n"
        report += "|---------|------------|-----------|\n"

        total_revenue_multiple = 0
        total_ebitda_multiple = 0

        for comp in comparables:
            report += f"| {comp['name']} | {comp['ev_revenue_multiple']:.1f}x | {comp['ev_ebitda_multiple']:.1f}x |\n"
            total_revenue_multiple += comp['ev_revenue_multiple']
            total_ebitda_multiple += comp['ev_ebitda_multiple']

        mean_revenue_multiple = total_revenue_multiple / len(comparables)
        mean_ebitda_multiple = total_ebitda_multiple / len(comparables)

        report += f"\n**Mean Multiples:**\n"
        report += f"- **EV/Revenue**: {mean_revenue_multiple:.1f}x\n"
        report += f"- **EV/EBITDA**: {mean_ebitda_multiple:.1f}x\n"
        report += "\n*Note: This is a simplified analysis based on mock data. A full valuation would require a DCF, precedent transaction analysis, and detailed financial projections.*"

        return report
