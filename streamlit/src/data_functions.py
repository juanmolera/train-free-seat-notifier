import pandas as pd

def get_timetable(day_of_the_week):

    if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':

        timetables = pd.read_csv('../data/timetables/saturday_and_sunday_timetable.csv')
        timetables['Departure'] = timetables['Departure'].apply(lambda x: '{:,.2f}'.format(x)).tolist()
        timetables['Arrival'] = timetables['Arrival'].apply(lambda x: '{:,.2f}'.format(x)).tolist()

    else:

        timetables = pd.read_csv('../data/timetables/monday_to_friday_timetable.csv')
        timetables['Departure'] = timetables['Departure'].apply(lambda x: '{:,.2f}'.format(x)).tolist()
        timetables['Arrival'] = timetables['Arrival'].apply(lambda x: '{:,.2f}'.format(x)).tolist()

    return timetables