import csv
from collections import Counter

LABELS = ["Positive", "Negative", "Undetermined"]

def accuracy(rows, pred_col, gold_col="gold_label"):
    return sum(r[pred_col] == r[gold_col] for r in rows) / len(rows)

def macro_f1(rows, pred_col, gold_col="gold_label"):
    scores = []
    for label in LABELS:
        tp = sum(r[pred_col] == label and r[gold_col] == label for r in rows)
        fp = sum(r[pred_col] == label and r[gold_col] != label for r in rows)
        fn = sum(r[pred_col] != label and r[gold_col] == label for r in rows)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        scores.append((2 * precision * recall / (precision + recall)) if precision + recall else 0.0)
    return sum(scores) / len(scores)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--pred-col", required=True)
    args = parser.parse_args()
    with open(args.csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print({"accuracy": accuracy(rows, args.pred_col), "macro_f1": macro_f1(rows, args.pred_col)})
