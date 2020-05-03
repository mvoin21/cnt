def cnt():
    lines_ = 0
    words_ = 0
    letters_ = 0
    for item in open('alex.text', 'r'):
        lines_ += 1
        letters_ += len(item)
        words_ += len(item.split())
    return f'Lines = {lines_}, words = {words_}, letters = {letters_}'
print(cnt())
