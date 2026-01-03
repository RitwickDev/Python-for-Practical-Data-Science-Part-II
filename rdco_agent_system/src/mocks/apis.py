def web_search(query: str):
    """Mock web search API."""
    print(f"--- MOCK API: web_search(query='{query}') ---")
    if "fintech lending" in query:
        return [
            {
                "title": "The Rise of Fintech Lending in India - A Complete Overview",
                "link": "https://example.com/fintech-lending-india",
                "snippet": "The Indian fintech lending market has seen exponential growth, driven by digital adoption and financial inclusion...",
                "source": "Example Research Firm"
            },
            {
                "title": "Top 10 Fintech Lending Companies in India 2024",
                "link": "https://example.com/top-10-fintech-lenders",
                "snippet": "Featuring major players like Razorpay, Pine Labs, and others who are disrupting traditional lending models.",
                "source": "Example Tech News"
            }
        ]
    return []

def financial_database_query(company: str):
    """Mock financial database API."""
    print(f"--- MOCK API: financial_database_query(company='{company}') ---")
    if company.lower() == "razorpay":
        return {
            "company_name": "Razorpay",
            "valuation_usd_billions": 7.5,
            "last_funding_round": "Series F",
            "total_funding_usd_millions": 741.5,
            "key_investors": ["Sequoia Capital", "Tiger Global", "Y Combinator"],
            "founded": 2014,
            "business_model": "Payment Gateway and Financial Services"
        }
    return {}

def news_search(topic: str):
    """Mock news search API."""
    print(f"--- MOCK API: news_search(topic='{topic}') ---")
    if "saas market" in topic:
        return [
            {
                "headline": "Indian SaaS Market to Reach $50 Billion by 2030",
                "source": "Reuters",
                "date": "2024-01-15"
            },
            {
                "headline": "Freshworks, Zoho lead the charge in India's SaaS boom",
                "source": "The Economic Times",
                "date": "2024-01-12"
            }
        ]
    return []
