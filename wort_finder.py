woerter = ["haus","auto","scheibe"]

while True:
	print("Welches Wort suchst du?")
	suche = input()
	i = 0
	for w in woerter:
		if suche in w:
			i=+1

	if i >= 1:
		print("Gefunden!")
	else:
		print("Nicht gefunden!")
