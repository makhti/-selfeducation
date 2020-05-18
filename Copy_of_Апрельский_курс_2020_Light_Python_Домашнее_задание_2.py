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
      "name": "Copy of Апрельский курс-2020 Light. Python. Домашнее задание 2",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
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
        "<a href=\"https://colab.research.google.com/github/makhti/-selfeducation/blob/master/Copy_of_%D0%90%D0%BF%D1%80%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%83%D1%80%D1%81_2020_Light_Python_%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B5%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rt7rnNMZ8SYb",
        "colab_type": "text"
      },
      "source": [
        "# Нейронные сети\n",
        "\n",
        "## Домашнее задание 2. Numpy и функции\n",
        "\n",
        "# Light"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x3viGq298SYv",
        "colab_type": "text"
      },
      "source": [
        "### Задача 1\n",
        "\n",
        "1. Подгрузите файл **train_vector_1.csv** с помощью функции **np.loadtxt**. \n",
        "\n",
        "2. Назовите подгруженный массив my_array.\n",
        "\n",
        "3. Убедитесь, что подгруженный массив имеет тип np.ndarray (выведите тип переменной my_array).\n",
        "\n",
        "Ссылка на файл: https://drive.google.com/open?id=1ngnrhmoMInequrA6JyAe90lEPhcbi0iH"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1VmqX2psBIj0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6Ie5QM1XB-AY",
        "colab_type": "code",
        "outputId": "5ea86d2d-d9ae-44a8-f43b-e311844ed94e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 463,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZNFCvJrWvVgK",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "my_array = np.loadtxt('/content/train_vector_1.csv', delimiter=',', skiprows=1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "messVsZAwvIT",
        "colab_type": "code",
        "outputId": "85f9abd6-c3cd-4e39-f574-93e98572a9a2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "type(my_array)\n",
        "print(type(my_array))"
      ],
      "execution_count": 465,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'numpy.ndarray'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Sa06XNJq8SY4",
        "colab_type": "text"
      },
      "source": [
        "### Задача 2\n",
        "\n",
        "Напишите код, который считает среднее значение всех элементов массива (без использования встроенных функций np.mean и т.д.). Для решения задачи воспользуйтесь циклом.\n",
        "* С помощью команды %%timeit отобразите время выполнения написанного кода.\n",
        "* Преобразуйте массив my_array в список (с помощью метода list()), сохраните его в переменной my_list.\n",
        "* В новой ячейке посчитайте среднее значение всех элементов списка (воспользуйтесь тем же самым кодом, что и для массива).\n",
        "* Командой %%timeit отобразите время выполнения и этой ячейки."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xj8_LCzuBz3b",
        "colab_type": "code",
        "outputId": "411f4471-8dec-4b83-8e51-ce42ec84b97b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "summa = 0\n",
        "for i in range (my_array.size):\n",
        "  summa += my_array [i]\n",
        "x = summa/my_array.size\n",
        "print(x)"
      ],
      "execution_count": 466,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0543624161073835\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WNjwiJ9yB4Hi",
        "colab_type": "code",
        "outputId": "0c408643-6601-4b20-b932-f194322bdd5e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "%%timeit n = 1\n",
        "summa=0\n",
        "for i in range(my_array.size):\n",
        "  summa+=my_array [i]\n",
        "x=summa/my_array.size"
      ],
      "execution_count": 467,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10000 loops, best of 3: 35.9 µs per loop\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pm9ribD-VLCv",
        "colab_type": "code",
        "outputId": "11ba5910-3208-43cf-aa41-d364106fdc32",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "my_array = list (my_array)\n",
        "print(my_array)"
      ],
      "execution_count": 468,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3.0, 3.0, 4.0, 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6, 3.3, 3.4, 3.0, 3.4, 3.5, 3.4, 3.2, 3.1, 3.4, 4.1, 4.2, 3.1, 3.2, 3.5, 3.6, 3.0, 3.4, 3.5, 2.3, 3.2, 3.5, 3.8, 3.0, 3.8, 3.2, 3.7, 3.3, 3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 2.0, 3.0, 2.2, 2.9, 2.9, 3.1, 3.0, 2.7, 2.2, 2.5, 3.2, 2.8, 2.5, 2.8, 2.9, 3.0, 2.8, 3.0, 2.9, 2.6, 2.4, 2.4, 2.7, 2.7, 3.0, 3.4, 3.1, 2.3, 3.0, 2.5, 2.6, 3.0, 2.6, 2.3, 2.7, 3.0, 2.9, 2.9, 2.5, 2.8, 3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6, 3.2, 2.7, 3.0, 2.5, 2.8, 3.2, 3.0, 3.8, 2.6, 2.2, 3.2, 2.8, 2.8, 2.7, 3.3, 3.2, 2.8, 3.0, 2.8, 3.0, 2.8, 3.8, 2.8, 2.8, 2.6, 3.0, 3.4, 3.1, 3.0, 3.1, 3.1, 3.1, 2.7, 3.2, 3.3, 3.0, 2.5, 3.0, 3.4, 3.0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "outputId": "26f1eaa6-dfe8-47f9-888e-2c86664744b7",
        "id": "As5qkDQ5FnYB",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "summa = 0\n",
        "for i in range (len(my_array)):\n",
        "  summa += my_array [i]\n",
        "x = summa / len(my_array)\n",
        "print(x)"
      ],
      "execution_count": 469,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0543624161073835\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z7JZ-m918SZA",
        "colab_type": "text"
      },
      "source": [
        "### Задача 3\n",
        "\n",
        "Подгрузите файл **iris.csv** с помощью встроенной функции **np.loadtxt**. Назовите его my_2d_array. Напиишите код, который считает сумму элементов массива по столбцам (для решения данной задачи воспользуйтесь разделом ноутбук \"Операции с двумерными массивами и встроенные методы\")."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QcXeYLWxhTDl",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "juy4TtK-N_Yp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "my_2d_array = np.loadtxt('/content/iris.csv', delimiter=',', skiprows=1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OVq4uU7BgV8O",
        "colab_type": "code",
        "outputId": "d719f017-0067-4de2-958e-31c36a6b46ee",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print(my_2d_array.sum(axis=0))"
      ],
      "execution_count": 472,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[11175.    876.5   458.6   563.7   179.9]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5lm0wgbRzVSA",
        "colab_type": "text"
      },
      "source": [
        "### Задача 4 \n",
        "\n",
        "* Используя библиотеку numpy, создайте массив 3x3, значения которого находятся в диапазоне от 11 до 40 (раздел \"Семплирование из распределений\"). \n",
        "\n",
        "* Не используя цикл for,  выведите на экран список элементов, которые меньше 20 (раздел \"Индексация\").\n",
        "\n",
        "* Просуммируйте все элементы, не используя цикл for (раздел \"Встроенные методы\").\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_P31vkQTiSAn",
        "colab_type": "code",
        "outputId": "7612e5aa-9f38-4bc7-c1dd-0e8049dee35f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "my_numpy_1 = np.random.randint(11, 40, (3,3))\n",
        "print(my_numpy_1)"
      ],
      "execution_count": 473,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[14 38 20]\n",
            " [34 14 12]\n",
            " [32 15 23]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ciZaiL2GkM7G",
        "colab_type": "code",
        "outputId": "3c72053b-7308-4808-89b6-2c0a2619a2bb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "print(my_numpy_1 < 20)"
      ],
      "execution_count": 474,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[ True False False]\n",
            " [False  True  True]\n",
            " [False  True False]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZUGqIMCjzkZY",
        "colab_type": "code",
        "outputId": "103c371d-17b3-44b3-fffe-a9bb373e96ad",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "my_numpy_2 = np.array([14, 38, 20, 34, 14, 12, 32, 15, 23]) \n",
        "print(my_numpy_2 < 20) "
      ],
      "execution_count": 476,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[ True False False False  True  True False  True False]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "75wsUWpOmvxo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# print(my_numpy_1[my_numpy_1 < 20])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5L6wy6FJm6Af",
        "colab_type": "code",
        "outputId": "ff6cbac9-0ef3-49b8-8e4b-2ec009800d98",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print(my_numpy_1.sum())"
      ],
      "execution_count": 477,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "202\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "4t6Yrs7Vj80p"
      },
      "source": [
        "### Задача 5\n",
        "\n",
        "* Создайте массив, который будет содержать списки с именем студента(str), его возрастом(int) и средней оценкой(float) (обратите внимание на пример с занятия со списком автомобильных регионов).\n",
        "* Отсортируйте такой массив (обратите внимание на параметр order метода sort()).\n",
        "* Замените значение, отвечающее за возраст, у всех студентов на одно и то же, например, 10. Отсортируйте такой массив. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w8z9gNyrr7RL",
        "colab_type": "code",
        "outputId": "7eb5fce6-6bf2-4687-dfc3-4310f17b0a9e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "my_numpy_3 = [('student', '<U32'), ('age', np.int64), ('average mark', np.float32)]\n",
        "values = [('Magomet',18,95), \n",
        "          ('Islam',17,93), \n",
        "          ('Khamzat',19,99)]\n",
        "stobalniki_Dagestana = np.array(values, dtype = my_numpy_3) \n",
        "print(stobalniki_Dagestana) "
      ],
      "execution_count": 478,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[('Magomet', 18, 95.) ('Islam', 17, 93.) ('Khamzat', 19, 99.)]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zlzNmv64HC05",
        "colab_type": "code",
        "outputId": "878c5b24-1731-4bbd-f66d-0244e4963a98",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "my_numpy_3 = [('student', '<U32'), ('age', np.int64), ('average mark', np.float32)]\n",
        "my_numpy_3.sort()\n",
        "print(my_numpy_3)"
      ],
      "execution_count": 479,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[('age', <class 'numpy.int64'>), ('average mark', <class 'numpy.float32'>), ('student', '<U32')]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "outputId": "d73e85a6-95dc-4462-e146-73ffa2db8efd",
        "id": "OhX1r1azHjfj",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "my_numpy_3 = np.array([['Magomet',18,95], \n",
        "                       ['Islam',17,93], \n",
        "                       ['Khamzat',19,99]])\n",
        "np.sort(stobalniki_Dagestana, order = 'age')"
      ],
      "execution_count": 480,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([('Islam', 17, 93.), ('Magomet', 18, 95.), ('Khamzat', 19, 99.)],\n",
              "      dtype=[('student', '<U32'), ('age', '<i8'), ('average mark', '<f4')])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 480
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2uVkTo2iDYcd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# print(my_numpy_3)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vl0mM1mc8SZc",
        "colab_type": "text"
      },
      "source": [
        "## Pro версия"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iQhtbx8Z8SZj",
        "colab_type": "text"
      },
      "source": [
        "### Задача 1\n",
        "\n",
        "* Подгрузите массив **iris.csv** и назовите его my_array. \n",
        "\n",
        "* Создайте двумерный массив из случайных чисел той же размерности, что и my_array (раздел \"Семплирование из распределений\", потребуется использовать размерность массива my_array).\n",
        "\n",
        "* Назовите его my_generated_array."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZDKe5WRK5TT_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a1OH6xyo5WYe",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "bcc7f1fb-b315-4c5a-e03b-1df0c800bc78"
      },
      "source": [
        "my_array = np.loadtxt('/content/iris.csv', delimiter=',', skiprows=1)\n",
        "my_array.shape"
      ],
      "execution_count": 482,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(150, 5)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 482
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qE5oHYlD72g1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# my_array = np.random.normal(0, 10, (150, 5))\n",
        "# my_generated_array = my_array\n",
        "# print(my_generated_array)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gy_ZqdwoLQcm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# my_generated_array.mean()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "umU8ImXdLc0t",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# my_generated_array.std()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cpjjcghg_Q9f",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "8703aa96-054f-49b5-ff35-3682c910266c"
      },
      "source": [
        "my_array = np.random.randint(0, 99, (150, 5))\n",
        "my_generated_array = my_array\n",
        "print(my_generated_array)"
      ],
      "execution_count": 490,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[44 95 53 63 39]\n",
            " [24  4 16 58 59]\n",
            " [66 36 16 40 75]\n",
            " [ 2 90  4 12 84]\n",
            " [ 6 88 85  6 54]\n",
            " [ 4 67 52 32 95]\n",
            " [49 27 96 38 47]\n",
            " [87 12 49 67 55]\n",
            " [ 0 19 15 78 66]\n",
            " [58  1 47 91 80]\n",
            " [ 4 55 91  6 75]\n",
            " [43  2 12 77 10]\n",
            " [52 56 46 72 60]\n",
            " [41 63  6 12 79]\n",
            " [ 9 72 25 10 82]\n",
            " [58 87 93 56 43]\n",
            " [90 23 78  7 67]\n",
            " [52 82 47 75 84]\n",
            " [35 62 17 26 88]\n",
            " [41 96 19 70 59]\n",
            " [85 56 75 76 11]\n",
            " [66 65 13  9 79]\n",
            " [55 28 63 98  9]\n",
            " [13 76 66 20 16]\n",
            " [52 91 93 56 61]\n",
            " [35 51 95 91 41]\n",
            " [68 45 31 73 87]\n",
            " [ 3 85 37 60 93]\n",
            " [86 40 24 29 18]\n",
            " [16 68 85 91 22]\n",
            " [19 48  6 40 23]\n",
            " [24 32 72 48 75]\n",
            " [84 28 19 28 87]\n",
            " [84 22  3 83  1]\n",
            " [19  1 16 24 41]\n",
            " [71 48 52 51 26]\n",
            " [80 35 67 47 88]\n",
            " [ 0 72 73 60 16]\n",
            " [63  7 90 62 39]\n",
            " [50 76 65 83 59]\n",
            " [37 14 33 86  3]\n",
            " [77 18 75 76 19]\n",
            " [13 75 20 15 54]\n",
            " [32 45  0 16 86]\n",
            " [77 70 57 75  6]\n",
            " [65 65  1 10 67]\n",
            " [95 16 61 20 60]\n",
            " [53 70 26 66 32]\n",
            " [70 40 66 75 76]\n",
            " [ 6 94 44 49 94]\n",
            " [64 30 45 97 23]\n",
            " [84 69 94  6 51]\n",
            " [23 74 24 14 66]\n",
            " [88 16 30 49 57]\n",
            " [10 79 38 20 51]\n",
            " [15  9 59 94 93]\n",
            " [ 5 70  0 93 29]\n",
            " [98 35 49 87 74]\n",
            " [90 74 21 76 61]\n",
            " [33 46 27 96  1]\n",
            " [30 68 95  9 49]\n",
            " [13 83 59 12 40]\n",
            " [87 79 40 52 57]\n",
            " [10 85 73 86 79]\n",
            " [87  7 71  9 37]\n",
            " [47 71 73  5 44]\n",
            " [ 3 73 76  9 62]\n",
            " [94 55 79  2  6]\n",
            " [60 72 59 69 52]\n",
            " [47 64 79 36 41]\n",
            " [80 32 24 16 48]\n",
            " [29 22 29 82 16]\n",
            " [63 90 40 44 51]\n",
            " [89 57 80 56 69]\n",
            " [86 47 93 62 53]\n",
            " [47 81 74 73 74]\n",
            " [31 75 89 83 36]\n",
            " [56 65 58 68 61]\n",
            " [57 34 84 67 51]\n",
            " [66 66 56 69  0]\n",
            " [28 46 23 24 79]\n",
            " [36  9 58 37 74]\n",
            " [45  7 58 45  1]\n",
            " [66 90 48 30 77]\n",
            " [12  3 32 29 44]\n",
            " [23 87 10 71 22]\n",
            " [18  6 48 24 42]\n",
            " [93 12 11  9 92]\n",
            " [91 98 25 13 38]\n",
            " [20 61 61 23 28]\n",
            " [28 41 52 87 96]\n",
            " [93 80 65 36 22]\n",
            " [54 74 90 42 79]\n",
            " [10 34 26 33 55]\n",
            " [91 96 88 21 29]\n",
            " [13 93 37 50 98]\n",
            " [74 38 51  6 91]\n",
            " [ 8 69  4 78 94]\n",
            " [91 23 39 30 74]\n",
            " [21 15 96 80  3]\n",
            " [73 69 14 47 41]\n",
            " [77 17 53 29 44]\n",
            " [82 20 91  0 90]\n",
            " [18 45 81 77 43]\n",
            " [12 23 94 36 88]\n",
            " [17 86 46 16 16]\n",
            " [60 36 30 14 16]\n",
            " [56 88 57 28 25]\n",
            " [86 43 41 89  2]\n",
            " [17 51 90 52 54]\n",
            " [54 23 36 64 72]\n",
            " [46 23  5 14 11]\n",
            " [12 93 14 37  6]\n",
            " [97 75 19 16 64]\n",
            " [55 69 31 84 67]\n",
            " [54 66 82 15 64]\n",
            " [72 80 95 28  0]\n",
            " [ 4 24 60 14 19]\n",
            " [54 24 65 37 63]\n",
            " [ 4 62  8 15 27]\n",
            " [37 39 32 67 72]\n",
            " [46 28 88 68 38]\n",
            " [40  9 82 95  7]\n",
            " [30 90 87 96 38]\n",
            " [84 23 67 17 52]\n",
            " [50 92 14  8 38]\n",
            " [45  4 48 19 10]\n",
            " [77 38 92 25  0]\n",
            " [33 81 54 14 35]\n",
            " [15 13 59 47 32]\n",
            " [55 71  0 72 84]\n",
            " [ 0 64 45 28 83]\n",
            " [ 6 61 44 66 98]\n",
            " [ 4 64 83 54 48]\n",
            " [38 88 47 58 63]\n",
            " [64 59  3  8 11]\n",
            " [87 20 80 51 18]\n",
            " [ 6 72 61 39 65]\n",
            " [34 30 73 38 74]\n",
            " [ 4 40 36 54 65]\n",
            " [13 13  7 56 91]\n",
            " [75 28 79 13 58]\n",
            " [31 41 93 97 35]\n",
            " [68 18  7  7 92]\n",
            " [33 72 54 17 35]\n",
            " [83 35 63 41 58]\n",
            " [10 11 68 31 43]\n",
            " [77 77 95 64 83]\n",
            " [63 73 90 72 60]\n",
            " [37 11 46 27  0]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hzR46ceA8SZp",
        "colab_type": "text"
      },
      "source": [
        "### Задача 2\n",
        "\n",
        "* Выполните поэлементное умножение my_array на my_generated_array (раздел \"векторные операции\").\n",
        "\n",
        "* Склейте массивы my_array, my_generated_array в один (могут помочь методы np.concatenate, np.vstack, np.hstack).\n",
        "\n",
        "* Возьмите склеенный массив и разделите его на равные части (больше двух). Можно сделать вручную через циклы либо воспользоваться методом vsplit."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a-YoM6q7OW2R",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "c0621a4f-fa0f-46dc-eaa9-0af5f83e5631"
      },
      "source": [
        "print(my_array * my_generated_array)"
      ],
      "execution_count": 491,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1936 9025 2809 3969 1521]\n",
            " [ 576   16  256 3364 3481]\n",
            " [4356 1296  256 1600 5625]\n",
            " [   4 8100   16  144 7056]\n",
            " [  36 7744 7225   36 2916]\n",
            " [  16 4489 2704 1024 9025]\n",
            " [2401  729 9216 1444 2209]\n",
            " [7569  144 2401 4489 3025]\n",
            " [   0  361  225 6084 4356]\n",
            " [3364    1 2209 8281 6400]\n",
            " [  16 3025 8281   36 5625]\n",
            " [1849    4  144 5929  100]\n",
            " [2704 3136 2116 5184 3600]\n",
            " [1681 3969   36  144 6241]\n",
            " [  81 5184  625  100 6724]\n",
            " [3364 7569 8649 3136 1849]\n",
            " [8100  529 6084   49 4489]\n",
            " [2704 6724 2209 5625 7056]\n",
            " [1225 3844  289  676 7744]\n",
            " [1681 9216  361 4900 3481]\n",
            " [7225 3136 5625 5776  121]\n",
            " [4356 4225  169   81 6241]\n",
            " [3025  784 3969 9604   81]\n",
            " [ 169 5776 4356  400  256]\n",
            " [2704 8281 8649 3136 3721]\n",
            " [1225 2601 9025 8281 1681]\n",
            " [4624 2025  961 5329 7569]\n",
            " [   9 7225 1369 3600 8649]\n",
            " [7396 1600  576  841  324]\n",
            " [ 256 4624 7225 8281  484]\n",
            " [ 361 2304   36 1600  529]\n",
            " [ 576 1024 5184 2304 5625]\n",
            " [7056  784  361  784 7569]\n",
            " [7056  484    9 6889    1]\n",
            " [ 361    1  256  576 1681]\n",
            " [5041 2304 2704 2601  676]\n",
            " [6400 1225 4489 2209 7744]\n",
            " [   0 5184 5329 3600  256]\n",
            " [3969   49 8100 3844 1521]\n",
            " [2500 5776 4225 6889 3481]\n",
            " [1369  196 1089 7396    9]\n",
            " [5929  324 5625 5776  361]\n",
            " [ 169 5625  400  225 2916]\n",
            " [1024 2025    0  256 7396]\n",
            " [5929 4900 3249 5625   36]\n",
            " [4225 4225    1  100 4489]\n",
            " [9025  256 3721  400 3600]\n",
            " [2809 4900  676 4356 1024]\n",
            " [4900 1600 4356 5625 5776]\n",
            " [  36 8836 1936 2401 8836]\n",
            " [4096  900 2025 9409  529]\n",
            " [7056 4761 8836   36 2601]\n",
            " [ 529 5476  576  196 4356]\n",
            " [7744  256  900 2401 3249]\n",
            " [ 100 6241 1444  400 2601]\n",
            " [ 225   81 3481 8836 8649]\n",
            " [  25 4900    0 8649  841]\n",
            " [9604 1225 2401 7569 5476]\n",
            " [8100 5476  441 5776 3721]\n",
            " [1089 2116  729 9216    1]\n",
            " [ 900 4624 9025   81 2401]\n",
            " [ 169 6889 3481  144 1600]\n",
            " [7569 6241 1600 2704 3249]\n",
            " [ 100 7225 5329 7396 6241]\n",
            " [7569   49 5041   81 1369]\n",
            " [2209 5041 5329   25 1936]\n",
            " [   9 5329 5776   81 3844]\n",
            " [8836 3025 6241    4   36]\n",
            " [3600 5184 3481 4761 2704]\n",
            " [2209 4096 6241 1296 1681]\n",
            " [6400 1024  576  256 2304]\n",
            " [ 841  484  841 6724  256]\n",
            " [3969 8100 1600 1936 2601]\n",
            " [7921 3249 6400 3136 4761]\n",
            " [7396 2209 8649 3844 2809]\n",
            " [2209 6561 5476 5329 5476]\n",
            " [ 961 5625 7921 6889 1296]\n",
            " [3136 4225 3364 4624 3721]\n",
            " [3249 1156 7056 4489 2601]\n",
            " [4356 4356 3136 4761    0]\n",
            " [ 784 2116  529  576 6241]\n",
            " [1296   81 3364 1369 5476]\n",
            " [2025   49 3364 2025    1]\n",
            " [4356 8100 2304  900 5929]\n",
            " [ 144    9 1024  841 1936]\n",
            " [ 529 7569  100 5041  484]\n",
            " [ 324   36 2304  576 1764]\n",
            " [8649  144  121   81 8464]\n",
            " [8281 9604  625  169 1444]\n",
            " [ 400 3721 3721  529  784]\n",
            " [ 784 1681 2704 7569 9216]\n",
            " [8649 6400 4225 1296  484]\n",
            " [2916 5476 8100 1764 6241]\n",
            " [ 100 1156  676 1089 3025]\n",
            " [8281 9216 7744  441  841]\n",
            " [ 169 8649 1369 2500 9604]\n",
            " [5476 1444 2601   36 8281]\n",
            " [  64 4761   16 6084 8836]\n",
            " [8281  529 1521  900 5476]\n",
            " [ 441  225 9216 6400    9]\n",
            " [5329 4761  196 2209 1681]\n",
            " [5929  289 2809  841 1936]\n",
            " [6724  400 8281    0 8100]\n",
            " [ 324 2025 6561 5929 1849]\n",
            " [ 144  529 8836 1296 7744]\n",
            " [ 289 7396 2116  256  256]\n",
            " [3600 1296  900  196  256]\n",
            " [3136 7744 3249  784  625]\n",
            " [7396 1849 1681 7921    4]\n",
            " [ 289 2601 8100 2704 2916]\n",
            " [2916  529 1296 4096 5184]\n",
            " [2116  529   25  196  121]\n",
            " [ 144 8649  196 1369   36]\n",
            " [9409 5625  361  256 4096]\n",
            " [3025 4761  961 7056 4489]\n",
            " [2916 4356 6724  225 4096]\n",
            " [5184 6400 9025  784    0]\n",
            " [  16  576 3600  196  361]\n",
            " [2916  576 4225 1369 3969]\n",
            " [  16 3844   64  225  729]\n",
            " [1369 1521 1024 4489 5184]\n",
            " [2116  784 7744 4624 1444]\n",
            " [1600   81 6724 9025   49]\n",
            " [ 900 8100 7569 9216 1444]\n",
            " [7056  529 4489  289 2704]\n",
            " [2500 8464  196   64 1444]\n",
            " [2025   16 2304  361  100]\n",
            " [5929 1444 8464  625    0]\n",
            " [1089 6561 2916  196 1225]\n",
            " [ 225  169 3481 2209 1024]\n",
            " [3025 5041    0 5184 7056]\n",
            " [   0 4096 2025  784 6889]\n",
            " [  36 3721 1936 4356 9604]\n",
            " [  16 4096 6889 2916 2304]\n",
            " [1444 7744 2209 3364 3969]\n",
            " [4096 3481    9   64  121]\n",
            " [7569  400 6400 2601  324]\n",
            " [  36 5184 3721 1521 4225]\n",
            " [1156  900 5329 1444 5476]\n",
            " [  16 1600 1296 2916 4225]\n",
            " [ 169  169   49 3136 8281]\n",
            " [5625  784 6241  169 3364]\n",
            " [ 961 1681 8649 9409 1225]\n",
            " [4624  324   49   49 8464]\n",
            " [1089 5184 2916  289 1225]\n",
            " [6889 1225 3969 1681 3364]\n",
            " [ 100  121 4624  961 1849]\n",
            " [5929 5929 9025 4096 6889]\n",
            " [3969 5329 8100 5184 3600]\n",
            " [1369  121 2116  729    0]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O0If4NkEP3W-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "07885b84-6428-4724-9e3c-3406c3a5d97c"
      },
      "source": [
        "a = np.concatenate([my_array, my_generated_array])\n",
        "print(a)"
      ],
      "execution_count": 492,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[44 95 53 63 39]\n",
            " [24  4 16 58 59]\n",
            " [66 36 16 40 75]\n",
            " ...\n",
            " [77 77 95 64 83]\n",
            " [63 73 90 72 60]\n",
            " [37 11 46 27  0]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5IBkfkV7QEPk",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "dcbc751f-61e9-44c6-c3a3-313e993a8bac"
      },
      "source": [
        "b = np.vstack((my_array, my_generated_array))\n",
        "print(b)"
      ],
      "execution_count": 493,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[44 95 53 63 39]\n",
            " [24  4 16 58 59]\n",
            " [66 36 16 40 75]\n",
            " ...\n",
            " [77 77 95 64 83]\n",
            " [63 73 90 72 60]\n",
            " [37 11 46 27  0]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fow7y5HMQMNU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "01ded6fe-9787-4dfe-f5e4-a8b6b8e16b39"
      },
      "source": [
        "c = np.hstack((my_array, my_generated_array))\n",
        "print(c)"
      ],
      "execution_count": 494,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[44 95 53 ... 53 63 39]\n",
            " [24  4 16 ... 16 58 59]\n",
            " [66 36 16 ... 16 40 75]\n",
            " ...\n",
            " [77 77 95 ... 95 64 83]\n",
            " [63 73 90 ... 90 72 60]\n",
            " [37 11 46 ... 46 27  0]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eefBxZ6aaCuf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "a24283ca-33ca-491e-c880-bbcf6007cc1f"
      },
      "source": [
        "np.vsplit(a, 100)"
      ],
      "execution_count": 495,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[array([[44, 95, 53, 63, 39],\n",
              "        [24,  4, 16, 58, 59],\n",
              "        [66, 36, 16, 40, 75]]), array([[ 2, 90,  4, 12, 84],\n",
              "        [ 6, 88, 85,  6, 54],\n",
              "        [ 4, 67, 52, 32, 95]]), array([[49, 27, 96, 38, 47],\n",
              "        [87, 12, 49, 67, 55],\n",
              "        [ 0, 19, 15, 78, 66]]), array([[58,  1, 47, 91, 80],\n",
              "        [ 4, 55, 91,  6, 75],\n",
              "        [43,  2, 12, 77, 10]]), array([[52, 56, 46, 72, 60],\n",
              "        [41, 63,  6, 12, 79],\n",
              "        [ 9, 72, 25, 10, 82]]), array([[58, 87, 93, 56, 43],\n",
              "        [90, 23, 78,  7, 67],\n",
              "        [52, 82, 47, 75, 84]]), array([[35, 62, 17, 26, 88],\n",
              "        [41, 96, 19, 70, 59],\n",
              "        [85, 56, 75, 76, 11]]), array([[66, 65, 13,  9, 79],\n",
              "        [55, 28, 63, 98,  9],\n",
              "        [13, 76, 66, 20, 16]]), array([[52, 91, 93, 56, 61],\n",
              "        [35, 51, 95, 91, 41],\n",
              "        [68, 45, 31, 73, 87]]), array([[ 3, 85, 37, 60, 93],\n",
              "        [86, 40, 24, 29, 18],\n",
              "        [16, 68, 85, 91, 22]]), array([[19, 48,  6, 40, 23],\n",
              "        [24, 32, 72, 48, 75],\n",
              "        [84, 28, 19, 28, 87]]), array([[84, 22,  3, 83,  1],\n",
              "        [19,  1, 16, 24, 41],\n",
              "        [71, 48, 52, 51, 26]]), array([[80, 35, 67, 47, 88],\n",
              "        [ 0, 72, 73, 60, 16],\n",
              "        [63,  7, 90, 62, 39]]), array([[50, 76, 65, 83, 59],\n",
              "        [37, 14, 33, 86,  3],\n",
              "        [77, 18, 75, 76, 19]]), array([[13, 75, 20, 15, 54],\n",
              "        [32, 45,  0, 16, 86],\n",
              "        [77, 70, 57, 75,  6]]), array([[65, 65,  1, 10, 67],\n",
              "        [95, 16, 61, 20, 60],\n",
              "        [53, 70, 26, 66, 32]]), array([[70, 40, 66, 75, 76],\n",
              "        [ 6, 94, 44, 49, 94],\n",
              "        [64, 30, 45, 97, 23]]), array([[84, 69, 94,  6, 51],\n",
              "        [23, 74, 24, 14, 66],\n",
              "        [88, 16, 30, 49, 57]]), array([[10, 79, 38, 20, 51],\n",
              "        [15,  9, 59, 94, 93],\n",
              "        [ 5, 70,  0, 93, 29]]), array([[98, 35, 49, 87, 74],\n",
              "        [90, 74, 21, 76, 61],\n",
              "        [33, 46, 27, 96,  1]]), array([[30, 68, 95,  9, 49],\n",
              "        [13, 83, 59, 12, 40],\n",
              "        [87, 79, 40, 52, 57]]), array([[10, 85, 73, 86, 79],\n",
              "        [87,  7, 71,  9, 37],\n",
              "        [47, 71, 73,  5, 44]]), array([[ 3, 73, 76,  9, 62],\n",
              "        [94, 55, 79,  2,  6],\n",
              "        [60, 72, 59, 69, 52]]), array([[47, 64, 79, 36, 41],\n",
              "        [80, 32, 24, 16, 48],\n",
              "        [29, 22, 29, 82, 16]]), array([[63, 90, 40, 44, 51],\n",
              "        [89, 57, 80, 56, 69],\n",
              "        [86, 47, 93, 62, 53]]), array([[47, 81, 74, 73, 74],\n",
              "        [31, 75, 89, 83, 36],\n",
              "        [56, 65, 58, 68, 61]]), array([[57, 34, 84, 67, 51],\n",
              "        [66, 66, 56, 69,  0],\n",
              "        [28, 46, 23, 24, 79]]), array([[36,  9, 58, 37, 74],\n",
              "        [45,  7, 58, 45,  1],\n",
              "        [66, 90, 48, 30, 77]]), array([[12,  3, 32, 29, 44],\n",
              "        [23, 87, 10, 71, 22],\n",
              "        [18,  6, 48, 24, 42]]), array([[93, 12, 11,  9, 92],\n",
              "        [91, 98, 25, 13, 38],\n",
              "        [20, 61, 61, 23, 28]]), array([[28, 41, 52, 87, 96],\n",
              "        [93, 80, 65, 36, 22],\n",
              "        [54, 74, 90, 42, 79]]), array([[10, 34, 26, 33, 55],\n",
              "        [91, 96, 88, 21, 29],\n",
              "        [13, 93, 37, 50, 98]]), array([[74, 38, 51,  6, 91],\n",
              "        [ 8, 69,  4, 78, 94],\n",
              "        [91, 23, 39, 30, 74]]), array([[21, 15, 96, 80,  3],\n",
              "        [73, 69, 14, 47, 41],\n",
              "        [77, 17, 53, 29, 44]]), array([[82, 20, 91,  0, 90],\n",
              "        [18, 45, 81, 77, 43],\n",
              "        [12, 23, 94, 36, 88]]), array([[17, 86, 46, 16, 16],\n",
              "        [60, 36, 30, 14, 16],\n",
              "        [56, 88, 57, 28, 25]]), array([[86, 43, 41, 89,  2],\n",
              "        [17, 51, 90, 52, 54],\n",
              "        [54, 23, 36, 64, 72]]), array([[46, 23,  5, 14, 11],\n",
              "        [12, 93, 14, 37,  6],\n",
              "        [97, 75, 19, 16, 64]]), array([[55, 69, 31, 84, 67],\n",
              "        [54, 66, 82, 15, 64],\n",
              "        [72, 80, 95, 28,  0]]), array([[ 4, 24, 60, 14, 19],\n",
              "        [54, 24, 65, 37, 63],\n",
              "        [ 4, 62,  8, 15, 27]]), array([[37, 39, 32, 67, 72],\n",
              "        [46, 28, 88, 68, 38],\n",
              "        [40,  9, 82, 95,  7]]), array([[30, 90, 87, 96, 38],\n",
              "        [84, 23, 67, 17, 52],\n",
              "        [50, 92, 14,  8, 38]]), array([[45,  4, 48, 19, 10],\n",
              "        [77, 38, 92, 25,  0],\n",
              "        [33, 81, 54, 14, 35]]), array([[15, 13, 59, 47, 32],\n",
              "        [55, 71,  0, 72, 84],\n",
              "        [ 0, 64, 45, 28, 83]]), array([[ 6, 61, 44, 66, 98],\n",
              "        [ 4, 64, 83, 54, 48],\n",
              "        [38, 88, 47, 58, 63]]), array([[64, 59,  3,  8, 11],\n",
              "        [87, 20, 80, 51, 18],\n",
              "        [ 6, 72, 61, 39, 65]]), array([[34, 30, 73, 38, 74],\n",
              "        [ 4, 40, 36, 54, 65],\n",
              "        [13, 13,  7, 56, 91]]), array([[75, 28, 79, 13, 58],\n",
              "        [31, 41, 93, 97, 35],\n",
              "        [68, 18,  7,  7, 92]]), array([[33, 72, 54, 17, 35],\n",
              "        [83, 35, 63, 41, 58],\n",
              "        [10, 11, 68, 31, 43]]), array([[77, 77, 95, 64, 83],\n",
              "        [63, 73, 90, 72, 60],\n",
              "        [37, 11, 46, 27,  0]]), array([[44, 95, 53, 63, 39],\n",
              "        [24,  4, 16, 58, 59],\n",
              "        [66, 36, 16, 40, 75]]), array([[ 2, 90,  4, 12, 84],\n",
              "        [ 6, 88, 85,  6, 54],\n",
              "        [ 4, 67, 52, 32, 95]]), array([[49, 27, 96, 38, 47],\n",
              "        [87, 12, 49, 67, 55],\n",
              "        [ 0, 19, 15, 78, 66]]), array([[58,  1, 47, 91, 80],\n",
              "        [ 4, 55, 91,  6, 75],\n",
              "        [43,  2, 12, 77, 10]]), array([[52, 56, 46, 72, 60],\n",
              "        [41, 63,  6, 12, 79],\n",
              "        [ 9, 72, 25, 10, 82]]), array([[58, 87, 93, 56, 43],\n",
              "        [90, 23, 78,  7, 67],\n",
              "        [52, 82, 47, 75, 84]]), array([[35, 62, 17, 26, 88],\n",
              "        [41, 96, 19, 70, 59],\n",
              "        [85, 56, 75, 76, 11]]), array([[66, 65, 13,  9, 79],\n",
              "        [55, 28, 63, 98,  9],\n",
              "        [13, 76, 66, 20, 16]]), array([[52, 91, 93, 56, 61],\n",
              "        [35, 51, 95, 91, 41],\n",
              "        [68, 45, 31, 73, 87]]), array([[ 3, 85, 37, 60, 93],\n",
              "        [86, 40, 24, 29, 18],\n",
              "        [16, 68, 85, 91, 22]]), array([[19, 48,  6, 40, 23],\n",
              "        [24, 32, 72, 48, 75],\n",
              "        [84, 28, 19, 28, 87]]), array([[84, 22,  3, 83,  1],\n",
              "        [19,  1, 16, 24, 41],\n",
              "        [71, 48, 52, 51, 26]]), array([[80, 35, 67, 47, 88],\n",
              "        [ 0, 72, 73, 60, 16],\n",
              "        [63,  7, 90, 62, 39]]), array([[50, 76, 65, 83, 59],\n",
              "        [37, 14, 33, 86,  3],\n",
              "        [77, 18, 75, 76, 19]]), array([[13, 75, 20, 15, 54],\n",
              "        [32, 45,  0, 16, 86],\n",
              "        [77, 70, 57, 75,  6]]), array([[65, 65,  1, 10, 67],\n",
              "        [95, 16, 61, 20, 60],\n",
              "        [53, 70, 26, 66, 32]]), array([[70, 40, 66, 75, 76],\n",
              "        [ 6, 94, 44, 49, 94],\n",
              "        [64, 30, 45, 97, 23]]), array([[84, 69, 94,  6, 51],\n",
              "        [23, 74, 24, 14, 66],\n",
              "        [88, 16, 30, 49, 57]]), array([[10, 79, 38, 20, 51],\n",
              "        [15,  9, 59, 94, 93],\n",
              "        [ 5, 70,  0, 93, 29]]), array([[98, 35, 49, 87, 74],\n",
              "        [90, 74, 21, 76, 61],\n",
              "        [33, 46, 27, 96,  1]]), array([[30, 68, 95,  9, 49],\n",
              "        [13, 83, 59, 12, 40],\n",
              "        [87, 79, 40, 52, 57]]), array([[10, 85, 73, 86, 79],\n",
              "        [87,  7, 71,  9, 37],\n",
              "        [47, 71, 73,  5, 44]]), array([[ 3, 73, 76,  9, 62],\n",
              "        [94, 55, 79,  2,  6],\n",
              "        [60, 72, 59, 69, 52]]), array([[47, 64, 79, 36, 41],\n",
              "        [80, 32, 24, 16, 48],\n",
              "        [29, 22, 29, 82, 16]]), array([[63, 90, 40, 44, 51],\n",
              "        [89, 57, 80, 56, 69],\n",
              "        [86, 47, 93, 62, 53]]), array([[47, 81, 74, 73, 74],\n",
              "        [31, 75, 89, 83, 36],\n",
              "        [56, 65, 58, 68, 61]]), array([[57, 34, 84, 67, 51],\n",
              "        [66, 66, 56, 69,  0],\n",
              "        [28, 46, 23, 24, 79]]), array([[36,  9, 58, 37, 74],\n",
              "        [45,  7, 58, 45,  1],\n",
              "        [66, 90, 48, 30, 77]]), array([[12,  3, 32, 29, 44],\n",
              "        [23, 87, 10, 71, 22],\n",
              "        [18,  6, 48, 24, 42]]), array([[93, 12, 11,  9, 92],\n",
              "        [91, 98, 25, 13, 38],\n",
              "        [20, 61, 61, 23, 28]]), array([[28, 41, 52, 87, 96],\n",
              "        [93, 80, 65, 36, 22],\n",
              "        [54, 74, 90, 42, 79]]), array([[10, 34, 26, 33, 55],\n",
              "        [91, 96, 88, 21, 29],\n",
              "        [13, 93, 37, 50, 98]]), array([[74, 38, 51,  6, 91],\n",
              "        [ 8, 69,  4, 78, 94],\n",
              "        [91, 23, 39, 30, 74]]), array([[21, 15, 96, 80,  3],\n",
              "        [73, 69, 14, 47, 41],\n",
              "        [77, 17, 53, 29, 44]]), array([[82, 20, 91,  0, 90],\n",
              "        [18, 45, 81, 77, 43],\n",
              "        [12, 23, 94, 36, 88]]), array([[17, 86, 46, 16, 16],\n",
              "        [60, 36, 30, 14, 16],\n",
              "        [56, 88, 57, 28, 25]]), array([[86, 43, 41, 89,  2],\n",
              "        [17, 51, 90, 52, 54],\n",
              "        [54, 23, 36, 64, 72]]), array([[46, 23,  5, 14, 11],\n",
              "        [12, 93, 14, 37,  6],\n",
              "        [97, 75, 19, 16, 64]]), array([[55, 69, 31, 84, 67],\n",
              "        [54, 66, 82, 15, 64],\n",
              "        [72, 80, 95, 28,  0]]), array([[ 4, 24, 60, 14, 19],\n",
              "        [54, 24, 65, 37, 63],\n",
              "        [ 4, 62,  8, 15, 27]]), array([[37, 39, 32, 67, 72],\n",
              "        [46, 28, 88, 68, 38],\n",
              "        [40,  9, 82, 95,  7]]), array([[30, 90, 87, 96, 38],\n",
              "        [84, 23, 67, 17, 52],\n",
              "        [50, 92, 14,  8, 38]]), array([[45,  4, 48, 19, 10],\n",
              "        [77, 38, 92, 25,  0],\n",
              "        [33, 81, 54, 14, 35]]), array([[15, 13, 59, 47, 32],\n",
              "        [55, 71,  0, 72, 84],\n",
              "        [ 0, 64, 45, 28, 83]]), array([[ 6, 61, 44, 66, 98],\n",
              "        [ 4, 64, 83, 54, 48],\n",
              "        [38, 88, 47, 58, 63]]), array([[64, 59,  3,  8, 11],\n",
              "        [87, 20, 80, 51, 18],\n",
              "        [ 6, 72, 61, 39, 65]]), array([[34, 30, 73, 38, 74],\n",
              "        [ 4, 40, 36, 54, 65],\n",
              "        [13, 13,  7, 56, 91]]), array([[75, 28, 79, 13, 58],\n",
              "        [31, 41, 93, 97, 35],\n",
              "        [68, 18,  7,  7, 92]]), array([[33, 72, 54, 17, 35],\n",
              "        [83, 35, 63, 41, 58],\n",
              "        [10, 11, 68, 31, 43]]), array([[77, 77, 95, 64, 83],\n",
              "        [63, 73, 90, 72, 60],\n",
              "        [37, 11, 46, 27,  0]])]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 495
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z08ODJt78SZw",
        "colab_type": "text"
      },
      "source": [
        "### Задача 3\n",
        "\n",
        "* Найдите все элементы массива my_array, которые больше трех и меньше 5 одновременно. Используйте методологию подвыборки массива с условием (раздел \"Индексация\")."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K-u52EdTih4I",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "eaa6fe03-760c-4c90-981e-a612d0c9b7b8"
      },
      "source": [
        "print(my_array[(my_array > 3) & (my_array <= 5)])"
      ],
      "execution_count": 496,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[4 4 4 4 5 5 4 5 4 4 4 4 4]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P_O3RZUR8SZ6",
        "colab_type": "text"
      },
      "source": [
        "### Задача 4\n",
        "\n",
        "Создайте трехмерный массив размера 2 на 3 на 4, состоящий из случайных ВЕЩЕСТВЕННЫХ чисел от 15 до 37. Используйте встроенные методы библиотеки  np.random."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gVBmk2FXp2bu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "c16a3f34-5e2a-4d63-edd5-3c45bfbf62d0"
      },
      "source": [
        "my_array_3d = np.random.randint(15, 37, (2, 3, 4))\n",
        "print(my_array_3d)"
      ],
      "execution_count": 497,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[18 21 31 18]\n",
            "  [36 21 15 34]\n",
            "  [27 21 17 18]]\n",
            "\n",
            " [[36 18 34 25]\n",
            "  [29 29 29 16]\n",
            "  [23 27 36 18]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1NdemOWxswbm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# print(my_array_3d[:1])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_8q3NF_k8SaA",
        "colab_type": "text"
      },
      "source": [
        "### Задача 5\n",
        "\n",
        "Используя массив из предыдущей задачи, преобразуйте его в новый массив со следующими значениями:\n",
        "\n",
        "    * \"small\", если значения меньше 20\n",
        "    * \"medium\", если значения в промежутке [20, 30]\n",
        "    * \"large\", если значения больше 30"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2TCjxQxmtP0r",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# print(my_array_3d.shape)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1maGNxcKv73-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "241e77c5-83e6-4223-f0fa-d1b3bcbf1661"
      },
      "source": [
        "small = my_array_3d\n",
        "my_array_3d = np.random.randint(0, 20, (2,3,4))\n",
        "print(small)"
      ],
      "execution_count": 501,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[15  6 17  9]\n",
            "  [ 9  2 12  8]\n",
            "  [ 0  7  6 13]]\n",
            "\n",
            " [[ 0  0  9  6]\n",
            "  [17  0  1  5]\n",
            "  [11  3  7 12]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XSoXRr1lzs0V",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "a37235ab-5ca6-44fd-bebc-de2772a2765c"
      },
      "source": [
        "medium = my_array_3d\n",
        "medium = np.random.randint(20, 30, (2, 3, 4))\n",
        "medium"
      ],
      "execution_count": 502,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[[21, 23, 23, 21],\n",
              "        [23, 21, 26, 23],\n",
              "        [22, 25, 23, 21]],\n",
              "\n",
              "       [[27, 27, 27, 22],\n",
              "        [29, 23, 24, 21],\n",
              "        [26, 20, 27, 23]]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 502
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uBJk40hQ022s",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "outputId": "18bae697-ecc1-4e33-a91c-59b436b505d5"
      },
      "source": [
        "large = my_array_3d\n",
        "large = np.random.randint(30, 37, (2, 3, 4))\n",
        "large"
      ],
      "execution_count": 503,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[[31, 34, 31, 31],\n",
              "        [35, 36, 33, 31],\n",
              "        [34, 30, 35, 33]],\n",
              "\n",
              "       [[30, 35, 30, 31],\n",
              "        [32, 32, 31, 35],\n",
              "        [30, 36, 33, 32]]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 503
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hOhMOcs18SaF",
        "colab_type": "text"
      },
      "source": [
        "### Задача 6\n",
        "\n",
        "Создайте одномерный массив из случайных 10 значений. \n",
        "\n",
        "* Не используя цикл for, найдите сумму значений с 3 по 7 элемент.\n",
        "* Найдите сумму квадратов последних двух элементов."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1H3P_LjO1Gjz",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "649c6f69-ece2-49c2-a102-a23e2bed599e"
      },
      "source": [
        "my_array_6 = np.array([0, 10, 7, 8, 12, 25, 1578, 36, 10, 10])\n",
        "print(my_array_6)\n",
        "print(my_array_6[2] + my_array_6[3] + my_array_6[4] + my_array_6[5] + my_array_6[6])\n",
        "print((my_array_6[8]**2) + (my_array_6[9]**2))"
      ],
      "execution_count": 504,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[   0   10    7    8   12   25 1578   36   10   10]\n",
            "1630\n",
            "200\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}