import random
import smtplib

otp = str(random.randint(100, 999))

def send_email(email, otp):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    subject = "OTP Verification"
    message = f"Your OTP is: {otp}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Using Gmail's SMTP server and port
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, f"Subject: {subject}\n\n{message}")
        server.quit()
        print("OTP sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    user_email = input("Enter your email address: ")

    try:
        user_otp = int(input("Enter the OTP you received: "))
    except ValueError:
        print("Invalid OTP format. Please enter a 3-digit number.")
        return

    if user_otp == int(otp):
        print("OTP verification successful. You can proceed.")
    else:
        print("OTP verification failed. Please try again.")

if __name__ == "__main__":
    send_email("swethavanitha172@yahoo.com", otp)  # Replace with the recipient's email
    main()
