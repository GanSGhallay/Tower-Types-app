# This is a program for tower types testing

tower_types = ["DA","da", "DB","db", "DBS","dbs", "DC","dc", "DCS","dcs", "DD","dd", "DDS","dds", "DD+18","dd+18", "DD+25","dd+25", "DDH","ddh", "DDH+18","ddh+18", "DDH+25","ddh+25"]

tower = input("Enter tower types:")
for tower in tower_types:
    def t_type(a, b, c, d):
        basic_tower = ["-4.5", "-3.0", "-1.5", "0.0", "1.5", "3.0"]
        normal_tower = ["4.5", "6.0", "7.5", "9.0"]
        body_ext = ["18.0", "25.0"]
        if a in basic_tower:
            print(tower + " is a Basic Body Tower having leg extensions : " + "\nLeg A: " + str(a) + "\nLeg B:" + str(b) + "\nLeg C:" + str(c) + "\nLeg D:" + str(d))
        elif b in normal_tower:
            print(tower + " is a Normal Body Tower having leg extensions : " + "\nLeg A: " + str(a) + "\nLeg B:" + str(b) + "\nLeg C:" + str(c) + "\nLeg D:" + str(d))
        elif d in normal_tower:
            print(tower + " is a Normal Body Tower having leg extensions : " + "\nLeg A: " + str(a) + "\nLeg B:" + str(b) + "\nLeg C:" + str(c) + "\nLeg D:" + str(d))
        else:
            print("Try and Try")

    print("Please enter leg extensions for all four legs:")
    a = float(input("Enter Leg A extension:"))
    b = float(input("Enter Leg B extension:"))
    c = float(input("Enter Leg C extension:"))
    d = float(input("Enter Leg D extension:"))
    t_type(a, b, c, d)




