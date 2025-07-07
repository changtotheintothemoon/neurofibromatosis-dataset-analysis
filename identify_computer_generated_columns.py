#!/usr/bin/env python3
"""
Computer-Generated vs Human-Annotated Column Identifier

This script analyzes CSV files to identify columns that likely contain:
1. Computer-generated data (IDs, hashes, UUIDs, etc.)
2. Human-annotated data (descriptive text, categories, etc.)

Based on column names and data patterns.
"""

import os
import csv
import re
from collections import defaultdict

def get_csv_files(directory):
    """Get all CSV files from the specified directory."""
    csv_files = []
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            csv_files.append(os.path.join(directory, file))
    return sorted(csv_files)

def is_likely_computer_generated_column(column_name):
    """
    Identify if a column name suggests computer-generated data.
    Returns a tuple: (is_computer_generated, reason)
    """
    column_lower = column_name.lower()
    
    # Definitive computer-generated patterns
    computer_patterns = [
        # IDs and handles
        (r'.*id$', 'Ends with ID'),
        (r'.*_id$', 'Ends with _ID'),
        (r'.*key$', 'Ends with Key'),
        (r'.*_key$', 'Ends with _Key'),
        (r'handle', 'Contains handle'),
        (r'uuid', 'Contains UUID'),
        (r'guid', 'Contains GUID'),
        
        # Hashes and checksums
        (r'.*hash.*', 'Contains hash'),
        (r'.*md5.*', 'Contains MD5'),
        (r'.*checksum.*', 'Contains checksum'),
        (r'.*etag.*', 'Contains etag'),
        
        # System metadata
        (r'created.*', 'Creation metadata'),
        (r'modified.*', 'Modification metadata'),
        (r'.*by$', 'Created/Modified by field'),
        (r'.*on$', 'Created/Modified on field'),
        (r'version', 'Version field'),
        (r'.*size.*', 'File size field'),
        (r'.*bucket.*', 'Storage bucket field'),
        (r'.*path.*', 'File path field'),
        
        # Technical identifiers
        (r'benefactor.*', 'System benefactor'),
        (r'parent.*id.*', 'Parent ID reference'),
        (r'project.*id.*', 'Project ID reference'),
        (r'entity.*id.*', 'Entity ID reference'),
        (r'resource.*id.*', 'Resource ID reference'),
        (r'component', 'Component identifier'),
        (r'alias', 'System alias'),
        (r'view.*id.*', 'View ID reference'),
        (r'concrete.*type.*', 'Concrete type field'),
        
        # File metadata
        (r'filename', 'Filename field'),
        (r'.*format$', 'File format field'),
        (r'.*type$', 'Type field (often system-generated)'),
        (r'.*bytes.*', 'Byte size field'),
        (r'.*length.*', 'Length field'),
        (r'url', 'URL field'),
        (r'.*milestone.*', 'Milestone field'),
        
        # Timestamps and technical values
        (r'.*\d{4,}.*', 'Contains long numbers (likely timestamps)'),
        (r'.*current.*', 'Current state field'),
    ]
    
    for pattern, reason in computer_patterns:
        if re.search(pattern, column_lower):
            return True, reason
    
    return False, "Likely human-annotated"

