import argparse

def get_args():
    
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('-lb', '--local_broker_IP', type=str, help='ip address of the local broker', required=True)
    parser.add_argument('-rb', '--remote_broker_IP', type=str, help='ip address of remote broker', required=False)
    args = parser.parse_args()
    local_broker_IP = args.local_broker_IP
    remote_broker_IP = args.remote_broker_IP
    
    return local_broker_IP, remote_broker_IP

local_broker_IP, remote_broker_IP  = get_args()

# Print the values

print ("\n ip address : [ %s ]\n" % local_broker_IP)
