Ошибка: Не верная обработка сторк с несколькими словами.
Описание: Метод `capitilize` в классе `StringUtils` не обрабатывает 
строки с несколькими словами должным образом

Ожидаемый результат: katerina Alybertovna Galyametdinova --> Katerina Albertovna Galyametdinova
В первом слове сделает букву заглавной, остальную часть оставит без изменений

Фактический результат: katerina Albertovna Galyametdinova --> Katerina Albertovna galyametdinova
В первом слове измененен регист буквы на заглавную, а так же был поменян регистр в двух оставшихся словах на строчную

Отсутствуют ожидаемые ошибки в коде.