def analyze_sample_data(file_path, column_name, max_samples=5):
    """
    Analyze sample data values to determine if they're computer-generated.
    Returns a tuple: (is_computer_generated, sample_values, pattern_description)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            sample_values = []
            
            # Get first few non-empty values
            for i, row in enumerate(reader):
                if i >= max_samples:
                    break
                value = row.get(column_name, '').strip()
                if value and value != 'NA':
                    sample_values.append(value)
            
            if not sample_values:
                return False, [], "No data available"
            
            # Check patterns in the data
            first_value = sample_values[0]
            
            # UUID pattern
            if re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', first_value.lower()):
                return True, sample_values, "UUID format"
            
            # Hash-like (long hex strings)
            if re.match(r'^[0-9a-f]{16,}$', first_value.lower()):
                return True, sample_values, "Hash-like hex string"
            
            # Synapse ID pattern
            if re.match(r'^syn\d+$', first_value):
                return True, sample_values, "Synapse ID format"
            
            # Long numeric IDs
            if re.match(r'^\d{10,}$', first_value):
                return True, sample_values, "Long numeric ID"
            
            # File handle ID pattern
            if re.match(r'^\d{6,}$', first_value) and 'handle' in column_name.lower():
                return True, sample_values, "File handle ID"
            
            # URL pattern
            if first_value.startswith(('http://', 'https://', 'ftp://')):
                return True, sample_values, "URL format"
            
            # File path pattern
            if '/' in first_value and ('.' in first_value or 'syn' in first_value):
                return True, sample_values, "File path format"
            
            # Check if all values are similar format (suggesting system generation)
            if len(set(len(v) for v in sample_values)) == 1 and len(first_value) > 10:
                if all(any(c.isdigit() for c in v) and any(c.isalpha() for c in v) for v in sample_values):
                    return True, sample_values, "Consistent alphanumeric format"
            
            return False, sample_values, "Human-readable format"
            
    except Exception as e:
        return False, [], f"Error reading data: {e}"

def analyze_csv_files(directory):
    """Analyze all CSV files to identify computer-generated vs human-annotated columns."""
    print(f"Analyzing CSV files for computer-generated vs human-annotated columns...")
    print("=" * 80)
    
    csv_files = get_csv_files(directory)
    
    if not csv_files:
        print("No CSV files found in the directory.")
        return
    
    all_results = {}
    
    for file_path in csv_files:
        filename = os.path.basename(file_path)
        print(f"\nAnalyzing: {filename}")
        print("-" * 50)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue
        
        file_results = {
            'computer_generated': [],
            'likely_human': [],
            'uncertain': []
        }
        
        for column in headers:
            # Check column name patterns
            is_computer_by_name, name_reason = is_likely_computer_generated_column(column)
            
            # Check sample data patterns
            is_computer_by_data, sample_values, data_reason = analyze_sample_data(file_path, column)
            
            # Make final determination
            if is_computer_by_name or is_computer_by_data:
                category = 'computer_generated'
                reason = name_reason if is_computer_by_name else data_reason
            else:
                category = 'likely_human'
                reason = "No computer-generated patterns detected"
            
            file_results[category].append({
                'column': column,
                'reason': reason,
                'sample_values': sample_values[:3],  # First 3 samples
                'name_check': name_reason,
                'data_check': data_reason
            })
        
        all_results[filename] = file_results
        
        # Print results for this file
        print(f"Computer-generated columns ({len(file_results['computer_generated'])}):")
        for item in file_results['computer_generated']:
            sample_str = f" | Samples: {', '.join(item['sample_values'])}" if item['sample_values'] else ""
            print(f"  • {item['column']}: {item['reason']}{sample_str}")
        
        print(f"\nLikely human-annotated columns ({len(file_results['likely_human'])}):")
        for item in file_results['likely_human']:
            sample_str = f" | Samples: {', '.join(item['sample_values'])}" if item['sample_values'] else ""
            print(f"  • {item['column']}: {item['reason']}{sample_str}")
    
    # Create summary analysis
    print(f"\n\nSUMMARY ANALYSIS:")
    print("=" * 80)
    
    # Count columns across all files
    all_computer_columns = set()
    all_human_columns = set()
    
    for filename, results in all_results.items():
        for item in results['computer_generated']:
            all_computer_columns.add(item['column'])
        for item in results['likely_human']:
            all_human_columns.add(item['column'])
    
    print(f"Total unique computer-generated columns: {len(all_computer_columns)}")
    print(f"Total unique human-annotated columns: {len(all_human_columns)}")
    
    # Find most common computer-generated columns
    computer_column_counts = defaultdict(int)
    human_column_counts = defaultdict(int)
    
    for filename, results in all_results.items():
        for item in results['computer_generated']:
            computer_column_counts[item['column']] += 1
        for item in results['likely_human']:
            human_column_counts[item['column']] += 1
    
    print(f"\nMost common computer-generated columns:")
    for col, count in sorted(computer_column_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  {col}: appears in {count} files")
    
    print(f"\nMost common human-annotated columns:")
    for col, count in sorted(human_column_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  {col}: appears in {count} files")
    
    # Save detailed results
    print(f"\nSAVING DETAILED RESULTS:")
    print("-" * 30)
    
    # Save per-file analysis
    with open('computer_vs_human_columns_detailed.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['File', 'Column', 'Category', 'Reason', 'Sample_Values', 'Name_Check', 'Data_Check'])
        
        for filename, results in all_results.items():
            for category, items in results.items():
                for item in items:
                    writer.writerow([
                        filename,
                        item['column'],
                        category.replace('_', ' ').title(),
                        item['reason'],
                        ' | '.join(item['sample_values']),
                        item['name_check'],
                        item['data_check']
                    ])
    
    print("Detailed analysis saved to: computer_vs_human_columns_detailed.csv")
    
    # Save summary by column
    with open('column_classification_summary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Column', 'Classification', 'Frequency', 'Example_Files'])
        
        # Computer-generated columns
        for col, count in sorted(computer_column_counts.items(), key=lambda x: x[1], reverse=True):
            example_files = []
            for filename, results in all_results.items():
                if any(item['column'] == col for item in results['computer_generated']):
                    example_files.append(filename)
                    if len(example_files) >= 3:
                        break
            
            writer.writerow([col, 'Computer Generated', count, ', '.join(example_files)])
        
        # Human-annotated columns
        for col, count in sorted(human_column_counts.items(), key=lambda x: x[1], reverse=True):
            example_files = []
            for filename, results in all_results.items():
                if any(item['column'] == col for item in results['likely_human']):
                    example_files.append(filename)
                    if len(example_files) >= 3:
                        break
            
            writer.writerow([col, 'Human Annotated', count, ', '.join(example_files)])
    
    print("Column classification summary saved to: column_classification_summary.csv")
    
    return all_results

def main():
    """Main function to run the analysis."""
    # Define the directory containing CSV files
    ground_truth_dir = "ground_truth"
    
    # Check if directory exists
    if not os.path.exists(ground_truth_dir):
        print(f"Directory '{ground_truth_dir}' not found.")
        print("Please ensure the script is run from the correct directory.")
        return
    
    # Run the analysis
    results = analyze_csv_files(ground_truth_dir)
    
    print(f"\nAnalysis complete! Check the generated CSV files for detailed results.")
    print("Files generated:")
    print("- computer_vs_human_columns_detailed.csv: Detailed per-file analysis")
    print("- column_classification_summary.csv: Summary by column type")

if __name__ == "__main__":
    main()
