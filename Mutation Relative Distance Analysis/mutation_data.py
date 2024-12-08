import pandas as pd

gene_df = pd.read_csv('filtered_genelist.txt', sep=' ', header=None, names=['scaffold', 'start', 'end', 'strand'])
mutation_df = pd.read_csv('filtered_mutation.txt', sep=' ', header=None, names=['scaffold', 'position'])

UPSTREAM_RANGE = 1000000
DOWNSTREAM_RANGE = 1000000

#This code records the excat locus of the mutation in scaffold. The gene location is set as the standard
#which will be considered as 0. Then the upstream region or the region before the transcription site
# is called upstream and downstream for positive numbers. According to this, data is arranged in csv file.


def find_mutations_in_regions(gene_row, mutation_df):
    gene_start = gene_row['start']
    gene_end = gene_row['end']

    upstream_start = max(0, gene_start - UPSTREAM_RANGE)
    upstream_end = gene_start - 1
    downstream_start = gene_end + 1
    downstream_end = gene_end + DOWNSTREAM_RANGE

    mutations_on_scaffold = mutation_df[mutation_df['scaffold'] == gene_row['scaffold']]['position']

    upstream_mutations = mutations_on_scaffold[mutations_on_scaffold.between(upstream_start, upstream_end)]
    downstream_mutations = mutations_on_scaffold[mutations_on_scaffold.between(downstream_start, downstream_end)]

    upstream_distances = [(pos, pos - gene_start) for pos in upstream_mutations]
    downstream_distances = [(pos, pos - gene_end) for pos in downstream_mutations]

    if gene_row['strand'] == '-':
        return [(pos, -dist) for pos, dist in downstream_distances], [(pos, -dist) for pos, dist in upstream_distances]

    else:
        return upstream_distances, downstream_distances

results = []

for _, gene_row in gene_df.iterrows():
    upstream_mutations_with_distances, downstream_mutations_with_distances = find_mutations_in_regions(gene_row, mutation_df)

    results.append({

        'gene_scaffold': gene_row['scaffold'],
        'gene_start': gene_row['start'],
        'gene_end': gene_row['end'],
        'strand': gene_row['strand'],
        'upstream_mutations': upstream_mutations_with_distances,
        'downstream_mutations': downstream_mutations_with_distances,
        'upstream_count': len(upstream_mutations_with_distances),
        'downstream_count': len(downstream_mutations_with_distances)

    })

results_df = pd.DataFrame(results)
results_df.to_csv('mutation_distance.csv', index=False)

print("mutation_distance.csv Created")