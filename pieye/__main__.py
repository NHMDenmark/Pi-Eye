"""main.py

This file is the entry point for the PiEye Server. It is run when the user runs
`pieye` from the command line.
"""

import argparse
from bottle import run
from pieye.routes import *


def run_server(host="0.0.0.0", port=8080, debug=False, reloader=False):
    """Start the server with the given configuration.
    
    Args:
        host (str, optional): Host to run server on (default: '0.0.0.0')
        port (int, optional): Port to run server on (default: 8080)
        debug (bool, optional): Run in debug mode (default: False)
        reloader (bool, optional): Run with reloader (default: False). Only works when not using camera.
        """
    run(host=host, port=port, debug=debug, reloader=reloader)

def main():
    """Main entry point for the PiEye Server."""
    parser = argparse.ArgumentParser(description="Run PiEye Server")

    # Add arguments for parser
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run in debug mode (default: False)",
    )
    parser.add_argument(
        "--reloader",
        action="store_true",
        help="Run with reloader (default: False). Only works when not using camera.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to run server on (default: '0.0.0.0')",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port to run server on (default: 8080)",
    )

    args = parser.parse_args()

    run_server(args.host, args.port, args.debug, args.reloader)


if __name__ == "__main__":
    main()
