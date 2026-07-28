import livef1

# Get a specific race session
session = livef1.get_session(
    season=2026,
    meeting_identifier="Hungary",
    session_identifier="Race"
)

# Load position data
position_data = session.get_data(
    dataNames="Position.z"
)

driver_data = session.drivers

print(position_data.head())

print(driver_data)