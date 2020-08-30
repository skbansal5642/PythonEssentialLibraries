from fs.osfs import OSFS

size = 0
with OSFS(".") as myfs:
    for path, info in myfs.walk.info(namespaces=["details"]):
        if not info.is_dir and path.endswith(".py"):
            size += info.size

print(f"\nTotal size of all files is: {size/1024}K\n")