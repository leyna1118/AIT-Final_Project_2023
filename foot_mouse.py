import serial
import pyautogui, sys

COM_PORT = '/dev/ttyACM0'
BAUD_RATES = 38400
ser = serial.Serial(COM_PORT, BAUD_RATES)

try:
    while True:
        while ser.in_waiting:
            data_raw = ser.readline()
            data = data_raw.decode('latin-1')
            print('data:', data)
            data_list = data.split('\t')
            if len(data_list) == 9:
                # click = int(data_list[0])
                # if click >= 1:
                #     print("c")
                # left = int(data_list[1])
                # if left < 200:
                #     print("l")
                #     pyautogui.hotkey('tab')
                # right = int(data_list[2])
                # if right < 200:
                #     print("r")
                #     pyautogui.hotkey('tab')
                y = int(data_list[4])
                if y < -5000:
                    # print(1)
                    pyautogui.scroll(5)
                elif y > 7000:
                    # print(-1)
                    pyautogui.scroll(-5)
                elif y < -3000:
                    # print(1)
                    pyautogui.scroll(1)
                elif y > 5000:
                    # print(-1)
                    pyautogui.scroll(-1)
                
except KeyboardInterrupt:
    ser.close()
    print('bye')