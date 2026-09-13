import traci


AEB_TTC = 1.5

emergency_decel = -8



def AEB_control(vehicle):

    speed = traci.vehicle.getSpeed(vehicle)

    new_speed = speed + emergency_decel * 0.2


    if new_speed < 0:
        new_speed = 0


    traci.vehicle.setSpeed(
        vehicle,
        new_speed
    )


    return new_speed