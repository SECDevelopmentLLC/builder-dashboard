# 🏗 Company Budget Overview

This dashboard tracks **project budgets vs actual spending** across all active construction projects.
It provides real-time visibility into where money is being allocated and whether spending is staying on track.

---

## 📊 Key Metrics

| Term | Meaning |
|------|---------|
| **Budgeted Cost** | Approved spending amount for the project |
| **Actual Cost (Spent)** | Real dollars spent to date |
| **Remaining** | Budget - Spent |
| **Status** | Whether the project is under, on, or over budget |

---

## 🏗 Projects Displayed in This Dashboard

> Currently showing **106 E High Bluff**  
> More projects can be added automatically — just add new `.yaml` files inside `docs/data/`

{% set p = read_yaml('docs/data/106 E High Bluff.yaml') %}

| Project | Budget | Spent | Remaining | Status |
|--------|--------|-------|-----------|--------|
| 106 E High Bluff | ${{ p.budget }} | ${{ p.spent }} | ${{ p.budget - p.spent }} | {% if p.spent > p.budget %}🚨 **Over Budget**{% elif p.spent == p.budget %}⚠️ **At Limit**{% else %}✅ **On Track**{% endif %} |

---

## ✅ How to Update the Dashboard

You **do not edit this page** to update data.

To change values:
1. Go to: **`docs/data/106 E High Bluff.yaml`**
2. Update these numbers:

```yaml
budget: 0          # total planned budget
spent: 0           # amount already spent
vendors_paid: 0
invoices_outstanding: 0
tasks_complete: 0
tasks_total: 0
