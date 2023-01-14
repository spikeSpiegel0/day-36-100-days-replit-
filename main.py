blue = "\033[34m"
reset = "\033[0m"
namelist = []

def printList():
  print()
  for i in namelist:
    print(f"{blue}{i}{reset}")
  print()
    
    
while True:
  firstname = input("First Name: ").strip().capitalize()
  lastname = input("Last Name: ").strip().capitalize()
  fNl = f"{firstname} {lastname}"
  if fNl not in namelist:
    namelist.append(fNl)
  else:
    print()
    print("error: duplicate name")
    print()
  printList()
