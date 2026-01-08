import numpy as np
def calculate_llm_advise(query, context):
    metrics = context.get("metrics", {})
    issues = []
    if metrics.get("fill_rate", 100) < 95: issues.append("fill_rate_below_target")
    if metrics.get("inventory_turns", 12) < 6: issues.append("slow_inventory_turns")
    if metrics.get("otd", 100) < 93: issues.append("delivery_performance_gap")
    priority = issues[0] if issues else "all_healthy"
    recommendations = {"fill_rate_below_target": "Review safety stock levels and supplier reliability",
                       "slow_inventory_turns": "Implement demand-driven replenishment and reduce excess",
                       "delivery_performance_gap": "Audit carrier performance and optimize routing",
                       "all_healthy": "Continue monitoring, focus on continuous improvement"}
    return {"query": query, "top_issue": priority, "recommendation": recommendations[priority], "all_issues": issues}
if __name__=="__main__":
    ctx = {"metrics": {"fill_rate": 93, "inventory_turns": 5, "otd": 91}}
    print(calculate_llm_advise("What should I focus on?", ctx))
