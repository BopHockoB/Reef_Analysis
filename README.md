# Reef Analysis

Predictive machine learning analysis of global coral reef bleaching using environmental and oceanographic data.

---

## Overview

This project investigates coral reef bleaching prediction using machine learning regression models trained on global reef environmental datasets. The analysis focuses on identifying environmental factors associated with bleaching severity and evaluating the effectiveness of multiple predictive modeling approaches.

The work explores:
- Exploratory data analysis (EDA)
- Feature engineering and preprocessing
- Distribution normalization
- Correlation and multicollinearity analysis
- Regression model benchmarking
- Ensemble and non-linear learning methods

The primary prediction target is:

```python
Percent_Bleaching
```

---

## Objective

The objective of this project is to:

- Predict coral bleaching severity using environmental variables
- Compare baseline and advanced regression models
- Investigate linear and non-linear feature relationships
- Evaluate preprocessing techniques for skewed ecological data
- Identify key environmental drivers of reef bleaching

---

## Dataset

Dataset source:

- https://www.kaggle.com/datasets/mehrdat/coral-reef-global-bleaching

### Dataset Characteristics

- ~41,361 observations
- Two CSV files
- 18-feature and 62-feature dataset variants
- Combined using `Sample_ID`

### Example Features

- Water temperature
- ClimSST
- Turbidity
- Distance to shore
- Cyclone frequency
- Water depth
- Exposure metrics
- Bleaching level categories

### Target Variable

```python
Percent_Bleaching
```

---

## Technologies & Libraries

### Core Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- XGBoost
- TensorFlow / Keras

### Statistical Analysis

- SciPy
- StatsModels

---

## Project Workflow

### 1. Data Cleaning

The preprocessing pipeline includes:

- Removal of irrelevant columns:
  - `Sample_ID`
  - `Percent_Cover`
  - `Date_Year`
- Handling missing values
- Dataset splitting into:
  - Population-level bleaching samples
  - Colony-level bleaching samples

---

### 2. Exploratory Data Analysis (EDA)

The notebook performs extensive EDA including:

#### Target Distribution Analysis

The bleaching target distribution is:
- Highly skewed
- Concentrated around low bleaching percentages
- Contains significant outliers

Separate distributions are analyzed for:
- Population-level bleaching
- Colony-level bleaching

#### Correlation Analysis

Both:
- Pearson correlation
- Spearman correlation

were used to investigate:
- Linear relationships
- Monotonic non-linear relationships

#### Multicollinearity Analysis

Variance Inflation Factor (VIF) analysis identified:
- Strong redundancy among temperature-related variables
- Significant multicollinearity

#### Mutual Information Regression

Non-linear feature relevance analysis showed strong predictive influence from:
- Distance to shore
- Cyclone frequency
- Temperature-related variables

---

### 3. Feature Engineering & Normalization

To address severe feature skewness:

#### Transformations Used

| Distribution Type | Transformation |
|---|---|
| Right-skewed | Box-Cox |
| Left-skewed | Yeo-Johnson |

#### Additional Processing

- One-hot encoding for categorical variables
- Standard scaling for numerical variables
- Combined processed feature matrices

---

### 4. Machine Learning Models

#### Baseline Models

Simple regression baselines:
- Mean predictor
- Median predictor

Evaluation metrics:
- MAE
- RMSE
- R²

---

### Support Vector Regression (SVR)

Several SVM kernels were evaluated:

#### Kernels Tested

- RBF kernel
- Polynomial kernel (degree 2)
- Polynomial kernel (degree 3)

#### Findings

The notebook concludes that:
- SVMs struggled with scalability
- Non-linear kernels were computationally expensive
- Multicollinearity negatively impacted stability

---

### Ensemble Models

The analysis also investigates:
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost

Feature importance analysis was used to evaluate predictor contribution.

---

### Neural Networks

TensorFlow/Keras models were included using:
- Dense layers
- Dropout regularization
- Early stopping

---

## Evaluation Metrics

### Metrics Used

| Metric | Purpose |
|---|---|
| MAE | Robust average prediction error |
| RMSE | Penalizes larger prediction errors |
| R² Score | Overall model fit |

The baseline MAE reported in the notebook:

```text
MAEbaseline ≈ 11.29
```

---

## Key Insights

- Coral bleaching relationships are strongly non-linear
- Environmental variables exhibit substantial skewness
- Temperature-related features are highly collinear
- Ensemble methods are better suited than SVMs for this dataset
- Population-level and colony-level bleaching require separate models

---

## Repository Structure

```text
Reef_Analysis/
│
├── final_code_report.ipynb
├── coral-reef-global-bleaching/
│   ├── coral_whole.csv
│   └── ...
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/BopHockoB/Reef_Analysis.git
cd Reef_Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
final_code_report.ipynb
```

Run all notebook cells sequentially.

---

## Future Improvements

Potential future work includes:

- Hyperparameter optimization
- Cross-validation experiments
- Deep learning architecture tuning
- Time-series environmental analysis
- Spatial reef clustering
- Explainable AI (SHAP/LIME)
- Climate forecasting integration

---

## Authors

- Danylo Zemskyi
- Omari March

---

## License

This project is intended for educational and research purposes.
