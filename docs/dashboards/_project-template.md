# {{ project_name }}

| Metric | Value |
|-------|------:|
| **Budgeted** | ${{ budget }} |
| **Spent** | ${{ spent }} |
| **Remaining** | ${{ budget - spent }} |
| **Vendors Paid** | {{ vendors_paid }} |
| **Invoices Outstanding** | {{ invoices_outstanding }} |
| **Tasks Complete** | {{ tasks_complete }}/{{ tasks_total }} |

---

### 📊 Progress

#### Budget Usage
```mermaid
pie showData
    title Budget Allocation
    "Spent" : {{ spent }}
    "Remaining" : {{ budget - spent }}
