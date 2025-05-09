import sys
from stats import whats_the_word, character_counter, pretty

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	file_contents = get_book_text(filepath)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")

	numw = whats_the_word(file_contents)
	print("----------- Word Count ----------")
	print(f"Found {numw} total words")
	final_counts = character_counter(file_contents)
	print("--------- Character Count -------")
	print(pretty(final_counts))
	print("============= END ===============")

main()
