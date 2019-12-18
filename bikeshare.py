# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:27:09 2019

@author: Mark S. Shenouda
"""

# Importing libraries

import os
import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
month_options = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
hours = ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('')
    # DONE: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city == None:
        print('Would you like to see data for Chicago, New York, or Washington?')
        city_input = input('> ')
        print('')
        options = ['chicago', 'new york', 'washington']
        if city_input.lower() in options:
            city = CITY_DATA[city_input.lower()]
            break
        else:
            print('Please enter a valid city value!')
            print('')
            continue


    # DONE: get user input for month (all, january, february, ... , june)
    month = None
    while month == None:
        print('Which month? January, February, March, April, May, June or All?')
        month_input = input('> ')
        print('')
        if month_input.lower() in month_options:
            month = month_options.index(month_input)
            break
        else:
            print('Please enter a valid month value!')
            print('')
            continue

    # DONE: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day == None:
        print('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All?')
        day_input = input('> ')
        print('')
        if day_input.lower() in day_options:
            day = day_options.index(day_input)
            break
        else:
            print('Please enter a valid day value!')
            print('')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('')
    print('Loading Data...')

    # Load city csv file
    df = pd.read_csv(city, index_col=0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['dow'] = df['Start Time'].dt.weekday


    # Filter by month
    if month != 0:
        df = df[df['Start Time'].map(lambda x: x.month) == month]


    # Filter by day
    if day != 7:
        df = df[df['dow'] == day]


    print('')
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('')
    # DONE: display the most common month
    print('The most common month is', month_options[df['Start Time'].dt.month.value_counts().index[0]].title()+'!')

    # DONE: display the most common day of week
    print('The most common day of week is', day_options[df['dow'].value_counts().index[0]].title()+'!')


    # Done: display the most common start hour
    print('The most start hour is', hours[df['Start Time'].dt.hour.value_counts().index[0]]+'!')


    print('')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # DONE: display most commonly used start station
    print('The most commonly used start station is', df['Start Station'].value_counts().index[0]+'.')


    # DONE: display most commonly used end station
    print('The most commonly used end station is', df['End Station'].value_counts().index[0]+'.')


    # DONE: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is', df['Start Station'].groupby(df['End Station']).value_counts().index[0][1], 'as a start station, and', df['Start Station'].groupby(df['End Station']).value_counts().index[0][0], 'as a end station.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # DONE: display total travel time
    print('The total travel time:', (df['End Time'] - df['Start Time']).sum())

    # DONE: display mean travel time
    print('The mean travel time:', (df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # DONE: Display counts of user types
    print('Counts of user types:')
    print(str(df['User Type'].value_counts()).split('\n')[0])
    print(str(df['User Type'].value_counts()).split('\n')[1])
    print('')

    # DONE: Display counts of gender
    if 'Gender' in df:
        print('Counts of gender:')
        print(str(df['Gender'].value_counts()).split('\n')[0])
        print(str(df['Gender'].value_counts()).split('\n')[1])
    else:
        print('There are no Gender data!')
    print('')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The most earliest year of birth:', int(df['Birth Year'].min()))
        print('The most recent year of birth:', int(df['Birth Year'].max()))
        print('The most common year of birth:', int(df['Birth Year'].mode()))
    else:
        print('There are no Birth Year Data!')
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_table(df):
	choice = '1'
	page = -5
	while True:
		clear()
		if choice == '1':
			page = min(page + 5, df.shape[0])
		if choice == '2':
			page = max(0, page - 5)
		if choice == '3':
			main()
		if choice == '4':
			quit()
		print('-'*40)
		print('US Bikeshare - By Mark S. Shenouda')
		print('-'*40)
		print('Data View')
		print('')
		print(str(df.reset_index().iloc[page:, 1:-1].head()))
		print('')
		print('')
		print('')
		print('Choices:')
		print('[NEXT = 1 , PREVIOUS = 2 , HOME = 3 , EXIT = 4]')
		print('')
		choice = None
		while choice == None:
			data_choice_input = input('> ')
			if data_choice_input in ['1', '2', '3', '4']:
				choice = data_choice_input

			else:
				print('')
				print('Please enter a valid choice!')
				continue


def show_data(df):
	show = None
	while show == None:
		print('')
		print('Would you like to look at the data? yes or no?')
		show_data_input = input('> ')
		if show_data_input.lower() in ['yes', 'no']:
			show = show_data_input
		else:
			print('')
			print('Please enter a valid value!')
			continue
	if show == 'yes':
		show_table(df)

	


    


def main():
	def main_screen():
		clear()
		print('-'*40)
		print('Explore US Bikeshare Data - By Mark S. Shenouda')
		print('-'*40)
		print('')
		print('')
		city, month, day = get_filters()
		df = load_data(city, month, day)
		clear()
		print('-'*40)
		print('***US Bikeshare Report***')
		print('')
		print('By Mark S. Shenouda')
		print('-'*40)
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		show_data(df)
	main_screen()
	restart = input('\nWould you like to restart? Enter yes or no.\n> ')
	if restart.lower() == 'yes':
		main()
	else:
		quit()


if __name__ == "__main__":
	main()