# CIM Update vs Ground Truth Comparison Report

Generated: July 22, 2025

## Overview

This report compares the manually curated CIM_update files against the original ground_truth files. The CIM (you) made strategic modifications to remove columns with constant values, non-deducible information from study papers alone, and administrative metadata that doesn't contribute to scientific analysis.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Files Compared | 38 |
| Average Columns in Ground Truth | 55.9 |
| Average Columns in CIM Update | 17.6 |
| Average Column Reduction | 68.5% |

### Most Dramatic Transformations
| File | Original | Curated | Reduction | Reason |
|------|----------|---------|-----------|---------|
| nf_38.csv | 69 columns | 3 columns | 95.7% | Extremely sparse data, only study metadata remained |
| nf_28.csv | 78 columns | 8 columns | 89.7% | Heavy platform metadata, mostly derived/calculated fields |
| nf_22.csv | 50 columns | 6 columns | 88.0% | Redundant study information, constant values |
| nf_21.csv | 50 columns | 7 columns | 86.0% | Similar to nf_22, administrative overhead |
| nf_20.csv | 57 columns | 10 columns | 82.5% | Experimental metadata with low information content |

## Column Removal Patterns

The following columns were strategically removed across multiple files:

| Column Name | Files Removed From | Category | Rationale |
|-------------|-------------------|----------|-----------|
| `id` | 38/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `name` | 38/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `studyId` | 38/38 | Study Metadata | Administrative metadata, constant across datasets |
| `fundingAgency` | 35/38 | Funding/Administrative | Often not deducible from study papers alone |
| `resourceType` | 35/38 | Study Metadata | Administrative metadata, constant across datasets |
| `studyName` | 30/38 | Study Metadata | Administrative metadata, constant across datasets |
| `initiative` | 26/38 | Funding/Administrative | Often not deducible from study papers alone |
| `benefactorId` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `cellType` | 26/38 | Unknown | Manual curation decision |
| `createdBy` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `createdOn` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `etag` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `modifiedOn` | 26/38 | Unknown | Manual curation decision |
| `parentId` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `projectId` | 26/38 | Unknown | Manual curation decision |
| `type` | 26/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `nf2Genotype` | 25/38 | Constant/Derived | Often constant ('Unknown') or derivable from other fields |
| `currentVersion` | 24/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `dataFileHandleId` | 23/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `modifiedBy` | 23/38 | Platform Generated | System-generated metadata, not relevant for analysis |

## Detailed File-by-File Analysis

### Column Reduction Summary

