import time
from datetime import datetime
from plyer import notification

def notify_water_drink():
    notification.notify(
        title="Please Drink Water Now!!",
        message='''Hydration: Water is essential for the body to function properly. It makes up 50–70% of body weight and is needed by every cell, tissue, and organ. ''',
        app_icon="water.ico",  # Ensure this icon file exists in the same directory
        timeout=10
    )

if __name__ == "__main__":
    while True:
        current_hour = datetime.now().hour
        if 5 <= current_hour < 24:  # Notify only between 5 AM and 12 AM
            notify_water_drink()
        time.sleep(60 * 60)  # Check every hour