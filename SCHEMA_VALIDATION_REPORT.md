# Schema Validation Report: Neurofibromatosis Dataset Columns

## Executive Summary

This report compares the 135 unique columns identified in the neurofibromatosis dataset against the properties defined in the NF.jsonld schema. Of these columns, **41 columns (30.4%) were not found in the schema**, indicating potential gaps between the actual data structure and the formal schema definition.

## Key Findings

### Schema Coverage Statistics
- **Total columns analyzed**: 135
- **Found in schema (exact match)**: 3 (2.2%)
- **Found in schema (case insensitive)**: 91 (67.4%)
- **NOT FOUND in schema**: 41 (30.4%)

### Breakdown by Classification

#### Computer-Generated Columns Not in Schema (20 columns)
These are system-generated metadata fields that appear in the data but are not formally defined in the schema:

**File System & Metadata (11 columns):**
- `modifiedOn`, `projectId`, `entityId`, `dataFileSizeBytes`
- `dataFileMD5Hex`, `path`, `dataFileName`, `dataFileBucket`
- `dataFileConcreteType`, `dataFileKey`, `Uuid`

**Analysis & Reporting (4 columns):**
- `reportMilestone`, `analysisType`, `Resource_id`, `fileType`

**Study Management (5 columns):**
- `tissueType`, `disease`, `data_type`, `structureType`, `name`

#### Human-Annotated Columns Not in Schema (23 columns)
These are research-relevant fields that scientists manually curate but are not defined in the schema:

**Research Context (8 columns):**
- `consortium`, `accessTeam`, `study`, `modelOf`
- `modelSystem`, `caseNumber`, `studySite`, `sampleIdentifier`
- `modelSystemStrainNomenclature`

**Experimental Design (8 columns):**
- `transplantationDonorTissue`, `transplantationDonorSpecies`
- `secondCompoundName`, `compoundDoseRange`, `detailed_diagnosis`
- `bodyPart`, `age_months`, `disease`

**Analysis Methods (5 columns):**
- `differentialExpressionMethod`, `multipleTestingAdjustmentMethod`
- `alignmentMethod`, `transcriptQuantificationMethod`, `chemicalStructure`

**General (2 columns):**
- `name`

## Schema Completeness Assessment

### Well-Covered Areas
The schema effectively covers core biological and experimental metadata:
- Basic specimen information (specimenID, individualID, cellType)
- Genomic data types (assay, platform, species, fileFormat)
- NF-specific genetics (nf1Genotype, nf2Genotype, tumorType)
- Experimental conditions (treatment, perturbation methods)

### Schema Gaps

#### 1. File Management Infrastructure
The schema lacks definitions for file system and data management fields that are essential for data operations:
- File storage metadata (bucket, path, size, MD5 checksums)
- Version control and provenance tracking
- System identifiers and handles

#### 2. Research Context and Methodology
Research workflow and analysis method descriptions are underrepresented:
- Computational pipeline specifications (alignment methods, expression quantification)
- Study design metadata (consortium information, case numbers)
- Chemical structure and compound information

#### 3. Extended Biological Annotations
Some biological and clinical fields that researchers commonly use are missing:
- Detailed diagnostic classifications
- Donor tissue and species information for transplantation studies
- Model system strain nomenclature

## Recommendations

### 1. Schema Extension Priority
**High Priority**: Add definitions for file management and system metadata fields that are critical for data operations.

**Medium Priority**: Include research methodology and analysis pipeline fields to better document computational workflows.

**Low Priority**: Extend biological annotation vocabularies for specialized research contexts.

### 2. Data Harmonization
Consider standardizing or deprecating some of the unmapped fields, particularly where similar concepts are expressed differently (e.g., `disease` vs `diagnosis`).

### 3. Documentation Updates
Update schema documentation to clarify the relationship between formal schema properties and operational data fields.

## Files Generated
- `column_classification_summary_with_schema_flags.csv`: Complete summary with schema validation flags
- `schema_column_comparison.py`: Analysis script for reproducible validation

---
*Report generated on: 2025-01-22*  
*Schema file: NF.jsonld*  
*Data source: 38 CSV files from neurofibromatosis research datasets*
