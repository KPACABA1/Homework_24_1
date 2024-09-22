Здравсвуйте, в этом проекте я буду работать с DRF

Все зависимсоти можно найти в файле requirements.txt. Виртуальное окружение - pip

Для моделей курсов я реализовал Viewset, для моделей уроков Generic-классы. Работаю с ними через Postman.

В приложении users созданы 2 модели - пользователи и платежи

Так же я еализовал эндпоинт для редактирования профиля любого пользователя на основе Generic.

Для модели курса добавил в сериализатор поле вывода количества уроков.

Для моделей платежей сделал Generic-классы на создание и просмотр списка платежей. Дополнительно сделал кастомную комнду для создания 2 моделей платежей(первая модель на оплату курса, вторая для оплаты урока)

Настроил фильтрацию для эндпоинта вывода списка платежей с возможностями:
  1. Менять порядок сортировки по дате оплаты;
  2. Фильтровать по курсу или уроку;
  3. Фильтровать по способу оплаты

Для профиля пользователя сделал вывод истории платежей, расширив сериализатор для вывода списка платежей
