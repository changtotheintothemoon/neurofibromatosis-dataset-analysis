# Neurofibromatosis Research Dataset Analysis

## Overview

This repository contains tools for analyzing CSV files from neurofibromatosis research datasets to identify and classify columns as either **computer-generated** or **human-annotated**. The analysis helps researchers understand which data fields contain system metadata versus human-curated scientific annotations.

## Dataset Structure

```
pz-nf-testing-data/
├── ground_truth/          # 40 CSV files with research data
├── unstructured_input/     # PDFs and compressed XML files
├── analysis scripts/       # Python scripts for data analysis
└── output files/          # Generated analysis results
```

## Analysis Results Summary

### Dataset Statistics
- **Total CSV files analyzed:** 40
- **Total unique computer-generated columns:** 77
- **Total unique human-annotated columns:** 89
- **Analysis approach:** Pattern recognition + data content analysis

### Most Common Computer-Generated Columns

| Column Name | Frequency | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `id` | 40 files | Synapse identifiers | `syn30058767`, `syn33395848` |
| `dataSubtype` | 38 files | Data processing categories | `raw`, `processed`, `normalized` |
| `dataType` | 38 files | Data type classifications | `genomicVariants`, `geneExpression` |
| `fileFormat` | 38 files | File format specifications | `fastq`, `csv`, `bam`, `idat` |
| `individualID` | 38 files | Individual identifiers | `MPNST-1`, `SYN_NF_001` |
| `resourceType` | 38 files | Resource classifications | `experimentalData` |
| `specimenID` | 38 files | Specimen identifiers | `MPNST-1`, `MS378A` |
| `studyId` | 38 files | Study identifiers | `syn22392179`, `syn11681835` |
| `tumorType` | 38 files | Tumor type classifications | `Malignant Peripheral Nerve Sheath Tumor` |
| `nf1Genotype` | 36 files | NF1 genotype status | `-/-`, `+/-`, `Unknown` |

### Most Common Human-Annotated Columns

| Column Name | Frequency | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `assay` | 38 files | Experimental assay types | `RNA-seq`, `SNP array`, `methylation array` |
| `species` | 38 files | Species information | `Homo sapiens`, `Mus musculus` |
| `fundingAgency` | 36 files | Funding sources | `NTAP`, `CTF`, `NIH-NCI` |
| `sex` | 36 files | Gender information | `Female`, `Male` |
| `isCellLine` | 34 files | Cell line indicators | `Yes`, `No` |
| `initiative` | 32 files | Research initiatives | `Synodos`, `Francis S. Collins Scholars Program` |
| `organ` | 31 files | Organ information | `brain`, `skin`, `nerves` |
| `tissue` | 31 files | Tissue types | `primary tumor`, `blood`, `nerve tissue` |
| `readPair` | 28 files | Sequencing read pair info | `1`, `2`, `150` |
| `age` | 22 files | Age information | `11.67`, `19`, `54` |

## Classification Methodology

The analysis script (`identify_computer_generated_columns.py`) uses multiple sophisticated approaches:

### 1. Pattern Recognition
Identifies system-generated patterns including:
- **IDs and handles:** Fields ending with `ID`, `Key`, containing `handle`, `uuid`, `guid`
- **Hashes and checksums:** Fields containing `md5`, `hash`, `etag`
- **System metadata:** `createdOn`, `modifiedOn`, `createdBy`, `modifiedBy`
- **File system:** `path`, `filename`, `bucket`, `size`, `format`
- **Technical identifiers:** `component`, `alias`, `benefactor`, `parent`

### 2. Data Content Analysis
Examines sample values to detect:
- **UUID formats:** `42bce1a4-63ba-4ec8-b221-ea981151e88a`
- **Synapse IDs:** `syn33395848`
- **Long numeric IDs:** `1658525458801`
- **Hash values:** `3ccb295c73ea50bfd9138249e875a0b1`
- **URLs:** `https://www.synapse.org/Synapse:syn60247805`
- **File paths:** System-generated directory structures

### 3. Content Distinction
Differentiates between:
- **Human-readable descriptions:** Scientific terminology, experimental conditions
- **System codes:** Automatically generated identifiers and metadata
- **Research annotations:** Manually curated experimental parameters

## Key Research Insights

### Computer-Generated Data Characteristics
- **System identifiers:** Synapse platform IDs, UUIDs, hash values
- **File metadata:** Automatically captured file information
- **Processing metadata:** System timestamps, version numbers, ETags
- **Data classifications:** Standardized categorical assignments

### Human-Annotated Data Characteristics
- **Experimental design:** Assay types, experimental conditions
- **Biological information:** Species, organs, tissues, genotypes
- **Clinical data:** Age, sex, diagnosis, tumor types
- **Research context:** Funding agencies, initiatives, study names

## Scripts and Tools

### `identify_computer_generated_columns.py`
**Purpose:** Main analysis script for column classification
**Features:**
- Pattern-based column name analysis
- Sample data content examination
- Comprehensive reporting with reasoning
- CSV output generation

**Usage:**
```bash
python3 identify_computer_generated_columns.py
```

### `analyze_csv_columns_simple.py`
**Purpose:** Basic CSV structure analysis
**Features:**
- Column pattern grouping
- File structure comparison
- Frequency analysis

## Output Files

### `computer_vs_human_columns_detailed.csv`
Detailed per-file analysis including:
- File name
- Column name
- Classification (Computer Generated/Human Annotated)
- Reasoning for classification
- Sample values
- Pattern analysis results

### `column_classification_summary.csv`
Summary statistics including:
- Column name
- Classification type
- Frequency across files
- Example files containing the column

## Applications

This analysis is valuable for:

1. **Data Processing Pipelines:** Distinguish metadata from research data
2. **Quality Control:** Identify inconsistencies in data annotation
3. **Data Integration:** Understand which fields are standardized vs. custom
4. **Research Automation:** Focus on human-curated fields for analysis
5. **Documentation:** Understand dataset structure and provenance

## Technical Notes

### Dependencies
- Python 3.6+
- Standard library modules: `csv`, `re`, `os`, `collections`
- No external dependencies required

### Performance
- Analyzes 40 CSV files in under 30 seconds
- Memory efficient processing
- Handles large files through sampling

### Accuracy
- Multi-layered classification approach
- Pattern matching with data validation
- Human-interpretable reasoning for each classification

## Dataset Context

This analysis was performed on a comprehensive neurofibromatosis research dataset containing:
- **Genomic data:** Whole genome/exome sequencing, RNA-seq
- **Epigenomic data:** Methylation arrays, ChIP-seq, ATAC-seq
- **Clinical data:** Patient demographics, tumor characteristics
- **Experimental metadata:** Platform information, processing details
- **System metadata:** File management, version control, provenance

The classification helps researchers focus on scientifically relevant annotations while understanding the technical infrastructure supporting the data.

---

*Generated on July 7, 2025*  
*Analysis covers 40 CSV files from neurofibromatosis research datasets*
