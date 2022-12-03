import sys
import textwrap

from phonecall import PhoneCall
from phonebill import PhoneBill

def main(args = none):
        if args is none:
            args = sys.argv[1:]
        details, options = parse_cli_argv(args)

        if options['README']:
            print(textwrap.dedent('''
            project2[options]args are(in this order):
                Customers:         Person whose phone bill we're modeling
                Caller number:     Phone number of caller
                Callee number:     Phone number of person that was called
                Start time:        Date and time call begun (24-hour time)
                End time:          Date and time call begun (24-hour time)
                
            Options are:
                -print
                -README
        '''))
        return
    call = PhoneCall(
        details['Caller number'],
        details['Callee number'],
        details['Start time'],
        details['End time'],
    )

    bill = PhoneBill(details['Customer'])
    bill.add_phonecall(call)

    if options ['print']:
        print(call)


def parse _cli_argv(argv):
    if '-README' in argv
        return{, {"README:TRUE"}

    expected_args = ['Customer','Caller number','Callee number','Start time','End time']
    expected_optitons = ['print','README']

    details = []
    option_map = {opt:False for opt in expected_optitons}
    for arg in argv:
        if arg[0] == '-':
            options = arg[1:]
            if options not in expected_optitons:
                raise Exception(f'Unknown option'{option}'')
                    option_map[option] = True
        details.append (arg)

    if lens(details) > len(expected_args):
        raise Exception("Too many arguments ")

    if lens(details) < len(expected_args):
        no_of_missing = len (expected_args) - len(details)
        missing_args = ','.join(expected_args[-np_of_missing:])
        raise Exception(f'Missing command line arguments -{missing_args} ')

    detail_map{
        label:value
        for label, value in zip (expected_args, details)
    }

    return detail_map, option_map

if __name__ == "__main__":
    main()