    Стек: 
    Python 
    Django 
    Django Rest Framework 
    Docker 
    Docker-Compose 
    Celery 
    Redis
    Postgres(Postgis extension)

    СТруктура - описание положения привязанных объектов:

    Объекты которые являются Узлами:
            • Город (root)
            • Район
            • Улица
            • Дом
            • Квартира

        Город только содержит районы
        Район только содержит улицы
        Улица только содержит дома 
        Дом только содержит квартиры
        Квартира не содержит узлов
        К квартире подключаются устройства
        К устройству подключается множество разных счетчиков для передачи показания.
    Общий функционал проекта:

        - Возможность авторизации по токену на 7 дней - через JWT аутентификацию.
        - Создавать узлы, устройства и счетчики могут только зарегистрированные пользователи.
        - Пользователь может передать права на объекты (узел, устройство, счетчик).
        - Передать право можно только на просмотр, а также полные права на объект.
        - Только сам владелец и пользователи которым передали право (также администратор) могут дальше передавать права.
        - Возможность забрать право имеет только тот пользователь который сам дал другому пользователю эти права.
        - Возможность фильтровать клиентов по юзернейму и почте.
        - Возможность передавать права на просмотр или редактирование узлов.
        - Возможность фильтровать узлы по имени, по описанию, по адресу, по владельцу и по uuid.
        - Возможность передавать права на просмотр или редактирование устройств.
        - Возможность видеть показания устройства за период.
        - Возможность экспортировать данные в виде csv файла у устройства.
        - Возможность фильтровать устройства по dev_eui, по владельцу и по uuid.
        - Возможность передавать права на просмотр или редактирование счетчиков.
        - У узла любого уровня имеется возможность просматривать все счетчики которые содержаться в данном узле.
        - Возможность фильтровать счетчики по serial_number и по uuid.
        - Возможность проверять другой микросервис(google) с помощью периодических тасков. Периодическая проверка организована с помощью Сelery, в качестве брокера используется Redis



