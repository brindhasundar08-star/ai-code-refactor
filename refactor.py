def refactor_code(code, issues):
    """
    Refactors the given code based on a list of issues.
    
    Args:
        code (str): The original code as a string.
        issues (list): A list of issue strings.
    
    Returns:
        str: The refactored code.
    """
    new_code = code
    
    # Use a dictionary for mappings to make it extensible
    replacements = {
        "Bad function name": ("calc", "calculate_sum"),
        "Bad variable name": ("printval", "print_value"),
    }
    
    for issue in issues:
        if issue in replacements:
            old, new = replacements[issue]
            new_code = new_code.replace(old, new)
    
    return new_code