def check_brackets(brackets_row: str):
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    if brackets_row != '' and (brackets_row[0] == ')' or brackets_row[-1] == '('
                               or brackets_row.count('(') != brackets_row.count(')')):
        return False  # Уже проходит все тесты.
    open_closed_brackets_counter = 0
    for _ in brackets_row:
        if _ == '(':
            open_closed_brackets_counter += 1
        if _ == ')':
            open_closed_brackets_counter -= 1
        if open_closed_brackets_counter < 0:
            return False  # Позволяет вычленять последовательности типа: ()))((().
    return True
