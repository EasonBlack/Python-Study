


p = 'Input: '
f = open('d.txt','r')
all_lines = [x.strip() for x in f.readlines()]
while True:
    word = raw_input(p).strip()
    if word == 'exit':
        print 'exit......'
        break
    for line in all_lines:
        index = line.find(' ')
        line_words = line[:index]
        if word == line_words:
            print line
            break
    else:
        print 'the word not exist'

f.close()
    
