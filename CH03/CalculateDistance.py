"""Calculate distance in m, dm, cm, and mm"""

distance = float(input("Enter distance in m that the athlete jumped: "))

world_record = 8.85

difference_meter = world_record-distance

meters = int(difference_meter%10)
decimeters = int(difference_meter*100%100/10)
centimeters = int(difference_meter*100%100%10)
milimeters = int(difference_meter*1000%10)

print(f"You need to jump: {difference_meter:.3f} additional meters to improve the world record")
print(f'Meters: {meters:.1f} meters')
print(f'Decimers: {decimeters:.1f} decimeters')
print(f'Centimeters: {centimeters:.1f} centimeters')
print(f'Millimeters: {milimeters:.1f} millimeters')