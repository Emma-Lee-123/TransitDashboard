![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### Transit Data Analysis in Power BI
This project demonstrates how to analyze public transit data using GTFS files, **Python**, and **Power BI**. It includes Python scripts to transform GTFS `.txt` files into CSVs and a Power BI report to visualize transit activity, stop amenities, and weekday patterns.
>⚠️ This repo does not include GTFS files to keep the repo small and focused.

### Tech Stack
- **Python:** Data transformation (with with `pandas`, `os`)
- **Power BI:** Data modeling, relationships, and visuals
- **VS Code**: Development environment

### Features
- Parse GTFS files using Python (via `pandas`)
- Export clean CSVs for use in Power BI
- Interactive Power BI dashboards:
  - Map of stops with amenities (e.g., shelter, bike racks, benches)
  - Trips per route
  - Trips by weekday (with proper sorting)
  - Calendar filtering and service date analysis

### Setup Instructions
1. Download the latest GTFS feed from https://www.gotransit.com/en/partner-with-us/software-developers
2. Extract the following files into a folder named gtfs under the project directory
	<pre> <code>
	gtfs/
	├── calendar_dates.txt
	├── routes.txt
	├── shapes.txt
	├── stop_times.txt
	├── stops.txt
	└── trips.txt
	</code> </pre>
3. Make sure you have Python 3 and Power BI Desktop installed
4. Run the Python Scripts
  <pre> <code>
  cd python/
  python process_gtfs.py
  </code> </pre>
  This will read sample GTFS files from gtfs/ and output CSVs to output/
  Open the Power BI Report
  Open transit_report.pbix in Power BI Desktop.  It will load data from output/, use the slicers and visuals to explor the transit data.

Publish the report from Power BI Desktop to app.powerbi.com
- Publish to My Workspace
- Login app.powerbi.com, goto My Workspace to view reports

  
