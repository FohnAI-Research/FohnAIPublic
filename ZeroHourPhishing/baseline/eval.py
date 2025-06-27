"""
Zero-Hour Phishing • Baseline Evaluator
--------------------------------------
Loads the saved model and evaluates on a held-out test set
(shell example uses 2024 PhishTank data unseen during training).

Run:
    python baseline/eval.py --model_dir baseline/models \
                            --test_csv data/raw/phishtank_2024.csv
"""
import argparse, pathlib, json
import pandas as pd, joblib
from sklearn.metrics import classification_report

def load_test(csv_path: pathlib.Path) -> tuple[list[str], list[int]]:
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["url"])
    # Convert URLs into pseudo-email bodies
    messages = [f"Urgent account alert: verify here {u}" for u in df["url"]]
    labels = [1]*len(messages)   # phishing == 1
    return messages, labels

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_dir", type=str, required=True)
    ap.add_argument("--test_csv", type=str, required=True)
    args = ap.parse_args()

    model_path = pathlib.Path(args.model_dir) / "tfidf_logreg.joblib"
    model = joblib.load(model_path)

    x_test, y_test = load_test(pathlib.Path(args.test_csv))
    preds = model.predict(x_test)
    report = classification_report(y_test, preds, output_dict=True)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
