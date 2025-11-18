{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMt2eliXOlaN2gELpCU4mbR"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-fF-kSVLwmr4",
        "outputId": "6edee1fa-89e1-408e-aa0a-6c66a286ea6d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: ColabTurtlePlus in /usr/local/lib/python3.12/dist-packages (2.0.1)\n"
          ]
        }
      ],
      "source": [
        "!pip install ColabTurtlePlus\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import ColabTurtlePlus.Turtle as t"
      ],
      "metadata": {
        "id": "6CS4ZsQHw2FU"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#square\n",
        "t.initializeTurtle()\n",
        "t.fd(90)\n",
        "t.rt(90)\n",
        "t.fd(90)\n",
        "t.rt(90)\n",
        "t.fd(90)\n",
        "t.rt(90)\n",
        "t.fd(90)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "mg_SfWvUxTol",
        "outputId": "fc273db1-43ef-4a23-9eea-1917a3106440"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"600\">  \n",
              "        <rect width=\"100%\" height=\"100%\" style=\"fill:white;stroke:;stroke-width:1\"/>\n",
              "        \n",
              "        \n",
              "        <line x1=\"400.0\" y1=\"300.0\" x2=\"490.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"490.0\" y1=\"300.0\" x2=\"490.0\" y2=\"390.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"490.0\" y1=\"390.0\" x2=\"400.0\" y2=\"390.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"390.0\" x2=\"400.0\" y2=\"380.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"380.0\" x2=\"400.0\" y2=\"370.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"370.0\" x2=\"400.0\" y2=\"360.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"360.0\" x2=\"400.0\" y2=\"350.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"350.0\" x2=\"400.0\" y2=\"340.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"340.0\" x2=\"400.0\" y2=\"330.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"330.0\" x2=\"400.0\" y2=\"320.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"320.0\" x2=\"400.0\" y2=\"310.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"310.0\" x2=\"400.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" />\n",
              "        \n",
              "        \n",
              "        <g id=\"classic\" visibility=\"visible\" transform=\"rotate(180,400.0,300.0) translate(400.0, 300.0)\">\n",
              "<polygon points=\"-5,-4.5 0,-2.5 5,-4.5 0,4.5\" transform=\"skewX(0) scale(1,1)\" style=\"stroke:black;fill:black;stroke-width:1\" />\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#rectangle\n",
        "t.initializeTurtle()\n",
        "t.fd(200)\n",
        "t.rt(90)\n",
        "t.fd(100)\n",
        "t.rt(90)\n",
        "t.fd(200)\n",
        "t.rt(90)\n",
        "t.fd(100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "jWtQaocmx2Co",
        "outputId": "a6ff2af6-79fe-4cd8-ef21-a933b9052c51"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"600\">  \n",
              "        <rect width=\"100%\" height=\"100%\" style=\"fill:white;stroke:;stroke-width:1\"/>\n",
              "        \n",
              "        \n",
              "        <line x1=\"400.0\" y1=\"300.0\" x2=\"600.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"600.0\" y1=\"300.0\" x2=\"600.0\" y2=\"400.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"600.0\" y1=\"400.0\" x2=\"400.0\" y2=\"400.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"400.0\" x2=\"400.0\" y2=\"390.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"390.0\" x2=\"400.0\" y2=\"380.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"380.0\" x2=\"400.0\" y2=\"370.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"370.0\" x2=\"400.0\" y2=\"360.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"360.0\" x2=\"400.0\" y2=\"350.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"350.0\" x2=\"400.0\" y2=\"340.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"340.0\" x2=\"400.0\" y2=\"330.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"330.0\" x2=\"400.0\" y2=\"320.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"320.0\" x2=\"400.0\" y2=\"310.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"400.0\" y1=\"310.0\" x2=\"400.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" />\n",
              "        \n",
              "        \n",
              "        <g id=\"classic\" visibility=\"visible\" transform=\"rotate(180,400.0,300.0) translate(400.0, 300.0)\">\n",
              "<polygon points=\"-5,-4.5 0,-2.5 5,-4.5 0,4.5\" transform=\"skewX(0) scale(1,1)\" style=\"stroke:black;fill:black;stroke-width:1\" />\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#triangle\n",
        "t.initializeTurtle()\n",
        "t.fd(200)\n",
        "t.lt(135)\n",
        "t.fd(145)\n",
        "t.lt(90)\n",
        "t.fd(145)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "GOZzXNPO87L3",
        "outputId": "ff0cd9b9-0d88-42fa-82e5-a86f1648e191"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"600\">  \n",
              "        <rect width=\"100%\" height=\"100%\" style=\"fill:white;stroke:;stroke-width:1\"/>\n",
              "        \n",
              "        \n",
              "        <line x1=\"400.0\" y1=\"300.0\" x2=\"600.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"600.0\" y1=\"300.0\" x2=\"497.47\" y2=\"197.47\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"497.47\" y1=\"197.47\" x2=\"490.39893218813455\" y2=\"204.54106781186547\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"490.39893218813455\" y1=\"204.54106781186547\" x2=\"483.3278643762691\" y2=\"211.61213562373095\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"483.3278643762691\" y1=\"211.61213562373095\" x2=\"476.2567965644036\" y2=\"218.68320343559643\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"476.2567965644036\" y1=\"218.68320343559643\" x2=\"469.1857287525381\" y2=\"225.7542712474619\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"469.1857287525381\" y1=\"225.7542712474619\" x2=\"462.11466094067265\" y2=\"232.82533905932738\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"462.11466094067265\" y1=\"232.82533905932738\" x2=\"455.0435931288072\" y2=\"239.89640687119285\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"455.0435931288072\" y1=\"239.89640687119285\" x2=\"447.9725253169417\" y2=\"246.96747468305833\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"447.9725253169417\" y1=\"246.96747468305833\" x2=\"440.9014575050762\" y2=\"254.0385424949238\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"440.9014575050762\" y1=\"254.0385424949238\" x2=\"433.83038969321075\" y2=\"261.10961030678925\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"433.83038969321075\" y1=\"261.10961030678925\" x2=\"426.7593218813453\" y2=\"268.1806781186547\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"426.7593218813453\" y1=\"268.1806781186547\" x2=\"419.6882540694798\" y2=\"275.2517459305202\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"419.6882540694798\" y1=\"275.2517459305202\" x2=\"412.6171862576143\" y2=\"282.3228137423857\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"412.6171862576143\" y1=\"282.3228137423857\" x2=\"405.54611844574885\" y2=\"289.39388155425115\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"405.54611844574885\" y1=\"289.39388155425115\" x2=\"398.47505063388337\" y2=\"296.4649493661166\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" /><line x1=\"398.47505063388337\" y1=\"296.4649493661166\" x2=\"394.93951672795066\" y2=\"300.00048327204934\" stroke-linecap=\"round\" style=\"stroke:black;stroke-width:1\" />\n",
              "        \n",
              "        \n",
              "        <g id=\"classic\" visibility=\"visible\" transform=\"rotate(45,394.93951672795066,300.00048327204934) translate(394.93951672795066, 300.00048327204934)\">\n",
              "<polygon points=\"-5,-4.5 0,-2.5 5,-4.5 0,4.5\" transform=\"skewX(0) scale(1,1)\" style=\"stroke:black;fill:black;stroke-width:1\" />\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#circle\n",
        "t.initializeTurtle()\n",
        "t.circle(50)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "X6JQFypK9GBT",
        "outputId": "2d546e8f-aa6b-4199-a253-1305237601bb"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"600\">  \n",
              "        <rect width=\"100%\" height=\"100%\" style=\"fill:white;stroke:;stroke-width:1\"/>\n",
              "        \n",
              "        \n",
              "        <path d=\"M 400.0 300.0 A 50 50 0 0 0 412.941 298.296\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 412.941 298.296 A 50 50 0 0 0 425.0 293.301\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 425.0 293.301 A 50 50 0 0 0 435.355 285.355\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 435.355 285.355 A 50 50 0 0 0 443.301 275.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 443.301 275.0 A 50 50 0 0 0 448.296 262.941\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 448.296 262.941 A 50 50 0 0 0 450.0 250.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 450.0 250.0 A 50 50 0 0 0 448.296 237.059\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 448.296 237.059 A 50 50 0 0 0 443.301 225.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 443.301 225.0 A 50 50 0 0 0 435.355 214.645\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 435.355 214.645 A 50 50 0 0 0 425.0 206.699\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 425.0 206.699 A 50 50 0 0 0 412.941 201.704\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 412.941 201.704 A 50 50 0 0 0 400.0 200.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 400.0 200.0 A 50 50 0 0 0 387.059 201.704\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 387.059 201.704 A 50 50 0 0 0 375.0 206.699\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 375.0 206.699 A 50 50 0 0 0 364.645 214.645\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 364.645 214.645 A 50 50 0 0 0 356.699 225.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 356.699 225.0 A 50 50 0 0 0 351.704 237.059\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 351.704 237.059 A 50 50 0 0 0 350.0 250.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 350.0 250.0 A 50 50 0 0 0 351.704 262.941\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 351.704 262.941 A 50 50 0 0 0 356.699 275.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 356.699 275.0 A 50 50 0 0 0 364.645 285.355\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 364.645 285.355 A 50 50 0 0 0 375.0 293.301\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 375.0 293.301 A 50 50 0 0 0 387.059 298.296\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/><path d=\"M 387.059 298.296 A 50 50 0 0 0 400.0 300.0\" stroke-linecap=\"round\" \n",
              "            fill=\"transparent\" fill-opacity=\"0\" style=\"stroke:black;stroke-width:1\"/>\n",
              "        \n",
              "        \n",
              "        <g id=\"classic\" visibility=\"visible\" transform=\"rotate(-90.0,400.0,300.0) translate(400.0, 300.0)\">\n",
              "<polygon points=\"-5,-4.5 0,-2.5 5,-4.5 0,4.5\" transform=\"skewX(0) scale(1,1)\" style=\"stroke:black;fill:black;stroke-width:1\" />\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Generate a prompt for user to enter the name and specification of shapes for example side(for square),length and breadth (for rectangle) , radius (for circle)\n",
        "#and triangle and code for trutle to drw the shape with the correct specification\n",
        "a=input(\"shape?\")\n",
        "b=input('length?')\n",
        "c=input('breath?')\n",
        "\n"
      ],
      "metadata": {
        "id": "-3beHn9_-2Sj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "LyY0vr0TDXPR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}