.. _input:

#############
Input Documentation
#############

This document describes the input data structure, processing steps, and expected outputs for the **PetroCast** application.

---

## **1️⃣ Data Location**
The application expects input data files in the following locations:

- **Raw input data** (historical production records, with year, production, unit as a csv-file ): `data/raw/`
- **Processed data** (URR estimates, formatted data): `data/processed/`
- **Configuration files** (user settings, set up the files you want to use for your analysis): `config.toml`

Example file paths:
```toml
dataset = "data/raw/data1_oil_his_havard.csv"
urr_file = "data/processed/Oil_estimate.csv"
unit = "EJ"
```

---

## **2️⃣ Analysis Types**
The application supports the following modeling approaches:

1. **Hubbert Curve Model** – Models resource extraction using a logistic function.
2. **Laherrère Bell Curve Model** – Uses a hyperbolic cosine function to fit extraction trends.
3. **Cumulative Production Calculation** – Computes total extracted resources over time.

---

## **3️⃣ Output Location and Formats**
### **Output Storage:**
- **Processed results**: `data/output/`
- **Visualization plots**: `plots/`
- **Cumulative analysis reports**: `reports/`

### **Output Formats:**
- **CSV** – Processed datasets (`output.csv`)
- **JSON** – Structured report output (`results.json`)
- **PNG/JPG** – Visualization charts (`model_plot.png`)

---

## **4️⃣ Operations & Execution**
### **Running the Application**
Use the following command to execute the analysis:
```sh
petrocast --config config.toml --urr-key "Estimate1"
```
Or run manually via Python:
```sh
python -m petrocast --config config.toml --urr-key "Estimate 1"
```

### **Command-Line Arguments:**
- `--config <file>` → Specifies the TOML configuration file.
- `--urr-key <estimate>` → Selects a URR estimate from the processed file.

This document serves as a reference for users setting up and running **PetroCast** effectively.
