#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import urllib.request
import crayons
import yaml

# function to push commands
def commandpush(work): # devicecmd==list
    for task in work['todo']:
        print ('Handshaking. .. ... connecting with ' + task['ipaddr'] )
        # we'll learn to write code that connects to devices here
        print(crayons.yellow('Attempting to sending command --> ' + task['name'] + " " +  task['state'] ))
        # we'll learn to write code that sends cmds to device here
def url2yaml(url):
    with urllib.request.urlopen(url) as response:
        return(yaml.load(response.read()))

# start our main script
def main():
        # download yaml file using http 
        work2do = url2yaml('https://labs.alta3.com/courses/pyb/work2do-two')

        print (crayons.green(yaml.dump(work2do)))
        print (crayons.red("Welcome to the network device command pusher", bold=True)) # welcome message

        ## run
        commandpush(work2do) # call function to push commands to devices

# call our main function
main()
