{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.8"
    },
    "colab": {
      "name": "Copy of Апрельский курс 2020. Light. Python, Домашнее задание 1",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/makhti/-selfeducation/blob/master/Copy_of_%D0%90%D0%BF%D1%80%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%83%D1%80%D1%81_2020_Light_Python%2C_%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B5%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "U7hoFvcehdnc",
        "colab_type": "text"
      },
      "source": [
        "## Домашнее задание 1. Введение в Python."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0cQ01NCnkysR",
        "colab_type": "text"
      },
      "source": [
        "## Light версия"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bW_kKRKthdn7",
        "colab_type": "text"
      },
      "source": [
        "### Задача 1\n",
        "\n",
        "С помощью функции input считайте с входящей строки два целых числа и выведите их сумму, разность, произведение."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ncbpypGALLqs",
        "colab_type": "code",
        "outputId": "07f264da-7013-49cd-c931-3b4e14986a2b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        }
      },
      "source": [
        "a = int(input(\"первое число: \"))\n",
        "b = int(input('второе число:'))\n",
        "print(a+b)\n",
        "print(a-b)\n",
        "print(a*b)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "первое число: 10\n",
            "второе число:3\n",
            "13\n",
            "7\n",
            "30\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PguJdnEqhdoI",
        "colab_type": "text"
      },
      "source": [
        "### Задача 2\n",
        "\n",
        "Дан ряд целых чисел от 10 до 25 включительно. Используя цикл for, выведите на экран сумму двух последовательно идущих чисел.\n",
        "\n",
        "\n",
        "**Пример**: \n",
        "\n",
        "для ряда от 2 до 6 включительно выдача выглядит так: \n",
        "\n",
        "5\n",
        "\n",
        "7\n",
        "\n",
        "9\n",
        "\n",
        "11\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IClzFGZu8nW3",
        "colab_type": "code",
        "outputId": "93f2b207-152c-4ed1-9a0d-ecdae1c11842",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 289
        }
      },
      "source": [
        "for i in range (10, 26):\n",
        "  a = 2 * i + 1\n",
        "  i += 1\n",
        "  print(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "21\n",
            "23\n",
            "25\n",
            "27\n",
            "29\n",
            "31\n",
            "33\n",
            "35\n",
            "37\n",
            "39\n",
            "41\n",
            "43\n",
            "45\n",
            "47\n",
            "49\n",
            "51\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CZpydHtThdoR",
        "colab_type": "text"
      },
      "source": [
        "### Задача 3\n",
        "\n",
        "Для ряда целых чисел от 100 до 150 включительно выведите на экран только те, что делятся на 5 без остатка."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aQfQEKQS_iEL",
        "colab_type": "code",
        "outputId": "9ae968fc-6fc5-46b4-d002-b53ffd409a6a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "for i in range (100, 151):\n",
        "  if i % 5 == 0:\n",
        "      print(i)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "100\n",
            "105\n",
            "110\n",
            "115\n",
            "120\n",
            "125\n",
            "130\n",
            "135\n",
            "140\n",
            "145\n",
            "150\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_L4Bd414hdog",
        "colab_type": "text"
      },
      "source": [
        "### Задача 4\n",
        "\n",
        "С помощью функции input считайте с входящей строки целое положительное число и сохраните его в переменную N. Используя конструкцию if...else, выведите на экран результат в зависимости от условий:\n",
        "\n",
        "* Если N нечетное, то выведите на экран \"N нечетное\"\n",
        "* Если N четное и входит в интервал от 5 до 10 включительно, выведите на экран \"N четное и принадлежит интервалу [5, 10]\"\n",
        "* Если N четное и больше 10, выведите на экран \"N четное и N > 10\"\n",
        "* Если N четное и меньше 5, выведите на экран \"N четное и N < 5\""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dmtnxWz6Ac32",
        "colab_type": "code",
        "outputId": "ab19b0ff-a732-44aa-9ed7-e9ecaa042687",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "N = int(input(\"Число: \"))\n",
        "if N % 2 !=0:\n",
        "  print(\"N нечетное\")\n",
        "elif 5 < N < 10:\n",
        "  print(\"N четное и принадлежит интервалу [5, 10]\")\n",
        "elif N > 10 and N //2:\n",
        "  print(\"N четное и N > 10\")\n",
        "elif N // 2 and N < 5:\n",
        "  print(\"N четное и N < 5\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Число: 2\n",
            "N четное и N < 5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WQweBQ8nhdol",
        "colab_type": "text"
      },
      "source": [
        "### Задача 5\n",
        "\n",
        "Используя цикл while, посчитайте и выведите на экран сумму всех целых чисел от 15 до 22 включительно.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "URixlbYPJNRA",
        "colab_type": "code",
        "outputId": "42b25620-5699-4bf1-e0df-d074416db1fa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "x = 15\n",
        "y = 0\n",
        "while x <= 22:\n",
        "  y = y + x\n",
        "  x = x + 1\n",
        "print(y)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "148\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YhJKiRAchdow",
        "colab_type": "text"
      },
      "source": [
        "### Задача 6\n",
        "\n",
        "Используя цикл for, найдите сумму всех элементов заданного списка (без использования встроенных функций sum, len, sort и т.д.)."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Im5W6TNGhdo6",
        "colab_type": "code",
        "outputId": "83e8e68b-9d51-41b3-d69e-d2a420565344",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]\n",
        "x = 0\n",
        "for i in my_list:\n",
        "  x += i\n",
        "print(x)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "880\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wIZELo0mhdpU",
        "colab_type": "text"
      },
      "source": [
        "### Задача 7\n",
        "\n",
        "Используя цикл (любой), найдите значение максимального элемента списка из предыдущего задания (без использования встроенных функций max и т.д.). Можно использовать встроенные методы списков (любые). \n",
        "\n",
        "P.S. Не стесняйтесь гуглить :)\n",
        "\n",
        "P.S. 2 Гуглить нужно фразу \"алгоритм поиска максимального элемента массива\".\n",
        "\n",
        "Пример: для списка [3, 4, 1, 7, 2] значением максимального элемента является число 7."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0bicWnAZPpn5",
        "colab_type": "code",
        "outputId": "df3690d1-ad98-4a55-d5f7-c8e634e3397e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]\n",
        "kh_z = 0\n",
        "for x in my_list:\n",
        "  if x > kh_z:\n",
        "    kh_z = x\n",
        "print('kh_z равно: ', kh_z)\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "kh_z равно:  158\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "omPfU7u9hdpi",
        "colab_type": "text"
      },
      "source": [
        "### Задача 8\n",
        "\n",
        "Создайте словарь, соответствующий следующему описанию. \n",
        "    \n",
        "В честь 8 марта начальник отдела Валера решил принести на работу коробку конфет и угостить коллег :) Красотка Наташа съела две конфеты, ее подруга Алина - целых три, разработчик Марат унес с собой в соседний опен-спейс целых пятнадцать, чтобы поделиться со своей командой, менеджер проекта Лев проходил мимо и съел одну конфету, а сам Валера, будучи сторонником здорового образа жизни, не съел ни одной.\n",
        "\n",
        "P.S. Все совпадения случайны :)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2jm5gsyQVmFa",
        "colab_type": "code",
        "outputId": "a940a6e8-b73e-4585-fef1-955ea2c37beb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "подгон_от_Валеры_dictionary = {'Pretty Natasha' : 2, 'Alina' : 3, 'Marat WTF' : 15, 'Lev PM' : 1, 'Valera ЗОЖник' : 0}\n",
        "print(подгон_от_Валеры_dictionary)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Pretty Natasha': 2, 'Alina': 3, 'Marat WTF': 15, 'Lev PM': 1, 'Valera ЗОЖник': 0}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UUK9d5hUhdpz",
        "colab_type": "text"
      },
      "source": [
        "### Задача 9\n",
        "\n",
        "Добавьте в словарь из предыдущего задания данные для студента Ромы, который работает неполный рабочий день, и, придя на работу после экзамена, с удовольствием съел 4 конфеты.\n",
        "\n",
        "P.S. Используйте встроенный метод .update"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dkkZD0LVY1u5",
        "colab_type": "code",
        "outputId": "76ebae1f-d657-413d-d401-4ba6bd6f455d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "подгон_от_Валеры_dictionary.update({'Roma student' : 4})\n",
        "print(подгон_от_Валеры_dictionary)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Pretty Natasha': 2, 'Alina': 3, 'Marat WTF': 15, 'Lev PM': 1, 'Valera ЗОЖник': 0, 'Roma student': 4}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vpQOcxmhhdp9",
        "colab_type": "text"
      },
      "source": [
        "## Pro-версия"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g9pd3inChdqC",
        "colab_type": "text"
      },
      "source": [
        "### Задача 1\n",
        "\n",
        "Выведите на экран следующий паттерн:\n",
        "\n",
        "@\n",
        "\n",
        "@ @\n",
        "\n",
        "@ @ @\n",
        "\n",
        "@ @ @ @ @\n",
        "\n",
        "Обратите внимание на пробел между символами. Рекомендуется использовать циклы (любые) для решения данного задания."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gnTf8b9Mx5L2",
        "colab_type": "code",
        "outputId": "7577c4ff-eb2a-4d4e-9133-0805743ebd3b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 153
        }
      },
      "source": [
        "a = '@'\n",
        "for p in range (1, 6):\n",
        "  if p != 4:\n",
        "    print()\n",
        "    print((a + ' ') * p)   "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "@ \n",
            "\n",
            "@ @ \n",
            "\n",
            "@ @ @ \n",
            "\n",
            "@ @ @ @ @ \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Vh7SqVB5hdqL",
        "colab_type": "text"
      },
      "source": [
        "### Задача 2\n",
        "\n",
        "Выведите на экран следующий паттерн:\n",
        "\n",
        "1\n",
        "\n",
        "2 2 \n",
        "\n",
        "3 3 3 \n",
        "\n",
        "4 4 4 4 \n",
        "\n",
        "5 5 5 5 5\n",
        "\n",
        "6 6 6 6\n",
        "\n",
        "7 7 7\n",
        "\n",
        "8 8\n",
        "\n",
        "9\n",
        "\n",
        "Обратите внимание на пробел между символами. Обратите внимание на пробел между символами. Рекомендуется использовать циклы (любые) для решения данного задания."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p635NSBG0Ngr",
        "colab_type": "code",
        "outputId": "cb50388c-4a4b-4f2f-e02e-f9d9c8aa0812",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 323
        }
      },
      "source": [
        "for i in range(1, 10):\n",
        "  if i < 6:\n",
        "    print((str(i) + ' ')*i)\n",
        "  else:\n",
        "    print((str(i) + ' ')*(10 - i))\n",
        "  print()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1 \n",
            "\n",
            "2 2 \n",
            "\n",
            "3 3 3 \n",
            "\n",
            "4 4 4 4 \n",
            "\n",
            "5 5 5 5 5 \n",
            "\n",
            "6 6 6 6 \n",
            "\n",
            "7 7 7 \n",
            "\n",
            "8 8 \n",
            "\n",
            "9 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IMoF_J7AhdqT",
        "colab_type": "text"
      },
      "source": [
        "### Задача 3\n",
        "\n",
        "Используя цикл while, выведите на экран таблицу умножения для числа 7.\n",
        "\n",
        "**Пример:**\n",
        "    \n",
        "Для числе 5 выдача выглядит так:\n",
        "    \n",
        "5 * 1 = 5\n",
        "\n",
        "5 * 2 = 10\n",
        "\n",
        "5 * 3 = 15\n",
        "\n",
        "5 * 4 = 20\n",
        "\n",
        "5 * 5 = 25\n",
        "\n",
        "...\n",
        "\n",
        "5 * 9 = 45"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lAnHrvwU2SoY",
        "colab_type": "code",
        "outputId": "47f2d634-80a7-44e9-8800-20bf4a27a003",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "X = 7\n",
        "i = 0\n",
        "while i in range(0, 10):\n",
        "  i += 1\n",
        "  print(X, '*', i, '=', X*i)\n",
        "  print()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "7 * 1 = 7\n",
            "\n",
            "7 * 2 = 14\n",
            "\n",
            "7 * 3 = 21\n",
            "\n",
            "7 * 4 = 28\n",
            "\n",
            "7 * 5 = 35\n",
            "\n",
            "7 * 6 = 42\n",
            "\n",
            "7 * 7 = 49\n",
            "\n",
            "7 * 8 = 56\n",
            "\n",
            "7 * 9 = 63\n",
            "\n",
            "7 * 10 = 70\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rvEbKNeIhdqY",
        "colab_type": "text"
      },
      "source": [
        "### Задача 4\n",
        "\n",
        "Представьте, что вы подбрасываете два кубика одновременно. Считайте с входящей строки два целых числа d1 и d2. Проверьте, соответсуют ли введенные числа интервалу значений для кубика. Если нет, то выведите на экран строку \"Ошибка! Значение на кубике (1 или 2, вставьте подходящее значение) не входит в интервал [1, 6]\". В противном случае посчитайте сумму выпавших значений. Если сумма равна 7 или 11, выведите на экран \"Я победил!!!\". Если сумма равна 2, 3 или 12, то выведите на экран \"Я проиграл :(\". Во всех остальных случаях выведите на экран сумму значений.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eD0iIRG24MQa",
        "colab_type": "code",
        "outputId": "7a9d9d45-6f5a-4bbe-f381-808e5b64fee7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "d1 = int(input('Значение кубика № 1: '))\n",
        "d2 = int(input('Значение кубика № 2: '))\n",
        "if d1 < 1 or d1 > 6:\n",
        "  print('Ошибка! Значение на кубике №1 не входит в интервал [1, 6]')\n",
        "if d2 < 1 or d2 > 6:\n",
        "  print('Ошибка! Значение на кубике №2 не входит в интервал [1, 6]')\n",
        "else:\n",
        "  if d1 + d2 ==7 or d1 + d2 == 11:\n",
        "    print('Я победил!!!')\n",
        "  elif d1 + d2 ==2 or d1 + d2 == 3 or d1 + d2 == 12:\n",
        "   print('Я проиграл :(')\n",
        "  else:\n",
        "    print('Сумма выпавших значений', d1 + d2)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Значение кубика № 1: 6\n",
            "Значение кубика № 2: 6\n",
            "Я проиграл :(\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OTSU9QTLhdqe",
        "colab_type": "text"
      },
      "source": [
        "### Задача 5\n",
        "\n",
        "Напишите код, который ищет все числа в интервале от 3000 до 4300 включительно, делящиеся на 11, но не делящиеся на 5. Выведите на экран все найденные числа."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NbTyaTDIMkex",
        "colab_type": "code",
        "outputId": "bab869ed-0a79-4f07-8190-10578c829e9c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "for q in range(3000, 4301):\n",
        "  if q % 11 == 0 and q % 5 !=0:\n",
        "    print(q)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3003\n",
            "3014\n",
            "3036\n",
            "3047\n",
            "3058\n",
            "3069\n",
            "3091\n",
            "3102\n",
            "3113\n",
            "3124\n",
            "3146\n",
            "3157\n",
            "3168\n",
            "3179\n",
            "3201\n",
            "3212\n",
            "3223\n",
            "3234\n",
            "3256\n",
            "3267\n",
            "3278\n",
            "3289\n",
            "3311\n",
            "3322\n",
            "3333\n",
            "3344\n",
            "3366\n",
            "3377\n",
            "3388\n",
            "3399\n",
            "3421\n",
            "3432\n",
            "3443\n",
            "3454\n",
            "3476\n",
            "3487\n",
            "3498\n",
            "3509\n",
            "3531\n",
            "3542\n",
            "3553\n",
            "3564\n",
            "3586\n",
            "3597\n",
            "3608\n",
            "3619\n",
            "3641\n",
            "3652\n",
            "3663\n",
            "3674\n",
            "3696\n",
            "3707\n",
            "3718\n",
            "3729\n",
            "3751\n",
            "3762\n",
            "3773\n",
            "3784\n",
            "3806\n",
            "3817\n",
            "3828\n",
            "3839\n",
            "3861\n",
            "3872\n",
            "3883\n",
            "3894\n",
            "3916\n",
            "3927\n",
            "3938\n",
            "3949\n",
            "3971\n",
            "3982\n",
            "3993\n",
            "4004\n",
            "4026\n",
            "4037\n",
            "4048\n",
            "4059\n",
            "4081\n",
            "4092\n",
            "4103\n",
            "4114\n",
            "4136\n",
            "4147\n",
            "4158\n",
            "4169\n",
            "4191\n",
            "4202\n",
            "4213\n",
            "4224\n",
            "4246\n",
            "4257\n",
            "4268\n",
            "4279\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m-pYH0xDhdqk",
        "colab_type": "text"
      },
      "source": [
        "### Задача 6\n",
        "\n",
        "Используя циклы, напишите код, который создает список (list) путем конкатенации значений данного листа с целыми числами от 1 до (произвольного) n включительно.\n",
        "\n",
        "Пример:\n",
        "\n",
        "для списка [\"сосиски\", \"горчица\"] при n = 3 результат должен выглядеть так:\n",
        "\n",
        "['сосиски$\\_$1', 'горчица$\\_$1', 'сосиски$\\_2$', 'горчица$\\_$2', 'сосиски$\\_$3', 'горчица$\\_$3']"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Eqz3zAL-hdqq",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "a544c9e7-b8e0-4512-cfff-17dbec1427a5"
      },
      "source": [
        "sample_list = [\"мандаринки\", \"киви\", \"лимон\"]\n",
        "n = int(input('Введите число '))\n",
        "my_list = []\n",
        "a = 1\n",
        "while a <= n:\n",
        "  for i in sample_list:\n",
        "    my_list.append(str(i + '_' + str(a)))\n",
        "  a += 1\n",
        "print(my_list)"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Введите число 3\n",
            "['мандаринки_1', 'киви_1', 'лимон_1', 'мандаринки_2', 'киви_2', 'лимон_2', 'мандаринки_3', 'киви_3', 'лимон_3']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WtwsV6BRhdrE",
        "colab_type": "text"
      },
      "source": [
        "### Задача 7\n",
        "\n",
        "Напишите код, который считает количество элементов в заданном списке до тех пор, пока не встретится элемент типа словарь.\n",
        "\n",
        "Пример:\n",
        "\n",
        "для списка [3, \"котики\", 0.45, 5, {'котики' : 2, 'слоники' : 9}, \"слоники\", 34] на выходе должны получить число 4"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "m5iv-Hj9hdrM",
        "colab_type": "code",
        "outputId": "9bef3d62-e802-4b4c-fa71-c337de0baffa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "list_for_pro_task_2 = [35, 0.24, 3 + 4j, \"котики\", 0.45, (8, 9), \"слоники\", {\"Мадрид\": 3, 'Лондон':5}, 23498]\n",
        "print(list_for_pro_task_2)\n",
        "i = 0\n",
        "while type(list_for_pro_task_2[i]) != dict:\n",
        "   i += 1\n",
        "print(i)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[35, 0.24, (3+4j), 'котики', 0.45, (8, 9), 'слоники', {'Мадрид': 3, 'Лондон': 5}, 23498]\n",
            "7\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fHMBDh-ahdrz",
        "colab_type": "text"
      },
      "source": [
        "### Задача 8\n",
        "\n",
        "Создайте словарь (dict) c ключами, соответствующими числам от 1 до 20 включительно и значениями, соответствующими квадратам ключей. \n",
        "\n",
        "P.S. Используйте циклы или функции, прямое \"ручное\" присваивание не допускается (!!!)\n",
        "\n",
        "Пример: \n",
        "\n",
        "для чисел от 1 до 3 включительно словарь должен выглядеть так: {1 : 1, 2 : 4, 3 : 9}"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DPe_S6KuPYM5",
        "colab_type": "code",
        "outputId": "e8f969f5-bf6b-4820-bff3-f930ea944dc3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "my_dict = {}\n",
        "for i in range (1, 21):\n",
        "  my_dict.update({i : i ** 2})\n",
        "print(my_dict)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}