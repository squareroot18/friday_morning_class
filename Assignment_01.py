class AirConditioner:
    """A room air-conditioner. Reported buggy by the QA team - fix it!"""
    VALID_MODES = ("cool", "fan", "dry", "auto")
    MIN_TEMP = 16
    MAX_TEMP = 30

    def __init__(self, brand, room_name, temperature=25, mode="cool", fan_speed=1):
        self.brand = brand
        self.room_name = room_name
        self.is_on = False
        self.temperature = temperature
        self.mode = mode
        self.fan_speed = fan_speed
        

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < self.MIN_TEMP or value > self.MAX_TEMP: #a number cannot be <16 and >30 at the same time. Thats the reason why 99 is accepted. so changed to Or instead of AND.
            raise ValueError(f"Temperature must be {self.MIN_TEMP}-{self.MAX_TEMP} C.")
        self._temperature = value #it should assign to the backing variable not calling the setter again.

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.VALID_MODES:
            raise ValueError(f"Mode must be one of {self.VALID_MODES}.")
        self._mode = value

    @property
    def fan_speed(self):
        return self._fan_speed

    @fan_speed.setter
    def fan_speed(self, value):
        if value not in (1, 2, 3):
            raise ValueError("Fan speed must be 1 (low), 2 (medium) or 3 (high).")
        self._fan_speed = value

    @property
    def is_energy_saving(self):
        return self.temperature >= 25 #last code was wrong because it needed to be the current temperature soinstead of storing an old True/False value, we calculate it whenever it is needed.
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def cooler(self):
        self._temperature = max(self.MIN_TEMP, self._temperature - 1) #the error was resulting in 15 in temperature eventhough the MIN_TEMP = 16 so fix the cooler so it cannot go below 16.

    def warmer(self):
        self._temperature = min(self.MAX_TEMP, self._temperature + 1)#the error was resulting in 31 in temperature eventhough the MAX_TEMP = 30 so fix the cooler so it cannot go above 30.

    def __str__(self):
        power = "ON" if self.is_on else "OFF"
        return (f"{self.brand} AC in {self.room_name}: {power}, "
                f"{self.temperature}C, mode={self.mode}, fan={self.fan_speed}") #there will be AttributeError with self.fan cuz there's no attribute 'fan' so changed to existing attribute 'fan_speed'.
