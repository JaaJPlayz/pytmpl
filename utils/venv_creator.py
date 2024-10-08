from typing import List, Optional
import os

def venv_creator(directory: str, deps: Optional[List[str]] = None) -> None:
    os.system(f"python -m venv {directory}")
    os.system(f"source {directory}/bin/activate")
    if deps:
        for dep in deps:
            os.system(f"pip install {dep}")