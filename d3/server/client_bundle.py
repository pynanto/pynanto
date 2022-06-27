import os

import zipfile
from pathlib import Path


def build_archive() -> Path:
    bundle_zip = Path("../client_bundle.zip").absolute()
    if bundle_zip.exists():
        bundle_zip.unlink()
    zf = zipfile.ZipFile(bundle_zip, "w")
    root = os.path.normpath(Path('../..').absolute())

    def fix_arcname(n: str):
        return 'additional' + n.removeprefix(root)

    for dirname, subdirs, files in os.walk(root + '/d3'):
        remove_elements(subdirs, ['__pycache__'])

        dir_name = fix_arcname(dirname)
        zf.write(dirname, dir_name)
        for filename in [f for f in files if _accept(f)]:
            file_path = os.path.join(dirname, filename)
            file_name = fix_arcname(file_path)
            zf.write(file_path, file_name)
    zf.close()
    return bundle_zip


def _accept(filename):
    return filename.endswith('.py') or filename.endswith('.html')


def remove_elements(arr, to_remove):
    [arr.remove(f) for f in to_remove if f in arr]


if __name__ == '__main__':
    build_archive()
