ptd = open("project_twitter_data.csv", "r")
rd = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of postive and negative words 
with open("positive_words.txt") as pwf:
    positive_words = [ c.strip() for c in pwf.readlines() if c[0] not in [';', '\n'] ]
    
with open("negative_words.txt") as nwf:
    negative_words = [ c.strip() for c in nwf.readlines() if c[0] not in [';', '\n'] ]
    
# strip_punctuation() function 
def strip_punctuation(word):
    for character in punctuation_chars:
        word.replace(character, "")
    return word
    
# get_pos() function 
def get_pos(sentences):
    s = strip_punctuation(sentences)
    wordlist = s.split()
    for i in range(len(wordlist)):
        wordlist[i].lower()
    count = 0 
    for word in wordlist:
        for pw in positive_words:
            if word == pw:
                count = count + 1 
    return count 
    
    
# get_neg() function 
def get_neg(sentences):
    s = strip_punctuation(sentences)
    wordlist = s.split()
    for i in range(len(wordlist)):
        wordlist[i].lower()
    count = 0 
    for word in wordlist:
        for nw in negative_words:
            if word == nw:
                count = count + 1 
    return count 
    
# writing() function 
def writing(fn1, fn2):
    fn2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    fn2.write("\n")
    lines = fn1.readlines()
    lines.pop(0)
    for line in lines:
        l = line.strip().split(',')
        fn2.write("{}, {}, {}, {}, {}".format(l[1], l[2], get_pos(l[0]), get_neg(l[0]), get_pos(l[0])-get_neg(l[0])))
        fn2.write("\n")
        
        
writing(ptd, rd)
ptd.close()
rd.close()

        


                
           

