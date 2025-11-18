{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Bhavik-Arora/Python-Codes/blob/main/TestApp.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 998
        },
        "id": "a7cfBLqbXvK-",
        "outputId": "8e4bb0b4-ed28-48e3-fd1f-aea695b29dcb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Welcome to Bhavik's Services Test App v1.00\n",
            "1. Book a service\n",
            "2. View bookings\n",
            "3. Cancel booking\n",
            "4. Check availability\n",
            "5. Exit\n",
            "Enter your choice: 1\n",
            "Enter your name: 67\n",
            "Enter the service you want: apps\n",
            "Enter the date (YYYY-MM-DD): 2025-11-18\n",
            "Booking successful! 67 booked apps on 2025-11-18\n",
            "\n",
            "Welcome to Bhavik's Services Test App v1.00\n",
            "1. Book a service\n",
            "2. View bookings\n",
            "3. Cancel booking\n",
            "4. Check availability\n",
            "5. Exit\n",
            "Enter your choice: 4\n",
            "Enter the date to check availability (YYYY-MM-DD): 2025-11-18\n",
            "Sorry, Bhavik is not available on this date. Date:- 2025-11-18.\n",
            "\n",
            "Welcome to Bhavik's Services Test App v1.00\n",
            "1. Book a service\n",
            "2. View bookings\n",
            "3. Cancel booking\n",
            "4. Check availability\n",
            "5. Exit\n",
            "Enter your choice: 2\n",
            "Upcoming Bookings:\n",
            "67 - apps on 2025-11-18\n",
            "\n",
            "Welcome to Bhavik's Services Test App v1.00\n",
            "1. Book a service\n",
            "2. View bookings\n",
            "3. Cancel booking\n",
            "4. Check availability\n",
            "5. Exit\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-2186041468.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     76\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     77\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 78\u001b[0;31m     \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/tmp/ipython-input-2186041468.py\u001b[0m in \u001b[0;36mmain\u001b[0;34m()\u001b[0m\n\u001b[1;32m     47\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"5. Exit\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 49\u001b[0;31m         \u001b[0mchoice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter your choice: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mchoice\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'1'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "# My application\n",
        "class BhavikServices:\n",
        "    def __init__(self):\n",
        "        self.bookings = []\n",
        "\n",
        "    def book_service(self, client_name, service_type, date):\n",
        "        booking = {\n",
        "            'client_name': client_name,\n",
        "            'service_type': service_type,\n",
        "            'date': date\n",
        "        }\n",
        "        self.bookings.append(booking)\n",
        "        print(f\"Booking successful! {client_name} booked {service_type} on {date}\")\n",
        "\n",
        "    def view_bookings(self):\n",
        "        if not self.bookings:\n",
        "            print(\"No bookings yet.\")\n",
        "        else:\n",
        "            print(\"Upcoming Bookings:\")\n",
        "            for booking in self.bookings:\n",
        "                print(f\"{booking['client_name']} - {booking['service_type']} on {booking['date']}\")\n",
        "\n",
        "    def cancel_booking(self, client_name, service_type, date):\n",
        "        for booking in self.bookings:\n",
        "            if booking['client_name'] == client_name and booking['service_type'] == service_type and booking['date'] == date:\n",
        "                self.bookings.remove(booking)\n",
        "                print(f\"Booking for {client_name} ({service_type} on {date}) cancelled.\")\n",
        "                return\n",
        "        print(\"Sorry, booking not found.\")\n",
        "\n",
        "    def check_availability(self, date):\n",
        "        for booking in self.bookings:\n",
        "            if booking['date'] == date:\n",
        "                print(f\"Sorry, Bhavik is not available on this date. Date:- {date}.\")\n",
        "                return\n",
        "        print(f\"Bhavik is available on {date}.\")\n",
        "\n",
        "def main():\n",
        "    bhavik_services = BhavikServices()\n",
        "\n",
        "    while True:\n",
        "        print(\"\\nWelcome to Bhavik's Services Test App v1.00\")\n",
        "        print(\"1. Book a service\")\n",
        "        print(\"2. View bookings\")\n",
        "        print(\"3. Cancel booking\")\n",
        "        print(\"4. Check availability\")\n",
        "        print(\"5. Exit\")\n",
        "\n",
        "        choice = input(\"Enter your choice: \")\n",
        "\n",
        "        if choice == '1':\n",
        "            client_name = input(\"Enter your name: \")\n",
        "            service_type = input(\"Enter the service you want: \")\n",
        "            date = input(\"Enter the date (YYYY-MM-DD): \")\n",
        "            bhavik_services.book_service(client_name, service_type, date)\n",
        "\n",
        "        elif choice == '2':\n",
        "            bhavik_services.view_bookings()\n",
        "\n",
        "        elif choice == '3':\n",
        "            client_name = input(\"Enter your name: \")\n",
        "            service_type = input(\"Enter the service you want to cancel: \")\n",
        "            date = input(\"Enter the date of booking (YYYY-MM-DD): \")\n",
        "            bhavik_services.cancel_booking(client_name, service_type, date)\n",
        "\n",
        "        elif choice == '4':\n",
        "            date = input(\"Enter the date to check availability (YYYY-MM-DD): \")\n",
        "            bhavik_services.check_availability(date)\n",
        "\n",
        "        elif choice == '5':\n",
        "            print(\"Exiting Bhavik's Services App. Goodbye!\")\n",
        "            break\n",
        "\n",
        "        else:\n",
        "            print(\"Invalid choice. Please enter a number from 1 to 5.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXHXNcQpppt0HOZt8t71yA",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}