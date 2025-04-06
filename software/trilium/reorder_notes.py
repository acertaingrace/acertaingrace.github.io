# import trilium-py
from trilium_py.client import ETAPI

# url of etapi on local desktop installation;
# usually it's on port 37840
# (ty Trilium Rocks, I would not have figured that out)
server_url = 'http://localhost:37840'
token = # etapi token 
ea = ETAPI(server_url, token)

# change variables
# parent is ancestor note id (i.e. OneNote tab)
# order id is note id of 'file order.txt' under parent note
parent = "dx4M7kDvrmIL"
order_id = "xS19FOP5w2Ee"

# open file order file
# change name of file if you renamed it e.g. 'cooking.txt'
f = open("file order.txt", "r")

# notePosition
# default note ordering in Trilium is 10, 20, 30 ...
pos = 10

# change 'file order.txt' to top
file_id = parent + "_" + order_id
ea.patch_branch(file_id, pos, "", 0)

# read file line by line
for x in f:
  print(x.rstrip())

  # underscores are replaced by spaces in trilium 
  # (and underscores replace special characters in file export of onenote)
  # also escaping regex special characters
  # there's probably a better way to do this
  string = "note.title %= '^" + x.replace("_", " ").replace("(", r"\\(").replace(")", r"\\)").replace(",", r"\,").replace("'", r"\'").rstrip() + ".*'"

  # find note & get note id
  res = ea.search_note(
    search=string,
    ancestorNoteId=parent
  )

  thing = ""

  # for each search results 
  # e.g. 'unfiled 1.htm' and 'unfiled 1 files'
  for x in res['results']:
    print(x['noteId'], x['title'])
    thing = x['noteId']

    # edit note position of branch
    b_id = parent + "_" + thing
    branch = ea.get_branch(b_id)
    print(branch)

    # increase note position by 10 (default trilium ordering)
    pos += 10
    print(pos)

    patch_req = ea.patch_branch(b_id, pos, "", 0)
    print(patch_req)

  print()

# refresh note ordering
# trilium api does not automatically refresh note position after patch
# bc usually notes are edited in bulk (like now)
ea.refresh_note_ordering(parent)
