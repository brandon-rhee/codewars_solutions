
def top_3_words(text):
    import re
    from string import punctuation
    if re.search('[a-zA-Z]', text):
        my_punc = punctuation.replace("'","")
        stripped = text.translate(str.maketrans("","",my_punc))

        words = stripped.split()
        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        my_keys = sorted(word_counts, key=word_counts.get, reverse=True)
        return my_keys[:3]
    else:
        return []

print(top_3_words("  , e   .. "))

