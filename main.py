"""
Created: 12/06/2020
Project Author(s): Sigfried Hache
Description: 
    This script runs the Astrobotic Lander mission, including all 
    relevant phases from pre-check through landing itself.
Updates:
    12/06/2020 - Sigfried Hache
        > Created high-level runner for mission
        > Created initial sequence for the main mission phases
"""

# Custom Library and Special Library Imports
import krpc # https://github.com/krpc/krpc
import AstroUtilities
import AstroPhases

# Standard Library Imports
import shutil
import os
import json

# Config location
CONFIG = r'C:\scratch\git\krpc_scratchpad_py\astrobotic_lander\config.json'

###############################################################################
# Marshall the configuration from config.json
with open(CONFIG, "r") as config_file:
    config = json.load(config_file)

# Clear and ensure the existence of the logdir (more elegant ways on linux...)
try:
    shutil.rmtree(config["log_dir"])
except WindowsError as e:
    print "Couldn't delete the logdir because of the following error:"
    print e
try:
    os.mkdir(config["log_dir"])
except WindowsError as e:
    print "Couldn't create the logdir because of the following error:"
    print e

# Create system logs
system_logger = AstroUtilities.createLogger(
    log_name = config["system_log_handle"],
    log_level = config["logging_level"],
    log_filepath = str(config["log_dir"] + config["system_filename"]),
    log_format = "%(asctime)sZ %(levelname)s %(message)s"
)
system_logger.info("Systems Logging has been initialized.")

# Create telemetry logs
telemetry_logger = AstroUtilities.createLogger(
    log_name = config["telemetry_log_handle"],
    log_level = config["logging_level"],
    log_filepath = str(config["log_dir"] + config["telemetry_filename"]),
    log_format = "%(message)s"
)
system_logger.info("Telemetry Logging has been initialized.")

# Initialize the KSP Connection
try:
    krpc_connection = krpc.connect(
        name = config["krpc_name"],
        address = config["krpc_address"],
        rpc_port = config["krpc_port"],
        stream_port = config["krpc_stream_port"]
    )
    system_logger.info("KRPC Connection has been successfully set up.")
except Exception as e:
    system_logger.error("There was a problem setting up the KRPC Connection:")
    system_logger.error(e)
    # raise Exception(e)
    krpc_connection = "Whoops!"

###############################################################################
# Initialize vehicle object
system_logger.info("Initializing the Vessel.")
astrobotic_lander = AstroUtilities.Vessel(
    connection = krpc_connection, 
    vessel_name = config["vessel_name"], 
    telemetry_log_handle = config["telemetry_log_handle"],
    system_log_handle = config["system_log_handle"]
)

###############################################################################
# Run Phase 1: Pre-launch Checks
system_logger.info("Phase 1: Pre-launch Checks is commencing.")
AstroPhases.Phase1(astrobotic_lander)

# Run Phase 2: Launch to circular low Kerbin orbit
system_logger.info("Phase 2: Low Kerbin Orbit Navigation is commencing.")
AstroPhases.Phase2(astrobotic_lander)

# Run Phase 3: Navigate and guide from low Kerbin orbit to a low, circular, 
# highly-inclined Munar orbit
system_logger.info("Phase 3: Polar Low Munar Orbit Navigation is commencing.")
AstroPhases.Phase3(astrobotic_lander)

# Run Phase 4: Land on the morning horizon of the Mun
system_logger.info("Phase 4: Munar Landing is commencing.")
AstroPhases.Phase4(astrobotic_lander)

# End!
system_logger.info("End of mission automation!")
