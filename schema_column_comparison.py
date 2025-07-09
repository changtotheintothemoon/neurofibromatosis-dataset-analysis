#!/usr/bin/env python3
"""
Compare columns from the summary table with properties defined in the NF.jsonld schema.
Flag columns that are not found in the schema.
"""

import pandas as pd
import json
import re

def extract_schema_properties(jsonld_file):
    """Extract all property names from the NF.jsonld schema"""
    schema_properties = set()
    
    with open(jsonld_file, 'r') as f:
        data = json.load(f)
        
    # Extract from @graph
    if '@graph' in data:
        for item in data['@graph']:
            if 'rdfs:label' in item:
                label = item['rdfs:label']
                # Skip enum types and institution names
                if not (label.endswith('Enum') or 
                       any(keyword in label for keyword in [
                           'University', 'College', 'Hospital', 'Institute', 
                           'Laboratory', 'Medical', 'School', 'Center', 'Foundation'
                       ])):
                    schema_properties.add(label)
    
    return schema_properties

def load_column_summary(csv_file):
    """Load columns from the summary CSV"""
    df = pd.read_csv(csv_file)
    return set(df['Column'].str.strip())

def compare_columns_to_schema(columns, schema_properties):
    """Compare columns against schema properties"""
    results = {
        'found_in_schema': [],
        'not_found_in_schema': [],
        'case_sensitive_matches': [],
        'case_insensitive_matches': []
    }
    
    # Create case-insensitive lookup
    schema_lower = {prop.lower(): prop for prop in schema_properties}
    
    for column in columns:
        column_clean = column.strip()
        
        # Exact match
        if column_clean in schema_properties:
            results['found_in_schema'].append((column_clean, column_clean))
        # Case-insensitive match
        elif column_clean.lower() in schema_lower:
            schema_match = schema_lower[column_clean.lower()]
            results['case_insensitive_matches'].append((column_clean, schema_match))
        else:
            results['not_found_in_schema'].append(column_clean)
    
    return results

def create_flagged_summary(summary_file, results):
    """Create a new summary file with flags for schema presence"""
    df = pd.read_csv(summary_file)
    
    # Add schema status column
    df['Schema_Status'] = 'Unknown'
    df['Schema_Match'] = ''
    
    for column, match in results['found_in_schema']:
        mask = df['Column'] == column
        df.loc[mask, 'Schema_Status'] = 'Found (Exact)'
        df.loc[mask, 'Schema_Match'] = match
    
    for column, match in results['case_insensitive_matches']:
        mask = df['Column'] == column
        df.loc[mask, 'Schema_Status'] = 'Found (Case Insensitive)'
        df.loc[mask, 'Schema_Match'] = match
    
    for column in results['not_found_in_schema']:
        mask = df['Column'] == column
        df.loc[mask, 'Schema_Status'] = 'NOT FOUND IN SCHEMA'
        df.loc[mask, 'Schema_Match'] = ''
    
    # Save flagged summary
    output_file = 'column_classification_summary_with_schema_flags.csv'
    df.to_csv(output_file, index=False)
    print(f"Created flagged summary: {output_file}")
    
    return df

def main():
    # Load data
    print("Loading schema properties from NF.jsonld...")
    schema_properties = extract_schema_properties('NF.jsonld')
    print(f"Found {len(schema_properties)} properties in schema")
    
    print("\nLoading columns from summary...")
    columns = load_column_summary('column_classification_summary.csv')
    print(f"Found {len(columns)} unique columns in summary")
    
    # Compare
    print("\nComparing columns to schema...")
    results = compare_columns_to_schema(columns, schema_properties)
    
    # Report results
    print(f"\n=== SCHEMA COMPARISON RESULTS ===")
    print(f"Total columns analyzed: {len(columns)}")
    print(f"Found in schema (exact match): {len(results['found_in_schema'])}")
    print(f"Found in schema (case insensitive): {len(results['case_insensitive_matches'])}")
    print(f"NOT FOUND in schema: {len(results['not_found_in_schema'])}")
    
    print(f"\n=== COLUMNS NOT FOUND IN SCHEMA ===")
    for i, column in enumerate(results['not_found_in_schema'], 1):
        print(f"{i:2d}. {column}")
    
    if results['case_insensitive_matches']:
        print(f"\n=== CASE INSENSITIVE MATCHES ===")
        for column, match in results['case_insensitive_matches']:
            print(f"Column: {column} -> Schema: {match}")
    
    # Create flagged summary
    print(f"\n=== Creating flagged summary ===")
    create_flagged_summary('column_classification_summary.csv', results)
    
    # Summary by classification
    df = pd.read_csv('column_classification_summary.csv')
    
    print(f"\n=== BREAKDOWN BY CLASSIFICATION ===")
    computer_generated = df[df['Classification'] == 'Computer Generated']['Column'].tolist()
    human_annotated = df[df['Classification'] == 'Human Annotated']['Column'].tolist()
    
    cg_not_found = [col for col in computer_generated if col in results['not_found_in_schema']]
    ha_not_found = [col for col in human_annotated if col in results['not_found_in_schema']]
    
    print(f"Computer Generated columns NOT in schema ({len(cg_not_found)}):")
    for col in cg_not_found:
        print(f"  - {col}")
    
    print(f"\nHuman Annotated columns NOT in schema ({len(ha_not_found)}):")
    for col in ha_not_found:
        print(f"  - {col}")

if __name__ == "__main__":
    main()
