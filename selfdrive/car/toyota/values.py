from selfdrive.car import dbc_dict

class CAR:
  OLD_CAR = "#OLD_CARS!"


class ECU:
  CAM = 0 # camera
  DSU = 1 # driving support unit
  APGS = 2 # advanced parking guidance system


# addr: (ecu, cars, bus, 1/freq*100, vl)
STATIC_MSGS = [
  (0x130, ECU.CAM, (CAR.OLD_CAR), 1, 100, '\x00\x00\x00\x00\x00\x00\x38'),
  (0x240, ECU.CAM, (CAR.OLD_CAR), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x241, ECU.CAM, (CAR.OLD_CAR), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x244, ECU.CAM, (CAR.OLD_CAR), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x245, ECU.CAM, (CAR.OLD_CAR), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x248, ECU.CAM, (CAR.OLD_CAR), 1,   5, '\x00\x00\x00\x00\x00\x00\x01'),
  (0x367, ECU.CAM, (CAR.OLD_CAR), 0,  40, '\x06\x00'),
  (0x414, ECU.CAM, (CAR.OLD_CAR), 0, 100, '\x00\x00\x00\x00\x00\x00\x17\x00'),
  (0x466, ECU.CAM, (CAR.OLD_CAR), 1, 100, '\x24\x20\xB1'),
  (0x489, ECU.CAM, (CAR.OLD_CAR), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
  (0x48a, ECU.CAM, (CAR.OLD_CAR), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
  (0x48b, ECU.CAM, (CAR.OLD_CAR), 0, 100, '\x66\x06\x08\x0a\x02\x00\x00\x00'),
  (0x4d3, ECU.CAM, (CAR.OLD_CAR), 0, 100, '\x1C\x00\x00\x01\x00\x00\x00\x00'),

  (0x128, ECU.DSU, (CAR.OLD_CAR), 1,   3, '\xf4\x01\x90\x83\x00\x37'),
  (0x141, ECU.DSU, (CAR.OLD_CAR), 1,   2, '\x00\x00\x00\x46'),
  (0x160, ECU.DSU, (CAR.OLD_CAR), 1,   7, '\x00\x00\x08\x12\x01\x31\x9c\x51'),
  (0x161, ECU.DSU, (CAR.OLD_CAR), 1,   7, '\x00\x1e\x00\x00\x00\x80\x07'),
  (0x344, ECU.DSU, (CAR.OLD_CAR), 0,   5, '\x00\x00\x01\x00\x00\x00\x00\x50'),
  (0x365, ECU.DSU, (CAR.OLD_CAR), 0,  20, '\x00\x00\x00\x80\xfc\x00\x08'),
  (0x366, ECU.DSU, (CAR.OLD_CAR), 0,  20, '\x00\x72\x07\xff\x09\xfe\x00'),
  (0x4CB, ECU.DSU, (CAR.OLD_CAR), 0, 100, '\x0c\x00\x00\x00\x00\x00\x00\x00'),
]

ECU_FINGERPRINT = {
  ECU.CAM: 0x2e4,   # steer torque cmd
  ECU.DSU: 0x343,   # accel cmd
  ECU.APGS: 0x835,  # angle cmd
}


def check_ecu_msgs(fingerprint, ecu):
  # return True if fingerprint contains messages normally sent by a given ecu
  return ECU_FINGERPRINT[ecu] in fingerprint


FINGERPRINTS = {
  CAR.OLD_CAR: [{
    36: 8, 37: 8, 170: 8, 180: 8, 186: 4, 253:8, 254:8, 255: 8, 426: 6, 452: 8, 464: 8, 466: 8, 467: 8, 512: 6, 513:6, 547: 8, 548: 8, 552: 4, 608: 8, 610: 5, 643: 7, 705: 8, 740: 5, 800: 8, 835: 8, 836: 8, 849: 4, 869: 7, 870: 7, 871: 2, 896: 8, 897: 8, 900: 6, 902: 6, 905: 8, 911: 8, 916: 2, 921: 8, 933: 8, 944: 8, 945: 8, 951: 8, 955: 4, 956: 8, 979: 2, 998: 5, 999: 7, 1000: 8, 1001: 8, 1017: 8, 1041: 8, 1042: 8, 1043: 8, 1044: 8, 1056: 8, 1059: 1, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1196: 8, 1222:8, 1224:8, 1227: 8, 1235: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1561: 8, 1562: 8, 1568: 8, 1569: 8, 1570: 8, 1571: 8, 1572: 8, 1592: 8, 1596: 8, 1597: 8, 1600: 8, 1664: 8, 1779: 8, 1904: 8, 1912: 8, 1990: 8, 1998: 8, 2016: 8, 2017: 8, 2018: 8, 2019: 8, 2020: 8, 2021: 8, 2022: 8, 2023: 8, 2024: 8
  }],
}

STEER_THRESHOLD = 100

DBC = {
  CAR.OLD_CAR: dbc_dict('toyota_corolla_2017_pt_generated', 'toyota_adas'),
}

NO_DSU_CAR = []
TSS2_CAR = []
NO_STOP_TIMER_CAR = []  # no resume button press required
