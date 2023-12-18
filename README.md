# Shopping list

Для проекта требуется:
* Python >=3.8
* pdm 2.4.9

### Установка пакетов c помощью asdf

---
Про asdf можно почитать [тут](https://github.com/asdf-vm/asdf) 

#### python
```sh
asdf plugin add python
asdf install python 3.8.9
asdf global python 3.8.9
```

#### pdm
```sh
asdf plugin add pdm
asdf install pdm 2.9.2
asdf global pdm 2.9.2
```

## установка pdm
Про pdm можно почитать [тут](https://github.com/pdm-project/pdm) 

### Установка зависимостей

```sh
pdm install --verbose
```

### Активация виртуального окружения

```sh
source .venv/bin/activate
```


## Шаги требующиеся для запуска модели:
```
rasa train
````
