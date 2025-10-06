"""Основная точка входа для SGR Deep Research API сервера."""

import argparse
import os

import uvicorn

from sgr_deep_research.api.endpoints import app


def main():
    """Запуск FastAPI сервера."""

    parser = argparse.ArgumentParser(description="SGR Deep Research Server")
    parser.add_argument(
        "--host", type=str, dest="host", default=os.environ.get("HOST", "0.0.0.0"), help="Хост для прослушивания"
    )
    parser.add_argument(
        "--port", type=int, dest="port", default=int(os.environ.get("PORT", 8010)), help="Порт для прослушивания"
    )
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
