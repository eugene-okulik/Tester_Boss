text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

words = text.split()
new_words = []

for word in words:
    # Проверяем, заканчивается ли слово на запятую или точку
    if word.endswith(',') or word.endswith('.'):
        # Убираем знак препинания, добавляем 'ing', возвращаем знак
        clean_word = word[:-1]
        new_words.append(clean_word + 'ing' + word[-1])
    else:
        # Если знака нет, просто добавляем 'ing'
        new_words.append(word + 'ing')

result = ' '.join(new_words)
print(result)