| File | Original Columns | CIM Columns | Reduction | Key Removals |
|------|-----------------|-------------|-----------|--------------|
| nf_1.csv | 30 | 19 | 36.7% | ageUnit, entityId, fundingAgency, id, initiative (+ 6 more) |
| nf_10.csv | 27 | 19 | 29.6% | Resource_id, disease, fundingAgency, id, name (+ 3 more) |
| nf_11.csv | 27 | 20 | 25.9% | Resource_id, dataSubtype, disease, fundingAgency, id (+ 3 more) |
| nf_12.csv | 40 | 30 | 25.0% | Resource_id, accessTeam, accessType, entityId, fundingAgency (+ 5 more) |
| nf_13.csv | 63 | 18 | 71.4% | accessType, benefactorId, bodyPart, cellType, consortium (+ 40 more) |
| nf_14.csv | 63 | 20 | 68.3% | accessType, benefactorId, bodyPart, consortium, createdBy (+ 38 more) |
| nf_15.csv | 63 | 19 | 69.8% | accessType, benefactorId, bodyPart, cellType, consortium (+ 39 more) |
| nf_16.csv | 63 | 14 | 77.8% | accessType, benefactorId, bodyPart, cellType, consortium (+ 44 more) |
| nf_17.csv | 57 | 13 | 77.2% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 39 more) |
| nf_18.csv | 57 | 13 | 77.2% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 39 more) |
| nf_19.csv | 57 | 18 | 68.4% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 34 more) |
| nf_2.csv | 46 | 30 | 34.8% | ageUnit, aliquotID, cellType, comments, fundingAgency (+ 11 more) |
| nf_20.csv | 57 | 10 | 82.5% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 42 more) |
| nf_21.csv | 50 | 7 | 86.0% | Component, Id, accessTeam, accessType, age (+ 38 more) |
| nf_22.csv | 50 | 6 | 88.0% | Component, Id, accessTeam, accessType, age (+ 39 more) |
| nf_23.csv | 50 | 7 | 86.0% | Component, Id, accessTeam, accessType, age (+ 38 more) |
| nf_24.csv | 67 | 12 | 82.1% | Filename, accessTeam, accessType, age, benefactorId (+ 50 more) |
| nf_25.csv | 67 | 23 | 65.7% | Filename, accessTeam, accessType, age, assay (+ 39 more) |
| nf_26.csv | 64 | 16 | 75.0% | accessTeam, accessType, benefactorId, caseNumber, comments (+ 43 more) |
| nf_27.csv | 64 | 24 | 62.5% | accessTeam, accessType, age, benefactorId, caseNumber (+ 35 more) |
| nf_28.csv | 78 | 8 | 89.7% | Component, Uuid, accessTeam, accessType, age_months (+ 65 more) |
| nf_29.csv | 78 | 14 | 82.1% | Uuid, accessTeam, accessType, age_months, analysisType (+ 59 more) |
| nf_3.csv | 47 | 25 | 46.8% | ageUnit, aliquotID, cellType, comments, dissociationMethod (+ 17 more) |
| nf_30.csv | 78 | 8 | 89.7% | Component, Uuid, accessTeam, accessType, age_months (+ 65 more) |
| nf_31.csv | 68 | 27 | 60.3% | alignmentMethod, analysisType, benefactorId, chemicalStructure, compoundDose (+ 36 more) |
| nf_32.csv | 68 | 14 | 79.4% | alignmentMethod, analysisType, benefactorId, chemicalStructure, compoundDose (+ 49 more) |
| nf_33.csv | 69 | 18 | 73.9% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 46 more) |
| nf_34.csv | 69 | 23 | 66.7% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 41 more) |
| nf_35.csv | 69 | 25 | 63.8% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 39 more) |
| nf_36.csv | 69 | 12 | 82.6% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 52 more) |
| nf_37.csv | 69 | 26 | 62.3% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 38 more) |
| nf_38.csv | 69 | 3 | 95.7% | Component, Uuid, age, ageUnit, aliquotID (+ 61 more) |
| nf_4.csv | 44 | 22 | 50.0% | ageUnit, aliquotID, cellType, comments, currentVersion (+ 17 more) |
| nf_5.csv | 31 | 20 | 35.5% | ageUnit, entityId, fundingAgency, id, initiative (+ 6 more) |
| nf_6.csv | 31 | 20 | 35.5% | ageUnit, eTag, entityId, fundingAgency, id (+ 6 more) |
| nf_7.csv | 28 | 18 | 35.7% | ageUnit, entityId, fundingAgency, id, initiative (+ 5 more) |
| nf_8.csv | 46 | 22 | 52.2% | Uuid, ageUnit, aliquotID, cellType, comments (+ 19 more) |
| nf_9.csv | 50 | 26 | 48.0% | Uuid, age, ageUnit, aliquotID, cellType (+ 19 more) |

## Categories of Removed Columns

### Platform-Generated Metadata
These columns are automatically generated by data platforms and don't provide scientific value:
- `id` (removed from 38 files)
- `name` (removed from 38 files)
- `benefactorId` (removed from 26 files)
- `createdBy` (removed from 26 files)
- `createdOn` (removed from 26 files)
- `etag` (removed from 26 files)
- `parentId` (removed from 26 files)
- `type` (removed from 26 files)
- `currentVersion` (removed from 24 files)
- `dataFileHandleId` (removed from 23 files)
- `modifiedBy` (removed from 23 files)
- `entityId` (removed from 21 files)

### Funding and Administrative Information
These fields are often not available in published papers and represent administrative rather than scientific data:
- `fundingAgency` (removed from 35 files)
- `initiative` (removed from 26 files)

### Study Metadata
Constant across datasets or administrative in nature:
- `studyId` (removed from 38 files)
- `resourceType` (removed from 35 files)
- `studyName` (removed from 30 files)
- `progressReportNumber` (removed from 18 files)

### Unit and Descriptive Fields
Redundant information that can be standardized or is implicit:
- `ageUnit` (removed from 15 files)
- `timePointUnit` (removed from 15 files)

