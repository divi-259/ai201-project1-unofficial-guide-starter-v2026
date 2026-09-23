def judge(question, expects, answer, results) -> bool:
    """
    Simple Check - if expected string is in the answer
    """
    expects_norm = expects.lower().strip()
    answer_norm = answer.lower().strip()

    return expects_norm in answer_norm
