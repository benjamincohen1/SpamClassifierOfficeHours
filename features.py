def numwords(emailtext):
	splittext = emailtext.split(" ")
	return len(splittext)

def has_html(emailtext):
	return 1 if "html" in emailtext.lower() else 0

def num_link(emailtext):
	return emailtext.count('http')

#join free buy start click discount

def spammy_words(emailtext):
	spam_words = ['helvetica', 'new', 'money', 'e-mail', 'recieve', 'business']
	splittext = emailtext.split(" ")
	total = 0
	for word in spam_words:
		total += splittext.count(word)

	return total

def not_spammy_words(emailtext):
	spam_words = ['email', 'people', 'time', 'please']
	splittext = emailtext.split(" ")
	total = 0
	for word in spam_words:
		total += splittext.count(word)

	return total


def all_caps(emailtext):
	return 1 if emailtext == emailtext.upper() else 0

def cap_ratio(emailtext):
	lowers = float(len([f for f in emailtext if f == f.lower()]))
	uppers = float(len([f for f in emailtext if f == f.upper()]))

	return uppers/lowers