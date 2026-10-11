# ME 505 –  Steel Fatigue Dataset

## Dataset Overview

This dataset contains experimental data for predicting the fatigue strength of steels based on their chemical composition and processing conditions.

- **Number of observations:** 437
- **Original dataset:** 27 columns (25 features, 1 target, 1 identifier)
- **Processed dataset:** 26 columns (25 features and 1 target)
- **Target:** Fatigue strength (`Fatigue`), measured in MPa
- **Testing condition:** Rotating-bending fatigue strength at \(10^7\) cycles

## Data Source

The dataset was compiled from the Japanese National Institute for Materials Science (NIMS) fatigue database and distributed through Kaggle.

**Dataset:** [Steel Fatigue Strength Prediction – Kaggle](https://www.kaggle.com/datasets/chaozhuang/steel-fatigue-strength-prediction)

**Reference:** Agrawal et al. (2014), *Exploration of data science techniques to predict fatigue strength of steel from composition and processing parameters*, Integrating Materials and Manufacturing Innovation.

## Features and Units

The dataset contains several groups of features:

- **Chemical composition:** C, Si, Mn, P, S, Ni, Cr, Cu, Mo (wt.%)
- **Heat treatment:** Normalising, through-hardening, carburising and tempering parameters
- **Upstream processing:** Reduction ratio (`RedRatio`)
- **Inclusions:** `dA`, `dB`, `dC` (area fractions)
- **Target:** `Fatigue` (MPa)

Some processing-parameter units still require verification against the original documentation.

## Data Cleaning

The dataset was inspected using pandas to identify missing values, duplicate observations, infinite values, and unusual numerical values.

The following decisions were made:

1. Removed the `Sl. No.` column because it is only a serial identifier and does not describe the material.
2. Inspected the numerical distributions using `df.describe()`.
3. Identified sentinel values in processing-related columns. In particular, `CT = 30` indicates that carburisation was not performed.
4. Retained these sentinel values to preserve information about processing history.
5. Preserved unusual observations unless there was evidence that they represented data errors.

### Observations

- The carburisation-related columns `CT` and `DT` each contain 389 observations equal to 30.
- The columns `THT` and `TT` contain 59 and 11 values equal to 30, respectively.
- The meaning of sentinel values in other processing columns should be checked before modifying them.

## Reproducibility

The original dataset is preserved separately from the processed dataset. Cleaning and analysis are documented in the Jupyter notebook.

The project uses Python, NumPy, pandas, Matplotlib and scikit-learn.

The notebook should be executable from beginning to end using **Restart & Run All**.