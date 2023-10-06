from nltk.translate.bleu_score import sentence_bleu

reference = open(r"reference_path", "r", encoding="utf8").read().splitlines()
new_reference = []
for lines in reference:
    new_reference.append(lines.split())

candidate = open(r"candidate_path", "r", encoding="utf8").read().split()

print('BLEU score -> {}'.format(sentence_bleu(new_reference, candidate)))

