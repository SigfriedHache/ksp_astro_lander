PHASE_NUMBER = 4

def run(vessel):
    """
    This run script is intended to be a "Lunar EDL" phase
    
    Parameters
    ----------
    vessel : AstroUtilities.Vessel
        This vessel is a custom-defined AstroUtilities.Vessel object, which is
        based off of the Krpc Vessel object but minified by quite a bit for 
        efficiency's sake.

    Returns
    -------
    none

    External Connections
    --------------------
    KRPC Connection with a locally-hosted instance of Kerbal Space Program, the
    default destination of which is 127.0.0.1:50000 and 127.0.0.1:50001
    """
    vessel.system_logger.info(str(PHASE_NUMBER) + " has commenced.")
    vessel.system_logger.info(str(vessel))
    vessel.telemetry_logger.info(str(PHASE_NUMBER))
