import pandas as pd
import os

file_path = "song_lyrics.csv"
chunksize = 250000

pop_dataframe = pd.DataFrame()

reader = pd.read_csv(file_path, chunksize=chunksize)

if not os.path.exists('Createdcsv'):
    os.makedirs('Createdcsv')

drop_cols = ['title', 'artist', 'year', 'views', 'features', 'language_ft', 'language_cld3']
for chunk in reader:
    chunk_drop_rows = chunk.drop(columns=drop_cols)
    chunk_filtered = chunk_drop_rows[(chunk_drop_rows.language == "en") & (chunk_drop_rows.tag == "pop")]
    drop_popcol = chunk_filtered.drop(columns=['tag', 'language'])
    pop_dataframe = pd.concat([pop_dataframe, drop_popcol], ignore_index=True)



# Now we want to take a sample of the pop_dataframe so we can use it for the BLEU referenceset

reference_set = pop_dataframe.sample(frac=0.025, replace=False)
anti_join_result = pop_dataframe.merge(reference_set, on=['lyrics', 'id'], how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])

intersection_result = anti_join_result.merge(reference_set, on=['lyrics', 'id'], how='inner')

print(len(anti_join_result.index))
print(len(reference_set.index))

reference_set = reference_set.drop(columns=['id'])
training_set = anti_join_result.drop(columns=['id'])

reference_set.to_csv("ReferenceSet.txt", index=False)
training_set.to_csv("Training_set.txt", index=False)