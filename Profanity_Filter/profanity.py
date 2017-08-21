from urllib.request import urlopen, Request

def read_text():
	with open('text.txt', 'r') as file:
		contents_of_file = file.read()
	
	return check_profanity(contents_of_file)

def check_profanity(text_to_check):
	text_list = text_to_check.split()
	for text in text_list:
		print(text)
		url = 'http://www.wdylike.appspot.com/?q=' + text
		with urlopen(url) as file:
			output = file.read().decode("utf-8")
			
			if 'true' in output:
				return ('Profanity Alert!!')
	
	return ('This document has no curse words!')

print(read_text())