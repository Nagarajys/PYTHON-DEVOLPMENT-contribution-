import argparse

from data_loader import load_csv
from analyzer import analyze_dataset
from report_generator import generate_report


def main():

    parser = argparse.ArgumentParser(
        description="AI Dataset Quality Analyzer"
    )

    parser.add_argument("--file", required=True)

    args = parser.parse_args()

    try:

        headers, rows = load_csv(args.file)

        result = analyze_dataset(headers, rows)

        print("\nDATASET ANALYSIS REPORT")
        print("-----------------------")

        print("Total Rows:", result["rows"])
        print("Total Columns:", result["columns"])

        print("\nMissing Values:")

        for column, count in result["missing"].items():
            print(column, ":", count)

        print("\nDuplicate Rows:", result["duplicates"])

        generate_report(result)

        print("\nAnalysis completed successfully!")

    except Exception as error:

        print("Error:", error)


if __name__ == "__main__":
    main()
  
