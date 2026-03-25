ip = input("Enter IP address: ")

parts = ip.split(".")

if len(parts) != 4:
    print("Invalid IP Address")
else:
    valid = True

    for part in parts:
        if not part.isdigit():
            valid = False
            break

        num = int(part)
        if num < 0 or num > 255:
            valid = False
            break

    if valid:
        print("Valid IP Address")
    else:
        print("Invalid IP Address")
