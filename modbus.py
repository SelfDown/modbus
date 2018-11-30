# -*- coding: utf_8 -*-
import sys
import logging
import serial
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.modbus_rtu as modbus_rtu
import time
logger = modbus_tk.utils.create_logger("console")
if __name__ == "__main__":
    try:
        #master = modbus_tcp.TcpMaster(host="192.168.2.124")
        master = modbus_rtu.RtuMaster(serial.Serial("COM3", baudrate=9600))
        master.set_timeout(5.0)

        print "hello world"
        logger.info("connected")
        while 1>0:
            time.sleep(0.3)
            dat=master.execute(3, cst.READ_HOLDING_REGISTERS, 0, 2)
            print(str(dat))
            print str((dat[0]/10.0))+"% "+str(dat[1]/10.0)
            #logger.info()            
    except modbus_tk.modbus.ModbusError, e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
