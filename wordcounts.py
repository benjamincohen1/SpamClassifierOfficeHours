import os, glob
spamwords = {}
notspamwords = {}
spam_directory = "is-spam"
not_spam = "not-spam"
os.chdir(spam_directory)
for email in glob.glob("*"):#ITERATE THROUGH ALL DATA HERE 
	text = open(email).read().lower().split(' ')
	for word in text:
		if word in spamwords:
			spamwords[word] += 1
		else:
			spamwords[word] = 1

keys = sorted(spamwords.keys(), key=lambda x: spamwords[x])

for word in keys:
	print word, spamwords[word]

os.chdir('../'+not_spam)
for email in glob.glob("*"):#ITERATE THROUGH ALL DATA HERE 
	text = open(email).read().lower().split(' ')
	for word in text:
		if word in spamwords:
			spamwords[word] += 1
		else:
			spamwords[word] = 1

keys = sorted(spamwords.keys(), key=lambda x: spamwords[x])

for word in keys:
	print word, spamwords[word]
#