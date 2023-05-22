"""
This script performs EDA on a given dataset and saves the report to a file.


Date: 2021-06-01

"""
import argparse
import logging
import pandas as pd
from ydata_profiling import ProfileReport

# Set logging level
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()


def generate_eda_report(input_path: str, output_path: str):
    """Generates an EDA report for the given dataset.

    Args:
        input_path (str): Path to the dataset.
        output_path (str): Path to save the report.

    Returns:
        File of generated EDA report for the given dataset.

    """
    # Load dataset.
    # This part can be customized to load data from different sources using
    # the import_data module.
    df_data = pd.read_csv(input_path)
    logging.info("Loaded %s dataset.", input_path)

    # Generate report
    logging.info("Generating EDA report...")
    report = ProfileReport(
        df_data,
        title=f"{input_path} EDA Report",
        explorative=True)

    logging.info("Saving generated report to %s ...", output_path)

    return report.to_file(output_path)


if __name__ == "__main__":
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument(
        "--output_path",
        type=str,
        required=False,
        default="eda_report.html")
    args = parser.parse_args()

    # call the generate report function
    generate_eda_report(args.input_path, args.output_path)
