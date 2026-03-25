#Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I love learning new programming languages.\n"
contents += "I love building new projects.\n"
contents += "I love sharing my knowledge with others.\n"
contents += "I love helping other programmers.\n"


path = Path('c:\\Users\\NightManager\\OneDrive - Equivo IT\\Desktop\\EDWARD FOLDER\\Python File\\Chapter10\\.Book.txt')
path.write_text(contents)

