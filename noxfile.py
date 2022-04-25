import os
from pathlib import Path

import nox

nox.options.sessions = ["tests"]


VENV_DIR = Path(__file__).parent.resolve() / ".venv"


@nox.session
def tests(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest", *session.posargs)


@nox.session
def dev(session: nox.Session) -> None:
    session.install("virtualenv")
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)
    python = os.fsdecode(VENV_DIR / "bin/python")
    session.run(python, "-m", "pip", "install", "-e", ".", external=True)
