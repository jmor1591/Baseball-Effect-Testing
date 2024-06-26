import pandas as pd

# Load the CSV into a pandas DataFrame
df = pd.read_csv('count_stats.csv')

# Display the first few rows to understand the structure
print(df.head())

# Example to calculate statistics for different counts
count_stats = {}

# Iterate over unique counts (assuming 'Split' column represents counts)
for count in df['Split'].unique():
    # Filter data for the current count
    count_data = df[df['Split'] == count]

    # Calculate statistics (e.g., mean batting average)
    mean_batting_average = count_data['BA'].mean()
    mean_on_base_percentage = count_data['OBP'].mean()
    total_plate_appearances = count_data['PA'].sum()

    # Store results in a dictionary
    count_stats[count] = {
        'Mean Batting Average': mean_batting_average,
        'Mean On-Base Percentage': mean_on_base_percentage,
        'Total Plate Appearances': total_plate_appearances
    }

# Print out statistics for each count
for count, stats in count_stats.items():
    print(f"Count: {count}")
    print(f"  Mean Batting Average: {stats['Mean Batting Average']:.3f}")
    print(f"  Mean On-Base Percentage: {stats['Mean On-Base Percentage']:.3f}")
    print(f"  Total Plate Appearances: {stats['Total Plate Appearances']}")

# Additional calculations and analysis can be added based on your specific requirements
