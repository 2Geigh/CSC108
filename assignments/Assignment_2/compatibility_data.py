# NOTE FROM BOB:
# The following is some data to test our compatibility calculator with.
# I might change some data around later (e.g. update start/end months),
# or modify which numbers are compatible with whom, etc.
# The calculator must still work correctly with new data, as long as it's
# in this same format.

# Here is data about the astrological signs, their sign groups, and their
# start and end dates. It's in this format:
# sign,sign_group,start_month,start_date,end_month,end_date
# This list specifies the date ranges for the various signs.
#
# NOTE FROM BOB: I'm not sure I buy into this particular set of signs and
# dates. I may change these, adding, removing, or renaming the signs, and
# changing the dates.
SIGN_DATA = ['ARI,1,3,21,4,19',
             'TAU,2,4,20,5,20',
             'GEM,3,5,21,6,21',
             'CAN,4,6,22,7,22',
             'LEO,1,7,23,8,22',
             'VIR,2,8,23,9,22',
             'LIB,3,9,23,10,23',
             'SCO,4,10,24,11,20',
             'SAG,1,11,21,12,21',
             'CAP,2,12,22,1,20',
             'AQU,3,1,21,2,21',
             'PIS,4,2,22,3,20']


# Here is the list of compatible and incompatible numerological numbers. Each
# item in the list is a string in the format 'N1,N2,STR', where 'STR' is
# either 'YES' or 'NO'. This indicates that `N2` is a compatible number for
# `N1`, but does NOT indicate that `N1` is a compatible number for `N2`.
#
# For example `1,2,YES` indicates that numerological number 2 is compatible
# for numerological number 1.
NUM_COMPATIBILITY_DATA = \
    ['1,1,YES', '1,2,YES', '1,4,NO', '1,5,YES', '1,6,NO',
     '2,1,YES', '2,2,YES', '2,4,YES', '2,5,NO', '2,6,YES', '2,7,NO', '2,8,YES',
     '3,3,YES', '3,4,NO', '3,6,YES', '3,7,NO', '3,8,NO', '3,9,YES',
     '4,1,NO', '4,2,YES', '4,3,NO', '4,4,YES', '4,5,NO', '4,8,YES', '4,9,NO',
     '5,1,YES', '5,2,NO', '5,4,NO', '5,5,YES', '5,6,NO', '5,7,YES',
     '6,1,NO', '6,3,YES', '6,6,YES', '6,5,NO', '6,7,NO', '6,9,YES',
     '7,2,NO', '7,3,NO', '7,4,YES', '7,5,YES', '7,6,NO', '7,7,YES', '7,8,NO',
     '8,2,YES', '8,4,YES', '8,8,YES', '8,2,NO', '8,7,NO', '8,9,NO',
     '9,3,YES', '9,6,YES', '9,9,YES', '9,4,NO', '9,8,NO',
     '11,1,YES', '11,2,YES', '11,4,YES', '11,6,YES', '11,8,YES', '11,5,NO',
        '11,7,NO',
     '22,2,YES', '22,4,YES', '22,8,YES', '22,1,NO', '22,3,NO', '22,5,NO',
        '22,9,NO']
