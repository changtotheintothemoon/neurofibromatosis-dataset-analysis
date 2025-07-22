#!/usr/bin/env python3
"""
Script to filter ground truth CSV files to contain only evaluatable columns
based on the CIM curated schema column list.
"""

import pandas as pd
import os
import glob
from pathlib import Path

def get_evaluatable_columns(schema_file):
    """
    Extract columns marked as 'Evaluate' from the schema CSV file.
    Remove duplicates while preserving order.
    
    Args:
        schema_file (str): Path to the schema CSV file
        
    Returns:
        list: List of unique column names to evaluate
    """
    schema_df = pd.read_csv(schema_file)
    all_evaluatable_columns = schema_df[schema_df['Classification'] == 'Evaluate']['Column'].tolist()
    
    # Remove duplicates while preserving order
    unique_evaluatable_columns = []
    seen = set()
    for col in all_evaluatable_columns:
        if col not in seen:
            unique_evaluatable_columns.append(col)
            seen.add(col)
    
    print(f"Found {len(unique_evaluatable_columns)} unique evaluatable columns:")
    for i, col in enumerate(sorted(unique_evaluatable_columns), 1):
        print(f"{i:2d}. {col}")
    
    if len(all_evaluatable_columns) > len(unique_evaluatable_columns):
        print(f"\nNote: Removed {len(all_evaluatable_columns) - len(unique_evaluatable_columns)} duplicate column names from schema")
    
    return unique_evaluatable_columns

def has_meaningful_data(series):
    """
    Check if a column has meaningful data (not just empty, NA, or 'Not Applicable').
    
    Args:
        series: pandas Series to check
        
    Returns:
        bool: True if column has meaningful data
    """
    # Remove NaN and empty strings
    meaningful_values = series.dropna()
    meaningful_values = meaningful_values[meaningful_values != '']
    
    # For string columns, also remove common non-meaningful values
    if series.dtype == 'object':
        meaningful_values = meaningful_values[meaningful_values.astype(str).str.lower() != 'not applicable']
        meaningful_values = meaningful_values[meaningful_values.astype(str).str.lower() != 'na']
        meaningful_values = meaningful_values[meaningful_values.astype(str).str.lower() != 'unknown']
    
    # Consider column meaningful if at least 25% of rows have meaningful data
    threshold = len(series) * 0.25
    return len(meaningful_values) >= threshold

def filter_csv_file(input_file, output_file, evaluatable_columns):
    """
    Filter a CSV file to contain only evaluatable columns with meaningful data.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        evaluatable_columns (list): List of columns to keep
    """
    try:
        # Read the input CSV
        df = pd.read_csv(input_file)
        
        # Find which evaluatable columns exist in this file (remove duplicates)
        existing_evaluatable_cols = []
        seen_cols = set()
        for col in evaluatable_columns:
            if col in df.columns and col not in seen_cols:
                existing_evaluatable_cols.append(col)
                seen_cols.add(col)
        
        if not existing_evaluatable_cols:
            print(f"  WARNING: No evaluatable columns found in {os.path.basename(input_file)}")
            return
        
        # Filter the dataframe to only include evaluatable columns
        filtered_df = df[existing_evaluatable_cols]
        
        # Remove columns that don't have meaningful data
        meaningful_cols = []
        removed_cols = []
        
        for col in filtered_df.columns:
            if has_meaningful_data(filtered_df[col]):
                meaningful_cols.append(col)
            else:
                removed_cols.append(col)
        
        if not meaningful_cols:
            print(f"  WARNING: No columns with meaningful data in {os.path.basename(input_file)}")
            return
        
        # Keep only columns with meaningful data
        final_df = filtered_df[meaningful_cols]
        
        # Save the filtered data
        final_df.to_csv(output_file, index=False)
        
        print(f"  Filtered {os.path.basename(input_file)}: {len(df.columns)} -> {len(final_df.columns)} columns")
        print(f"    Kept columns: {', '.join(meaningful_cols)}")
        if removed_cols:
            print(f"    Removed (no meaningful data): {', '.join(removed_cols)}")
        
    except Exception as e:
        print(f"  ERROR processing {input_file}: {str(e)}")

def main():
    # Define paths
    base_dir = "/Users/jmoon/Documents/sandbox/neurofibromatosis-dataset-analysis"
    schema_file = os.path.join(base_dir, "CIM_curated_NF_schema_column_list_7_11_25.csv")
    ground_truth_dir = os.path.join(base_dir, "ground_truth")
    output_dir = os.path.join(base_dir, "filtered_evaluatable_data")
    
    # Get evaluatable columns from schema
    print("=" * 60)
    print("EXTRACTING EVALUATABLE COLUMNS FROM SCHEMA")
    print("=" * 60)
    evaluatable_columns = get_evaluatable_columns(schema_file)
    
    # Process all CSV files in ground_truth directory
    print("\n" + "=" * 60)
    print("FILTERING GROUND TRUTH CSV FILES")
    print("=" * 60)
    
    csv_files = glob.glob(os.path.join(ground_truth_dir, "*.csv"))
    csv_files.sort()
    
    print(f"Found {len(csv_files)} CSV files to process\n")
    
    for i, input_file in enumerate(csv_files, 1):
        filename = os.path.basename(input_file)
        output_file = os.path.join(output_dir, f"filtered_{filename}")
        
        print(f"[{i:2d}/{len(csv_files)}] Processing {filename}...")
        filter_csv_file(input_file, output_file, evaluatable_columns)
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total unique evaluatable columns: {len(evaluatable_columns)}")
    print(f"Processed files: {len(csv_files)}")
    print(f"Output directory: {output_dir}")
    
    # Show a sample of the first filtered file
    if csv_files:
        sample_file = os.path.join(output_dir, f"filtered_{os.path.basename(csv_files[0])}")
        if os.path.exists(sample_file):
            print(f"\nSample output from {os.path.basename(sample_file)}:")
            sample_df = pd.read_csv(sample_file)
            print(f"Columns ({len(sample_df.columns)}): {', '.join(sample_df.columns)}")
            print(f"Rows: {len(sample_df)}")
            
            # Show data quality stats
            print(f"\nData Quality Check:")
            empty_count = 0
            na_count = 0
            for col in sample_df.columns:
                empty_in_col = sample_df[col].isna().sum() + (sample_df[col] == '').sum()
                na_in_col = (sample_df[col].str.lower() == 'not applicable').sum() if sample_df[col].dtype == 'object' else 0
                if empty_in_col > 0:
                    empty_count += 1
                if na_in_col > 0:
                    na_count += 1
            print(f"Columns with some empty values: {empty_count}/{len(sample_df.columns)}")
            print(f"Columns with 'Not Applicable' values: {na_count}/{len(sample_df.columns)}")

if __name__ == "__main__":
    main()
