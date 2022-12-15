# read the file and store all in the list

with open ('test.txt','r') as reader:
    content = reader.readlines()# [abc, ball, cat, dog, egg]
    reversed(content) #[egg, dog, cat, ball, abc] # reverse the list    
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)