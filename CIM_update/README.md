# CIM Update vs Ground Truth Comparison Report

Generated: July 22, 2025

## Overview

This report compares the manually curated CIM_update files against the original ground_truth files. The CIM (you) made strategic modifications to remove columns with constant values, non-deducible information from study papers alone, and administrative metadata that doesn't contribute to scientific analysis.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Files Compared | 38 |
| Average Columns in Ground Truth | 55.9 |
| Average Columns in CIM Update | 24.8 |
| Average Column Reduction | 55.5% |

## Column Removal Patterns

The following columns were strategically removed across multiple files:

| Column Name | Files Removed From | Category | Rationale |
|-------------|-------------------|----------|-----------|
| `id` | 38/38 | Platform Generated | System-generated metadata, not relevant for analysis |
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
| `entityId` | 21/38 | Platform Generated | System-generated metadata, not relevant for analysis |
| `dataFileSizeBytes` | 19/38 | Unknown | Manual curation decision |
| `tumorType` | 19/38 | Unknown | Manual curation decision |
| `dataFileMD5Hex` | 17/38 | Unknown | Manual curation decision |
| `libraryPrep` | 17/38 | Unknown | Manual curation decision |
| `sex` | 17/38 | Unknown | Manual curation decision |
| `isPrimaryCell` | 16/38 | Unknown | Manual curation decision |

## Detailed File-by-File Analysis

### Column Reduction Summary

| File | Original Columns | CIM Columns | Reduction | Key Removals |
|------|-----------------|-------------|-----------|--------------|
| nf_1.csv | 30 | 26 | 13.3% | entityId, id, nf2Genotype, progressReportNumber |
| nf_10.csv | 27 | 24 | 11.1% | Resource_id, disease, id |
| nf_11.csv | 27 | 24 | 11.1% | Resource_id, disease, id |
| nf_12.csv | 40 | 36 | 10.0% | Resource_id, accessTeam, entityId, id |
| nf_13.csv | 63 | 27 | 57.1% | accessType, benefactorId, bodyPart, cellType, consortium (+ 31 more) |
| nf_14.csv | 63 | 27 | 57.1% | benefactorId, bodyPart, consortium, createdBy, createdOn (+ 31 more) |
| nf_15.csv | 63 | 26 | 58.7% | benefactorId, bodyPart, cellType, consortium, createdBy (+ 32 more) |
| nf_16.csv | 63 | 21 | 66.7% | benefactorId, bodyPart, cellType, consortium, createdBy (+ 37 more) |
| nf_17.csv | 57 | 19 | 66.7% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 33 more) |
| nf_18.csv | 57 | 19 | 66.7% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 33 more) |
| nf_19.csv | 57 | 24 | 57.9% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 28 more) |
| nf_2.csv | 46 | 38 | 17.4% | aliquotID, cellType, comments, id, modelSystemName (+ 3 more) |
| nf_20.csv | 57 | 16 | 71.9% | benefactorId, cellType, compoundDoseUnit, compoundName, consortium (+ 36 more) |
| nf_21.csv | 50 | 16 | 68.0% | Id, accessTeam, accessType, age, benefactorId (+ 29 more) |
| nf_22.csv | 50 | 14 | 72.0% | Id, accessTeam, accessType, age, benefactorId (+ 31 more) |
| nf_23.csv | 50 | 15 | 70.0% | Id, accessTeam, accessType, age, benefactorId (+ 30 more) |
| nf_24.csv | 67 | 19 | 71.6% | Filename, accessTeam, accessType, age, benefactorId (+ 43 more) |
| nf_25.csv | 67 | 29 | 56.7% | Filename, accessTeam, accessType, age, assay (+ 33 more) |
| nf_26.csv | 64 | 25 | 60.9% | accessTeam, benefactorId, caseNumber, comments, createdBy (+ 34 more) |
| nf_27.csv | 64 | 32 | 50.0% | accessTeam, age, benefactorId, caseNumber, comments (+ 27 more) |
| nf_28.csv | 78 | 17 | 78.2% | Component, Uuid, accessTeam, age_months, analysisType (+ 56 more) |
| nf_29.csv | 78 | 22 | 71.8% | Uuid, accessTeam, age_months, analysisType, averageBaseQuality (+ 51 more) |
| nf_3.csv | 47 | 34 | 27.7% | aliquotID, cellType, comments, entityId, id (+ 8 more) |
| nf_30.csv | 78 | 17 | 78.2% | Component, Uuid, accessTeam, age_months, analysisType (+ 56 more) |
| nf_31.csv | 68 | 32 | 52.9% | alignmentMethod, analysisType, benefactorId, chemicalStructure, compoundDose (+ 31 more) |
| nf_32.csv | 68 | 19 | 72.1% | alignmentMethod, analysisType, benefactorId, chemicalStructure, compoundDose (+ 44 more) |
| nf_33.csv | 69 | 27 | 60.9% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 37 more) |
| nf_34.csv | 69 | 33 | 52.2% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 31 more) |
| nf_35.csv | 69 | 34 | 50.7% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 30 more) |
| nf_36.csv | 69 | 21 | 69.6% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 43 more) |
| nf_37.csv | 69 | 35 | 49.3% | Uuid, age, ageUnit, aliquotID, benefactorId (+ 29 more) |
| nf_38.csv | 69 | 6 | 91.3% | Component, Uuid, age, ageUnit, aliquotID (+ 58 more) |
| nf_4.csv | 44 | 31 | 29.5% | aliquotID, cellType, comments, currentVersion, experimentalCondition (+ 8 more) |
| nf_5.csv | 31 | 27 | 12.9% | entityId, id, nf2Genotype, progressReportNumber |
| nf_6.csv | 31 | 27 | 12.9% | eTag, entityId, id, progressReportNumber |
| nf_7.csv | 28 | 25 | 10.7% | entityId, id, progressReportNumber |
| nf_8.csv | 46 | 28 | 39.1% | Uuid, ageUnit, aliquotID, cellType, comments (+ 13 more) |
| nf_9.csv | 50 | 32 | 36.0% | Uuid, age, ageUnit, aliquotID, cellType (+ 13 more) |

