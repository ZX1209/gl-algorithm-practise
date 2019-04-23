import logging as log

log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',
                level=log.DEBUG)



T = int(input())

for i in range(T):
    log.debug('this is a debug message')


    print('Case #'+str(i+1)+': ')
