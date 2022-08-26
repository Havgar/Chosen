init python:
    class day_time(object):
        def __init__(self):
            self.day = 1 # set this to whatever starting day is
            self.weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # arrange these so first weekday goes first
            self.time_of_day = ["Morning","Noon","Evening","Night"] # add or remove to increase time of day slots
            self.end_of_day = self.time_of_day[-1] # automatically picks last slot as end of day

        @property
        def weekday(self):
            return self.weekdays[(self.day-1)%7]

        @property
        def time(self):
            return self.time_of_day[0]

        def advance(self, increment = 0, days = 0):
            if not (increment + days): # no input
                increment = 1

            if days: # add to increment by length of time_of_day
                increment += days * len(self.time_of_day)

            while increment > 0: # loop through increments to shift timeslot and days forward
                if self.time_of_day[0] == self.end_of_day:
                    self.day += 1
                self.time_of_day.append(self.time_of_day.pop(0))
                increment -= 1 # reduce incrememnt to escape loop after enough runs

default clock = day_time()
