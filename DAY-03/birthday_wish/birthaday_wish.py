import pandas as pd
import datetime
import smtplib
import os

# Change directory to where the script is
os.chdir(r"D:\PRACTICE-01\PYTHON\PROJECTS\DAY-03")

# Enter your authentication details
GMAIL_ID = 'your_email@gmail.com'
GMAIL_PSWD = 'your_password'  # Use an app password if needed

def sendEmail(to, sub, msg):
    try:
        print(f"Sending email to {to} with subject: {sub}")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(GMAIL_ID, GMAIL_PSWD)
        s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email to {to}: {e}")

if __name__ == "__main__":
    try:
        # Read the Excel file
        df = pd.read_excel(r"D:/PRACTICE-01/PYTHON/PROJECTS/DAY-03/dataone.xlsx")
        df['Birthday'] = pd.to_datetime(df['Birthday'])  # Ensure Birthday is in datetime format
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        exit()

    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().year
    writeInd = []

    for index, item in df.iterrows():
        try:
            bday = item['Birthday'].strftime("%d-%m")
            if today == bday and str(yearNow) not in str(item['Year']):
                sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
                writeInd.append(index)
        except Exception as e:
            print(f"Error processing row {index}: {e}")

    for i in writeInd:
        try:
            yr = df.loc[i, 'Year']
            df.loc[i, 'Year'] = f"{yr}, {yearNow}"
        except Exception as e:
            print(f"Error updating Year for index {i}: {e}")

    try:
        # Save the updated DataFrame back to Excel
        df.to_excel('data_updated.xlsx', index=False)
        print("Updated file saved as 'data_updated.xlsx'")
    except Exception as e:
        print(f"Error saving Excel file: {e}")
