import copernicusmarine
import calendar

# Years you want
years = [2023]

# Indian Ocean bounds
MIN_LON, MAX_LON = 40, 110
MIN_LAT, MAX_LAT = -40, 30

for year in years:
    for month in range(6, 13):

        # Start date
        start_date = f"{year}-{month:02d}-01T00:00:00"

        # End date (last day of month)
        last_day = calendar.monthrange(year, month)[1]
        end_date = f"{year}-{month:02d}-{last_day}T00:00:00"

        print(f"Downloading: {year}-{month:02d}")

        copernicusmarine.subset(
            dataset_id="cmems_obs-mob_glo_phy-cur_my_0.25deg_P1D-m",
            variables=["uo", "vo"],
            minimum_longitude=MIN_LON,
            maximum_longitude=MAX_LON,
            minimum_latitude=MIN_LAT,
            maximum_latitude=MAX_LAT,
            start_datetime=start_date,
            end_datetime=end_date,
            minimum_depth=0.49,
            maximum_depth=0.49,
            output_filename=f"indian_ocean_{year}_{month:02d}.nc"
        )