def analyze_dataset(headers, rows):

    missing = {}

    for column in headers:

        count = 0

        for row in rows:

            value = row.get(column)

            if value is None or value.strip() == "":
                count += 1

        missing[column] = count

    duplicates = len(rows) - len({
        tuple(sorted(row.items()))
        for row in rows
    })

    result = {

        "rows": len(rows),

        "columns": len(headers),

        "missing": missing,

        "duplicates": duplicates

    }

    return result
