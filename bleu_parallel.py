"""Script that calculates the BLEU score for a folder of text files against
   a reference set. This is the parallel version that runs quite
   a lot faster.
"""

from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import os
import statistics
import time
from multiprocessing import Pool

#Reference set path, also tokenizes.
reference = open("ReferenceSet.txt", "r", encoding="utf8").read().splitlines()
reference = [x.split() for x in reference]

#Remove empty lists
reference = [x for x in reference if x != []]


#Folder of text files path
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

#Wrangle candidates
candidate = []
for x in candidates:
    for y in x:
        candidate.append(y)

#Tokenize
candidate = [x.split() for x in candidate]
#Remove empty lists
candidate = [x for x in candidate if x != []]


#Function used to calculate BLEU inside the Pool section
def calculate_bleu(candidate):
    smoother = SmoothingFunction()
    score = sentence_bleu(reference, candidate, smoothing_function=smoother.method4)
    return score

if __name__ == "__main__":
    start = time.time()

    #Parallelize with Pool to run much faster
    with Pool(16) as pool:  
        scores = pool.map(calculate_bleu, candidate)

    average_bleu = statistics.mean(scores)
    end = time.time()

    print(average_bleu)
    print(scores)
    print(end - start)

