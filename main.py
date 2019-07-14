#!/usr/bin/python3

from methods import *
from tests import *

create_dir()

if sys.argv.__contains__("test"):
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
else:
    # Read server file
    servers = read_file("SE_test_1_servers.txt")
    
    # Get API request for servers
    get_servers_status(servers)
    
    # Write Success Rate Not Grouped
    write_success_rates()

    # Group by Application and Version
    group_success_rate()

    # Compute and Display the results
    compute_and_display()
