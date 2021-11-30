class DVD:
    def __init__(self, name, dvd_id, creation_year, creation_month: str, age_restriction):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def _date_convertor(date: str):
        """
        converts f.ex. "25.11.1995" -> 25, 'November', 1995
        """
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
            12: "December",
        }
        day, month, year = date.split(".")
        creation_year = int(year)
        creation_month = months[int(month)]
        return creation_month, creation_year

    @classmethod
    def from_date(cls, dvd_id, name, date, age_restriction):  # date: "day.month.year" - numbers
        creation_month, creation_year = cls._date_convertor(date)
        return cls(name, dvd_id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
