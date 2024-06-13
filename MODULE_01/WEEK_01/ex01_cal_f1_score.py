def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)


def f1_score(tp, fp, fn):
    return 2 * (precision(tp, fp) * recall(tp, fn)) / (precision(tp, fp) + recall(tp, fn))


def exercise1(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("fp must be int")
        return

    if not isinstance(fn, int):
        print("fn must be int")
        return

    if (tp <= 0) or (fp <= 0) or (fn <= 0):
        print("tp and fp and fn must be greater than zero")
        return

    print(f"Precision is {precision(tp=tp, fp=fp):.5f}")
    print(f"Recall is {recall(tp=tp, fn=fn):.5f}")
    print(f"F1-score is {f1_score(tp=tp, fp=fp, fn=fn):.5f}")
