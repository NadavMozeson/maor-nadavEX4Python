# Months Dictionary
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Days in each month dictionary
monthsDays = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


class Date:
    """
    Date Class Contains: Year, month and day of specific date in integer form
    """

    def __init__(self):
        """
        Default constructor.
        In case we need to use it, will create a date with no information (all fields will be None)
        """
        self.year = None
        self.month = None
        self.day = None

    def __init__(self, year, month, day):
        """
        Parameter constructor.
        Create an object with given parameters.
        :param year: What year the date will be (integer)
        :param month: What month the date will be (integer)
        :param day: What day the date will be (integer)
        """
        try:
            if len(str(year)) == 4:
                self.year = year
            else:
                raise Exception("Invalid Year Input")
            if 12 >= month >= 1:
                self.month = month
            else:
                raise Exception("Invalid Month Input")
            if monthsDays[month] >= day >= 0:
                self.day = day
            else:
                raise Exception("Invalid Day Input")
        except:
            print("Invalid Date Input")

    def __str__(self):
        """
        String convertor for objects created by this class.
        :return: A string format of the object
        """
        resultStr = ""
        if self.day == 11 or self.day == 12 or self.day == 13:
            resultStr += f"{self.day}th"
        elif self.day % 10 == 1:
            resultStr += f"{self.day}st"
        elif self.day % 10 == 2:
            resultStr += f"{self.day}nd"
        elif self.day % 10 == 3:
            resultStr += f"{self.day}rd"
        else:
            resultStr += f"{self.day}th"
        resultStr += f" of {months[self.month]}, {self.year}"
        return resultStr

    def __repr__(self):
        """
        Repr convertor for objects created by this class.
        Made more for debugging then for display to users.
        :return: Return a repr to the current object as a string.
        """
        return f"{self.year}-{self.month}-{self.day}"


class Time:
    """
    Time Class Contains: Hour and minute of specific time in integer form
    """

    def __init__(self):
        """
        Default constructor.
        In case we need to use it, will create a time with no information (all fields will be None)
        """
        self.hour = None
        self.minute = None

    def __init__(self, hour, minute):
        """
        Parameter constructor.
        Create an object with given parameters.
        :param hour: What hour the time will be (integer)
        :param minute: What minute the time will be (integer)
        """
        # Checks if time is valid and correct
        try:
            if 24 >= hour >= 0:
                self.hour = hour
            else:
                raise Exception("Invalid Hour Input")
            if 59 >= minute >= 0:
                self.minute = minute
            else:
                raise Exception("Invalid Minute Input")
        except:
            print("Wrong Time Input")

    def __str__(self):
        """
        String convertor for objects created by this class.
        :return: A string format of the object
        """
        m = str(self.minute)
        h = str(self.hour)
        if 10 > self.minute >= 0:
            m = "0" + str(self.minute)
        if 10 > self.hour >= 0:
            h = "0" + str(self.hour)
        return f"{h}:{m}"

    def __repr__(self):
        """
        Repr convertor for objects created by this class.
        Made more for debugging then for display to users.
        :return: Return a repr to the current object as a string.
        """
        return f"{self.hour}-{self.minute}"

    def __ge__(self, other):
        """
        An operator overloading function for the operator >=
        :param other: a other Time object
        :return: True if the current object is >= to the other object, else returns False
        """
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute >= other.minute:
                return True
            return False
        return False


class CalendarEntry:
    """
    CalendarEntry Class Contains: Date, an object created by Date class and taskDic, a dictionary of all tasks in current day.
    """

    def __init__(self):
        """
        Default constructor.
        In case we need to use it, will create a CalendarEntry with no information (all fields will be None)
        """
        self.date = Date()
        self.taskDic = dict()

    def __init__(self, year, month, day):
        """
        Parameter constructor.
        Create an object with given parameters.
        :param year: What year the date will be (integer)
        :param month: What month the date will be (integer)
        :param day: What day the date will be (integer)
        """
        self.date = Date(year, month, day)
        self.taskDic = dict()

    def addTask(self, name, t1, t2):
        """
        The function adds a task to the dictionary only if there is place for it.
        If there isn't already another task on the same time of the new one.
        :param name: The name of the new task we wish to add. (string)
        :param t1: The start time of the task. (Time)
        :param t2: The end time of the task. (Time)
        :return: Adds the task to dictionary if there is a spot for it, else prints "Task Already Exists on this Time Frame!"
        """
        # runs all over the dictionary of tasks and checks if there is a conflict between the new task and
        # every one of the tasks already created in the dictionary
        try:
            for x in list(self.taskDic.keys()):
                minTime = Time(int(str(x[0])[:2]), int(str(x[0])[3:]))
                maxTime = Time(int(str(x[1])[:2]), int(str(x[1])[3:]))
                # if there is a task conflict will print an error message and returns back from the function
                if maxTime >= t1 >= minTime or maxTime >= t2 >= minTime:
                    # Only throws an error but doesn't stop the run of the code
                    raise
            # if we reached this line it means that the task doesn't conflict with any of the other tasks and will
            # add it to the dictionary.
            self.taskDic[(str(t1), str(t2))] = name
        except:
            print("Task Already Exists on this Time Frame!")


    def tasks(self):
        """
        The function returns the dictionary of the tasks.
        """
        return self.taskDic

    def __str__(self):
        """
        String convertor for objects created by this class.
        :return: A string format of the object
        """
        keys = list(self.taskDic.keys())
        keys.sort(key=lambda x: float(str(x[0])[:2] + "." + str(x[0])[3:]))
        count = 0
        resultStr = f"Todo list for {self.date}"
        for x in keys:
            count += 1
            resultStr += f"\n{count}. {x[0]}-{x[1]} - {self.taskDic[x]}"
        return resultStr

    def __repr__(self):
        """
        Repr convertor for objects created by this class.
        Made more for debugging then for display to users.
        :return: Return a repr to the current object as a string.
        """
        return f"{self.date}: {self.taskDic}"
