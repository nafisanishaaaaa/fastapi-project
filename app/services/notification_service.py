def write_notification(email: str, message: str = ""):
    with open("log.txt", mode="a") as file:
        content = f"notification for {email}: {message}\n"
        file.write(content)
