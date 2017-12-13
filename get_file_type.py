import magic


def get(path):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(path)
    return mime_type
