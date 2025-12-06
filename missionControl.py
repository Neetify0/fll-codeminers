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
    motion_sensor.reset_yaw(0)
    yawAngle=motion_sensor.tilt_angles()[0]
    while abs(yawAngle)<abs(degrees*9.4):
        yawAngle=motion_sensor.tilt_angles()[0]
        motor_pair.move(motor_pair.PAIR_1, 200*direction)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(500)
    return

async def main():
    #await mission6()
    #await mission5()
    #await mission10()
    #await mission9()
    #await mission8()
    #await mission9_2()
    await mission10_2()
    #await mission13()



async def mission6():
    await motor.run_for_degrees(attachment_right, 200, 660)
    await move_distance(62.5, 1, 660)
    await turn(30, -1)

async def mission5():
    await move_distance(2, 1, 660)
    await turn(18, -1)
    await motor.run_for_degrees(attachment_right, -200, 660)

async def mission10():
    await motor.run_for_degrees(attachment_right, -100, 600)
    await move_distance(1, -1,660)
    await turn(16, -1)
    await move_distance(39, 1,660)
    await turn(116, -1)
    await motor.run_for_degrees(attachment_right, 200, 660)
    await motor.run_for_degrees(attachment_right, -200, 660)

async def mission9():
    await move_distance(5, -1, 560)
    await turn(25, -1)
    await move_distance(33, 1, 460)
    await runloop.sleep_ms(250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,200, 0, velocity=-460)
    await turn(27, -1)
    await move_distance(17, 1, 660)
    await turn(22, 1)
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
    await turn(45, -1) 
    await motor.run_for_degrees(attachment_left, -200, 500)
    await move_distance(7, 1, 560)
    await turn(150, -1)
    await turn(42, 1)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 500, 0, velocity=460)

async def mission10_2():
    turn_up = 220
    turn_velocity = 600
    #await move_distance(5, 1, 560)
    #await turn(90, -1)
    await move_distance(23, 1, 560)
    await turn(64, 1)
    await move_distance(20, 1, 600)
    await motor.run_for_degrees(attachment_left, turn_up, turn_velocity)
    await turn(40, -1)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 900, 0, velocity=-460)

async def mission13():
    # await motor.run_for_degrees(attachment_right, -200, 700)
    turn_up = 200
    turn_velocity = 400
    await motor.run_for_degrees(attachment_left, turn_up, turn_velocity)
    #await runloop.sleep_ms(500)
    #await motor.run_for_degrees(attachment_right, turn_up, 350)
    # await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    # await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    # await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    # await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
    # await motor.run_for_degrees(attachment_right, turn_down, turn_velocity)
    # await motor.run_for_degrees(attachment_right, -1*turn_down, 350)
   


runloop.run(main())







