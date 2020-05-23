{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MeinModul.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMwt7Y6q+i0SJiIhuCL21rY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/PBeck20/DataScienceSS20/blob/master/exercises/MeinModul.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s3Pnq_-qGE67",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "class Listkeeper:\n",
        "    #Variable myList ist ein Dictionary \n",
        "    myList= {}\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "odvetRcuKLNb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #Initialisierung füllt myList mit dem Schlüssel \"example\" und den Werten 1,2,3,4,5\n",
        "    def __init__(self):\n",
        "        self.myList['example'] = [1,2,3,4,5]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CaZnZK-zK8jM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #Funktion show gibt den/die Schlüssel zurück\n",
        "    def show(self):\n",
        "        return self.myList(keys)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l5fHE1gTO-jo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #Mit add kann man weitere Werte und die dazugehörigen Schlüssel hinzufügen\n",
        "    def add(self, name, nList):\n",
        "        self.myList[name] = nList"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "diWnyelrLwK4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #Der schlüssel und die dazugehörigen Werte werden gelöscht\n",
        "    def delete(name):\n",
        "        self.myList.pop(name)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wx9oOxqtRQXL",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #Sortiert die Liste mit dem Schlüssel \"name\"\n",
        "    def sort(self, name):\n",
        "        self.myList[name].sort()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RQP7ZQm5KWkY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "    #An eine bestehende Liste mit dem Schlüssel \"name\" werden die Werte von \"extraList\" angehängt\n",
        "    def append (self, name, extraList):\n",
        "        self.myList[name].extend(extraList)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w5EAm5vSL8qO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}