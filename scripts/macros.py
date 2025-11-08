# builder-dashboard/scripts/macros.py
import os
from pathlib import Path
import yaml

def define_env(env):
    """Macros for MkDocs."""

    # Determine root of project
    site_root = Path(__file__).parent.parent.resolve()
    data_root = site_root / "builder-dashboard" / "docs" / "data"
    photos_root = site_root / "photos"

    # -------------------------------------------------------
    #  Load project financial + progress data from YAML
    # -------------------------------------------------------
    def load_project_data(project_name):
        safe_name = project_name.replace("/", " ")
        data_file = data_root / f"{safe_name}.yaml"

        if not data_file.exists():
            return {
                "project_name": project_name,
                "budget": 0,
                "spent": 0,
                "vendors_paid": 0,
                "invoices_outstanding": 0,
                "tasks_complete": 0,
                "tasks_total": 0,
            }

        with open(data_file, "r") as f:
            return yaml.safe_load(f)

    env.macro(load_project_data)

    # -------------------------------------------------------
    #  List files (PDFs, images, spreadsheets) for the project
    # -------------------------------------------------------
    def list_files(project_name):
        safe_name = project_name.replace("/", " ")
        folder = photos_root / safe_name

        if not folder.exists():
            return f"_No uploaded files for **{project_name}** yet._"

        allowed = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".xlsx", ".docx"}
        items = []

        for f in sorted(folder.iterdir()):
            if f.is_file() and f.suffix.lower() in allowed:
                rel = f.relative_to(site_root)
                items.append(f"- [{f.name}](/" + rel.as_posix() + ")")

        return "\n".join(items) if items else f"_No supported files for **{project_name}** yet._"

    env.macro(list_files)
