from collections import Counter

def word_frequency_analyzer(text):
    # Matnni kichik harflarga o'zgartirish
    text = text.lower()
    
    # Matnni tartiblash
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    
    # Matnni so'zlariga bo'lish
    words = text.split()
    
    # So'zlar sonini hisoblash
    frequency = Counter(words)
    
    return frequency

# Test ma'lumoti
text = "This is a sample text. This text is just a sample."

# Analyzer ishlatish
frequency = word_frequency_analyzer(text)

# Natija chiqarish
for word, count in frequency.items():
    print(f"{word}: {count}")
```

Kodni ishlatish uchun, siz matnni `text` deyarkaningiz va `word_frequency_analyzer` funksiyasini chaqiringiz. Natija so'zlar sonini ko'rsatadi.
