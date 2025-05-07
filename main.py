from stats import whats_the_word

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	file_contents = get_book_text("./books/frankenstein.txt")
	numw = whats_the_word(file_contents)
	print(f"{numw} words found in the document")

main()
