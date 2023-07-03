"""
* Project : 2023CDP Eddystone Broadcasting
* Program Purpose and Features :
* - send broadcasting message
* Author : JH KIM, JH SUN
* First Write Date : 2023.07.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.07.03      v1.01       First Write
"""
import os

def main():
    os.system("sudo hciconfig hci0 up")
    os.system("sudo hciconfig hcio leadv 3")
    os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 13 02 01 06 03 03 aa fe 0b 16 aa fe 10 00 74 72 66 52 36 30 00 00 00 00 00 00 00 00 00 00 00 00")

if __name__ == "__main__":
    main()
