import woodruffstats.helpers as helpers
import pandas as pd

def get_workouts_runs(workouts):
	return [i for i in workouts if i['_links']['activity_type'][0]['id'] in ('16', '188')]


def construct_run_df(runs):
	runs_df = pd.DataFrame([helpers.flatten(run) for run in runs])

	runs_df['start_datetime_obj'] = [helpers.get_datetime(i) for i in runs_df['start_datetime']]
	runs_df['start_datetime_year'] = [i.year for i in runs_df['start_datetime_obj']]
	runs_df['start_datetime_month'] = [i.month for i in runs_df['start_datetime_obj']]
	runs_df['start_datetime_week'] = [i.week for i in runs_df['start_datetime_obj']]
	runs_df['aggregates_distance_total_miles'] = helpers.convert_metres_to_miles(runs_df['aggregates_distance_total'])

	return runs_df