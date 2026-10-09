FROM python:3.13-slim

WORKDIR /tg-bot

COPY . .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --frozen

CMD ["uv", "run", "source/run.py"]