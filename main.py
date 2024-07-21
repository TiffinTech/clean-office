import datetime
import time

class BackpackOrganizer:
    def __init__(self, remind_interval_days=7):
        self.last_organized = None
        self.remind_interval = datetime.timedelta(days=remind_interval_days)

    def organize(self):
        print("Organizing your tech backpack...")
        time.sleep(1)  
        print("Tech backpack organized!")
        self.last_organized = datetime.datetime.now()

    def check_if_organization_needed(self):
        if self.last_organized is None:
            print("You haven't organized your tech backpack yet!")
            return True
        
        time_since_last_organized = datetime.datetime.now() - self.last_organized
        if time_since_last_organized >= self.remind_interval:
            print(f"It's been {time_since_last_organized.days} days since you last organized your tech backpack.")
            return True
        else:
            days_until_next_reminder = (self.remind_interval - time_since_last_organized).days
            print(f"Your tech backpack was organized {time_since_last_organized.days} days ago.")
            print(f"Next reminder in {days_until_next_reminder} days.")
            return False

def main():
    organizer = BackpackOrganizer(remind_interval_days=7)
    
    while True:
        print("\nChecking your tech backpack...")
        if organizer.check_if_organization_needed():
            choice = input("Would you like to organize your tech backpack now? (yes/no): ")
            if choice.lower() == 'yes':
                organizer.organize()
            else:
                print("Okay, we'll remind you again later.")
        
        print("\nTime passes...")
        time.sleep(2) 
        organizer.last_organized -= datetime.timedelta(days=3)  # Subtract 3 days from last_organized

        choice = input("Continue simulation? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("Backpack organizer reminder simulation ended.")

if __name__ == "__main__":
    main()