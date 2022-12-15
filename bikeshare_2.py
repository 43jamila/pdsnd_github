import time
import pandas as pd

# name of programmer jamilah asiri
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ['chicago', 'new york city', 'washington']
name_of_months = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November", "December"]
days = ["All", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# this function to take specific inputs from users


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # ابغاه اذا دخل بيناتات
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?? \n> ').lower()
        if city in cities:
            break
        else:
            print("Sorry, wrong input try again\n")
            continue
    while True:
        month = input('Which month ,Please enter the full month name or type "all" for no time filter \n').title()
        if month in name_of_months:
            print('correct')
            break
        else:
            print("Sorry wrong input try again\n")
        continue
    while True:
        day = input('Which day ,Please enter the full day name or type "all" for no time filter \n').title()
        if day in days:
            print('correct')
            break
        else:
            print("Sorry wrong input try again\n")
        continue

    print('-' * 40)
    return city, month, day

# this function to load data from files


def load_data(_city, month: object, day):
    # read the file csv
    df = pd.read_csv(CITY_DATA[_city])
    # extract the day and month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    # filtering by user input
    if month != 'all':
        month = name_of_months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        day = days.index(day) + 1
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # df['specific_month'] + df['specific_year'] or chose function can extract the month with year together
    common_month = df[['month']].mode()
    print('The most common month:', common_month)

    # display the most common day of week
    common_day = df['day'].mode()
    print('The most common day:', common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()
    print('The most common hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts()
    print('The most commonly used start station', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts()
    print('The most commonly used end station', common_end_station)

    # display most frequent combination of start station and end station trip
    combination_start_end_station = df['Start Station'].astype(str) + "-" + df['End Station']
    c = combination_start_end_station.mode()
    print("most frequent combination of start station and end station trip is % s" % c)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is % s' % (df['Trip Duration'].sum()))

    # display mean travel time
    print('The mean travel time is % s' % (df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The number of user types is % s\n' % df['User Type'].value_counts())

    # Display counts of gender
    try:
        counts_gender = df['Gender'].value_counts()
        print('The number of gender used bikeshare is', counts_gender)
    except KeyError:
        print("No 'Gender' column in this file .")

    # Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth is % s' % (df['Birth Year'].min()))
        print('The most recent year of birth is % s' % (df['Birth Year'].max()))
        print('The most common year of birth is % s' % (df['Birth Year'].mode()))
    except KeyError:
        print("No 'Birth Year' column in this file .")
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def data_display(df):
    answers = ['Yes', 'No']
    count = 5
    answer = input('Do you want view the data rows for chosen city ? \n Enter "Yes" or "NO" ').title()
    while answer in answers:
        if answer == 'Yes':
            print(df.head(count))
            answer1 = input('Do you want view more data rows for chosen city ? \n Enter "Yes" or "NO" ').title()
            if answer1 == 'Yes':
                count += 5
                print(df.head(count))
                continue
            elif answer1 == 'No':
                break
        else:
            break
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
