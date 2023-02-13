alert_failure_count = 0
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 500

def real_network_integration(celcius):
    # real network communication code goes here
    pass

def alert_in_celcius(farenheit, alert_function=network_alert_stub):
    global alert_failure_count 
    celcius = (farenheit - 32) * 5 / 9
    return_code = alert_function(celcius)
    if return_code != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        alert_failure_count += 1
    return alert_failure_count
