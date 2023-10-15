import wikipedia
from flask import *


def get_title():
    book_title = request.form["book_title"]
    return book_title


def get_summary(book_title):
    #book_title = request.form["book_title"]
    page = wikipedia.page(book_title, auto_suggest=False)

    summary_titles = ["Plot", "Plot summary", "Summary", "Synopsis"]

    summary_section = False
    for title in summary_titles:
        summary_section = page.section(title)
        if summary_section:
            return summary_section
    return


print(get_summary("Pride and Prejudice"))