### Other Removed Columns
Additional columns removed for data quality or relevance reasons:
- `cellType` (removed from 26 files)
- `modifiedOn` (removed from 26 files)
- `projectId` (removed from 26 files)
- `tumorType` (removed from 20 files)
- `dataFileSizeBytes` (removed from 19 files)
- `dataFileMD5Hex` (removed from 17 files)
- `libraryPrep` (removed from 17 files)
- `sex` (removed from 17 files)
- `isPrimaryCell` (removed from 16 files)
- `readStrandOrigin` (removed from 16 files)
- `readPair` (removed from 16 files)
- `transplantationType` (removed from 16 files)
- `comments` (removed from 16 files)
- `accessType` (removed from 15 files)
- `dissociationMethod` (removed from 15 files)
- `nf1Genotype` (removed from 15 files)
- `readPairOrientation` (removed from 15 files)
- `eTag` (removed from 15 files)
- `libraryPreparationMethod` (removed from 14 files)
- `organ` (removed from 14 files)
- `consortium` (removed from 13 files)
- `path` (removed from 13 files)
- `experimentalCondition` (removed from 13 files)
- `age` (removed from 13 files)
- `tissue` (removed from 13 files)
- `isCellLine` (removed from 12 files)
- `isStranded` (removed from 12 files)
- `modelSystemName` (removed from 12 files)
- `accessTeam` (removed from 11 files)
- `dataFileBucket` (removed from 11 files)
- `description` (removed from 11 files)
- `aliquotID` (removed from 11 files)
- `specimenPreparationMethod` (removed from 11 files)
- `Uuid` (removed from 11 files)
- `readLength` (removed from 10 files)
- `dataFileConcreteType` (removed from 9 files)
- `dataFileKey` (removed from 9 files)
- `dataFileName` (removed from 9 files)
- `runType` (removed from 9 files)
- `compoundName` (removed from 9 files)
- `drugScreenType` (removed from 9 files)
- `genePerturbed` (removed from 9 files)
- `study` (removed from 9 files)
- `readDepth` (removed from 9 files)
- `isMultiIndividual` (removed from 8 files)
- `isMultiSpecimen` (removed from 8 files)
- `specimenIdSource` (removed from 8 files)
- `genePerturbationTechnology` (removed from 8 files)
- `genePerturbationType` (removed from 8 files)
- `transplantationDonorTissue` (removed from 8 files)
- `individualID` (removed from 8 files)
- `specimenID` (removed from 8 files)
- `diagnosis` (removed from 8 files)
- `transplantationRecipientSpecies` (removed from 8 files)
- `parentSpecimenID` (removed from 8 files)
- `transplantationRecipientTissue` (removed from 7 files)
- `platform` (removed from 7 files)
- `individualIdSource` (removed from 6 files)
- `compoundDoseUnit` (removed from 6 files)
- `secondCompoundName` (removed from 6 files)
- `transplantationDonorSpecies` (removed from 6 files)
- `Component` (removed from 6 files)
- `disease` (removed from 5 files)
- `experimentalTimePoint` (removed from 5 files)
- `libraryStrand` (removed from 5 files)
- `modelOf` (removed from 5 files)
- `reportMilestone` (removed from 5 files)
- `workflow` (removed from 5 files)
- `workflowLink` (removed from 5 files)
- `analysisType` (removed from 5 files)
- `differentialExpressionMethod` (removed from 5 files)
- `experimentalTimepoint` (removed from 5 files)
- `nucleicAcidSource` (removed from 5 files)
- `bodyPart` (removed from 4 files)
- `detailed_diagnosis` (removed from 4 files)
- `pain` (removed from 4 files)
- `modelSystem` (removed from 4 files)
- `isXenograft` (removed from 4 files)
- `Resource_id` (removed from 3 files)
- `Id` (removed from 3 files)
- `age_months` (removed from 3 files)
- `averageBaseQuality` (removed from 3 files)
- `averageInsertSize` (removed from 3 files)
- `averageReadLength` (removed from 3 files)
- `expressionUnit` (removed from 3 files)
- `fileType` (removed from 3 files)
- `genomicReference` (removed from 3 files)
- `pairsOnDifferentChr` (removed from 3 files)
- `readsDuplicatedPercent` (removed from 3 files)
- `readsMappedPercent` (removed from 3 files)
- `sampleIdentifier` (removed from 3 files)
- `tissueType` (removed from 3 files)
- `totalReads` (removed from 3 files)
- `dataSubtype` (removed from 2 files)
- `Filename` (removed from 2 files)
- `experimentId` (removed from 2 files)
- `modelSystemStrainNomenclature` (removed from 2 files)
- `assay` (removed from 2 files)
- `caseNumber` (removed from 2 files)
- `data_type` (removed from 2 files)
- `studySite` (removed from 2 files)
- `alignmentMethod` (removed from 2 files)
- `chemicalStructure` (removed from 2 files)
- `compoundDose` (removed from 2 files)
- `compoundDoseRange` (removed from 2 files)
- `multipleTestingAdjustmentMethod` (removed from 2 files)
- `structureType` (removed from 2 files)
- `transcriptQuantificationMethod` (removed from 2 files)
- `dataType` (removed from 1 files)
- `fileFormat` (removed from 1 files)
- `species` (removed from 1 files)
- `targetDepth` (removed from 1 files)

