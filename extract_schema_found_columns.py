#!/usr/bin/env python3
"""
Extract columns that were found in the schema and create a separate CSV file.
"""

import csv

def extract_schema_found_columns():
    """Extract columns found in schema from the flagged summary file."""
    
    input_file = 'column_classification_summary_with_schema_flags.csv'
    output_file = 'columns_found_in_schema.csv'
    
    found_columns = []
    
    print(f"Reading from {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            schema_status = row['Schema_Status']
            
            # Include columns that were found (either exact or case insensitive match)
            if schema_status.startswith('Found'):
                found_columns.append(row)
    
    print(f"Found {len(found_columns)} columns that match the schema")
    
    # Write the found columns to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        if found_columns:
            fieldnames = found_columns[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(found_columns)
    
    print(f"Created {output_file} with schema-matched columns")
    
    # Print summary statistics
    exact_matches = sum(1 for col in found_columns if col['Schema_Status'] == 'Found (Exact)')
    case_insensitive_matches = sum(1 for col in found_columns if col['Schema_Status'] == 'Found (Case Insensitive)')
    
    print(f"\nSummary:")
    print(f"- Exact matches: {exact_matches}")
    print(f"- Case insensitive matches: {case_insensitive_matches}")
    print(f"- Total found in schema: {len(found_columns)}")
    
    # Count by classification type
    computer_generated = sum(1 for col in found_columns if col['Classification'] == 'Computer Generated')
    human_annotated = sum(1 for col in found_columns if col['Classification'] == 'Human Annotated')
    
    print(f"- Computer Generated columns in schema: {computer_generated}")
    print(f"- Human Annotated columns in schema: {human_annotated}")

if __name__ == "__main__":
    extract_schema_found_columns()
