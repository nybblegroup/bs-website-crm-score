{
    "name": "Lead Scoring",
    "summary": "Compute scores and assign leads automatically",
    "category": "Sales/CRM",
    "version": "1.0",
    "depends": ["base", "sales_team", "website_crm", "crm_enterprise"],
    "description": """
Lead Scoring
============

This module allows you to:

* Track the page views of your visitors who posted a message on your Contact Us page.
  The page views are listed on the related lead.
* Compute a score on incoming leads, in order to assign accordingly.
* Assign leads to sales teams.
* Assign leads to specific salespersons in the sales team.
""",
    "data": [
        "views/crm_lead_views.xml",
        "views/marketing.xml",
        "security/ir.model.access.csv",
        "data/website_crm_score_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "website_crm_score/static/src/js/display_filters.js",
        ],
    },
    "installable": True,
    "application": False,
    "license": "OEEL-1",
}
