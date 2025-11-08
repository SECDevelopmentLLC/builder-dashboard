{# ------------------------------
   Modern Clean project view (Style 1)
   Reads values from page front matter
   ------------------------------ #}

{# -- Read numbers (default to 0) -- #}
{% set b = (budget or 0)|float %}
{% set s = (spent or 0)|float %}
{% set v_paid = (vendors_paid or 0)|int %}
{% set inv_out = (invoices_outstanding or 0)|int %}
{% set t_done = (tasks_complete or 0)|int %}
{% set t_tot  = (tasks_total or 0)|int %}
{% set remaining = b - s %}
{% set spent_pct = (s / b * 100) if b > 0 else 0 %}
{% set done_pct  = (t_done / t_tot * 100) if t_tot > 0 else 0 %}

{# -- Colors with safe defaults -- #}
{% set cproj     = (colors.project   or '#2563eb') %}
{% set cbudget   = (colors.budget    or '#16a34a') %}
{% set cvendors  = (colors.vendors   or '#f59e0b') %}
{% set cinvoices = (colors.invoices  or '#ef4444') %}
{% set ctasks    = (colors.tasks     or '#8b5cf6') %}

<div class="proj-wrap" style="
  --proj: {{ cproj }};
  --budget: {{ cbudget }};
  --vendors: {{ cvendors }};
  --invoices: {{ cinvoices }};
  --tasks: {{ ctasks }};
">
  <div class="proj-banner">
    <h1>{{ project_name }}</h1>
  </div>

  <div class="kpis">
    <div class="kpi" style="border-left:4px solid var(--budget);">
      <h4>Budgeted</h4>
      <div class="value">${{ '{:,.0f}'.format(b) }}</div>
      <div class="bar"><span class="bg-budget" style="width:100%"></span></div>
    </div>

    <div class="kpi" style="border-left:4px solid var(--budget);">
      <h4>Spent</h4>
      <div class="value">${{ '{:,.0f}'.format(s) }} ({{ '{:.1f}%'.format(spent_pct) }})</div>
      <div class="bar"><span class="bg-budget" style="width: {{ spent_pct }}%"></span></div>
    </div>

    <div class="kpi" style="border-left:4px solid var(--budget);">
      <h4>Remaining</h4>
      <div class="value">${{ '{:,.0f}'.format(remaining) }}</div>
      <div class="bar"><span class="bg-budget" style="width: {{ max(0, 100 - spent_pct) }}%"></span></div>
    </div>

    <div class="kpi" style="border-left:4px solid var(--tasks);">
      <h4>Tasks</h4>
      <div class="value">{{ t_done }} / {{ t_tot }} ({{ '{:.1f}%'.format(done_pct) }})</div>
      <div class="bar"><span class="bg-tasks" style="width: {{ done_pct }}%"></span></div>
    </div>
  </div>

  <div class="kpis">
    <div class="kpi" style="border-left:4px solid var(--vendors);">
      <h4>Vendors Paid</h4>
      <div class="value">{{ v_paid }}</div>
    </div>

    <div class="kpi" style="border-left:4px solid var(--invoices);">
      <h4>Invoices Outstanding</h4>
      <div class="value">{{ inv_out }}</div>
    </div>

    <div class="kpi" style="border-left:4px solid var(--proj);">
      <h4>Project Color</h4>
      <div class="bar"><span style="width:100%; background: var(--proj)"></span></div>
    </div>

    <div class="kpi">
      <h4>Notes</h4>
      <div>Update numbers in the page front-matter to refresh these cards.</div>
    </div>
  </div>
</div>
