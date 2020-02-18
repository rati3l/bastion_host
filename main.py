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
        config = yaml.load(f)
  
    try:
      ip = config[args.server_name]["ip"]

    except KeyError:
      print(f"Server {args.server_name} not found in config file")

    else:
      print(config[args.server_name])
      os.system(f"ssh ubuntu@{ip}")

if __name__ == "__main__":    
    main()
