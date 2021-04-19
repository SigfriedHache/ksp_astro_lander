from datetime import datetime

from System.Utilities.Logging import initialize_logs, get_system_logger
from Mission.MissionMain import mission


def main():
    start_time = datetime.now()
    initialize_logs()
    system_logger = get_system_logger()
    system_logger.info("")

    mission()


if __name__ == "__main__":
    main()
