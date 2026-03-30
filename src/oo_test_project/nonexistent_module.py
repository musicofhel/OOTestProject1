"""Module with data processing utilities."""


def process_data(data):
    """Process input data and return a dict.

    Returns an empty dict if data is None.
    """
    if data is None:
        return {}
    return dict(data)
