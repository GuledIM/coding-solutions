def read_row(file):
    next_line = file.readline()

    if len(next_line) > 0:
        return __parse_row(next_line)

    return None


def __parse_row(next_line):
    fields = []
    field = ''
    inside_quote = False
    i = 0

    while i < len(next_line):
        char = next_line[i]

        if char == '"':
            if inside_quote and i + 1 < len(next_line) and next_line[i + 1] == '"':
                field += '"'
                i += 1
            else:
                inside_quote = not inside_quote

        elif char == ',' and not inside_quote:
            fields.append(field.strip())
            field = ''
        else:
            field += char

        i += 1

    fields.append(field.strip())
    return fields

