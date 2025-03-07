"""
Minimal entry point for the PetroCast application.

This script initializes execution and delegates processing to `run.py`.
"""

import argparse
from pathlib import Path
from petrocast.run import run_petrocast


def main():
    """Entry point for PetroCast CLI."""
    example_folder = Path(__file__).parent.parent.absolute()
    example_folder = Path.joinpath(example_folder, "examples", "config.toml")
    parser = argparse.ArgumentParser(
        description="Run PetroCast model with a TOML configuration file."
    )
    parser.add_argument(
        "--config", type=str, required=False, default=example_folder,
        help="Path to the configuration TOML file."
    )
    parser.add_argument(
        "--urr-key", type=str, required=False, default="Estimate1",
        help="Specify the URR estimate to use from the file."
    )
    args = parser.parse_args()

    run_petrocast(args.config, args.urr_key)


if __name__ == "__main__":
    main()
