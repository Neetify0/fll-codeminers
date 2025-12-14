from hub import port, motion_sensor
import motor_pair, runloop, motor

wheel_circumference=17.6
motor_1=port.F
motor_2=port.B
attachment_left=port.C
attachment_right=port.A
motor_pair.pair(motor_pair.PAIR_1, motor_1, motor_2)

def distance_to_degrees(distance):
    return distance/360*wheel_circumference

async def move_distance(distance, direction, speed):
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(motor_2, 0)

    startPos=motor.relative_position(motor_2)
    currentPos=startPos

    while (abs(currentPos)<distance):
        currentPos= distance_to_degrees(motor.relative_position(motor_2))
        yawAngle=motion_sensor.tilt_angles()[0]
        correction=0

        if (yawAngle!=0):
            error=yawAngle*-0.1
            correction=int(error*-2)

        motor_pair.move(motor_pair.PAIR_1, correction, velocity=speed*direction, acceleration=1000)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(500)
    return

async def turn(degrees, direction):
    global lr
    if direction=="right":
        lr=1
    elif direction=="left":
        lr=-1
    else:
        print("fix grammar")
    motion_sensor.reset_yaw(0)
    yawAngle=motion_sensor.tilt_angles()[0]
    while abs(yawAngle)<abs(degrees*9.4):
        yawAngle=motion_sensor.tilt_angles()[0]
        motor_pair.move(motor_pair.PAIR_1, 200*lr)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(500)
    return

async def main():
    #await motor.run_for_degrees(attachment_right, 200, 300)
    #await motor.run_for_degrees(attachment_right, -200, 300)
    #await motor.run_for_degrees(attachment_right, 200, 300)
    #await motor.run_for_degrees(attachment_right, -200, 300)
    #await mission6()
    #await mission5()
    #await mission10()
    #await mission9()
    #await mission8()
    #await mission9_2()
    #await mission10_2()
    #await mission13()
    #await mission11()
    await mission1()

async def mission6():
    await motor.run_for_degrees(attachment_right, 200, 660)
    await move_distance(62.5, 1, 660)
    await turn(30, "left")

async def mission5():
    await move_distance(2, 1, 660)
    await turn(18, "left")
    await motor.run_for_degrees(attachment_right, -200, 660)

async def mission10():
    await motor.run_for_degrees(attachment_right, -100, 600)
    await move_distance(1, -1,660)
    await turn(16, "left")
    await move_distance(39, 1,660)
    await turn(116, "left")
    await motor.run_for_degrees(attachment_right, 200, 660)
    await motor.run_for_degrees(attachment_right, -200, 660)

async def mission9():
    await move_distance(5, -1, 560)
    await turn(25, "left")
    await move_distance(33, 1, 460)
    await runloop.sleep_ms(250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,200, 0, velocity=-460)
    await turn(27, "left")
    await move_distance(17, 1, 660)
    await turn(22, "right")
    await move_distance(45, 1 ,1000)

async def mission8():
    # await motor.run_for_degrees(attachment_right, -200, 700)
    turn_down = 220
    turn_velocity = 600
    await move_distance(36, 1, 660)
    await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    await move_distance(2, -1, 400)

async def mission9_2():
    await turn(45, "left")
    await motor.run_for_degrees(attachment_left, -200, 500)
    await move_distance(7, 1, 560)
    await turn(150, "left")
    await turn(42, "right")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 500, 0, velocity=460)

async def mission10_2():
    turn_down = -220
    turn_velocity = 600
    turn_up= 220
    #await move_distance(5, 1, 560)
    #await turn(90, -1)
    await move_distance(3, 1, 560)
    await turn(42, "right")
    await motor.run_for_degrees(attachment_left, turn_down, turn_velocity)
    await move_distance(37, 1, 600)
    await motor.run_for_degrees(attachment_left, turn_up, turn_velocity)
    await turn(40, "left")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1100, 0, velocity=-1010)

async def mission13():
    await move_distance(3, 1, 660)
    await turn(31, "right")
    await move_distance(70, 1, 660)
    await motor.run_for_degrees(attachment_left, -150, 600)
    await move_distance(9, 1, 660)
    await motor.run_for_degrees(attachment_left, 50, 500)
    await turn(12, "right")
    await motor.run_for_degrees(attachment_left, 200, 500)

async def mission11():
    await move_distance(3,-1, 300)
    await turn(150,"left")
    await move_distance(19, 1, 660)
    await turn(67, "left")

async def mission1():
    await move_distance(40, 1, 660)
    await motor.run_for_degrees(attachment_left, 200, -500)
    await move_distance(4, -2, 300)
    await motor.run_for_degrees(attachment_left, 80, 500)
    await move_distance(3, 1, 300)  
    await motor.run_for_degrees(attachment_left, 80, -500)
runloop.run(main())
