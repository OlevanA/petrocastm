"""
Minimal entry point for the PetroCast application.

This script initializes execution and delegates processing to `run.py`.
"""

import argparse
from pathlib import Path
from petrocast.run import run_petrocast


def main():
    """Entry point for PetroCast CLI."""
    root_folder = Path(__file__).parent.parent.absolute()
    example_folder = Path.joinpath(root_folder, "examples")
    config_file_name= Path.joinpath(example_folder, "config.toml")
    # Epilog creation
    epilog_str = """Example usage (see README for more details):
    - petrocast example_1 : runs the example_1 with the historical data and estimate 1 (Laherrare et al. 2022).
    - petrocast example_2 : runs the example_2 with the historical data and estimate 2 (IEA Reserves + cumulative extraction). 
    - petrocast --config config.toml --urr-key \"Estimate1\" : runs using a custom configuration file and estimate 1 (Laherrare et al. 2022).
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Run PetroCast model. Please run `petrocast --help` for more information.",
        epilog=epilog_str,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Add a positional argument (no -- prefix)
    parser.add_argument(
        "example_name",  # This will be the name of the attribute in the args object
        type=str,
        default=None,  # Default value if not provided
        help="The example to run (e.g., example_1)"
    )
    
    parser.add_argument(
        "--config", type=str, required=False, default=config_file_name,
        help="Path to the configuration TOML file."
    )
    parser.add_argument(
        "--urr-key", type=str, required=False, default="Estimate1",
        help="Specify the URR estimate to use from the file."
    )
    args = parser.parse_args()
    # Process the arguments
    if args.example_name:
        arg_cfn = config_file_name
        urr_key = f"Estimate{args.example_name.split("_")[1]}"
    else:
        arg_cfn = args.config
        urr_key = args.urr_key
    run_petrocast(config_path=arg_cfn, urr_key=urr_key, root_path=root_folder)


if __name__ == "__main__":
    main()
