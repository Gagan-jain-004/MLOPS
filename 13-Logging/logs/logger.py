## configuring logging

import logging

# below v r updating basicConfig  so restart kernel from top bar as v executed previous so that's why

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' 
)

