def check_brackets(brackets_row: str):
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    if brackets_row != '' and (brackets_row[0] == ')' or brackets_row[-1] == '('
                               or brackets_row.count('(') != brackets_row.count(')')):
        return False
    return True


if __name__ == "__main__":
    check_brackets("(()(")
    check_brackets("")
