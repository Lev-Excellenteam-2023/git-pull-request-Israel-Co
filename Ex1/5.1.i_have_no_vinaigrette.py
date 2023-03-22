import random
import calendar
import datetime


def vinaigrette_stock_check(from_date, to_date):
    """
    Get 2 date and generates a date between it.
    If the generated date is monday the function returns I have not vinaigrette
    :param from_date: first date
    :param to_date: second date
    :return: Generated tate and I have not vinaigrette if the dya is monday,
             generated tate otherwise
    """
    from_sec = datetime.datetime.strptime(from_date, '%Y-%m-%d').timestamp()
    to_sec = datetime.datetime.strptime(to_date, '%Y-%m-%d').timestamp()
    interval = to_sec - from_sec

    if interval < 0:
        return "The second date cannot be earlier than the first one"

    rand = random.randint(0, interval)
    today_sec = from_sec + rand
    now = datetime.datetime.fromtimestamp(today_sec)

    if now.weekday() == calendar.MONDAY:
        return f"{now.strftime('%Y-%m-%d')}: I have not vinaigrette!"
    else:
        return now.strftime('%Y-%m-%d')


def main():
    from_date = input('Enter a date in format of YYYY-mm-dd\n')
    to_date = input('Enter another date that is not before the first one in the same format\n')

    print(vinaigrette_stock_check(from_date, to_date))


if __name__ == main():
    main()
