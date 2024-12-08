import pandas as pd

gene_df = pd.read_csv('filtered_genelist.txt', sep=' ', header=None, names=['scaffold', 'start', 'end', 'strand'])
mutation_df = pd.read_csv('filtered_mutation.txt', sep=' ', header=None, names=['scaffold', 'position'])

UPSTREAM_RANGE = 1000000
DOWNSTREAM_RANGE = 1000000

#This program is to count the total number of mutation in the upstream and the downstream region.

def count_mutations(gene_row, mutation_df):
    gene_start = gene_row['start']
    gene_end = gene_row['end']

    upstream_start = max(0, gene_start - UPSTREAM_RANGE)
    upstream_end = gene_start - 1

    downstream_start = gene_end + 1
    downstream_end = gene_end + DOWNSTREAM_RANGE

    mutations_on_scaffold = mutation_df[mutation_df['scaffold'] == gene_row['scaffold']]['position']

    upstream_count = mutations_on_scaffold.between(upstream_start, upstream_end).sum()
    downstream_count = mutations_on_scaffold.between(downstream_start, downstream_end).sum()

    if gene_row['strand'] == '-':
        return downstream_count, upstream_count
    else:
        return upstream_count, downstream_count

results = []

for _, gene_row in gene_df.iterrows():
    upstream_count, downstream_count = count_mutations(gene_row, mutation_df)
    
    results.append({
        'gene_scaffold': gene_row['scaffold'],
        'gene_start': gene_row['start'],
        'gene_end': gene_row['end'],
        'strand': gene_row['strand'],
        'upstream_mutations': upstream_count,
        'downstream_mutations': downstream_count
    })

results_df = pd.DataFrame(results)
results_df.to_csv('mutation_gene_counts.csv', index=False)

print("Results saved to mutation_counts.csv")
