def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].lower().find(root_word.lower()) != -1:
            same_words.extend([other_words[i]])
    for i in range(len(other_words)):
        if root_word.lower().find(other_words[i].lower()) != -1:
            same_words.extend([other_words[i]])
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
