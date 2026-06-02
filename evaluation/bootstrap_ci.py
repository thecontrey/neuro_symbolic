import random

def bootstrap_accuracy_ci(y_true, y_pred, n=10000, alpha=0.05, seed=42):
    random.seed(seed)
    m = len(y_true)
    vals = []
    for _ in range(n):
        idx = [random.randrange(m) for _ in range(m)]
        vals.append(sum(y_true[i] == y_pred[i] for i in idx) / m)
    vals.sort()
    return vals[int((alpha/2)*n)], vals[int((1-alpha/2)*n)]

if __name__ == "__main__":
    print("Import bootstrap_accuracy_ci(y_true, y_pred) from this module.")
