from rapidfuzz import fuzz

FUZZY_THRESHOLD = 85  # partial_ratio score (0-100) above which we call it a match


def judge(question, expects, answer, results) -> bool:
    """
    Pass if `expects` is a close match somewhere inside `answer`.

    Exact substring match is checked first since it's cheap and unambiguous.
    Otherwise fall back to rapidfuzz's partial_ratio, which scores the best
    alignment of `expects` against any window of `answer` — this tolerates
    paraphrasing, typos, and minor wording differences that exact substring
    matching would wrongly fail.
    """
    expects_norm = expects.lower().strip()
    answer_norm = answer.lower().strip()

    if expects_norm in answer_norm:
        return True

    return fuzz.partial_ratio(expects_norm, answer_norm) >= FUZZY_THRESHOLD


def retrieval_hits(expects, results) -> bool:
    return any(expects.strip().lower() for chunk in results)