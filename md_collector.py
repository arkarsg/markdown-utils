from os import scandir, path

def get_mds(rel_path):
    '''
    Returns all `.md` files in a list
    '''
    abs_path = path.abspath(rel_path)
    md_files = []
    for entry in scandir(abs_path):
        if entry.name.endswith('.md'):
            md_files.append(entry.path)
    return md_files
