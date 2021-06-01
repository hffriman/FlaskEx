# Source: "Python Web Service from Idea to Production" by Tero Karvinen

import sys


if len(sys.argv) < 2:
	sys.exit("Please tell me your name")

name = sys.argv[1]

print(f"Hello, {name}")
