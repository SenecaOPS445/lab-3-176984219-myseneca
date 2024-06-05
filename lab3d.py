#!/usr/bin/env python3

# Author ID: osokunbi1

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}'
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 
                            shell=True, 
                            capture_output=True, 
                            text=True)
    # Return the output as a string in utf-8 with newline characters stripped
    return result.stdout.strip()

if __name__ == "_main_":
    print(free_space())


