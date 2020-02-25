#!/usr/bin/python3
# coding=utf-8
import pangu
import pyperclip

text = pyperclip.paste()
print(text)
new_text = pangu.spacing_text(text)
pyperclip.copy(new_text)
print(new_text)

