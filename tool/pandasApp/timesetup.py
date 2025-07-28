from datetime import datetime, timedelta

def generate_timestamps(start_date, interval_days, occurrences):
    """
    Generate a list of timestamps based on the start date, interval, and number of occurrences.

    :param start_date: str, the start date in format 'YYYY-MM-DD HH:MM:SS'
    :param interval_days: int, number of days between each occurrence
    :param occurrences: int, number of timestamps to generate
    :return: list of str, generated timestamps
    """
    try:
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        timestamps = [
            (start_datetime + timedelta(days=interval_days * i)).strftime("%Y-%m-%d %H:%M:%S")
            for i in range(occurrences)
        ]
        return timestamps
    except ValueError as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    #start_date = "2025-07-28 00:00:00"
    start_date = "2025-08-03 23:59:59"
    #start_date = "2025-07-10 02:00:00"

    #start_date = "2025-07-12 02:00:00"
    #start_date = "2025-07-13 23:59:59"
    interval_days = 7
    occurrences = 100

    timestamps = generate_timestamps(start_date, interval_days, occurrences)
    for timestamp in timestamps:
        print(timestamp)