from collections import Counter
def IOB_unique_tag_decoder(tags,words):
    #Will not work for NER because B-ORG can repeat and is not unique while B-ARG0 and B-ARG1 would be unique.
    tag_list=[]
    word_list=[]
    try:
        len(tags)==len(words)
        count_tags = Counter([re.split('[BILU]\-',tag)[1] for tag in tags if tag !='O'])
        for tag in count_tags.keys():
            word = words[tags.index('B-'+tag):tags.index('B-'+tag)+count_tags[tag]]
            #print(tag, word)
            tag_list.append(tag)
            word_list.append(word)


        return pd.DataFrame(np.column_stack([list(zip(tag_list,word_list))]), 
                               columns=['word', 'tags'])
    except:
        print("Issue with IOB_tag_decoder...maybe tags do not match the Text")
 