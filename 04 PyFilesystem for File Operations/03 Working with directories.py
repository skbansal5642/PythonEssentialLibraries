from fs.osfs import OSFS

# TODO: print a directory tree listing
# with OSFS(".") as myfs:
#     myfs.tree()

# TODO: use directory operation functions
# with OSFS(".") as myfs:
#     dirlist = list(myfs.filterdir("FileExamples", files=["*.txt"]))
#     print(dirlist)

# TODO: use resource info with scandir
# with OSFS(".") as myfs:
#     dirlist = myfs.scandir("FileExamples", namespaces=["details"])
#     #print(type(dirlist))
#     for info in dirlist:
#         #print(type(info))
#         print(info.name, info.size)

# TODO: to make a copy of dir
# with OSFS(".") as myfs:
#     myfs.copydir("FileExamples", "CopyOfFileExamples", create=True)

# TODO: to remove a directory
with OSFS(".") as myfs:
    if myfs.exists("CopyOfFileExamples"):
        myfs.removetree("CopyOfFileExamples")