![Bot](img/bot.jpg "Bot")
# Телеграм бот для получения и сдачи заданий

---

Функционал МВП:

- админ может создать задание
- админ может посмотреть список текущих заданий
- админ видит список заданий ожидающих оценки
- пользователь может посмотреть список заданий
- пользователь может записать одно задание на себя
- пользователь может сдать задание

---

## Общее описание сервиса

Функциональные части:

- админка
- интерфейс пользователя

### Как должно работать:

Администратор публикует в бота задание с описанием, критериями выполнения, ценой и сроком действия.

Пользователь может запросить список доступных заданий, проверить свой баланс и взять себе одно из доступных заданий.

Далее пользователь выполняет задание и сдает. Задание встает на ожидание подтверждения от админа.

Админ видит список заданий ожидающих подтверждения, проверяет критерии сдачи и дальше два вариант

- все отлично - задание принимается, закрывается а пользователю начисляют баллы
- что то не так - задание отправляется на доработку с комментарием

### Бот для админа:

- управление заданиями - создание, изменение, удаление, аппрув ожидающих либо отказ с комментарием
- управление пользователями (в более полной версии)

### Бот пользователя:

- посмотреть список текущих заданий
- посмотреть свой баланс
- выбрать задание и записать на себя
- сдать задание

## Какие данные надо хранить в базе:

- пользователи
    - id
    - баланс
    - id текущего задания
    - статус - админ или обычный
- задания
    - id
    - описание
    - стоимость
    - картинка(если надо)
    - срок действия

Команды бота:

/start - команда начала работы. Проверяет пользователя если он новый, если он уже существует - выводит список текущих задач

/task_list - выводит список текущих заданий с клавиатурой - пользователь может нажать на кнопку чтобы взять задание

/my_tasks - посмотреть список моих заданий со статусами

/create_task - создать задание, бот ожидает несколько заполненных полей для задания(посмотреть как это можно лучше сделать)