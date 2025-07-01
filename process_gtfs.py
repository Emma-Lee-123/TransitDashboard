import pandas as pd
import os

print("Processing GTFS data...")
GTFS_PATH = "gtfs"
OUTPUT_PATH = "output"

os.makedirs(OUTPUT_PATH, exist_ok=True)

#load gtfs files
#print(os.path.join(GTFS_PATH, "stops.txt"))
stops = pd.read_csv(os.path.join(GTFS_PATH, "stops.txt"))
routes = pd.read_csv(os.path.join(GTFS_PATH, "routes.txt"))
trips = pd.read_csv(os.path.join(GTFS_PATH, "trips.txt"))
stop_times = pd.read_csv(os.path.join(GTFS_PATH, "stop_times.txt"))
calendar_dates = pd.read_csv(os.path.join(GTFS_PATH, "calendar_dates.txt"))
stop_amenities = pd.read_csv(os.path.join(GTFS_PATH, "stop_amenities.txt"))
shapes = pd.read_csv(os.path.join(GTFS_PATH, "shapes.txt"))

print(f"✅ stops loaded: {len(stops)} rows")
print(f"✅ routes loaded: {len(routes)} rows")
print(f"✅ trips loaded: {len(trips)} rows")
print(f"✅ stop_times loaded: {len(stop_times)} rows")
print(f"✅ calendar loaded: {len(calendar_dates)} rows")
print(f"✅ stop_amenities loaded: {len(stop_amenities)} rows")
print(f"✅ shapes loaded: {len(shapes)} rows")

# === Summary 1: Trips per route ===
#trips_per_route = trips.groupby("route_id").size().reset_index(name="num_trips")
trips_per_route = trips.groupby(["route_id", "service_id"]).size().reset_index(name="num_trips")
trips_per_route = trips_per_route.merge(routes, on="route_id", how="left")

# Export
trips_per_route.to_csv(os.path.join(OUTPUT_PATH, "trips_per_route.csv"), index=False)
print("✅ Exported: trips_per_route.csv")

# === Summary 2: Average number of stops per route ===
# Count stops per trip
stops_per_trip = stop_times.groupby("trip_id").size().reset_index(name="num_stops")

# Add route_id to each trip
stops_per_trip = stops_per_trip.merge(trips[["trip_id", "route_id"]], on="trip_id", how="left")

# Calculate average per route
avg_stops_per_route = stops_per_trip.groupby("route_id")["num_stops"].mean().reset_index(name="avg_stops")
avg_stops_per_route = avg_stops_per_route.merge(routes, on="route_id", how="left")

# Export
avg_stops_per_route.to_csv(os.path.join(OUTPUT_PATH, "avg_stops_per_route.csv"), index=False)
print("✅ Exported: avg_stops_per_route.csv")

# === Summary 3: Stop locations ===
stops_map = stops[["stop_id", "stop_name", "stop_lat", "stop_lon"]]
# === Optional: Merge stop amenities from stop_amenities.txt ===
amenities_file = os.path.join(GTFS_PATH, "stop_amentities.txt")


# Merge amenities with stop locations
stops_with_amenities = stops_map.merge(stop_amenities, on="stop_id", how="left")

# Export merged data
stops_with_amenities.to_csv(os.path.join(OUTPUT_PATH, "stops_with_amenities.csv"), index=False)
print("✅ Exported: stops_with_amenities.csv")

# Export
stops_map.to_csv(os.path.join(OUTPUT_PATH, "stops_map.csv"), index=False)
print("✅ Exported: stops_map.csv")

# === Summary 4: Extract active service days from calendar_dates.txt ===
calendar_dates = pd.read_csv(os.path.join(GTFS_PATH, "calendar_dates.txt"))

# Keep only service additions (exception_type == 1)
active_dates = calendar_dates[calendar_dates["exception_type"] == 1].copy()

# Convert YYYYMMDD string to proper date format
active_dates["date"] = pd.to_datetime(active_dates["date"], format="%Y%m%d")

# Extract day of week
active_dates["weekday"] = active_dates["date"].dt.day_name()

# Export
active_dates.to_csv(os.path.join(OUTPUT_PATH, "calendar_active_days.csv"), index=False)
print("✅ Exported: calendar_active_days.csv")
