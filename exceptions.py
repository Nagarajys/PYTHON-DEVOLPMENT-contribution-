class DatasetError(Exception):
    """Base exception for dataset errors."""


class InvalidDatasetError(DatasetError):
    """Raised when dataset format is invalid."""


class MissingFileError(DatasetError):
    """Raised when dataset file is missing."""

try:
    class DatasetError
except valueError as error:
    print("VALUE ERROR")
else:
    print("dataset fetched succesfully")
finally:
    print("NO ERRORS")
    
