# Company Budget Overview

> Live budget vs. actuals for your active projects.  
> Numbers are pulled from YAML files in `docs/data/`.

---

{% set projects = [
    # ("Display Name", "path to YAML in docs/")
    ("New Project", "docs/data/New Project.yaml"),
] %}

{# ---------- Helpers ---------- #}
{% macro dollars(n) -%}
${{ "{:,}".format(n|int) }}
{%- endmacro %}

{% macro used_bar(pct) -%}
{% set blocks = (pct // 5) %}
{% set bar = "█" * blocks ~ "░" * (20 - blocks) %}
[{{ bar }}] {{ pct }}%
{%- endmacro %}

{% macro status_label(budget, spent) -%}
{% set remaining = budget - spent %}
{% set used_pct = 0 if budget == 0 else (spent * 100 // budget) %}
{% if remaining < 0 %}
Over Budget
{% elif used_pct >= 85 %}
Watch
{% else %}
On Track
{% endif %}
{%- endmacro %}

---

### Portfolio Summary

| Project | Budget | Spent | Remaining | Used | Status |
|---|---:|---:|---:|:---:|:---|
{% for name, path in projects %}
  {% set p = read_yaml(path) %}
  {% set budget = p.budget|int %}
  {% set spent = p.spent|int %}
  {% set remaining = budget - spent %}
  {% set used_pct = 0 if budget == 0 else (spent * 100 // budget) %}
| **{{ name }}** | {{ dollars(budget) }} | {{ dollars(spent) }} | {{ dollars(remaining) }} | {{ used_bar(used_pct) }} | {{ status_label(budget, spent) }} |
{% endfor %}

---

### Project Health (details)

{% for name, path in projects %}
  {% set p = read_yaml(path) %}

#### {{ name }}

- **Vendors Paid:** {{ p.vendors_paid|default(0) }}
- **Invoices Outstanding:** {{ p.invoices_outstanding|default(0) }}
- **Tasks Complete:** {{ p.tasks_complete|default(0) }}/{{ p.tasks_total|default(0) }}

{% set budget = p.budget|int %}
{% set spent = p.spent|int %}
{% set used_pct = 0 if budget == 0 else (spent * 100 // budget) %}

**Spend Progress:** {{ used_bar(used_pct) }}

---

{% endfor %}

> **Tip:** To update numbers, edit the matching YAML file in `docs/data/`.
