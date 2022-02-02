def very_input(user_input, expected_values):
    try:
        user_input = int(user_input)
    except ValueError:
        return False, None
    if user_input not in expected_values:
        return False, None
    return True, user_input
