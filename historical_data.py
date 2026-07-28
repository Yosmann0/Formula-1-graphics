import livef1

# Get a specific race session
session = livef1.get_session(
    season=2024,
    meeting_identifier="Spa",
    session_identifier="Race"
)

# Load position data
position_data = session.get_data(
    dataNames="Position.z"
)

driver_data = session.drivers

print(position_data.head())

print(driver_data)