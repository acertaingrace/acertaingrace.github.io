# imports
from trilium_py.client import ETAPI
import json

# url of etapi on local desktop installation; 
# usually it's on port 37840 
# (ty Trilium Rocks, I would not have figured that out)
server_url = 'http://localhost:37840'
token = # etapi token 
ea = ETAPI(server_url, token)

# change variables
# parent is the ancestor note id (i.e. OneNote tab)
parent = "7C9HejdaacBO"

# search for ' files'
res = ea.search_note(
  search="note.title %= ' files$'",
  ancestorNoteId=parent,
  ancestorDepth="directChildren"
)

# loop through each ' files' note
for x in res['results']:
  print(x['noteId'], x['title'])

  # split to find title of main note
  title, _ = x['title'].rsplit(" ", 1)

  print(title)

  # find title.htm
  string = "note.title %= '^" + title.replace("(", r"\\(").replace(")", r"\\)").replace(",", r"\,").replace("'", r"\'").replace("+", r"\\+") + ".htm'"
  res1 = ea.search_note(
    search=string,
    ancestorNoteId=parent
  )
  print(string)
  print(res1)

  y = res1['results'][0]['noteId']

  # get children of ' files' note
  for z in x['childNoteIds']:
    z_meta = ea.get_note(z)
    print(z_meta)

    # move child to y (two passes: create new, delete old)
    ea.create_branch(z,y,"",0,0)

    # delete old branch
    old_branch = x['noteId'] + "_" + z
    res3 = ea.delete_branch(old_branch)
    print(res3)
    print()

    # also delete filelist.xml
    if z_meta['title'] == "filelist.xml":
      ea.delete_note(z)
  
  # delete note when done
  ea.delete_note(x['noteId'])
