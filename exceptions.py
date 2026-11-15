class DatasetError(Exception):
    """Base exception for dataset errors."""


class InvalidDatasetError(DatasetError):
    """Raised when dataset format is invalid."""


class MissingFileError(DatasetError):
    """Raised when dataset file is missing."""
