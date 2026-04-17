import argparse
import os
import re
from colorama import init, Fore, Style

init()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Анализатор логов")
    parser.add_argument("path", help="Путь к папке или файлу с логами")
    parser.add_argument("--text", required=True, help="Текст для поиска")
    parser.add_argument("--all", action="store_true", help="Показать все совпадения")
    return parser.parse_args()


def get_files(path):
    files = []
    if os.path.isfile(path):
        files.append(path)
    elif os.path.isdir(path):
        # Убрал жесткую фильтрацию по .log, чтобы искать во всех файлах,
        # либо можно добавить аргумент для расширения
        for filename in os.listdir(path):
            full_path = os.path.join(path, filename)
            if os.path.isfile(full_path):
                files.append(full_path)
    else:
        print(Fore.RED + "Путь не существует!" + Style.RESET_ALL)
        exit(1)
    return files


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(Fore.RED + f"Ошибка чтения файла {filepath}: {e}" + Style.RESET_ALL)
        return None


def split_into_blocks(content):
    """
    Разбивает контент на блоки.
    Новый блок начинается с паттерна времени в начале строки.
    """
    # Паттерн: Начало строки (^), дата-время, пробел
    time_pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    # split с сохранением разделителя не всегда удобен, лучше найти индексы начал блоков
    lines = content.split("\n")
    blocks = []
    current_block = []
    current_time = "Неизвестно"

    for line in lines:
        match = re.match(time_pattern, line)
        if match:
            # Если накоплен предыдущий блок, сохраняем его
            if current_block:
                blocks.append(
                    {"timestamp": current_time, "content": "\n".join(current_block)}
                )
            # Начинаем новый блок
            current_time = match.group()
            current_block = [line]
        else:
            # Продолжаем текущий блок
            if not current_block and lines.index(line) == 0:
                # Обработка случая, если файл не начинается с времени (редко)
                current_block = [line]
            else:
                current_block.append(line)

    # Не забываем последний блок
    if current_block:
        blocks.append({"timestamp": current_time, "content": "\n".join(current_block)})

    return blocks


def search_in_blocks(blocks, search_text, find_all=False):
    results = []
    for block in blocks:
        if search_text in block["content"]:
            results.append(block)
            if not find_all:
                break  # Если нужно только первое совпадение в файле
    return results


def get_context_snippet(text_content, search_text, words_count=5):
    """
    Находит первое вхождение search_text в тексте и возвращает
    5 слов до и 5 слов после.
    """
    # Используем regex для поиска слова, чтобы избежать частичных совпадений,
    # если нужно, или просто in, как в задании.
    # Для простоты оставим поиск подстроки, но будем искать границы слов для контекста

    index = text_content.find(search_text)
    if index == -1:
        return text_content[:200]  # Fallback

    # Берем большой кусок текста вокруг нахождения
    start_idx = max(0, index - 100)  # Примерно символы
    end_idx = min(len(text_content), index + len(search_text) + 100)

    snippet = text_content[start_idx:end_idx]

    # Теперь работаем со словами в этом сниппете, но нужно учесть,
    # что мы могли обрезать слово посередине.
    # Упрощенный вариант: берем все слова из блока, находим индекс искомого,
    # берем соседей.

    words = text_content.split()
    # Найти индекс слова, которое содержит search_text
    target_word_index = -1
    for i, word in enumerate(words):
        if search_text in word:
            target_word_index = i
            break

    if target_word_index != -1:
        start_w = max(0, target_word_index - words_count)
        end_w = min(len(words), target_word_index + words_count + 1)
        return " ".join(words[start_w:end_w])

    return snippet


def print_result(filename, block, search_text):
    print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)
    print(f"Файл: {Fore.CYAN}{filename}{Style.RESET_ALL}")
    print(f"Время ошибки: {Fore.YELLOW}{block['timestamp']}{Style.RESET_ALL}")

    # Вывод контекста (5 слов до/после)
    context = get_context_snippet(block["content"], search_text)

    print("Контекст (фрагмент): ")
    highlighted = context.replace(search_text, Fore.RED + search_text + Style.RESET_ALL)
    # Ограничим вывод, чтобы не засорять экран, если блок огромный,
    # но по заданию просили именно слова.
    print(f"  {highlighted}")

    # Опционально: можно вывести весь блок, если он небольшой, или первые N строк
    # print(Fore.WHITE + block['content'][:500] + Style.RESET_ALL)

    print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)


def main():
    args = parse_arguments()
    print(Fore.CYAN + f'Поиск текста "{args.text}" в {args.path}' + Style.RESET_ALL)
    print()

    files = get_files(args.path)
    print(f"Найдено файлов: {len(files)}")
    print()

    total_found = 0
    for filepath in files:
        filename = os.path.basename(filepath)
        content = read_file(filepath)
        if content is None:
            continue

        blocks = split_into_blocks(content)
        # Ищем в блоках. Если --all не указан, ищем только первое совпадение в файле?
        # В задании: "программа может выводить все места... или только первое".
        # Реализуем поиск всех блоков с совпадением, если --all, иначе первый.

        found_blocks = []
        for block in blocks:
            if args.text in block["content"]:
                found_blocks.append(block)
                if not args.all:
                    break

        for block in found_blocks:
            print_result(filename, block, args.text)
            total_found += 1

    print()
    if total_found > 0:
        print(
            Fore.GREEN
            + f"Всего найдено блоков с совпадениями: {total_found}"
            + Style.RESET_ALL
        )
    else:
        print(Fore.YELLOW + "Ничего не найдено" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
