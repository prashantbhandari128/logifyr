from logifyr.logifyr import Logifyr

if __name__ == "__main__":
    # Create an instance of Logifyr
    logger = Logifyr()
    # Test the log function with different statuses
    logger.print_log("INFO", "This is an informational message.")
    logger.print_log("WARNING", "This is a warning!")
    logger.print_log("ERROR", "An error occurred!")
    logger.print_log("DEBUG", "Debugging information.")
    # Customize status colors (example)
    logger.set_status_color("INFO", "cyan")
    logger.set_status_color("WARNING", "magenta")
    # Test with customized status colors
    logger.print_log("INFO", "This is a customized informational message.")
    logger.print_log("WARNING", "This is a customized warning!")
    # Disable colorized output
    logger.disable_color()
    logger.print_log("INFO", "This message should not be colorized.")
    logger.enable_color()
    # Set a different timestamp format
    logger.set_timestamp_format("%Y/%m/%d %H:%M:%S")
    # Test with the new timestamp format
    logger.print_log("INFO", "This message has a custom timestamp format.")
    # Set a another timestamp format
    logger.set_timestamp_format("%m/%d/%Y %I:%M %p")
    # Test with the another timestamp format
    logger.print_log("INFO", "This message has another custom timestamp format.")