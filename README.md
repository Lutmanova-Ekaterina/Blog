### Курсовой проект по Django

Skychimp 2.0

Контекст
<aside>
📍 Сервис по управлению рассылками пользуется популярностью и запущенный MVP уже не удовлетворяет потребностям бизнеса. 

Вам нужно доработать сервис, чтобы он стал доступен для использования различными клиентами. А также сделать доработки для развития сервиса в интернете.

</aside>

### Описание задач

- Расширьте модель пользователя для регистрации по почте, а также верификации
- Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика
- Реализуйте ограничение доступа к рассылкам для разных пользователей
- Реализуйте интерфейс менеджера
- Создайте блог для продвижения сервиса

<aside>
ℹ️ **Примечание:**
Используйте для наследования модель `AbstractUser`

</aside>

### Функционал менеджера

- **может** просматривать любые рассылки
- **может** просматривать список пользователей сервиса
- **может** блокировать пользователей сервиса
- **может** отключать рассылки
- **не может** редактировать рассылки
- **не может** управлять списком рассылок
- **не может** изменять рассылки и сообщения

### Функционал пользователя
Весь функционал дублируется из старой версии, но теперь нужно следить за тем, чтобы пользователь не мог случайным образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.

## Продвижение

### Блог

Реализуйте приложение для ведения блога. При этом, отдельный интерфейс реализовывать нет необходимости, но настроить административную панель для контент-менеджера необходимо. В сущность блога добавьте следующие поля:

- заголовок
- содержимое статьи
- изображение
- количество просмотров
- дата публикации

### Главная страница

Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:

- количество рассылок всего
- количество активных рассылок
- количество уникальных клиентов для рассылок
- 3 случайные статьи из блога

Для блога и главной страницы самостоятельно выберите какие данные необходимо кешировать, а также каким способом необходимо произвести кеширование. 

### Критерии приемки

- [ ]  Все интерфейсы, не относящиеся к стандартной админке, для изменения и создания сущностей необходимо реализовать с помощью Django форм
- [ ]  Все настройки прав доступа реализованы верно
- [ ]  Использовано как минимум два типа кеширования
- [ ]  Решение выложено на [github.com](http://github.com/)
