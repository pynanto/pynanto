import os

import zipfile
from io import BytesIO
from pathlib import Path


def build_archive(
        root=os.path.normpath(Path('../..').absolute()),
        folders=('/app/browser', '/app/common')
) -> bytes:
    stream = BytesIO()
    zf = zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1)

    for folder in folders:
        _add_folder(root, zf, folder)
    zf.close()

    stream.seek(0)
    return stream.getbuffer().tobytes()


def _add_folder(root, zf, folder):
    def fix_arcname(n: str):
        return 'additional' + n.removeprefix(root)

    w = root + folder
    for dirname, subdirs, files in os.walk(w):
        remove_elements(subdirs, ['__pycache__'])

        dir_name = fix_arcname(dirname)
        zf.write(dirname, dir_name)
        for filename in [f for f in files if _accept(f)]:
            file_path = os.path.join(dirname, filename)
            file_name = fix_arcname(file_path)
            zf.write(file_path, file_name)


def _accept(filename):
    return filename.endswith('.py') or filename.endswith('.html')


def remove_elements(arr, to_remove):
    [arr.remove(f) for f in to_remove if f in arr]


if __name__ == '__main__':
    file = Path('../../client_bundle.zip').absolute()
    file.unlink(missing_ok=True)
    file.write_bytes(build_archive())
