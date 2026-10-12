sentences = [
       "I love AI",
       "AI is great",
       "I love great AI"
   ]

all_words=[]

for sentence in sentences:
    all_words.extend(sentence.split())

print(all_words)

vocab = {
    word:i
    for i, word in enumerate(set(all_words),start=1)
}

vocab["<PAD>"] = 0

print("Vocabulary",vocab)

token_ids=[]

for sentence in sentences:
    ids=[vocab[word] for word in sentence.split()]
    token_ids.append(ids)

print("Token IDs:", token_ids)

max_length = max(len(ids) for ids in token_ids)

print("Maximum length:", max_length)

padded_sentences = []

for ids in token_ids:
    padding_needed = max_length - len(ids)
    padded_ids = ids + [vocab["<PAD>"]]*padding_needed
    padded_sentences.append(padded_ids)

for sentence in padded_sentences:
    print(sentence)