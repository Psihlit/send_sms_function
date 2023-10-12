# шаблоны конца сообщений
ends_of_sms = ["[n/m]", "[n/ab]", "[nm/am]"]


def the_first_division_into_sms(input_text, size_of_sms, possible_count_of_sms):
    # выделяем количество слов в тексте
    words_in_sms = input_text.split(" ")
    # флаг для завершения сообщения
    end_point_find = True
    # список для результатов
    result_sms = ["start_0"]
    # строка результата
    result_string = ""
    # счетчик для прохода по словам
    i = 0
    # конец счетчика
    end_of_i = len(words_in_sms)
    # перебор идет до завершения строки
    while len(input_text) > 0:
        # проверяем, меньше ли результирующая строка допустимого максимума, не найдена ли точка остановки сообщения и не
        # последнее ли это слово в строке (защита от выхода за размер списка)
        if len(result_string) < size_of_sms and i != end_of_i and end_point_find:
            # последнее слово или нет
            if i == end_of_i - 1:
                result_string += words_in_sms[i]
            else:
                result_string += words_in_sms[i] + " "
            # если после добавления слова, строка вышла за допустимый результат, удаляем добавленное слово, и отправляем
            # результат в итоговый список с добавлением обозначения сообщения
            if len(result_string) >= size_of_sms:
                delete_index = len(words_in_sms[i]) + 1
                result_string = result_string[:-delete_index]
                result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
                end_point_find = False
                i -= 1
            i += 1
        # если слово было последним, добавляем результат
        elif i == end_of_i or input_text == " ":
            if input_text == " ":
                input_text = ""
            else:
                result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
                input_text = input_text.replace(result_string, "", 1)
        # если слово не последнее, но флаг опущен, сбрасываем значения , поднимаем флаг для продолжения
        else:
            input_text = input_text.replace(result_string, "", 1)
            result_string = ""
            end_point_find = True
    return result_sms


def adapted_division_into_sms(input_text, size_of_sms, possible_count_of_sms):
    # выделяем количество слов в тексте
    words_in_sms = input_text.split(" ")
    # флаг для завершения сообщения
    end_point_find = True
    # список для результатов
    result_sms = ["start_0"]
    # строка результата
    result_string = ""
    # счетчик для прохода по словам
    i = 0
    # конец счетчика
    end_of_i = len(words_in_sms)
    # временное значение для пересчета размера допустимой строки
    temp_size = size_of_sms
    # расчет размера допустимой строки
    size_of_sms = size_of_sms - len(ends_of_sms[1])
    # перебор идет до завершения строки или до добавления 10 сообщений
    while len(input_text) > 0:
        # проверяем, меньше ли результирующая строка допустимого максимума, не найдена ли точка остановки сообщения и не
        # последнее ли это слово в строке (защита от выхода за размер списка)
        if len(result_string) < size_of_sms and i != end_of_i and end_point_find:
            # последнее слово или нет
            if i == end_of_i - 1:
                result_string += words_in_sms[i]
            else:
                result_string += words_in_sms[i] + " "
            # если после добавления слова, строка вышла за допустимый результат, удаляем добавленное слово, и отправляем
            # результат в итоговый список с добавлением обозначения сообщения
            if len(result_string) >= size_of_sms:
                delete_index = len(words_in_sms[i]) + 1
                result_string = result_string[:-delete_index]
                result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
                end_point_find = False
                i -= 1
            i += 1
            # Если был достигнут результат в 10 сообщений, выходим из цикла
            if len(result_sms) == 10:
                break
        elif i == end_of_i:
            result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
            input_text = input_text.replace(result_string, "", 1)
            # Если был достигнут результат в 10 сообщений, выходим из цикла
            if len(result_sms) == 10:
                break
        # если слово не последнее, но флаг опущен, сбрасываем значения , поднимаем флаг для продолжения
        else:
            input_text = input_text.replace(result_string, "", 1)
            result_string = ""
            end_point_find = True

    # сброс значений и персчет допустимого размера
    input_text = input_text.replace(result_string, "", 1)
    size_of_sms = temp_size - len(ends_of_sms[2])
    end_point_find = True
    result_string = ""

    # аналогичное продолжение прохода, но с пересчитанной строкой
    while len(input_text) > 0:
        if len(result_string) < size_of_sms and i != end_of_i and end_point_find:
            if i == end_of_i - 1:
                result_string += words_in_sms[i]
            else:
                result_string += words_in_sms[i] + " "
            if len(result_string) >= size_of_sms:
                delete_index = len(words_in_sms[i]) + 1
                result_string = result_string[:-delete_index]
                result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
                end_point_find = False
                i -= 1
            i += 1
        elif i == end_of_i or input_text == " ":
            if input_text == " ":
                input_text = ""
            else:
                result_sms.append(result_string + f"[{len(result_sms)}/{possible_count_of_sms}]")
                input_text = input_text.replace(result_string, "", 1)
        else:
            input_text = input_text.replace(result_string, "", 1)
            result_string = ""
            end_point_find = True
    return result_sms


def send_sms(text: str, size_of_sms: int):
    # запоминаем исходные значения на случай второго прохода
    temp_text = text
    temp_size = size_of_sms

    # производим расчет предположительного разбиения
    length_of_text = len(text)
    possible_count_of_sms = round(length_of_text / size_of_sms) + 1

    # если количество разбиений меньше 10, то в конец строки будет добавляться запись минимального размера
    if possible_count_of_sms < 10:
        size_of_sms = size_of_sms - len(ends_of_sms[0])
    else:
        size_of_sms = size_of_sms - len(ends_of_sms[1])

    # первый проход
    result_sms = the_first_division_into_sms(text, size_of_sms, possible_count_of_sms)

    # проверяем, правильно ли отображаются записи деления сообщений
    # для этого из последнего сообщения выделяем часть с количеством сообщений
    start_of_slice = result_sms[-1].find("[")
    message_count_string = result_sms[-1][start_of_slice:]
    # переводим его в числовое значение
    numbers = []
    str_numbers = message_count_string[1:len(message_count_string) - 1].split("/")
    for str_number in str_numbers:
        numbers.append(int(str_number))
    # возвращаем первоначальные данные для адаптированного прохода
    text = temp_text
    size_of_sms = temp_size

    # если оно выходит больше, чем [n/m], берем максимальное значение из этих двух чисел
    if len(message_count_string) >= 6:
        final_count_of_messages = max(numbers)
        result_sms = adapted_division_into_sms(text, size_of_sms, final_count_of_messages)
    # иначе берем минимальное значение из этих двух чисел
    else:
        final_count_of_messages = min(numbers)
        result_sms = adapted_division_into_sms(text, size_of_sms, final_count_of_messages)

    # вывести результат без первого значения "start_0"
    return result_sms[1:]


test2 = ""
test1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Dolor purus non enim praesent elementum facilisis leo vel fringilla. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Lorem ipsum dolor sit amet consectetur."
print(send_sms(test1, 25))
print(send_sms(test1, 50))
print(send_sms(test1, 100))
print(send_sms(test1, 150))
print(send_sms(test1, 400))
