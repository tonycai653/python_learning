import os
import re


processed_to_target_dir = r'C:\Users\Tony_Cai\Desktop\temp_log'

def process_file(fullname_src, fullname_dest, interface):
    with open(fullname_src, 'r') as fr, open(fullname_dest, 'a') as fw:
        error_lines = []
        for line in fr:
            if line_not_contains_standard_pattern(line, interface):
                error_lines.append(line)
        fw.writelines(error_lines)

        

def handle_files():
    logs_dir = r'D:\responsibility\daily\logs\files'
    files_will_processed = ['TigFin_IP001_CreateUpdateAccount_21June14-Process_Archive.log',
                            'U2C_IP001_IP002_IP012-1-Process_Archive.log',
                            'MASTERTSID_CSC_TIBCO-Process_Archive.log']
    
    
    for filename in files_will_processed:
        fullname_src = os.path.join(logs_dir, filename)
        fullname_dest = os.path.join(processed_to_target_dir, filename)
        interface = get_interface(filename)
        process_file(fullname_src, fullname_dest, interface)



def line_not_contains_standard_pattern(line, interface):
    standard_patterns_tigfin_ip001 = [r'ENTRY_UPDATE_ACCOUNT_ID', r'SQLSTATE [tibcosoftwareinc][Oracle JDBC Driver]',
                        r'EXIT_UPDATE_ACCOUNT_ID', r'BLOCKED_ENTITY', r'The wireProtocolMode connect option has been internally changed to 2, due to the use of UTF8 transliteration.']
    standard_patterns_u2c_ip001_002_012 = [r'WebService called for', r'(\d+)account updated successfully',
                                           r'(\d+)account address updated successfully',
                                           r'Phone(\d+)account contact updated successfully',
                                           r'WebSite(\d+)account contact updated successfully',
                                           r'WebService called to', r'Fax(\d+)account contact updated successfully',
                                           r'(\d+)account created successfully',
                                           r'(\d+)account address created successfully',
                                           r'(\d+)WebSiteContact created successfully',
                                           r'Phone(\d+)account contact created successfully',
                                           r'Fax(\d+)account contact created successfully',
                                           r'found in the request and is blocked by U2C TIBCO.',
                                           r'at com.tibco.pe',
                                           r'Transaction Data:',
                                           r'Mandatory Parameter PhoneNumber is missing']
    standard_patterns_csc = [r'Error establishing socket. Unknown',
                             r'Cannot establish socket to redirected host an',
                             r'Request Received For Customer ID :(\d+)',
                             r'Request Successful For Customer ID :(\d+)']
    interface_pattern_dict = {'tigfin_ip001':standard_patterns_tigfin_ip001, 'u2c_ip001_002_012':standard_patterns_u2c_ip001_002_012,
                              'csc': standard_patterns_csc}
    for pattern in interface_pattern_dict[interface]:
        if re.search(pattern, line):
            return False
    return True



def get_interface(filename):
    '''interfaces:
    u2c_ip001_002_012
    u2c_ip080_081
    u2c_ip006
    tigfin_ip001
    tigfin_ip007
    tigfin_ip012
    csc'''

    interfaces = {'u2c_ip001':'u2c_ip001_002_012',
              'u2c_ip080':'u2c_ip080_081',
              'ip006':'u2c_ip006',
              'tigfin_tibco_ip007':'tigfin_ip007',
              'tigfin_tibco_ip012':'tigfin_ip012',
              'tigfin_ip001':'tigfin_ip001',
              'csc':'csc'}
    
    filename_lower = filename.lower()
    for interface in interfaces:
        if interface in filename_lower:
            return interfaces[interface]

       


if __name__ == '__main__':
    handle_files()    
