# Filtered Evaluatable Data Report

Generated: July 22, 2025

## Overview
This folder contains filtered versions of the 38 ground truth CSV files, containing only the columns marked as "Evaluate" in the CIM curated schema column list. The filtering process removes duplicate columns and columns with insufficient meaningful data.

## Source Files
- **Schema File**: `CIM_curated_NF_schema_column_list_7_11_25.csv`
- **Ground Truth Directory**: `ground_truth/`
- **Output Directory**: `filtered_evaluatable_data/`

## Processing Results

### Evaluatable Columns Identified
Total unique columns marked as "Evaluate": **81 columns** (removed 5 duplicates from original 86)

Key evaluatable columns include:
- Core identifiers: `individualID`, `specimenID`, `studyId`
- Data types: `dataSubtype`, `dataType`, `fileFormat`
- Clinical data: `diagnosis`, `tumorType`, `age`, `sex`
- Experimental data: `assay`, `platform`, `readLength`
- Biological context: `cellType`, `tissue`, `organ`
- Genetic information: `nf1Genotype`, `nf2Genotype`
- And many more...

### Data Quality Improvements
The improved filtering process:
1. **Removes duplicate columns** from the schema list
2. **Excludes columns with no meaningful data** (>75% empty, "Not Applicable", "Unknown", or "NA")
3. **Preserves only columns with sufficient data quality**

### Files Processed
Successfully processed: **38 CSV files**

All files from `nf_1.csv` through `nf_38.csv` were filtered to contain only evaluatable columns with meaningful data.

### Column Reduction Examples
- `nf_1.csv`: 30 → 25 columns (removed `nf2Genotype`, `progressReportNumber` - insufficient data)
- `nf_13.csv`: 63 → 26 columns (removed 14 columns with insufficient data)
- `nf_28.csv`: 78 → 16 columns (removed 27 columns with insufficient data)
- `nf_38.csv`: 69 → 5 columns (only 5 columns had meaningful data)

### Data Quality Metrics
The filtering removed columns that had:
- Empty values in >75% of rows
- "Not Applicable" in >75% of rows
- "Unknown" values in >75% of rows
- "NA" values in >75% of rows

## File Naming Convention
All filtered files follow the pattern: `filtered_[original_filename]`

## Usage
These filtered CSV files contain only the columns that have been manually curated for evaluation AND have sufficient meaningful data, making them ideal for focused analysis of high-quality data fields in the neurofibromatosis dataset.

## Script Features
The filtering was performed using `filter_evaluatable_columns.py` which:
1. Reads the schema CSV to identify "Evaluate" columns
2. Removes duplicate column names from the schema
3. Processes each ground truth CSV file
4. Filters to keep only evaluatable columns present in each file
5. Removes columns lacking meaningful data (25% threshold)
6. Saves filtered results with the `filtered_` prefix
7. Provides detailed reporting on removed columns

## Data Quality Notes
- All 38 files were successfully processed
- Significant data quality improvements through removal of low-value columns
- Column counts vary significantly by file based on data completeness
- Some files (like `nf_38.csv`) had very few columns with meaningful data
- The 25% meaningful data threshold ensures retained columns have substantial information content