## Practical Example: nf_1.csv Transformation

### Before (Ground Truth - 30 columns):
```
id,name,age,ageUnit,assay,dataSubtype,dataType,diagnosis,entityId,fileFormat,fundingAgency,individualID,initiative,isCellLine,isPrimaryCell,isXenograft,modelSystemName,nf1Genotype,nf2Genotype,nucleicAcidSource,parentSpecimenID,platform,progressReportNumber,resourceType,sex,species,specimenID,studyId,studyName,tumorType
```

### After (CIM Update - 19 columns):
```
dataSubtype,dataType,fileFormat,individualID,specimenID,tumorType,nf1Genotype,diagnosis,platform,parentSpecimenID,modelSystemName,assay,species,sex,isCellLine,isPrimaryCell,age,nucleicAcidSource,isXenograft
```

### Removed Columns (11 total):
- **Platform Generated**: `id`, `name`, `entityId` (system metadata)
- **Administrative**: `studyId`, `studyName`, `resourceType`, `progressReportNumber` (constant across datasets)
- **Funding/Initiative**: `fundingAgency`, `initiative` (not in papers)
- **Unit Information**: `ageUnit` (standardized to numeric)
- **Low Quality Data**: `nf2Genotype` (mostly "Unknown")

### Impact:
- **36.7% reduction** in columns
- **Improved data quality** - removed sparse/constant fields
- **Better focus** on scientifically relevant variables
- **Enhanced extractability** from published research papers

## Data Quality Improvements

The CIM curation process focused on:

1. **Removing Non-Deducible Information**: Fields like funding agencies and initiatives that often don't appear in published papers
2. **Eliminating Constant Values**: Columns with mostly "Unknown", "Not Applicable", or constant values
3. **Streamlining for Analysis**: Keeping only scientifically relevant columns that can be reliably extracted from publications
4. **Standardizing Format**: Consistent column selection across all files

## Curation Principles

The manual curation followed these principles:

- **Scientific Relevance**: Only keep columns that contribute to research analysis
- **Paper Extractability**: Remove information that cannot be reliably extracted from study papers
- **Data Quality**: Eliminate columns with insufficient meaningful data
- **Administrative Cleanup**: Remove platform-generated and administrative metadata
- **Consistency**: Apply uniform standards across all datasets

### Most Frequently Retained Columns
These columns were prioritized across the dataset for their scientific value:

| Column | Retained in Files | Priority | Rationale |
|--------|------------------|----------|-----------|
| `fileFormat` | 37/38 | High | Essential for data interpretation |
| `dataType` | 37/38 | High | Core data classification |
| `dataSubtype` | 36/38 | High | Detailed data categorization |
| `assay` | 36/38 | High | Experimental method information |
| `species` | 34/38 | High | Biological context |
| `specimenID` | 30/38 | Medium | Sample identification |
| `individualID` | 30/38 | Medium | Subject identification |
| `diagnosis` | 30/38 | Medium | Clinical information |
| `platform` | 29/38 | Medium | Technical platform data |

These retained columns represent the core scientific and technical information needed for meaningful analysis while eliminating administrative overhead.

## Files Processed

All 38 neurofibromatosis dataset files were successfully processed and curated.

---

*This report was generated automatically by comparing the CIM_update folder contents with the ground_truth folder contents.*
