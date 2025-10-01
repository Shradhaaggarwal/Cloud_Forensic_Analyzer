# Cloud_Forensic_Analyzer

Simple starter project for collecting and analyzing cloud forensic artifacts.

Project structure
------------------

```
/cloud-forensics-analyzer
|-- /data/
|-- /src/
   |-- __init__.py
   |-- main.py
   |-- collectors.py
   |-- analyzer.py
-- requirements.txt
-- README.md
-- .gitignore
```

Setup
-----

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

Run
-----

From the repository root (example):

```powershell
python -m src.main --source dropbox
```

Notes
-----

The collectors and analyzer are stubs. Implement API auth and parsing logic before using on real data.
# Cloud_Forensic_Analyzer