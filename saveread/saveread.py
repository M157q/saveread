def parse_args():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--web',
        action='store_true',
        default=False,
        help="Start a webserver serving at localhost."
    )

    return parser.parse_args()


def execute_saveread(args):
    from . import database
    db = database.SavereadDB()

    if args.web:
        from . import web_mode
        web_mode.main(db.records)
    else:
        from . import cli_mode
        cli_mode.main(db.records)


def main():
    args = parse_args()
    execute_saveread(args)

if __name__ == '__main__':
    main()
