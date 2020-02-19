#!/usr/bin/python3

import yaml
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="yaml config location")     
    parser.add_argument("server_name", help="server name to connect")
    args = parser.parse_args()
    
    with open(args.config_file, 'r') as f:
        config = yaml.safe_load(f)
  
    try:
      bastion_ip, host_ip = config[args.server_name].values()

    except KeyError:
      print(f"Server {args.server_name} not found in config file")

    else:
      print(f"Connecting to {args.server_name} - {host_ip} via {bastion_ip}")
      os.system(f"ssh -A -t ubuntu@{bastion_ip} ssh -A {host_ip}")

if __name__ == "__main__":    
    main()
