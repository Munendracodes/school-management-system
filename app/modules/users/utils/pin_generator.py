import secrets

MPIN_REGEX = r"^\d{4}$"

def generate_temporary_pin(length: int = 4) -> str:
    """
    Generate secure numeric temporary PIN
    """

    if length < 4:
        raise ValueError(
            "PIN length must be at least 4"
        )

    min_value = 10 ** (length - 1)
    max_value = (10 ** length) - 1

    return str(
        secrets.randbelow(
            max_value - min_value + 1
        ) + min_value
    )