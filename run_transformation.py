from pathlib import Path
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

import dill


def save_object(file_path: str, obj):
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        dill.dump(obj, f)


def build_and_save_preprocessor(dest_path: str):
    numerical_columns = ["writing_score", "reading_score"]

    categorical_columns = [
        "gender",
        "race_ethnicity",
        "parental_level_of_education",
        "lunch",
        "test_preparation_course",
    ]

    num_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ("scaler", StandardScaler(with_mean=False)),
        ]
    )

    preprocessor = ColumnTransformer(
        [
            ("num", num_pipeline, numerical_columns),
            ("cat", cat_pipeline, categorical_columns),
        ]
    )

    save_object(file_path=dest_path, obj=preprocessor)


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[0]
    artifacts = base / "artifacts"
    artifacts.mkdir(exist_ok=True)
    dest = str(artifacts / "preprocessor.pkl")
    build_and_save_preprocessor(dest)
    print("Saved preprocessor to", dest)
