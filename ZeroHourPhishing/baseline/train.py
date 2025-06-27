"""
Zero-Hour Phishing • Baseline Trainer
------------------------------------
A reproducible baseline: TF-IDF over email body + Logistic Regression.
Trains on Enron (ham) + Nazario (phish) + a 20 % slice of PhishTank URLs
converted to pseudo-emails. Saves vectorizer + model with joblib.

Run:
    python baseline/train.py --data_dir data/raw --model_dir baseline/models

Author: FohnAI Research
License: Apache-2.0
"""
import argparse, pathlib, joblib, json, random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pandas as pd

########################
# Data helpers
########################
def load_enron(path: pathlib.Path) -> pd.DataFrame:
    # Expecting CSV with 'text' column
    df = pd.read_csv(path)
    df["label"] = 0  # ham
    return df[["text", "label"]]

def load_nazario(path: pathlib.Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["label"] = 1  # phish
    return df[["text", "label"]]

def load_phishtank(path: pathlib.Path, n_samples: int = 6000) -> pd.DataFrame:
    """
    Convert phishing URLs into pseudo-email bodies so the text model sees them.
    """
    urls = pd.read_csv(path)["url"].dropna().tolist()
    random.shuffle(urls)
    urls = urls[: n_samples]
    rows = [f"Click the secure link: {u}" for u in urls]
    return pd.DataFrame({"text": rows, "label": [1]*len(rows)})

def build_dataset(data_dir: pathlib.Path) -> tuple[pd.Series, pd.Series]:
    enron = load_enron(data_dir / "enron.csv")
    nazario = load_nazario(data_dir / "nazario.csv")
    phishtank = load_phishtank(data_dir / "phishtank.csv")
    df = pd.concat([enron, nazario, phishtank], ignore_index=True)
    df = df.sample(frac=1.0, random_state=42)  # shuffle
    return df["text"], df["label"]

########################
# Training routine
########################
def train(x, y):
    pipe = Pipeline(
        [
            ("tfidf", TfidfVectorizer(
                lowercase=True,
                stop_words="english",
                ngram_range=(1, 2),
                max_features=50_000,
            )),
            ("clf", LogisticRegression(max_iter=200, n_jobs=-1)),
        ]
    )
    pipe.fit(x, y)
    return pipe

########################
# Main
########################
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", type=str, required=True)
    ap.add_argument("--model_dir", type=str, default="baseline/models")
    args = ap.parse_args()

    data_dir = pathlib.Path(args.data_dir)
    model_dir = pathlib.Path(args.model_dir)
    model_dir.mkdir(parents=True, exist_ok=True)

    x, y = build_dataset(data_dir)
    model = train(x, y)

    # quick train report
    preds = model.predict(x)
    report = classification_report(y, preds, output_dict=True)
    print(json.dumps(report, indent=2))

    # persist
    joblib.dump(model, model_dir / "tfidf_logreg.joblib")

if __name__ == "__main__":
    main()
