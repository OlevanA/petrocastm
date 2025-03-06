"""
Minimal entry point for the PetroCast application.

This script initializes execution and delegates processing to `run.py`.
"""

import argparse
from petrocast.run import run_petrocast


def main():
    """Entry point for PetroCast CLI."""
    parser = argparse.ArgumentParser(
        description="Run PetroCast model with a TOML configuration file."
    )
    parser.add_argument(
        "--config", type=str, required=True,
        help="Path to the configuration TOML file."
    )
    parser.add_argument(
        "--urr-key", type=str, required=True,
        help="Specify the URR estimate to use from the file."
    )
    args = parser.parse_args()

    run_petrocast(args.config, args.urr_key)


if __name__ == "__main__":
    main()
