"""

This module makes use of the prometheus client library to
provide the prometheus monitoring software with telemetry.

"""
from prometheus_client import start_http_server, Counter, Gauge
import time
# https://pypi.org/project/psutil/
import psutil
import math

objPsutilVirtualMemoryPercent = Gauge('psutil_virtual_memory_percent','psutil_virtual_memory_percent')
objPsutilCpuPercent = Gauge('psutil_cpu_percent','psutil_cpu_percent')
objPsutilDiskUsagePrecent = Gauge('psutil_disk_usage_percent','psutil_disk_usage_percent')
objPsutilSensorsTemperaturesCoretempPackageId0C = Gauge('psutil_sensors_temperatures_coretemp_package_id_0', 'psutil_sensors_temperatures_coretemp_package_id_0')
objPeriodicFunctionCalls = Counter('periodic_function_calls', 'periodic_function_calls')
objPeriodicFunctionArbitraryGraph = Gauge('periodic_function_arbitrary_graph', 'periodic_function_arbitrary_graph')

def vPeriodicFunction(dctCounterPar: dict):
    """ A function which periodically updates prometheus client info. 
    
    """

    # Get the virtual memory as a percentage
    try:
        objPsutilVirtualMemoryPercent.set(psutil.virtual_memory().percent)
    except Exception as e:
        print(f"{e}")

    # Get the CPU utilisation as a percentage
    try:
        objPsutilCpuPercent.set(psutil.cpu_percent(interval=0))
    except Exception as e:
        print(f"{e}")

    # Get the disk usage as a percentage
    try:
        objPsutilCpuPercent.set(psutil.disk_usage('/root/').percent)
    except Exception as e:
        print(f"{e}")

    # Get the CPU sensors temperature for Package ID 0
    try:
        objSensorsTemperatures = psutil.sensors_temperatures()
        objPsutilSensorsTemperaturesCoretempPackageId0C.set(objSensorsTemperatures['coretemp'][0].current)
    except Exception as e:
        print(f"{e}")

    # Keep a counter for how many times this function has been called
    try:
        dctCounterPar['iFunctionCounter'] = dctCounterPar['iFunctionCounter'] + 1
        objPeriodicFunctionCalls.inc(1)
    except Exception as e:
        print(f"{e}")

    # Set an arbitrary graph of a sine function
    try:
        fTrigValue = math.sin(math.pi * (dctCounterPar['iFunctionCounter'] / 450.0))
        objPeriodicFunctionArbitraryGraph.set(fTrigValue)
    except Exception as e:
        print(f"{e}")

    # Sleep for 500 milliseconds
    time.sleep(0.5)

    return


def vMain():
    """ The main function 
    
    """
    dctCounterPar = {}
    dctCounterPar['iFunctionCounter'] = 0

    # Start the prometheus client listen server
    start_http_server(8000)

    # Continuously call the function collecting the telemetry
    while True:
        vPeriodicFunction(dctCounterPar)

    return


if __name__ == '__main__':
    vMain()
