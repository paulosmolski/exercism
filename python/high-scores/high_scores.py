def latest(scores):
    return scores[-1]


def personal_best(scores):
    best_score = max(scores)
    return best_score


def personal_top_three(scores):
    scores = sorted(scores, reverse = True)
    return scores[:3]
