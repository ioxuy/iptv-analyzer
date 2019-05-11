class PAT:
    """
    Program Association Table (PAT) contains a directory listing of all Program Map Tables
    """
    def __init__(self):
        self.table_id = 0       # Table ID
        self.ts_id = 0          # Transport stream ID
        self.ver_num = 0        # Version number
        self.cur_next_ind = 0   # Current Next Indicator
        self.sec_num = 0        # Section Number
        self.last_sec_num = 0   # Last Section Number
        self.prog_nums = []     # Program numbers
        self.crc32 = 0          # 32-bit CRC
        self.crc32_ok = True    # Status of CRC verification
