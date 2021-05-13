#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginpass = 0 # counter for successes


# open the file for reading
with open("/home/student/mywork/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            splitline = line.split(' ')
            print (splitline[len(splitline)-1].rstrip())
            

print("The number of failed log in attempts is", loginfail)

