__author__ = 'projero'
import math

class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_minutes(self):
        result = self.hours * 60 + self.minutes
        return result

    def time_to_midnight(self):
        hours = 23 - self.hours
        minutes = 60 - self.minutes
        seconds = 60 - self.seconds
        return "Time to midnight : " + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "."

    def __str__(self):
        print(self.hours)
        return 'Time %d:%d:%d' % (self.hours, self.minutes, self.seconds)

class TrainTime(Time):
    def __init__(self, number, hours, minutes, seconds, destination):
        self.number = number
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.destination = destination

    def time_to_departure(self, hours, minutes, seconds):
        result = hours * 60 + minutes
        result = self.time_minutes() - result
        return result

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        result = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return result

    def __str__(self):
        return "Triangle (" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + \
               ") square = " + str(self.square()) + " perimeter = " + str(self.perimeter())

class Quard(Triangle):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        result = math.sqrt((4 * self.e ** 2 * self.f ** 2 -
                            (self.b ** 2 + self.d ** 2 - self.a ** 2 - self.c ** 2)) / 16)
        return result

    def __str__(self):
        return "Quard (" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d) + \
               ") square = " + str(self.square()) + " perimeter = " + str(self.perimeter())


time = Time(10, 11, 43)
trainTime = TrainTime(12, 14, 55, 0, "Kiev")
print(time)
print(time.time_minutes())
print(time.time_to_midnight())
print(trainTime)
print(trainTime.time_to_departure(10, 17, 0))
triangle = Triangle(3, 4, 5)
print(triangle)
quard = Quard(5, 3, 5, 7, 4, 7)
print(quard)
