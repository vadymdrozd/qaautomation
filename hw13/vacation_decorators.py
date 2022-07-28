def title(func):
    """
        This decorator inserts the title of vacation request
    Args:
        func: function as object
    Returns:
        string - title concatenated with func execution
    """
    def wrapper(*args, **kwargs):
        return '\nCEO Red Bull Inc.\nMr. John Bigbull\n' + func(*args, **kwargs)
    return wrapper
