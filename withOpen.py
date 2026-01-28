# write source to file
def with_open_write(fileName, extension, write_encoding, source):
    with open('{}.{}'.format(fileName, extension), 'w', encoding=write_encoding) as f:
        return f.write(source)


def with_open_read(fileName, extension, read_encoding):
    with open('{}.{}'.format(fileName, extension), 'r', encoding=read_encoding) as f:
        read_content = f.read()
        read_content.encode(read_encoding)
        return f
