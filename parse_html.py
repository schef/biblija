#!/usr/bin/env python

import re

import helper
import book_list

delimiters = ["<", ">"]
regexPattern = '|'.join(map(re.escape, delimiters))

html_path = "html/"
txt_path = "txt/"
py_path = "py/"

grep_book_start = "<td valign='top' class='b'><table cellpadding='2' cellspacing='2'>"
grep_book_end = "</table>"
grep_verse = "stih"

books = [
    [],
    [],
    [],
    []
]

book_names = [
    "ivan_saric",
    "jeruzalemska_biblija",
    "tomislav_dretar",
    "danicic-karadzic"
]

for e,book in enumerate(book_list.book_list):
    book_name = book[0]
    index_len = 0
    for i in range(1, book[1] + 1):
        chapter = str(i)
        filename = html_path + "biblija_" + str(e).zfill(2) + "_" + book_name.lower() + "_" + chapter.zfill(2) + ".html"
        print(filename)
        html_lines = helper.read_lines_from_file(filename)
        in_book = False
        book_index = 0
        for line in html_lines:
            if not in_book:
                if(grep_book_start in line):
                    # print("in_book", True, book_index)
                    in_book = True
            else:
                if(grep_book_end in line):
                    # print("in_book", False, book_index)
                    in_book = False
                    book_index += 1
                if (grep_verse in line):
                    splited_line = re.split(regexPattern, line)
                    chapter = splited_line[10]
                    verse = splited_line[16]
                    # print(chapter, verse)
                    books[book_index].append([chapter, verse])

for e,book in enumerate(books):
    transcript = []
    index_len = 0
    for verse in book:
        if (len(verse[0]) > index_len):
            index_len = len(verse[0])
    for verse in book:
        transcript.append(verse[0] + (index_len - len(verse[0])) * " " + verse[1] + "\n")
    filename = txt_path + "biblija_" + book_names[e] + ".txt"
    helper.write_lines_to_file(transcript, filename)

for e,book in enumerate(books):
    transcript = []
    index_len = 0
    for verse in book:
        for v in verse[1].split(' '):
            if (len(v) > index_len):
                index_len = len(v)
    for verse in book:
        for v in verse[1].split(' '):
            transcript.append(v + (index_len - len(v)) * " " + verse[0] + "\n")
    transcript.sort()
    filename = txt_path + "konkordanca_" + book_names[e] + ".txt"
    helper.write_lines_to_file(transcript, filename)