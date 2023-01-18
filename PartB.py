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


def make_date_class():
    """
    Creates a local area with 3 params and function
    :return: returns a dictionary of the functions
    """
    def new(y, m, d):
        """
        Sets the variables in the local zone from the params.
        :param y: Year to set
        :param m: Month to set
        :param d: Day to set
        """
        year = y
        month = m
        day = d

        def get(st):
            """
            The get function that returns values depending on the param it receives.
            :param st: What you wish to receive
            :return: Returns the wished upon value
            """

            def __str__():
                """
                String convertor.
                :return: A string format of all the fields.
                """
                resultStr = ""
                if day == 11 or day == 12 or day == 13:
                    resultStr += f"{day}th"
                elif day % 10 == 1:
                    resultStr += f"{day}st"
                elif day % 10 == 2:
                    resultStr += f"{day}nd"
                elif day % 10 == 3:
                    resultStr += f"{day}rd"
                else:
                    resultStr += f"{day}th"
                resultStr += f" of {months[month]}, {year}"
                return resultStr

            # Checks what wished to return and returns it.
            if st == "year":
                return year
            if st == "month":
                return months[month]
            if st == "day":
                return day
            if st == "__str__":
                return __str__

        return {"get": get}

    # Returns a dictionary of all the functions in the local zone
    return {"new": new}


def make_time_class():
    """
    Creates a local area with 2 params and function
    :return: returns a dictionary of the functions
    """

    def new(h, m):
        """
        Sets the variables in the local zone from the params.
        :param h: Hour to set for the time. (Integer)
        :param m: Minute to set for the time. (Integer)
        """
        hour = h
        minute = m

        def get(st):
            def __str__():
                """
                String convertor.
                :return: A string format of all the fields.
                """
                m = str(minute)
                h = str(hour)
                if 10 > minute >= 0:
                    m = "0" + str(minute)
                if 10 > hour >= 0:
                    h = "0" + str(hour)
                return f"{h}:{m}"

            def __ge__(other):
                """
                An operator overloading function for the operator >=
                :param other: a other Time object
                :return: True if the current object is >= to the other object, else returns False
                """
                if hour > other['get']("hour"):
                    return True
                elif hour == other['get']("hour"):
                    if minute >= other['get']("minute"):
                        return True
                    return False
                return False

            # Checks what wished to return and returns it.
            if st == "hour":
                return hour
            if st == "minute":
                return minute
            if st == "__str__":
                return __str__
            if st == ">=":
                return __ge__

        return {"get": get}

    # Returns a dictionary of all the functions in the local zone
    return {"new": new}


def make_calentry_class():
    """
    Creates a local area with 2 params and function
    :return: returns a dictionary of the functions
    """

    def new(y, m, d):
        """
        Sets the variables in the local zone from the params.
        :param h: Hour to set for the time. (Integer)
        :param m: Minute to set for the time. (Integer)
        """
        d = make_date_class()
        date = d["new"](2017, 1, 20)
        taskDic = dict()

        def get(st):
            def __str__():
                """
                String convertor.
                :return: A string format of all the fields.
                """
                nonlocal date
                keys = list(taskDic.keys())
                keys.sort(key=lambda x: float(str(x[0])[:2] + "." + str(x[0])[3:]))
                count = 0
                dateStr = date['get']("__str__")()
                resultStr = f"Todo list for {dateStr}"
                for x in keys:
                    count += 1
                    resultStr += f"\n{count}. {x[0]}-{x[1]} - {taskDic[x]}"
                return resultStr

            def addTask(name, t1, t2):
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
                for x in list(taskDic.keys()):
                    Time = make_time_class()
                    minTime = Time['new'](int(str(x[0])[:2]), int(str(x[0])[3:]))
                    maxTime = Time['new'](int(str(x[1])[:2]), int(str(x[1])[3:]))
                    # if there is a task conflict will print an error message and returns back from the function
                    if (maxTime['get'](">=")(t1) and t1['get'](">=")(minTime)) or (maxTime['get'](">=")(t2) and t2['get'](">=")(minTime)):
                        print("Task Already Exists on this Time Frame!")
                        return
                # if we reached this line it means that the task doesn't conflict with any of the other tasks and will
                # add it to the dictionary.
                taskDic[str(t1["get"]("__str__")()), str(t2["get"]("__str__")())] = name

            # Checks what wished to return and returns it.
            if st == "__str__":
                return __str__
            if st == "tasks":
                return taskDic
            if st == "addTask":
                return addTask

        # the new function returns a dictionary with the get function
        return {"get": get}

    # Returns a dictionary of the new function to create an object from the specific type
    return {"new": new}
