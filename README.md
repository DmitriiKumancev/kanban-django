### Установка локального окружения

```bash
git clone https://github.com/DmitriiKumancev/kanban-django.git
cd kanban

pip install -r requirements.dev.txt
python3 manage.py migrate
python3 manage.py createsuperuser
```

После изменений перед комитом выполнить `flake8`, поправить перечисленные им ошибки, для поддержания кода в едином стиле.

### Продакшн

1. Установить зависимости `pip install -r requirements.txt`
1. Создать файл конфигурации `local_settings.py` в папке [kanban](kanban).
1. Собрать статику командой `python3 manage.py collectstatic`, после чего она будет доступна в папке `./static`.
