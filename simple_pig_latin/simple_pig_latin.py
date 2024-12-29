def pig_it(text):
    og_words = text.split()
    words = [word for word in og_words if word.isalpha()]
    new_words = [word[1:] + word[0] + 'ay' for word in words]
    print(f"new words is {new_words}, og words is {og_words}")
    if og_words[-1].isalpha():
        return ' '.join(new_words)
    else:
        return ' '.join(new_words + [og_words[-1]])
print(pig_it('O tempora o mores !'))

