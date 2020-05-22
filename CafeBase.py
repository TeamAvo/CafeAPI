import datetime
from Crawler import Crawler
import json
import os.path


# Database that manages the data for the API
class CafeBase:
    def __init__(self):

        # Checks to see if a json file with the data for the week exists
        # TODO: Check if the file is up to date
        if os.path.isfile('../CafeAPI/data.json'):
            # Reads the data from the file into a variable
            with open('../CafeAPI/data.json', 'r') as f:
                self.base = json.load(f)
            print("Database: Retrieved data from file")
        else:
            # Run the Crawler a max of 5 times for more stability in case of unstable internet
            for i in range(4):
                try:
                    # Release Crawler
                    with Crawler() as c:
                        # Navigate and collect data
                        c.nav()

                        # Set data to variable
                        self.base = c.get_info()

                        # Write the data to a file for future reference
                        with open('../Throwaway/CafeAPI/data.json', 'w') as f:
                            json.dump(self.base, f)
                    # Break if all of the above works successfully
                    print(f"Database: Retrieved data from Crawler on try #{i}")
                    break
                except:
                    # This means that something failed and the program has to retry
                    print(f"Database: Something went wrong, loading data retry #{i}")
                    pass

        print("Database: Initiated Data Collection")

    # For future use of the app wants menus based on time
    @staticmethod
    def hrs_min(t=None):
        if not t:
            hrs = datetime.datetime.now().time().hour
            minutes = datetime.datetime.now().time().minute
            return (hrs * 100) + minutes
        hrs = t.time().hour
        minutes = t.time().minute
        return (hrs * 100) + minutes

    # Returns an organized dict of the menu for a specific day
    # Days are 0-7 with 0 = Sun
    def day_menu(self, day):
        day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][day]

        print("Collected Data:")
        print([
            {"title": 'Breakfast', "data": self.base[0].get(day, [])},
            {"title": 'Lunch', "data": self.base[1].get(day, [])},
            {"title": 'Dinner', "data": self.base[2].get(day, [])},
        ])

        return [
            {"title": 'Breakfast', "data": self.base[0].get(day, [])},
            {"title": 'Lunch', "data": self.base[1].get(day, [])},
            {"title": 'Dinner', "data": self.base[2].get(day, [])},
        ]

    # Test method for testing the return values of the database
    def test(self):
        print(self.base)


if __name__ == '__main__':
    base = CafeBase()
    base.test()
