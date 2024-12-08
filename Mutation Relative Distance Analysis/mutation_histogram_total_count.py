import pandas as pd
import matplotlib.pyplot as plt
import ast
import numpy as np

df = pd.read_csv('mutation_distance_arranged.csv')

bin_size = 1000
min_range = -1000000
max_range = 1000000
bins = range(min_range, max_range + bin_size, bin_size)

filtered_df = df[['upstream_mutations', 'downstream_mutations']].dropna()

all_positions = []

#The code draws the histogram of based on the mutation_distance.csv file.
#The range is from -1,000,000 to 1,000,000 with an interval 1000.
#Mutations of all the gene is all summed up by the same relative distance interval to find the
# overall trend of the mutation distribution.

for index, row in filtered_df.iterrows():
    if pd.notnull(row['upstream_mutations']):
        upstream_mutations = ast.literal_eval(row['upstream_mutations'])
        upstream_positions = [pos for _, pos in upstream_mutations]
        all_positions.extend(upstream_positions)
    
    if pd.notnull(row['downstream_mutations']):
        downstream_mutations = ast.literal_eval(row['downstream_mutations'])
        downstream_positions = [pos for _, pos in downstream_mutations]
        all_positions.extend(downstream_positions)


plt.hist(all_positions, bins=bins, edgecolor='black', linewidth=0.2)


plt.xlabel('Distance')
plt.ylabel('Mutation Count')
plt.title('Histogram of Mutations by Relative Distance')

plt.show()


# counts, bin_edges = np.histogram(all_positions, bins=bins)

# bin_data = pd.DataFrame({
#     'bin_start': bin_edges[:-1],
#     'bin_end': bin_edges[1:],
#     'mutation_count': counts
# })

# bin_data.to_csv('total_histogram_data.csv', index=False)