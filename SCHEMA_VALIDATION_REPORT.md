# Schema Validation Report: Neurofibromatosis Dataset Columns

## Executive Summary

This report compares the 158 unique columns identified in the neurofibromatosis dataset against the properties defined in the NF.jsonld schema. Of these columns, **63 columns (39.9%) were not found in the schema**, indicating potential gaps between the actual data structure and the formal schema definition.

## Key Findings

### Schema Coverage Statistics
- **Total columns analyzed**: 158
- **Found in schema (exact match)**: 4 (2.5%)
- **Found in schema (case insensitive)**: 91 (57.6%)
- **NOT FOUND in schema**: 63 (39.9%)

### Breakdown by Classification

#### Computer-Generated Columns Not in Schema (30 columns)
These are system-generated metadata fields that appear in the data but are not formally defined in the schema:

**File System & Metadata (15 columns):**
- `modifiedOn`, `projectId`, `entityId`, `dataFileSizeBytes`
- `dataFileMD5Hex`, `path`, `dataFileName`, `dataFileBucket`
- `dataFileConcreteType`, `dataFileKey`, `Uuid`
- `FileAlias`, `FileDescription`, `FileUrl`, `FileViewId`

**Analysis & Reporting (4 columns):**
- `reportMilestone`, `analysisType`, `Resource_id`, `fileType`

**Study Management (11 columns):**
- `tissueType`, `disease`, `data_type`, `structureType`
- `BiospecimenKey`, `DatasetViewKey`, `EntityId`, `StudyKey`
- `FileTumorType`, `FileLongitudinalEventType`, `name`

#### Human-Annotated Columns Not in Schema (33 columns)
These are research-relevant fields that scientists manually curate but are not defined in the schema:

**Research Context (9 columns):**
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

**File-Level Annotations (11 columns):**
- `DataUseCodes`, `FileAssay`, `FileDesign`, `FileLevel`
- `FileSpecies`, `FileTissue`, `FileDataUseCodes`
- `FileLongitudinalGroup`, `FileLongitudinalSequenceIdentifier`
- `FileLongitudinalSequentialTimeElapsed`, `FileLongitudinalTimeElapsedUnit`
- `FileLongitudinalTotalTimeElapsed`

## Schema Completeness Assessment

### Well-Covered Areas
The schema effectively covers core biological and experimental metadata:
- Basic specimen information (specimenID, individualID, cellType)
- Genomic data types (assay, platform, species, fileFormat)
- NF-specific genetics (nf1Genotype, nf2Genotype, tumorType)
- Experimental conditions (treatment, perturbation methods)

### Schema Gaps

#### 1. File Management Infrastructure
The schema lacks definitions for many file system and data management fields that are essential for data operations:
- File storage metadata (bucket, path, size, MD5 checksums)
- Version control and provenance tracking
- System identifiers and handles

#### 2. Longitudinal Study Support
Multiple columns related to longitudinal data tracking are missing:
- Time series identifiers and sequences
- Longitudinal grouping mechanisms
- Time elapsed measurements

#### 3. Advanced Analysis Metadata
Research workflow and analysis method descriptions are underrepresented:
- Computational pipeline specifications
- Quality control metrics
- Analysis parameter documentation

#### 4. Multi-File Relationships
File-level annotations that describe relationships between related data files are not captured in the schema.

## Recommendations

### 1. Schema Extension Priority
**High Priority**: Add definitions for file management and system metadata fields that are critical for data operations.

**Medium Priority**: Include longitudinal study design fields to support time series research.

**Low Priority**: Extend analysis method vocabularies for better pipeline documentation.

### 2. Data Harmonization
Consider standardizing or deprecating some of the unmapped fields, particularly where similar concepts are expressed differently (e.g., `disease` vs `diagnosis`).

### 3. Documentation Updates
Update schema documentation to clarify the relationship between formal schema properties and operational data fields.

## Files Generated
- `column_classification_summary_with_schema_flags.csv`: Complete summary with schema validation flags
- `schema_column_comparison.py`: Analysis script for reproducible validation

---
*Report generated on: 2025-07-09*  
*Schema file: NF.jsonld*  
*Data source: 40 CSV files from neurofibromatosis research datasets*
