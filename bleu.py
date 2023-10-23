"""Script that calculates the BLEU score for a folder of text files against
   a reference set. This is the non-parallel version that runs quite
   slow.
"""

from nltk.translate.bleu_score import sentence_bleu
import os
import statistics
#Reference path
reference = open("ReferenceSet.txt", "r", encoding="utf8").read().splitlines()

#Folder path
folder_path = 'samples'

candidates = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        #Create the full path to the file
        file_path = os.path.join(folder_path, filename)
        
        #Open the file and read its contents into a string
        with open(file_path, 'r') as file:
            candidates.append(file.read().splitlines())

# Split candidate samples into a single list of each line
candidate = []
for x in candidates:
    for y in x:
        candidate.append(y)

# Calculate score for every line and take the average. It has been done this way because of the way that bleu score works, but also because
# there is no way to tell where a song ends and another starts in the original data
scores = []
for x in candidate:
    scores.append(sentence_bleu(reference, x))
print(statistics.mean(scores))

