from aho_corasick import AhoCorasick

if __name__ == "__main__":
	words = ["he", "she", "hers", "his"]
	text = "ahishers"
	aho_chorasick = AhoCorasick(words)
	result = aho_chorasick.search_words(text)
	for word in result:
		for i in result[word]:
			print("Word", word, "appears from", i, "to", i+len(word)-1)