## Categories of Removed Columns

### Platform-Generated Metadata
These columns are automatically generated by data platforms and don't provide scientific value:
- `id` (removed from 38 files)
- `benefactorId` (removed from 26 files)
- `createdBy` (removed from 26 files)
- `createdOn` (removed from 26 files)
- `etag` (removed from 26 files)
- `parentId` (removed from 26 files)
- `type` (removed from 26 files)
- `currentVersion` (removed from 24 files)
- `dataFileHandleId` (removed from 23 files)
- `entityId` (removed from 21 files)

### Funding and Administrative Information
These fields are often not available in published papers and represent administrative rather than scientific data:

### Study Metadata
Constant across datasets or administrative in nature:
- `progressReportNumber` (removed from 6 files)
- `resourceType` (removed from 1 files)

### Unit and Descriptive Fields
Redundant information that can be standardized or is implicit:
- `timePointUnit` (removed from 15 files)
- `ageUnit` (removed from 8 files)

### Other Removed Columns
Additional columns removed for data quality or relevance reasons:
- `cellType` (removed from 26 files)
- `modifiedOn` (removed from 26 files)
- `projectId` (removed from 26 files)
- `dataFileSizeBytes` (removed from 19 files)
- `tumorType` (removed from 19 files)
- `dataFileMD5Hex` (removed from 17 files)
- `libraryPrep` (removed from 17 files)
- `sex` (removed from 17 files)
- `isPrimaryCell` (removed from 16 files)
- `readStrandOrigin` (removed from 16 files)
- `readPair` (removed from 16 files)
- `transplantationType` (removed from 16 files)
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
- `dissociationMethod` (removed from 10 files)
- `readLength` (removed from 10 files)
- `dataFileConcreteType` (removed from 9 files)
- `dataFileKey` (removed from 9 files)
- `dataFileName` (removed from 9 files)
- `runType` (removed from 9 files)
- `compoundName` (removed from 9 files)
- `drugScreenType` (removed from 9 files)
- `genePerturbed` (removed from 9 files)
- `study` (removed from 9 files)
- `comments` (removed from 9 files)
- `readDepth` (removed from 9 files)
- `isMultiIndividual` (removed from 8 files)
- `isMultiSpecimen` (removed from 8 files)
- `genePerturbationTechnology` (removed from 8 files)
- `genePerturbationType` (removed from 8 files)
- `transplantationDonorTissue` (removed from 8 files)
- `specimenID` (removed from 8 files)
- `diagnosis` (removed from 8 files)
- `transplantationRecipientSpecies` (removed from 8 files)
- `parentSpecimenID` (removed from 8 files)
- `specimenIdSource` (removed from 7 files)
- `transplantationRecipientTissue` (removed from 7 files)
- `accessType` (removed from 6 files)
- `compoundDoseUnit` (removed from 6 files)
- `secondCompoundName` (removed from 6 files)
- `transplantationDonorSpecies` (removed from 6 files)
- `disease` (removed from 5 files)
- `individualIdSource` (removed from 5 files)
- `experimentalTimePoint` (removed from 5 files)
- `individualID` (removed from 5 files)
- `libraryStrand` (removed from 5 files)
- `modelOf` (removed from 5 files)
- `reportMilestone` (removed from 5 files)
- `platform` (removed from 5 files)
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
- `Component` (removed from 3 files)
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
- `dataSubtype` (removed from 1 files)
- `dataType` (removed from 1 files)
- `fileFormat` (removed from 1 files)
- `species` (removed from 1 files)
- `targetDepth` (removed from 1 files)

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

## Files Processed

All 38 neurofibromatosis dataset files were successfully processed and curated.

---

*This report was generated automatically by comparing the CIM_update folder contents with the ground_truth folder contents.*
