from hub import port, motion_sensor
import motor_pair, runloop, motor


wheel_circumference=17.6

MoveMotor1=port.F
MoveMotor2=port.B
attachment_left=port.C
attachment_right=port.A
motor_pair.pair(motor_pair.PAIR_1, MoveMotor1, MoveMotor2)

def distance_to_degrees(distance):
    return (distance/360)*wheel_circumference

async def move_distance(distance, direction, vel):
    # print("In moveStraight")
    motion_sensor.reset_yaw(0)
    # Setting starting point and yaw to 0
    motor.reset_relative_position(MoveMotor2, 0)

    startPos = motor.relative_position(MoveMotor2)
    # print("Starting position is ", startPos)

    current_rel_pos = startPos

    #moving motor until new relative position is distance or greater
    while (abs(current_rel_pos) < abs(distance)):
        #collect the yaw angle and current relative position
        current_rel_pos = distance_to_degrees(motor.relative_position(MoveMotor2))
        yawAngle = motion_sensor.tilt_angles()[0]
        # print("currpos is ", current_rel_pos)
        correction = 0

        if (yawAngle != 0):
            # print("Yaw is ", yawAngle)
            error = yawAngle * -0.1
            correction = int(error * -2)


        motor_pair.move(motor_pair.PAIR_1, correction*direction, velocity=vel * direction, acceleration=1000)
    motor_pair.stop(motor_pair.PAIR_1)
    print("Now returning with relpos: ", current_rel_pos)
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
    #await mission0()
        # 6 5 10 9
    # await mission6()
    # await mission5()
    # await mission10()
    # await mission9()
        # 8
    #await mission8()
    # await mission9_2()
        # 9_2 10_2
    # await mission10_2()
        # 13
    # await mission13()
        # 11 wip
    # await mission11()
        # 1 and 2 done
    #await mission1and2()
        # 12 wip
    #await mission12()

async def mission6():
    runloop.run(motor.run_for_degrees(attachment_right, 135, 300), move_distance(61, 1, 660))
    await turn(28, "left")

async def mission5():
    await move_distance(5, 1, 660)
    await turn(16, "left")
    await motor.run_for_degrees(attachment_right, -150, 300)

async def mission10():
    runloop.run(motor.run_for_degrees(attachment_right, -100, 600), move_distance(1, -1,660))
    await turn(16, "left")
    await move_distance(40, 1,660)
    await turn(125, "left")
    await move_distance(4, 1, 300)
    await motor.run_for_degrees(attachment_right, 200, 660)
    await motor.run_for_degrees(attachment_right, -200, 660)

async def mission9():
    await move_distance(5, -1, 560)
    await turn(25, "left")
    runloop.run(move_distance(33, 1, 460), runloop.sleep_ms(250), motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity=-460))
    await turn(25, "left")
    await move_distance(64, 1 ,1000)

async def mission8():
    # await motor.run_for_degrees(attachment_right, -200, 700)
    turn_down = 220
    turn_velocity = 225
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
    turn_down = -240
    turn_velocity = 600
    turn_up= 220
    #await move_distance(5, 1, 560)
    #await turn(90, -1)
    await move_distance(3, 1, 560)
    await turn(42, "right")
    runloop.run(motor.run_for_degrees(attachment_right, -240, 600), move_distance(37, 1, 600))
    runloop.run(motor.run_for_degrees(attachment_left, 220, 600), turn(40, "left"))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1100, 0, velocity=-1010)

async def mission13():
    await move_distance(3, 1, 660)
    await turn(31, "right")
    runloop.run(move_distance(70, 1, 660), motor.run_for_degrees(attachment_right, -150, 350))
    runloop.run(move_distance(9, 1, 660), motor.run_for_degrees(attachment_right, 50, 500))
    await turn(12, "right")
    await motor.run_for_degrees(attachment_left, 200, 500)

async def mission11():
    await move_distance(3,-1, 300)
    await turn(150,"left")
    await move_distance(19, 1, 660)
    await turn(67, "left")

async def mission1and2():
    await motor.run_for_degrees(attachment_right, -81, 100) #down
    await move_distance(55, 1, 600)
    await turn(33, "left")
    await move_distance(21, 1, 300)
    await move_distance(21, -1, 300)
    await turn(42, "left")
    await move_distance(5, 1, 100)
    await turn(9, "left")
    await turn(11, "right")
    await turn(3, "left")
    await motor.run_for_degrees(attachment_right, 60, 200) #pick up
    await turn(51, "right")
    await motor.run_for_degrees(attachment_right, -70, 100)#down
    await move_distance(14, 1, 200)
    await motor.run_for_degrees(attachment_right, 260, 200)
    await move_distance(2,-1,100)
    await turn(20, "right"),
    await move_distance(65,-1,1000)

async def mission12():
    await move_distance(47, 1, 660) #move forward
    await motor.run_for_degrees(attachment_right, 56, 200) #down
    await move_distance(10, -1, 200) #move backward
    await motor.run_for_degrees(attachment_right, -56, 200) #up
    await move_distance(19, 1, 500)
    await move_distance(50, -1, 1000)

runloop.run(main())
