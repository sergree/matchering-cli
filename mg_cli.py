import matchering as mg
from argparse import ArgumentParser
import logging
import sys


def parse_args():
    parser = ArgumentParser(description='Simple Matchering 2.0 Command Line Application')
    parser.add_argument('target', type=str, help='The track you want to master')
    parser.add_argument('reference', type=str, help='Some "wet" reference track')
    parser.add_argument('result', type=str, help='Where to save your result')
    parser.add_argument('-b', '--bit', type=int, choices=[16, 24, 32], default=16,
                        help='The bit depth of your mastered result. 32 means 32-bit float')
    parser.add_argument('--log', type=str, default=None, help='The file to which the logs will be written')
    parser.add_argument('--no_limiter', dest='no_limiter', action='store_true',
                        help='Disables the limiter at the final stage of processing')
    parser.add_argument('--dont_normalize', dest='dont_normalize', action='store_true',
                        help='Disables normalization, if --no_limiter is set. '
                             'Can cause clipping if the bit depth is not 32')
    return parser.parse_args()


def set_logger(handler, formatter, logger):
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def prepare_logger(args):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('{asctime}: {levelname:>7}: {message}', style='{')

    if args.log:
        set_logger(logging.FileHandler(args.log), formatter, logger)

    set_logger(logging.StreamHandler(sys.stdout), formatter, logger)

    return args, logger


def run(args, logger):
    mg.log(
        warning_handler=logger.warning,
        info_handler=logger.info,
        debug_handler=logger.debug
    )

    bit_to_subtype = {
        16: 'PCM_16',
        24: 'PCM_24',
        32: 'FLOAT'
    }

    logger.debug(f'{mg.__title__} {mg.__version__}')
    logger.debug(f'Maintained by {mg.__author__}: {mg.__email__}')
    logger.debug(f'Contributors: {", ".join(mg.__credits__)}')

    try:
        mg.process(
            target=args.target,
            reference=args.reference,
            results=[
                mg.Result(
                    args.result,
                    bit_to_subtype.get(args.bit),
                    use_limiter=not args.no_limiter,
                    normalize=not args.dont_normalize
                )
            ]
        )
    except Exception as e:
        logger.exception('Got the exception while executing mg.process()')


if __name__ == '__main__':
    run(*prepare_logger(parse_args()))
