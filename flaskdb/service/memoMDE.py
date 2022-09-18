from flask import Markup, session
from markdown import markdown
import os
from flaskdb.service.mainService import file_name_list, now_dir

class memo_MDE:
  mdfile = None

  def __init__(self, file=None):
    self.mdfile = file

  def write_md(self, data):
    with open(now_dir() + '/' + self.mdfile + '.md', mode='w') as mdfile:
      mdfile.write(data)

  def read_md(self) -> str:
    with open(now_dir() + '/' + self.mdfile + '.md', mode='r') as mdfile:
      mdcontent = mdfile.read()
      return Markup(markdown(mdcontent))

  def read_edit_md(self) -> str:
    with open(now_dir() + '/' + self.mdfile + '.md', mode='r') as mdfile:
      mdcontent = mdfile.read()
      return mdcontent
  
  def delete_md(self):
    os.remove(now_dir() + '/' + self.mdfile + '.md')
