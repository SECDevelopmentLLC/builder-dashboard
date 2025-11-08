# scripts/macros.py
import os, re, yaml

def define_env(env):
    def _read_frontmatter():
        page = env.page
        with open(page.file.abs_src_path, "r", encoding="utf-8") as f:
            text = f.read()
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        if m:
            front = yaml.safe_load(m.group(1))
            return front
        return {}

    env.macro(_read_frontmatter)

    @env.macro
    def project_card():
        data = _read_frontmatter()
        project = data.get("project_name", "Project")
        budget = float(data.get("budget", 0))
        spent = float(data.get("spent", 0))
        remain = max(budget - spent, 0)
        vendors_paid = data.get("vendors_paid", 0)
        invoices_out = data.get("invoices_outstanding", 0)
        tasks_total = data.get("tasks_total", 0)
        tasks_complete = data.get("tasks_complete", 0)

        colors = data.get("colors", {})
        c_project = colors.get("project", "#2980b9")
        c_budget = colors.get("budget", "#27ae60")
        c_vendors = colors.get("vendors", "#f39c12")
        c_invoices = colors.get("invoices", "#c0392b")
        c_tasks = colors.get("tasks", "#8e44ad")

        return f"""
<div style="border-left: 6px solid {c_project}; padding: 12px; margin: 18px 0; background: #fafafa;">
<h2 style="margin-top: 0;">{project}</h2>

| Metric | Value |
|------|------|
| **Budgeted** | ${budget:,.0f} |
| **Spent** | ${spent:,.0f} |
| **Remaining** | ${remain:,.0f} |
| **Vendors Paid** | {vendors_paid} |
| **Invoices Outstanding** | {invoices_out} |
| **Tasks Complete** | {tasks_complete}/{tasks_total} |

</div>
"""
