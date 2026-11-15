def generate_report(result):

    with open("dataset_report.txt", "w") as file:

        file.write("AI DATASET QUALITY REPORT\n")

        file.write("=========================\n")

        file.write(
            f"Total Rows: {result['rows']}\n"
        )

        file.write(
            f"Total Columns: {result['columns']}\n"
        )

        file.write("\nMissing Values:\n")

        for column, count in result["missing"].items():

            file.write(
                f"{column}: {count}\n"
            )

        file.write(
            f"\nDuplicate Rows: {result['duplicates']}\n"
        )

    print("Report generated successfully!")
