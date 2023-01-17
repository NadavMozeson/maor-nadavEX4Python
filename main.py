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

class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
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
        return f"{self.year}-{self.month}-{self.day}"

class Time:
    def __init__(self):
        self.hour = None
        self.minute = None

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        m = str(self.minute)
        h = str(self.hour)
        if 10 > self.minute >= 0:
            m = "0" + str(self.minute)
        if 10 > self.hour >= 0:
            h = "0" + str(self.hour)
        return f"{h}:{m}"

    def __repr__(self):
        return f"{self.hour}-{self.minute}"

    def __ge__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute >= other.minute:
                return True
            return False
        return False

class CalendarEntry:
    def __init__(self):
        self.date = Date()
        self.taskDic = dict()

    def __init__(self, year, month, day):
        self.date = Date(year, month, day)
        self.taskDic = dict()

    def addTask(self, name, t1, t2):
        if len(self.taskDic.keys()) == 0:
            self.taskDic[(str(t1), str(t2))] = name
        else:
            for x in list(self.taskDic.keys()):
                minTime = Time(int(str(x[0])[:2]), int(str(x[0])[3:]))
                maxTime = Time(int(str(x[1])[:2]), int(str(x[1])[3:]))
                if maxTime >= t1 >= minTime or maxTime >= t2 >= minTime:
                    print("Event Already Exists on this Time Frame!")
                    return
                else:
                    self.taskDic[(str(t1), str(t2))] = name

    def tasks(self):
        return self.taskDic

    def __str__(self):
        keys = list(self.taskDic.keys())
        keys.sort(key=lambda x: float(str(x[0])[:2] + "." + str(x[0])[3:]))
        count = 0
        resultStr = f"Todo list for {self.date}"
        for x in keys:
            count += 1
            resultStr += f"\n{count}. {x[0]}-{x[1]} - {self.taskDic[x]}"
        return resultStr

today = Date(2023, 1, 17)
t = Time(15, 0)
todo = CalendarEntry(2023, 1, 17)
todo.addTask("Test", Time(11, 59), Time(12, 0))
todo.addTask("Test2", Time(11, 0), Time(11, 1))
todo.addTask("Test3", Time(20, 0), Time(22, 0))
print(todo.tasks())
print(todo)
