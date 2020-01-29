


import serial
import pathlib
import canmatrix
import time


_cfd = pathlib.Path(__file__).absolute().parent


def depack(data: bytearray):
    try:
        package_head_index = data.find(b'\xfe\xfe')
        if package_head_index >= 0:
            payload_len = data[package_head_index + 3]
            payload_index = package_head_index + 4
            package_end = data[package_head_index + payload_len + 6]
            # print(package_end)
            if package_end == 0xBB:
                return data[payload_index: payload_index + payload_len]
    except IndexError:
        pass
    return bytearray()


def read_total_data(ser: serial.Serial):
    tx_data = bytearray([0xfe, 0xfe, 0x01, 0x01, 0x11, 0x06, 0x11, 0xbb])
    rx_len = 7 + 103
    ser.write(tx_data)
    rx_data = ser.read(size=rx_len)
    # print(rx_data)
    return depack(rx_data)


def read_normal_data(ser: serial.Serial):
    tx_data = bytearray([0xfe, 0xfe, 0x01, 0x01, 0x22, 0x00, 0x21, 0xbb])
    rx_len = 7 + 23
    ser.write(tx_data)
    rx_data = ser.read(size=rx_len)
    return depack(rx_data)


def decode_data(frame: canmatrix.Frame, data: bytearray):
    if data:
        res = frame.decode(data)
        if res:
            s: canmatrix.DecodedSignal
            for s in res.values():
                print('{}-{} {} {}'.format(s.signal.name, s.signal.comment ,s.named_value,s.signal.unit))


if __name__ == '__main__':
    com = serial.Serial('COM3', 19200)
    com.timeout = 1

    dbc = canmatrix.formats.loadp_flat(
        str(_cfd.joinpath('GEEK智能叉车485通讯协议.dbc')),
        dbcImportEncoding='gbk',
        dbcImportCommentEncoding='gbk'
    )

    while True:
        print("<<总数据包>>")
        total_data = read_total_data(com)
        decode_data(dbc.frame_by_name('Total_DataPage'), total_data)
        print("<<常规数据包>>")
        normal_data = read_normal_data(com)
        decode_data(dbc.frame_by_name('Usually_DataPage'), normal_data)
        time.sleep(5)

