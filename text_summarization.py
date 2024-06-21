import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Raditz tells Goku that along with two stronger elites, Vegeta and Nappa, they are the only remaining Saiyans after their home planet Vegeta was destroyed. Raditz asks Goku to enlist in helping conquering planets and joining the remaining Saiyans. When Goku refuses to join and help them, Raditz takes Goku and Krillin down with one strike, kidnaps Gohan, and threatens to murder him if Goku does not kill 100 humans within the next 24 hours. Goku decides to team up with his arch-enemy Piccolo, who was also defeated by Raditz in an earlier encounter, to defeat him and save his son. During the battle, Gohan's rage momentarily makes him stronger than Piccolo and Goku as he attacks Raditz to protect his father. The battle ends with Goku restraining Raditz so that Piccolo can hit them with a deadly move called Special Beam Cannon (魔貫光殺砲, Makankōsappō, lit. "Demon Penetrating, Killing Ray Gun"), mortally wounding them both, and kills them after a short while. But before Raditz succumbs to his injuries, he reveals to Piccolo that the other two Saiyans are much stronger than him and will come for the Dragon Balls in one year. """




def summarizer(rawdocs):

	text = rawdocs

	stopwords = list(STOP_WORDS)
	#print(stopwords)



	prcs = spacy.load('en_core_web_sm')
	doc = prcs(text)
	# print(doc)
	tokens = [token.text for token in doc]
	# print(tokens)
	word_frq = {}
	for word in doc:
		if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
			if word.text not in word_frq.keys():
				word_frq[word.text] = 1
			else:
				word_frq[word.text] += 1

	# print(word_frq)

	max_freq= max(word_frq.values())
	# print(max_freq)

	for word in word_frq.keys():
		word_frq[word] = word_frq[word]/max_freq
	# print(word_frq)

	sent_tokens = [sent for sent in doc.sents]
	# print(sent_tokens)

	sent_scores = {}
	for sent in sent_tokens:
		for word in sent:
			if word.text in word_frq.keys():
				if sent not in sent_scores.keys():
					sent_scores[sent] = word_frq[word.text]
				else:
					sent_scores[sent] += word_frq[word.text]
	# print(sent_scores)

	select_len = int(len(sent_tokens) * 0.3)
	# print(select_len)

	summary = nlargest(select_len, sent_scores, key = sent_scores.get)
	# print(summary)

	final_sum = [word.text for word in summary]
	summary = ' '.join(final_sum)

	return(summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))) 