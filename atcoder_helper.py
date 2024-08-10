import sys
import argparse
from core.helpers import AtcoderContest, AtcoderCli
from core.logger import log


def main():
    parser = argparse.ArgumentParser(description="AtCoder Helper Script")
    parser.add_argument("action", choices=["download", "submit", "setup", "test"])
    parser.add_argument("--contest", help="Contest ID")
    parser.add_argument("--problem", help="Problem ID")
    parser.add_argument("--file", help="Solution file to submit")
    parser.add_argument("--targets", help="Test targets")
    args = parser.parse_args()

    if args.action == "download":
        if not args.contest or not args.problem:
            log.error("Contest ID and Problem ID are required for download action")
            sys.exit(1)
        AtcoderCli.download_problem(args.contest, args.problem)
    elif args.action == "submit":
        if not args.contest or not args.problem or not args.file:
            log.error(
                "Contest ID, Problem ID, and filename are required for submit action"
            )
            sys.exit(1)
        AtcoderCli.submit_solution(args.contest, args.problem, args.file)
    elif args.action == "setup":
        if not args.contest:
            log.error("Contest ID is required for fetch_contest action")
            sys.exit(1)
        AtcoderCli.fetch_contest_info(args.contest)
        AtcoderContest.copy_template()

    elif args.actio == "test":
        if not args.targets:
            log.info("Test targets are required for test action")
            sys.exit(1)


if __name__ == "__main__":
    main()
