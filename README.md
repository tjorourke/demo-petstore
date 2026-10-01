# demo-petstore

A small Flask sample app used as a fixture for a Solo.io agent-SDLC demo
(solo-demos `vision-demo-2026`): a PM agent files feature requests here as
GitHub issues, a developer agent implements them, and the result is deployed
through a staging/prod pipeline with a human-in-the-loop approval gate.

Not a real product — deliberately tiny so an LLM agent can make a believable,
reviewable change in a single turn.

## Run locally

    pip install -r requirements.txt
    python app.py
